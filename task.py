# -*- coding: utf-8 -*-
#
# Created on 2019/6/1
#
# @author: Sparcle F.
# Copyright: Beijing Yupont Electric Power Technology co.,ltd. 2013-2019

from PySide2.QtCore import QRunnable, QObject, Signal
import re, math, urllib, random, os


class TaskSignals(QObject):
    sigStatuChange = Signal(int, str)
    sigProgress = Signal(int, int)


class Task(QRunnable):
    agents = (
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
        'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1')

    def __init__(self, options):
        super(Task, self).__init__()
        self.mapType = options.mapType
        self.url = options.url
        self.minLevel = options.minLevel
        self.maxLevel = options.maxLevel
        self.area = options.area
        self.range = options.range
        self.timeout = options.timeout
        self.maxRetry = options.maxRetry
        self.status = "等待"
        self.rootDir = 'C:\\MapData\\'
        self.signals = TaskSignals()
        self.taskId = -1
        self.retry = 0
        self.tilesDone = 0
        self.stopReq = False

        if self.maxLevel < self.minLevel:
            self.maxLevel = self.minLevel

        self.totalTiles = 0
        for zoom in range(self.minLevel, self.maxLevel + 1):
            tile_range = self.calcZoomTileRange(zoom)
            self.totalTiles += (tile_range[1]-tile_range[0])*(tile_range[3]-tile_range[2])

    def run(self):
        self.signals.sigStatuChange.emit(self.taskId, "开始下载")
        for zoom in range(self.minLevel, self.maxLevel + 1):
            if self.stopReq:
                break
            tile_range = self.calcZoomTileRange(zoom)
            self.downRangeTiles(tile_range, zoom)

        self.signals.sigStatuChange.emit(self.taskId, "结束")

    # 经纬度反算切片行列号 3857坐标系
    @staticmethod
    def deg2num(lat_deg, lon_deg, zoom):
        lat_rad = math.radians(lat_deg)
        n = 2.0 ** zoom
        x_tile = int((lon_deg + 180.0) / 360.0 * n)
        y_tile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
        return x_tile, y_tile

    def calcZoomTileRange(self, zoom):
        if self.range == '全球':
            n = int(2.0 ** zoom)
            return [0, n, 0, n]

        left = self.range[0]
        right = self.range[2]
        if left > right:
            left = self.range[2]
            right = self.range[0]
        top = self.range[1]
        bottom = self.range[3]
        if top < bottom:
            top = self.range[3]
            bottom = self.range[1]
        x1,y1 = Task.deg2num(top, left, zoom)
        x2,y2 = Task.deg2num(bottom, right, zoom)
        return [x1, x2, y1, y2]

    # 下载图片
    def getImg(self, url, save_path):
        try:
            f = open(save_path, 'wb')
            req = urllib.request.Request(url)
            req.add_header('User-Agent', random.choice(Task.agents))  # 换用随机的请求头
            pic = urllib.request.urlopen(req, timeout=self.timeout)
            f.write(pic.read())
            f.close()
            self.tilesDone += 1
            self.signals.sigProgress.emit(self.taskId, self.tilesDone)
        except Exception:
            self.retry += 1
            if self.retry >= self.maxRetry:
                self.signals.sigStatuChange.emit(self.taskId, "出错了")
            elif not self.stopReq:
                self.getImg(url, save_path)

    def setRootDir(self, rootDir):
        self.rootDir = rootDir

    def getTileUrl(self, x, y, zoom) -> str:
        tile_url = self.url
        tile_url = re.sub('\{zoom\}', str(zoom), tile_url)
        tile_url = re.sub('\{x\}', str(x), tile_url)
        tile_url = re.sub('\{y\}', str(y), tile_url)
        return tile_url

    # 下载指定范围切片
    def downRangeTiles(self, tile_range: list, zoom: int) -> None:
        for x in range(tile_range[0], tile_range[1]):
            if self.stopReq:
                break
            for y in range(tile_range[2], tile_range[3]):
                if self.stopReq:
                    break
                path = self.rootDir + self.mapType + "\\" + str(zoom) + "\\" + str(x)
                if not os.path.exists(path):
                    os.makedirs(path)
                tile_url = self.getTileUrl(x, y, zoom)
                self.getImg(tile_url, os.path.join(path, str(y) + ".png"))
