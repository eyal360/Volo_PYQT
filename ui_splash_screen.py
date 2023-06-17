# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenywQcJg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import splash_window_icons_rc

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(928, 432)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setGeometry(QRect(10, 10, 911, 411))
        self.main_frame.setAutoFillBackground(False)
        self.main_frame.setStyleSheet(u"background-color: rgb(236,211,175);")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.main_frame.setLineWidth(0)
        self.splash_progress = QProgressBar(self.main_frame)
        self.splash_progress.setObjectName(u"splash_progress")
        self.splash_progress.setGeometry(QRect(80, 270, 781, 41))
        self.splash_progress.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	background-color: rgb(236,211,175);\n"
"\n"
"	color: rgb(255,255,255);\n"
"	border-style: none;\n"
"	border-radius: 15px;\n"
"	text-align: center;\n"
"	font: 75 12pt \"Segoe UI-Semibold\";\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius: 15px;	\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.506, x2:0, y2:0.495, stop:0.348259 rgba(189, 206, 233, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"")
        self.splash_progress.setValue(24)
        self.splash_progress.setOrientation(Qt.Horizontal)
        self.splash_progress.setTextDirection(QProgressBar.TopToBottom)
        self.splash_headline_label = QLabel(self.main_frame)
        self.splash_headline_label.setObjectName(u"splash_headline_label")
        self.splash_headline_label.setGeometry(QRect(220, 10, 621, 161))
        self.splash_headline_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.splash_sub_headline_label = QLabel(self.main_frame)
        self.splash_sub_headline_label.setObjectName(u"splash_sub_headline_label")
        self.splash_sub_headline_label.setGeometry(QRect(450, 130, 401, 61))
        self.splash_sub_headline_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.splash_author_label = QLabel(self.main_frame)
        self.splash_author_label.setObjectName(u"splash_author_label")
        self.splash_author_label.setGeometry(QRect(690, 380, 211, 20))
        self.splash_author_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.progress_loading_label = QLabel(self.main_frame)
        self.progress_loading_label.setObjectName(u"progress_loading_label")
        self.progress_loading_label.setGeometry(QRect(390, 310, 141, 31))
        self.progress_loading_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.volo_icon = QLabel(self.main_frame)
        self.volo_icon.setObjectName(u"volo_icon")
        self.volo_icon.setGeometry(QRect(-30, -10, 311, 311))
        self.volo_icon.setStyleSheet(u"image: url(:/icons/logo/Pheonix.png);")
        self.volo_icon.setPixmap(QPixmap(u":/splash_logo/logo/Pheonix.ico"))
        self.volo_icon.setScaledContents(True)
        self.volo_icon.raise_()
        self.splash_progress.raise_()
        self.splash_headline_label.raise_()
        self.splash_sub_headline_label.raise_()
        self.splash_author_label.raise_()
        self.progress_loading_label.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.splash_headline_label.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-size:48pt; font-weight:600;\">Volo </span><span style=\" font-size:48pt;\">Productions</span></p></body></html>", None))
        self.splash_sub_headline_label.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">|by S</span><span style=\" font-size:28pt;\">hiran </span><span style=\" font-size:28pt; font-weight:600;\">H</span><span style=\" font-size:28pt;\">arutz</span></p></body></html>", None))
        self.splash_author_label.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p align=\"right\"><span style=\" font-size:7.8pt;\">\u05e0\u05db\u05ea\u05d1 \u05e2\u05dc \u05d9\u05d3\u05d9 \u05d0.\u05d7 \u05e2\u05dc \u05de\u05dc\u05d0</span></p></body></html>", None))
        self.progress_loading_label.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">...\u05d8\u05d5\u05e2\u05df</span></p></body></html>", None))
        self.volo_icon.setText("")
    # retranslateUi

