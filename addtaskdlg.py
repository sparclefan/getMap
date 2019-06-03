# -*- coding: utf-8 -*-
#
# Created on 2019/5/31
#
# @author: Sparcle F.
# Copyright: Beijing Yupont Electric Power Technology co.,ltd. 2013-2019

from PySide2.QtWidgets import QDialog
from ui_addtaskdlg import Ui_Dialog
from task import Task


class TaskOptions:
    pass


class DlgAddTask(QDialog, Ui_Dialog):
    def __init__(self, settings, parent=None):
        super(DlgAddTask, self).__init__(parent)
        self.setupUi(self)

        self.settings = settings
        for key in settings.getMapTypeList():
            self.cb_mapTypes.addItem(key)

        self.cb_range.addItem("全球")
        for key in settings.getAreaList():
            self.cb_range.addItem(key)

    def getTask(self):
        options = TaskOptions
        options.mapType = self.cb_mapTypes.currentText()
        options.url = self.settings.getUrl(self.cb_mapTypes.currentText())
        options.minLevel = self.sp_level.value()
        options.maxLevel = self.sp_level_2.value()
        options.area = self.cb_range.currentText()
        options.range = self.settings.getAreaRange(self.cb_range.currentText())
        options.timeout = int(self.le_timeout.text())
        options.maxRetry = int(self.le_retry.text())
        return Task(options)
