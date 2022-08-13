from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from interfaces.untitled import Ui_MainWindow
from interfaces.prueba import *
from interfaces.subventan import *
import pyqtgraph as pg
import numpy as np
import re


import sys


class Subventana(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.mostrar_mensaje)
        self.pushButton.clicked.connect(self.close)
        self.subventan = Subventana()

    def mostrar_mensaje(self):
        fucn = str(self.lineEdit.text())
        setFunction(fucn)
        a = float(str(self.lineEdit_2.text()))
        b = float(str(self.lineEdit_3.text()))
        n = float(str(self.lineEdit_4.text()))
        hola = str(simpson(a, b, n))
        # graficos
        x, y = graphic(a, b)

        self.subventan.label_num.setText(hola)
        self.subventan.widget.setBackground("w")
        self.subventan.widget.plot(x, y, pen=pg.mkPen("r", width=3))
        self.subventan.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
