# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/addtaskdlg.ui',
# licensing of './ui/addtaskdlg.ui' applies.
#
# Created: Mon Jun  3 08:41:57 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(554, 267)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(440, 10, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(30, 10, 391, 231))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 36, 18))
        self.label.setObjectName("label")
        self.cb_mapTypes = QtWidgets.QComboBox(self.frame)
        self.cb_mapTypes.setGeometry(QtCore.QRect(90, 15, 251, 24))
        self.cb_mapTypes.setObjectName("cb_mapTypes")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(21, 70, 36, 18))
        self.label_2.setObjectName("label_2")
        self.sp_level = QtWidgets.QSpinBox(self.frame)
        self.sp_level.setGeometry(QtCore.QRect(91, 70, 49, 24))
        self.sp_level.setMaximum(19)
        self.sp_level.setObjectName("sp_level")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 36, 18))
        self.label_3.setObjectName("label_3")
        self.cb_range = QtWidgets.QComboBox(self.frame)
        self.cb_range.setGeometry(QtCore.QRect(88, 121, 251, 24))
        self.cb_range.setObjectName("cb_range")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(149, 70, 72, 18))
        self.label_4.setObjectName("label_4")
        self.sp_level_2 = QtWidgets.QSpinBox(self.frame)
        self.sp_level_2.setGeometry(QtCore.QRect(230, 70, 49, 24))
        self.sp_level_2.setMaximum(19)
        self.sp_level_2.setObjectName("sp_level_2")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(20, 180, 131, 27))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.le_timeout = QtWidgets.QLineEdit(self.widget)
        self.le_timeout.setObjectName("le_timeout")
        self.horizontalLayout.addWidget(self.le_timeout)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.widget1 = QtWidgets.QWidget(self.frame)
        self.widget1.setGeometry(QtCore.QRect(210, 180, 141, 27))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.widget1)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.le_retry = QtWidgets.QLineEdit(self.widget1)
        self.le_retry.setObjectName("le_retry")
        self.horizontalLayout_2.addWidget(self.le_retry)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "新增下载任务", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "地图", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog", "级别", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Dialog", "范围", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Dialog", "------->", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Dialog", "超时", None, -1))
        self.le_timeout.setText(QtWidgets.QApplication.translate("Dialog", "30", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("Dialog", "秒", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Dialog", "重试次数", None, -1))
        self.le_retry.setText(QtWidgets.QApplication.translate("Dialog", "3", None, -1))

