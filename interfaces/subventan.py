# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'designerBpZcEg.ui'
##
# Created by: Qt User Interface Compiler version 6.1.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from pyqtgraph import PlotWidget


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(606, 427)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(17, 21, 57, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        brush3 = QBrush(QColor(240, 240, 240, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        brush4 = QBrush(QColor(120, 120, 120, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        Form.setPalette(palette)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 10, 281, 61))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        self.label.setPalette(palette1)
        font = QFont()
        font.setFamilies([u"Script MT Bold"])
        font.setPointSize(34)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 90, 71, 31))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_2.setFont(font1)
        self.label_num = QLabel(Form)
        self.label_num.setObjectName(u"label_num")
        self.label_num.setGeometry(QRect(120, 90, 171, 31))
        self.label_num.setFont(font1)
        self.widget = PlotWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 140, 521, 271))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate(
            "Form", u"Resultado", None))
        self.label.setText(QCoreApplication.translate(
            "Form", u"RESULTADO", None))
        self.label_2.setText(
            QCoreApplication.translate("Form", u"Valor:", None))
        self.label_num.setText(
            QCoreApplication.translate("Form", u"0.121931", None))
    # retranslateUi
