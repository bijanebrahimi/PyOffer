#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from pyoffer.ui.mainwindow import MainWindow
from pyoffer.plugins.digikala.digikala import DigikalaWidget


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = MainWindow()
    w.show()

    sys.exit(app.exec_())
