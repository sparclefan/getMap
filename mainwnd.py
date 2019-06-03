# -*- coding: utf-8 -*-
#
# Created on 2019年5月31日
#
# @author: sparcle

from PySide2.QtCore import QThreadPool, Slot, Qt
from PySide2.QtWidgets import QMainWindow, QFileDialog, QDialog, QTableWidgetItem, QProgressBar
from ui_mainwindow import Ui_MainWindow
from addtaskdlg import DlgAddTask
from settings import Settings


class TaskObject:
    pass


class MainWnd(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWnd, self).__init__(None)
        self.setupUi(self)
        self.tb_task.setColumnWidth(4, 200)

        self.pb_browser.clicked.connect(self.onBrowser)
        self.pb_clear.clicked.connect(self.onClearTaskList)
        self.pb_addTask.clicked.connect(self.onAddTask)
        self.pb_start.clicked.connect(self.onStart)
        self.rootPath = 'C:\\MapData'
        self.le_path.setText(self.rootPath)
        self.settings = Settings()
        self.threadpool = QThreadPool()
        self.tasklist = []

    def onBrowser(self):
        path = QFileDialog.getExistingDirectory(self, '地图存储路径', self.rootPath)
        if path and path != '':
            self.rootPath = path
            self.le_path.setText(self.rootPath)

    def onClearTaskList(self):
        for task in self.tasklist:
            task.stopReq = True

        self.threadpool.clear()
        self.tasklist.clear()
        self.tb_task.clearContents()

    def onAddTask(self):
        dlg = DlgAddTask(self.settings, self)
        rt = dlg.exec_()
        if rt == QDialog.Accepted:
            task = dlg.getTask()
            task.taskId = len(self.tasklist)

            row = self.tb_task.rowCount()
            self.tb_task.setRowCount(row+1)
            self.tb_task.setItem(row, 0, QTableWidgetItem(task.mapType))
            self.tb_task.setItem(row, 1, QTableWidgetItem(str(task.minLevel)+"-->"+str(task.maxLevel)))
            self.tb_task.setItem(row, 2, QTableWidgetItem(task.area))
            self.tb_task.setItem(row, 3, QTableWidgetItem(task.status))

            prgs = QProgressBar()
            prgs.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
            prgs.setFormat("%v/%m")
            prgs.setTextVisible(True)
            prgs.setMinimum(0)
            prgs.setMaximum(task.totalTiles)
            task.signals.sigProgress.connect(self.onProgress)
            task.signals.sigStatuChange.connect(self.onTaskStatuChanged)
            self.tb_task.setCellWidget(row, 4, prgs)

            self.tasklist.append(task)
        else:
            print("Rejected")

    def onStart(self):
        self.threadpool.setMaxThreadCount(int(self.le_threadnum.text()))
        for task in self.tasklist:
            task.setRootDir(self.le_path.text()+"/")
            self.threadpool.start(task)

    @Slot(int, int)
    def onProgress(self, taskid, val):
        prgs = self.tb_task.cellWidget(taskid, 4)
        if prgs and isinstance(prgs, QProgressBar):
            prgs.setValue(val)

    @Slot(int, str)
    def onTaskStatuChanged(self, taskid, statustr):
        self.tb_task.setItem(taskid, 3, QTableWidgetItem(statustr) )
