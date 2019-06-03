# -*- coding: utf-8 -*-
'''
Created on 2019年5月31日

@author: sparcle
'''

import sys
from PySide2.QtWidgets import QApplication
from mainwnd import MainWnd

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MainWnd()
    wnd.show()
    app.exec_()
