# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'warning_windowRklNnN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import dialog_rc

class Ui_WarningWindow(object):
    def setupUi(self, WarningWindow):
        if not WarningWindow.objectName():
            WarningWindow.setObjectName(u"WarningWindow")
        WarningWindow.resize(472, 177)
        WarningWindow.setStyleSheet(u"background-color: rgb(236,211,175);\n"
"")
        self.centralwidget = QWidget(WarningWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.delete_button = QPushButton(self.centralwidget)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(320, 120, 131, 41))
        self.delete_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(227,140,140);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semilight\";\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(223,66,66);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(221,9,9);\n"
"}")
        self.cancel_button = QPushButton(self.centralwidget)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(20, 120, 131, 41))
        self.cancel_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(151,151,153);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semilight\";\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(130,130,131);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(108,108,109);\n"
"}")
        self.warning_subtext = QLabel(self.centralwidget)
        self.warning_subtext.setObjectName(u"warning_subtext")
        self.warning_subtext.setGeometry(QRect(50, 50, 341, 31))
        self.warning_subtext.setCursor(QCursor(Qt.BlankCursor))
        self.warning_subtext.setStyleSheet(u"font: 16pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.warning_subtext.setLineWidth(0)
        self.warning_subtext.setScaledContents(False)
        self.warning_subtext.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.unicorn_label = QLabel(self.centralwidget)
        self.unicorn_label.setObjectName(u"unicorn_label")
        self.unicorn_label.setGeometry(QRect(370, 49, 81, 71))
        self.unicorn_label.setStyleSheet(u"background-image: url(:/dialog/misc/sadunicorn_small_new.png);")
        self.unicorn_label.setScaledContents(True)
        self.warning_text = QLabel(self.centralwidget)
        self.warning_text.setObjectName(u"warning_text")
        self.warning_text.setGeometry(QRect(30, 0, 411, 51))
        self.warning_text.setCursor(QCursor(Qt.BlankCursor))
        self.warning_text.setStyleSheet(u"font: 16pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.warning_text.setLineWidth(0)
        self.warning_text.setScaledContents(False)
        self.warning_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        WarningWindow.setCentralWidget(self.centralwidget)
        self.delete_button.raise_()
        self.cancel_button.raise_()
        self.unicorn_label.raise_()
        self.warning_text.raise_()
        self.warning_subtext.raise_()

        self.retranslateUi(WarningWindow)

        QMetaObject.connectSlotsByName(WarningWindow)
    # setupUi

    def retranslateUi(self, WarningWindow):
        WarningWindow.setWindowTitle(QCoreApplication.translate("WarningWindow", u"MainWindow", None))
        self.delete_button.setText(QCoreApplication.translate("WarningWindow", u"\u05de\u05d7\u05d9\u05e7\u05d4", None))
        self.cancel_button.setText(QCoreApplication.translate("WarningWindow", u"\u05d1\u05d9\u05d8\u05d5\u05dc", None))
        self.warning_subtext.setText(QCoreApplication.translate("WarningWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semibold'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; color:#ef4040;\">!\u05dc\u05d0\u05d7\u05e8 \u05e4\u05e2\u05d5\u05dc\u05d4 \u05d6\u05d5 \u05dc\u05d0 \u05e0\u05d9\u05ea\u05df \u05dc\u05e9\u05d7\u05d6\u05e8 \u05d0\u05ea \u05d4\u05de\u05d9\u05d3\u05e2</span></p></body></html>", None))
        self.unicorn_label.setText("")
        self.warning_text.setText(QCoreApplication.translate("WarningWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semibold'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u05d1\u05d7\u05e8\u05ea \u05dc\u05de\u05d7\u05d5\u05e7 \u05d0\u05ea \u05db\u05dc \u05d4\u05e1\u05e4\u05e7\u05d9\u05dd</p></body></html>", None))
    # retranslateUi

