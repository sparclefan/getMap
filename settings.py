# -*- coding: utf-8 -*-
#
# Created on 2019/6/1
#
# @author: Sparcle F.
# Copyright: Beijing Yupont Electric Power Technology co.,ltd. 2013-2019

import re,json

class Settings:
    def __init__(self):
        with open("./config.json", 'r') as load_f:
            self.configDict = json.load(load_f)

    def getMapTypeList(self):
        return self.configDict['urls'].keys()

    def getAreaList(self):
        return self.configDict['areas'].keys()

    def getUrl(self, mapname):
        return self.configDict['urls'][mapname]

    def getAreaRange(self, areastr):
        if areastr in self.configDict['areas']:
            return self.configDict['areas'][areastr]
        else:
            return areastr

