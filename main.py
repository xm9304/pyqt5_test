import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import pandas as pd
import openpyxl as spxy

import test


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = test.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
