# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowaselyu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import main_window_icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1311, 820)
        MainWindow.setStyleSheet(u"background-color: rgb(236,211,175);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.upper_frame = QFrame(self.centralwidget)
        self.upper_frame.setObjectName(u"upper_frame")
        self.upper_frame.setGeometry(QRect(0, 0, 1311, 101))
        font = QFont()
        font.setPointSize(15)
        self.upper_frame.setFont(font)
        self.upper_frame.setStyleSheet(u"background-color: rgb(236,211,175);")
        self.upper_frame.setFrameShape(QFrame.StyledPanel)
        self.upper_frame.setFrameShadow(QFrame.Raised)
        self.upper_frame_header_btn = QPushButton(self.upper_frame)
        self.upper_frame_header_btn.setObjectName(u"upper_frame_header_btn")
        self.upper_frame_header_btn.setGeometry(QRect(110, 0, 721, 101))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(55)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(7)
        self.upper_frame_header_btn.setFont(font1)
        self.upper_frame_header_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.upper_frame_header_btn.setMouseTracking(True)
        self.upper_frame_header_btn.setFocusPolicy(Qt.ClickFocus)
        self.upper_frame_header_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(236,211,175);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 55pt \"Segoe UI Semibold\";\n"
"	border-radius: 0px;\n"
"}\n"
"")
        self.headline_logo_btn = QPushButton(self.upper_frame)
        self.headline_logo_btn.setObjectName(u"headline_logo_btn")
        self.headline_logo_btn.setGeometry(QRect(-20, -20, 131, 131))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semibold")
        font2.setPointSize(42)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(7)
        self.headline_logo_btn.setFont(font2)
        self.headline_logo_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.headline_logo_btn.setMouseTracking(True)
        self.headline_logo_btn.setFocusPolicy(Qt.ClickFocus)
        self.headline_logo_btn.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/logo/Pheonix.ico);\n"
"	background-color: rgb(236,211,175);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 42pt \"Segoe UI Semibold\";\n"
"	border-radius: 0px;\n"
"}\n"
"")
        self.leads_date_label = QLabel(self.upper_frame)
        self.leads_date_label.setObjectName(u"leads_date_label")
        self.leads_date_label.setGeometry(QRect(930, 60, 371, 31))
        self.leads_date_label.setLayoutDirection(Qt.RightToLeft)
        self.leads_date_label.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(236,211,175);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 15pt \"Segoe UI Semibold\";\n"
"	border-radius: 0px;\n"
"}")
        self.leads_date_label.setFrameShape(QFrame.NoFrame)
        self.leads_date_label.setLineWidth(0)
        self.leads_date_label.setTextFormat(Qt.AutoText)
        self.leads_date_label.setScaledContents(False)
        self.leads_date_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.leads_date_label.setWordWrap(False)
        self.setting_btn = QPushButton(self.upper_frame)
        self.setting_btn.setObjectName(u"setting_btn")
        self.setting_btn.setGeometry(QRect(410, 40, 61, 51))
        self.setting_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.setting_btn.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/misc/settings_icon.png);\n"
"	border: 0px solid;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(236,211,175);\n"
"}")
        self.upper_frame_logo_btn = QPushButton(self.upper_frame)
        self.upper_frame_logo_btn.setObjectName(u"upper_frame_logo_btn")
        self.upper_frame_logo_btn.setGeometry(QRect(170, 40, 51, 51))
        self.upper_frame_logo_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.upper_frame_logo_btn.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/misc/restart_prog_icon.png);\n"
"	border: 0px solid;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(236,211,175);\n"
"}")
        self.setting_btn_2 = QPushButton(self.upper_frame)
        self.setting_btn_2.setObjectName(u"setting_btn_2")
        self.setting_btn_2.setGeometry(QRect(680, 40, 51, 51))
        self.setting_btn_2.setCursor(QCursor(Qt.OpenHandCursor))
        self.setting_btn_2.setStyleSheet(u"QPushButton{	\n"
"	image: url(:/icons/misc/plus_icon.png);\n"
"	border: 0px solid;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(236,211,175);\n"
"}")
        self.backup_info_label = QLabel(self.upper_frame)
        self.backup_info_label.setObjectName(u"backup_info_label")
        self.backup_info_label.setGeometry(QRect(870, 10, 431, 31))
        self.backup_info_label.setLayoutDirection(Qt.RightToLeft)
        self.backup_info_label.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(236,211,175);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 11pt \"Segoe UI Semibold\";\n"
"	border-radius: 0px;\n"
"}")
        self.backup_info_label.setFrameShape(QFrame.NoFrame)
        self.backup_info_label.setLineWidth(0)
        self.backup_info_label.setTextFormat(Qt.AutoText)
        self.backup_info_label.setScaledContents(False)
        self.backup_info_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.backup_info_label.setWordWrap(False)
        self.lower_frame = QFrame(self.centralwidget)
        self.lower_frame.setObjectName(u"lower_frame")
        self.lower_frame.setGeometry(QRect(0, 740, 1311, 81))
        self.lower_frame.setCursor(QCursor(Qt.WhatsThisCursor))
        self.lower_frame.setFrameShape(QFrame.StyledPanel)
        self.lower_frame.setFrameShadow(QFrame.Raised)
        self.FB_btn = QPushButton(self.lower_frame)
        self.FB_btn.setObjectName(u"FB_btn")
        self.FB_btn.setGeometry(QRect(260, 10, 61, 61))
        self.FB_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.FB_btn.setFocusPolicy(Qt.StrongFocus)
        self.FB_btn.setAutoFillBackground(False)
        self.FB_btn.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/social/FB.png);\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 1px solid #FFFFFF;\n"
"	border-width: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 0px solid #FFFFFF;\n"
"}")
        self.FB_btn.setAutoRepeatDelay(300)
        self.FB_btn.setAutoDefault(False)
        self.FB_btn.setFlat(True)
        self.whatsapp_btn = QPushButton(self.lower_frame)
        self.whatsapp_btn.setObjectName(u"whatsapp_btn")
        self.whatsapp_btn.setGeometry(QRect(430, 10, 61, 61))
        self.whatsapp_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.whatsapp_btn.setFocusPolicy(Qt.StrongFocus)
        self.whatsapp_btn.setAutoFillBackground(False)
        self.whatsapp_btn.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/social/whatsapp.png);\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 1px solid #FFFFFF;\n"
"	border-width: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 0px solid #FFFFFF;\n"
"}")
        self.whatsapp_btn.setAutoRepeatDelay(300)
        self.whatsapp_btn.setAutoDefault(False)
        self.whatsapp_btn.setFlat(True)
        self.instagram_btn = QPushButton(self.lower_frame)
        self.instagram_btn.setObjectName(u"instagram_btn")
        self.instagram_btn.setGeometry(QRect(590, 10, 61, 61))
        self.instagram_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.instagram_btn.setFocusPolicy(Qt.StrongFocus)
        self.instagram_btn.setAutoFillBackground(False)
        self.instagram_btn.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/social/instagram.png);\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 1px solid #FFFFFF;\n"
"	border-width: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 0px solid #FFFFFF;\n"
"}")
        self.instagram_btn.setAutoRepeatDelay(300)
        self.instagram_btn.setAutoDefault(False)
        self.instagram_btn.setFlat(True)
        self.gmail_btn = QPushButton(self.lower_frame)
        self.gmail_btn.setObjectName(u"gmail_btn")
        self.gmail_btn.setGeometry(QRect(750, 10, 61, 61))
        self.gmail_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.gmail_btn.setFocusPolicy(Qt.StrongFocus)
        self.gmail_btn.setAutoFillBackground(False)
        self.gmail_btn.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/social/GMAIL.png);\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 1px solid #FFFFFF;\n"
"	border-width: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 0px solid #FFFFFF;\n"
"}")
        self.gmail_btn.setAutoRepeatDelay(300)
        self.gmail_btn.setAutoDefault(False)
        self.gmail_btn.setFlat(True)
        self.calender_btn = QPushButton(self.lower_frame)
        self.calender_btn.setObjectName(u"calender_btn")
        self.calender_btn.setGeometry(QRect(900, 10, 61, 61))
        self.calender_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.calender_btn.setFocusPolicy(Qt.StrongFocus)
        self.calender_btn.setAutoFillBackground(False)
        self.calender_btn.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/social/calender.png);\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 1px solid #FFFFFF;\n"
"	border-width: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 0px solid #FFFFFF;\n"
"}")
        self.calender_btn.setAutoRepeatDelay(300)
        self.calender_btn.setAutoDefault(False)
        self.calender_btn.setFlat(True)
        self.splash_author_label = QLabel(self.lower_frame)
        self.splash_author_label.setObjectName(u"splash_author_label")
        self.splash_author_label.setGeometry(QRect(1080, 50, 221, 20))
        self.splash_author_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.buttons_frame = QFrame(self.centralwidget)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setGeometry(QRect(0, 100, 1311, 111))
        self.buttons_frame.setMouseTracking(True)
        self.buttons_frame.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.buttons_frame.setFrameShape(QFrame.NoFrame)
        self.buttons_frame.setFrameShadow(QFrame.Raised)
        self.events_button = QPushButton(self.buttons_frame)
        self.events_button.setObjectName(u"events_button")
        self.events_button.setGeometry(QRect(660, 10, 211, 91))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Semibold")
        font3.setPointSize(20)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(7)
        self.events_button.setFont(font3)
        self.events_button.setCursor(QCursor(Qt.OpenHandCursor))
        self.events_button.setMouseTracking(True)
        self.events_button.setFocusPolicy(Qt.ClickFocus)
        self.events_button.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0, 0, 0);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(137,236,218);	\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(151,186,172);\n"
"}")
        self.leads_button = QPushButton(self.buttons_frame)
        self.leads_button.setObjectName(u"leads_button")
        self.leads_button.setGeometry(QRect(430, 10, 211, 91))
        self.leads_button.setFont(font3)
        self.leads_button.setCursor(QCursor(Qt.OpenHandCursor))
        self.leads_button.setMouseTracking(True)
        self.leads_button.setFocusPolicy(Qt.ClickFocus)
        self.leads_button.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0, 0, 0);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(196,213,242);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(196,197,242);\n"
"}")
        self.suppliers_button = QPushButton(self.buttons_frame)
        self.suppliers_button.setObjectName(u"suppliers_button")
        self.suppliers_button.setGeometry(QRect(200, 10, 211, 91))
        self.suppliers_button.setFont(font3)
        self.suppliers_button.setCursor(QCursor(Qt.OpenHandCursor))
        self.suppliers_button.setMouseTracking(True)
        self.suppliers_button.setFocusPolicy(Qt.ClickFocus)
        self.suppliers_button.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0, 0, 0);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255,211,182);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255,170,165);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.clients_button = QPushButton(self.buttons_frame)
        self.clients_button.setObjectName(u"clients_button")
        self.clients_button.setGeometry(QRect(900, 10, 211, 91))
        self.clients_button.setFont(font3)
        self.clients_button.setCursor(QCursor(Qt.OpenHandCursor))
        self.clients_button.setMouseTracking(True)
        self.clients_button.setFocusPolicy(Qt.ClickFocus)
        self.clients_button.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0, 0, 0);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(186,225,255);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(167,202,229);\n"
"}")
        self.center_frame = QFrame(self.centralwidget)
        self.center_frame.setObjectName(u"center_frame")
        self.center_frame.setGeometry(QRect(0, 220, 1311, 521))
        self.center_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.center_frame.setFrameShape(QFrame.StyledPanel)
        self.center_frame.setFrameShadow(QFrame.Raised)
        self.stacked_events_and_leads = QStackedWidget(self.center_frame)
        self.stacked_events_and_leads.setObjectName(u"stacked_events_and_leads")
        self.stacked_events_and_leads.setGeometry(QRect(0, -20, 1311, 531))
        self.stacked_events_and_leads.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.GIF_label = QLabel(self.home_page)
        self.GIF_label.setObjectName(u"GIF_label")
        self.GIF_label.setGeometry(QRect(230, -140, 871, 681))
        self.GIF_label.setCursor(QCursor(Qt.CrossCursor))
        self.GIF_label.setStyleSheet(u"border-image: url(:/icons/logo/FullsizeLOGO.png);")
        self.GIF_label.setScaledContents(True)
        self.GIF_label.setAlignment(Qt.AlignCenter)
        self.GIF_label.setTextInteractionFlags(Qt.NoTextInteraction)
        self.pauseGIF_btn = QPushButton(self.home_page)
        self.pauseGIF_btn.setObjectName(u"pauseGIF_btn")
        self.pauseGIF_btn.setGeometry(QRect(70, 480, 51, 51))
        self.pauseGIF_btn.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid #C9C9FF;\n"
"	image: url(:/icons/GIF/pause_btn.png);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid #32AE32;\n"
"	border-width: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 0px solid #32AE32;\n"
"}")
        self.playGIF_btn = QPushButton(self.home_page)
        self.playGIF_btn.setObjectName(u"playGIF_btn")
        self.playGIF_btn.setGeometry(QRect(10, 480, 51, 51))
        self.playGIF_btn.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid #C9C9FF;\n"
"	image: url(:/icons/GIF/play_btn.png);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid #32AE32;\n"
"	border-width: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 0px solid #32AE32;\n"
"}")
        self.nextGIF_btn = QPushButton(self.home_page)
        self.nextGIF_btn.setObjectName(u"nextGIF_btn")
        self.nextGIF_btn.setGeometry(QRect(130, 480, 51, 51))
        self.nextGIF_btn.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid #C9C9FF;\n"
"	\n"
"	image: url(:/gif/GIF/next_btn.png);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid #32AE32;\n"
"	border-width: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 0px solid #32AE32;\n"
"}")
        self.logo_browse_btn = QPushButton(self.home_page)
        self.logo_browse_btn.setObjectName(u"logo_browse_btn")
        self.logo_browse_btn.setGeometry(QRect(680, 380, 341, 51))
        font4 = QFont()
        font4.setFamily(u"Segoe UI Semilight")
        font4.setPointSize(20)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(7)
        self.logo_browse_btn.setFont(font4)
        self.logo_browse_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.logo_browse_btn.setMouseTracking(True)
        self.logo_browse_btn.setFocusPolicy(Qt.ClickFocus)
        self.logo_browse_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170,170,170);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid #090206;\n"
"	font: 63 20pt \"Segoe UI Semilight\";\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(133, 166, 177);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(133, 166, 177);\n"
"	font: 63 21pt \"Segoe UI Semibold\";\n"
"}")
        self.logo_notunique_warning = QLabel(self.home_page)
        self.logo_notunique_warning.setObjectName(u"logo_notunique_warning")
        self.logo_notunique_warning.setGeometry(QRect(735, 440, 221, 31))
        self.logo_notunique_warning.setStyleSheet(u"font: 11pt \"Segoe UI Semibold\";\n"
"color: rgb(239, 64, 64);")
        self.logo_notphoto_warning = QLabel(self.home_page)
        self.logo_notphoto_warning.setObjectName(u"logo_notphoto_warning")
        self.logo_notphoto_warning.setGeometry(QRect(730, 440, 241, 31))
        self.logo_notphoto_warning.setStyleSheet(u"font: 11pt \"Segoe UI Semibold\";\n"
"color: rgb(239, 64, 64);")
        self.reset_logo_btn = QPushButton(self.home_page)
        self.reset_logo_btn.setObjectName(u"reset_logo_btn")
        self.reset_logo_btn.setGeometry(QRect(615, 380, 51, 51))
        font5 = QFont()
        font5.setFamily(u"Segoe UI Semilight")
        font5.setPointSize(18)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(7)
        self.reset_logo_btn.setFont(font5)
        self.reset_logo_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.reset_logo_btn.setMouseTracking(True)
        self.reset_logo_btn.setFocusPolicy(Qt.ClickFocus)
        self.reset_logo_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170,170,170);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid #090206;\n"
"	font: 63 18pt \"Segoe UI Semilight\";\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(249,77,77);\n"
"	font: 63 22pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(170,170,170);\n"
"	font: 63 22pt \"Segoe UI Semibold\";\n"
"}")
        self.backup_Setup_btn = QPushButton(self.home_page)
        self.backup_Setup_btn.setObjectName(u"backup_Setup_btn")
        self.backup_Setup_btn.setGeometry(QRect(365, 380, 191, 51))
        self.backup_Setup_btn.setFont(font4)
        self.backup_Setup_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.backup_Setup_btn.setMouseTracking(True)
        self.backup_Setup_btn.setFocusPolicy(Qt.ClickFocus)
        self.backup_Setup_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170,170,170);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid #090206;\n"
"	font: 63 20pt \"Segoe UI Semilight\";\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(133, 166, 177);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(133, 166, 177);\n"
"	font: 63 21pt \"Segoe UI Semibold\";\n"
"}")
        self.line = QFrame(self.home_page)
        self.line.setObjectName(u"line")
        self.line.setWindowModality(Qt.ApplicationModal)
        self.line.setGeometry(QRect(590, 370, 3, 150))
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.VLine)
        self.backup_options_combobox = QComboBox(self.home_page)
        self.backup_options_combobox.addItem("")
        self.backup_options_combobox.addItem("")
        self.backup_options_combobox.addItem("")
        self.backup_options_combobox.addItem("")
        self.backup_options_combobox.addItem("")
        self.backup_options_combobox.addItem("")
        self.backup_options_combobox.setObjectName(u"backup_options_combobox")
        self.backup_options_combobox.setGeometry(QRect(310, 440, 181, 41))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backup_options_combobox.sizePolicy().hasHeightForWidth())
        self.backup_options_combobox.setSizePolicy(sizePolicy)
        self.backup_options_combobox.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(whatsthis)
        self.backup_options_combobox.setWhatsThis(u"<html><head/><body><p align=\"center\">\u05d1\u05d7\u05e8 \u05e1\u05d5\u05d2 \u05d0\u05d9\u05e8\u05d5\u05e2</p></body></html>")
#endif // QT_CONFIG(whatsthis)
        self.backup_options_combobox.setLayoutDirection(Qt.RightToLeft)
        self.backup_options_combobox.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border: 1px solid #090206;\n"
"background-color: rgb(255,255,255);")
        self.backup_options_combobox.setEditable(True)
        self.backup_options_combobox.setInsertPolicy(QComboBox.InsertAtBottom)
        self.backup_options_combobox.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.backup_options_combobox.setMinimumContentsLength(0)
        self.backup_options_combobox.setDuplicatesEnabled(False)
        self.restore_backup_btn = QPushButton(self.home_page)
        self.restore_backup_btn.setObjectName(u"restore_backup_btn")
        self.restore_backup_btn.setGeometry(QRect(305, 380, 51, 51))
        self.restore_backup_btn.setFont(font4)
        self.restore_backup_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.restore_backup_btn.setMouseTracking(True)
        self.restore_backup_btn.setFocusPolicy(Qt.ClickFocus)
        self.restore_backup_btn.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/misc/restore_icon.png);\n"
"	background-color: rgb(170,170,170);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid #090206;\n"
"	font: 63 20pt \"Segoe UI Semilight\";\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(133,177,144);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(170,170,170);\n"
"	font: 63 21pt \"Segoe UI Semibold\";\n"
"}")
        self.backup_freq_label = QLabel(self.home_page)
        self.backup_freq_label.setObjectName(u"backup_freq_label")
        self.backup_freq_label.setGeometry(QRect(500, 440, 81, 41))
        self.backup_freq_label.setStyleSheet(u"font: 63 14pt \"Segoe UI Semibold\";\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"\n"
"")
        self.restart_backup_warning = QLabel(self.home_page)
        self.restart_backup_warning.setObjectName(u"restart_backup_warning")
        self.restart_backup_warning.setGeometry(QRect(285, 490, 291, 31))
        self.restart_backup_warning.setStyleSheet(u"font: 11pt \"Segoe UI Semibold\";\n"
"color: rgb(239, 64, 64);")
        self.restart_for_backup_btn = QPushButton(self.home_page)
        self.restart_for_backup_btn.setObjectName(u"restart_for_backup_btn")
        self.restart_for_backup_btn.setGeometry(QRect(165, 490, 111, 31))
        font6 = QFont()
        font6.setFamily(u"Segoe UI Semilight")
        font6.setPointSize(13)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(7)
        self.restart_for_backup_btn.setFont(font6)
        self.restart_for_backup_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.restart_for_backup_btn.setMouseTracking(True)
        self.restart_for_backup_btn.setFocusPolicy(Qt.ClickFocus)
        self.restart_for_backup_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170,170,170);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid #090206;\n"
"	font: 63 13pt \"Segoe UI Semilight\";\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(133,177,144);\n"
"	font: 63 13pt \"Segoe UI Semilight\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(170,170,170);\n"
"	font: 63 14pt \"Segoe UI Semibold\";\n"
"}")
        self.quote_label = QLabel(self.home_page)
        self.quote_label.setObjectName(u"quote_label")
        self.quote_label.setGeometry(QRect(420, 400, 491, 71))
        self.quote_label.setCursor(QCursor(Qt.CrossCursor))
        self.quote_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 63 20pt \"Segoe UI Semilight\";\n"
"border-radius: 20px;\n"
"background-color: rgb(236, 211, 175);\n"
"")
        self.quote_label.setFrameShape(QFrame.NoFrame)
        self.quote_label.setLineWidth(0)
        self.quote_label.setAlignment(Qt.AlignCenter)
        self.quote_label.setMargin(0)
        self.stacked_events_and_leads.addWidget(self.home_page)
        self.leads_page = QWidget()
        self.leads_page.setObjectName(u"leads_page")
        self.leads_frame = QFrame(self.leads_page)
        self.leads_frame.setObjectName(u"leads_frame")
        self.leads_frame.setGeometry(QRect(0, 20, 1311, 521))
        self.leads_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.leads_frame.setFrameShape(QFrame.NoFrame)
        self.leads_frame.setFrameShadow(QFrame.Raised)
        self.leads_frame.setLineWidth(4)
        self.leads_head_label_line = QFrame(self.leads_frame)
        self.leads_head_label_line.setObjectName(u"leads_head_label_line")
        self.leads_head_label_line.setGeometry(QRect(480, 10, 118, 3))
        self.leads_head_label_line.setStyleSheet(u"border: 2px solid #C4D5F2;\n"
"")
        self.leads_head_label_line.setFrameShape(QFrame.HLine)
        self.leads_head_label_line.setFrameShadow(QFrame.Sunken)
        self.leads_head_label = QLabel(self.leads_frame)
        self.leads_head_label.setObjectName(u"leads_head_label")
        self.leads_head_label.setGeometry(QRect(500, 20, 81, 21))
        self.leads_head_label.setStyleSheet(u"QLabel {\n"
"	color: rgb(196,213,242);\n"
"	font: 63 14pt \"Segoe UI Semibold\";\n"
"	border-radius:15px;\n"
"}")
        self.leads_head_label.setFrameShape(QFrame.NoFrame)
        self.leads_head_label.setLineWidth(0)
        self.leads_head_label.setTextFormat(Qt.AutoText)
        self.leads_head_label.setScaledContents(False)
        self.leads_head_label.setAlignment(Qt.AlignCenter)
        self.leads_head_label.setWordWrap(False)
        self.leads_page_stacked = QStackedWidget(self.leads_frame)
        self.leads_page_stacked.setObjectName(u"leads_page_stacked")
        self.leads_page_stacked.setGeometry(QRect(40, 50, 971, 411))
        self.previous_leads_btn = QPushButton(self.leads_frame)
        self.previous_leads_btn.setObjectName(u"previous_leads_btn")
        self.previous_leads_btn.setGeometry(QRect(10, 240, 31, 91))
        self.previous_leads_btn.setFont(font4)
        self.previous_leads_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.previous_leads_btn.setMouseTracking(True)
        self.previous_leads_btn.setFocusPolicy(Qt.ClickFocus)
        self.previous_leads_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(151, 152, 186);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semilight\";\n"
"	border: none;	\n"
"	border-radius: 15px;\n"
"	}\n"
"\n"
"QPushButton:hover {\n"
"	font: 63 23pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(196,197,242);\n"
"}")
        self.next_leads_btn = QPushButton(self.leads_frame)
        self.next_leads_btn.setObjectName(u"next_leads_btn")
        self.next_leads_btn.setGeometry(QRect(1010, 240, 31, 91))
        self.next_leads_btn.setFont(font4)
        self.next_leads_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_leads_btn.setMouseTracking(True)
        self.next_leads_btn.setFocusPolicy(Qt.ClickFocus)
        self.next_leads_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(151, 152, 186);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semilight\";\n"
"	border: none;	\n"
"	border-radius: 15px;\n"
"	}\n"
"\n"
"QPushButton:hover {\n"
"	font: 63 23pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(196,197,242);\n"
"}")
        self.leads_page_number_label = QLabel(self.leads_frame)
        self.leads_page_number_label.setObjectName(u"leads_page_number_label")
        self.leads_page_number_label.setGeometry(QRect(530, 470, 41, 41))
        self.leads_page_number_label.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(215,227,246);\n"
"	color: rgb(0, 0, 0);	\n"
"	font: 63 14pt \"Segoe UI Semibold\";\n"
"	border-radius: 20px;\n"
"}")
        self.leads_page_number_label.setAlignment(Qt.AlignCenter)
        self.stacked_events_and_leads.addWidget(self.leads_page)
        self.events_page = QWidget()
        self.events_page.setObjectName(u"events_page")
        self.events_frame = QFrame(self.events_page)
        self.events_frame.setObjectName(u"events_frame")
        self.events_frame.setGeometry(QRect(0, 20, 1311, 521))
        self.events_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.events_frame.setFrameShape(QFrame.NoFrame)
        self.events_frame.setFrameShadow(QFrame.Raised)
        self.events_frame.setLineWidth(4)
        self.events_page_stacked = QStackedWidget(self.events_frame)
        self.events_page_stacked.setObjectName(u"events_page_stacked")
        self.events_page_stacked.setGeometry(QRect(40, 50, 971, 411))
        self.previous_events_btn = QPushButton(self.events_frame)
        self.previous_events_btn.setObjectName(u"previous_events_btn")
        self.previous_events_btn.setGeometry(QRect(10, 240, 31, 91))
        self.previous_events_btn.setFont(font4)
        self.previous_events_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.previous_events_btn.setMouseTracking(True)
        self.previous_events_btn.setFocusPolicy(Qt.ClickFocus)
        self.previous_events_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(151,186,172);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semilight\";\n"
"	border: none;	\n"
"	border-radius: 15px;\n"
"	}\n"
"\n"
"QPushButton:hover {\n"
"	font: 63 23pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(135,167,154);\n"
"}")
        self.next_events_btn = QPushButton(self.events_frame)
        self.next_events_btn.setObjectName(u"next_events_btn")
        self.next_events_btn.setGeometry(QRect(1010, 240, 31, 91))
        self.next_events_btn.setFont(font4)
        self.next_events_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_events_btn.setMouseTracking(True)
        self.next_events_btn.setFocusPolicy(Qt.ClickFocus)
        self.next_events_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(151,186,172);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semilight\";\n"
"	border: none;	\n"
"	border-radius: 15px;\n"
"	}\n"
"\n"
"QPushButton:hover {\n"
"	font: 63 23pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(135,167,154);\n"
"}")
        self.events_page_number_label = QLabel(self.events_frame)
        self.events_page_number_label.setObjectName(u"events_page_number_label")
        self.events_page_number_label.setGeometry(QRect(530, 470, 41, 41))
        self.events_page_number_label.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(137,236,218);;\n"
"	color: rgb(0, 0, 0);	\n"
"	font: 63 14pt \"Segoe UI Semibold\";\n"
"	border-radius: 20px;\n"
"}")
        self.events_page_number_label.setAlignment(Qt.AlignCenter)
        self.events_head_label = QLabel(self.events_frame)
        self.events_head_label.setObjectName(u"events_head_label")
        self.events_head_label.setGeometry(QRect(700, 20, 141, 31))
        self.events_head_label.setStyleSheet(u"QLabel {\n"
"	color: rgb(137,236,218);\n"
"	font: 63 14pt \"Segoe UI Semibold\";\n"
"	border-radius:15px;\n"
"}")
        self.events_head_label.setFrameShape(QFrame.NoFrame)
        self.events_head_label.setLineWidth(0)
        self.events_head_label.setTextFormat(Qt.AutoText)
        self.events_head_label.setScaledContents(False)
        self.events_head_label.setAlignment(Qt.AlignCenter)
        self.events_head_label.setWordWrap(False)
        self.events_head_label_line = QFrame(self.events_frame)
        self.events_head_label_line.setObjectName(u"events_head_label_line")
        self.events_head_label_line.setGeometry(QRect(710, 10, 118, 3))
        self.events_head_label_line.setStyleSheet(u"border: 2px solid #89ECDA;\n"
"")
        self.events_head_label_line.setFrameShape(QFrame.HLine)
        self.events_head_label_line.setFrameShadow(QFrame.Sunken)
        self.stacked_events_and_leads.addWidget(self.events_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.FB_btn.setDefault(False)
        self.whatsapp_btn.setDefault(False)
        self.instagram_btn.setDefault(False)
        self.gmail_btn.setDefault(False)
        self.calender_btn.setDefault(False)
        self.stacked_events_and_leads.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.upper_frame_header_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u05dc\u05d7\u05e5 \u05dc\u05de\u05e2\u05d1\u05e8 \u05dc\u05e2\u05de\u05d5\u05d3 \u05d4\u05e8\u05d0\u05e9\u05d9</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.upper_frame_header_btn.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u05dc\u05d7\u05e5 \u05dc\u05de\u05e2\u05d1\u05e8 \u05dc\u05e2\u05de\u05d5\u05d3 \u05d4\u05e8\u05d0\u05e9\u05d9</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.upper_frame_header_btn.setText(QCoreApplication.translate("MainWindow", u"Volo Productions", None))
#if QT_CONFIG(tooltip)
        self.headline_logo_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.headline_logo_btn.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.headline_logo_btn.setText("")
        self.leads_date_label.setText("")
#if QT_CONFIG(tooltip)
        self.setting_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u05e4\u05ea\u05d7 \u05d4\u05d2\u05d3\u05e8\u05d5\u05ea</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.setting_btn.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u05e4\u05ea\u05d7 \u05d4\u05d2\u05d3\u05e8\u05d5\u05ea</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.setting_btn.setText("")
#if QT_CONFIG(tooltip)
        self.upper_frame_logo_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u05dc\u05d7\u05e5 \u05dc\u05e2\u05d3\u05db\u05d5\u05df \u05de\u05d0\u05d2\u05e8 \u05d4\u05de\u05d9\u05d3\u05e2</span></p><p align=\"center\"><span style=\" font-size:11pt; text-decoration: underline; color:#ff0000;\">\u05d4\u05e9\u05ea\u05de\u05e9 \u05dc\u05d0\u05d7\u05e8: <br/></span><span style=\" font-size:11pt; color:#ff0000;\">\u05d4\u05d5\u05e1\u05e4\u05ea \u05d0\u05d9\u05e8\u05d5\u05e2\u05d9\u05dd \u05d5\u05dc\u05d9\u05d3\u05d9\u05dd <br/>\u05d4\u05d5\u05e1\u05e4\u05ea \u05de\u05e9\u05d9\u05de\u05d5\u05ea</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.upper_frame_logo_btn.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u05dc\u05d7\u05e5 \u05dc\u05e2\u05d3\u05db\u05d5\u05df \u05de\u05d0\u05d2\u05e8 \u05d4\u05de\u05d9\u05d3\u05e2</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.upper_frame_logo_btn.setText("")
#if QT_CONFIG(tooltip)
        self.setting_btn_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u05d4\u05e4\u05e2\u05dc \u05ea\u05d5\u05d1\u05e0\u05d5\u05ea</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.setting_btn_2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u05d4\u05e4\u05e2\u05dc \u05ea\u05d5\u05d1\u05e0\u05d5\u05ea</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.setting_btn_2.setText("")
        self.backup_info_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">\u05d2\u05d9\u05d1\u05d5\u05d9 \u05d0\u05d7\u05e8\u05d5\u05df \u05e0\u05d5\u05e6\u05e8 \u05d1\u05ea\u05d0\u05e8\u05d9\u05da 12/09/2021 \u05d1\u05e9\u05e2\u05d4 01:39</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.FB_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u05e4\u05ea\u05d7 \u05e4\u05d9\u05d9\u05e1\u05d1\u05d5\u05e7</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.FB_btn.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u05e4\u05ea\u05d7 \u05e4\u05d9\u05d9\u05e1\u05d1\u05d5\u05e7</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.FB_btn.setText("")
#if QT_CONFIG(tooltip)
        self.whatsapp_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u05e4\u05ea\u05d7 \u05d5\u05d5\u05d0\u05d8\u05e1\u05d0\u05e4</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.whatsapp_btn.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u05e4\u05ea\u05d7 \u05d5\u05d5\u05d0\u05d8\u05e1\u05d0\u05e4</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.whatsapp_btn.setText("")
#if QT_CONFIG(tooltip)
        self.instagram_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u05e4\u05ea\u05d7 \u05d0\u05d9\u05e0\u05e1\u05d8\u05d2\u05e8\u05dd</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.instagram_btn.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u05e4\u05ea\u05d7 \u05d0\u05d9\u05e0\u05e1\u05d8\u05d2\u05e8\u05dd</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.instagram_btn.setText("")
#if QT_CONFIG(tooltip)
        self.gmail_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u05e4\u05ea\u05d7 \u05d0\u05d9\u05de\u05d9\u05d9\u05dc</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.gmail_btn.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u05e4\u05ea\u05d7 \u05d0\u05d9\u05de\u05d9\u05d9\u05dc</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.gmail_btn.setText("")
#if QT_CONFIG(tooltip)
        self.calender_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u05e4\u05ea\u05d7 \u05dc\u05d5\u05d7 \u05e9\u05e0\u05d4</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.calender_btn.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u05e4\u05ea\u05d7 \u05dc\u05d5\u05d7 \u05e9\u05e0\u05d4</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.calender_btn.setText("")
        self.splash_author_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:7.8pt;\">\u05e0\u05db\u05ea\u05d1 \u05e2\u05dc \u05d9\u05d3\u05d9 \u05d0.\u05d7 (\u05d0\u05d9\u05d9\u05dc \u05d7\u05d5\u05e8\u05d9) \u05e2\u05dc \u05de\u05dc\u05d0</span></p></body></html>", None))
        self.events_button.setText(QCoreApplication.translate("MainWindow", u"\u05e0\u05d9\u05d4\u05d5\u05dc \u05d0\u05d9\u05e8\u05d5\u05e2\u05d9\u05dd", None))
        self.leads_button.setText(QCoreApplication.translate("MainWindow", u"\u05dc\u05d9\u05d3\u05d9\u05dd", None))
        self.suppliers_button.setText(QCoreApplication.translate("MainWindow", u"\u05e0\u05d9\u05d4\u05d5\u05dc \u05e1\u05e4\u05e7\u05d9\u05dd", None))
        self.clients_button.setText(QCoreApplication.translate("MainWindow", u"\u05e0\u05d9\u05d4\u05d5\u05dc \u05dc\u05e7\u05d5\u05d7\u05d5\u05ea", None))
        self.GIF_label.setText("")
        self.pauseGIF_btn.setText("")
        self.playGIF_btn.setText("")
        self.nextGIF_btn.setText("")
        self.logo_browse_btn.setText(QCoreApplication.translate("MainWindow", u"\u05d1\u05d7\u05e8 \u05dc\u05d5\u05d2\u05d5 \u05e2\u05d1\u05d5\u05e8 \u05d3\u05d5\"\u05d7\u05d5\u05ea", None))
        self.logo_notunique_warning.setText(QCoreApplication.translate("MainWindow", u"\u05e0\u05d9\u05ea\u05df \u05dc\u05d1\u05d7\u05d5\u05e8 \u05e7\u05d5\u05d1\u05e5 \u05d0\u05d7\u05d3 \u05d1\u05dc\u05d1\u05d3", None))
        self.logo_notphoto_warning.setText(QCoreApplication.translate("MainWindow", u"\u05d4\u05e7\u05d5\u05d1\u05e5 \u05e9\u05e0\u05d1\u05d7\u05e8 \u05d0\u05d9\u05e0\u05d5 \u05de\u05e1\u05d5\u05d2 \u05ea\u05de\u05d5\u05e0\u05d4", None))
#if QT_CONFIG(tooltip)
        self.reset_logo_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u05dc\u05dc\u05d0 \u05dc\u05d5\u05d2\u05d5</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.reset_logo_btn.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u05dc\u05dc\u05d0 \u05dc\u05d5\u05d2\u05d5</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.reset_logo_btn.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.backup_Setup_btn.setText(QCoreApplication.translate("MainWindow", u"\u05d4\u05d2\u05d3\u05e8\u05d5\u05ea \u05d2\u05d9\u05d1\u05d5\u05d9", None))
        self.backup_options_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u05d0\u05e3 \u05e4\u05e2\u05dd", None))
        self.backup_options_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u05db\u05dc 5 \u05d3\u05e7\u05d5\u05ea", None))
        self.backup_options_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u05db\u05dc 15 \u05d3\u05e7\u05d5\u05ea", None))
        self.backup_options_combobox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u05db\u05dc 30 \u05d3\u05e7\u05d5\u05ea", None))
        self.backup_options_combobox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u05db\u05dc 60 \u05d3\u05e7\u05d5\u05ea", None))
        self.backup_options_combobox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u05d1\u05e2\u05ea \u05db\u05e0\u05d9\u05e1\u05d4", None))

#if QT_CONFIG(tooltip)
        self.backup_options_combobox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u05d1\u05d7\u05e8 \u05e1\u05d5\u05d2 \u05d0\u05d9\u05e8\u05d5\u05e2</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.backup_options_combobox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.backup_options_combobox.setCurrentText("")
        self.backup_options_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u05ea\u05d3\u05d9\u05e8\u05d5\u05ea \u05d2\u05d9\u05d1\u05d5\u05d9", None))
#if QT_CONFIG(tooltip)
        self.restore_backup_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u05e9\u05d9\u05d7\u05d6\u05d5\u05e8 \u05de\u05d4\u05d2\u05d9\u05d1\u05d5\u05d9 \u05d4\u05d0\u05d7\u05e8\u05d5\u05df</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.restore_backup_btn.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u05e9\u05d9\u05d7\u05d6\u05d5\u05e8 \u05de\u05d4\u05d2\u05d9\u05d1\u05d5\u05d9 \u05d4\u05d0\u05d7\u05e8\u05d5\u05df</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.restore_backup_btn.setText("")
        self.backup_freq_label.setText(QCoreApplication.translate("MainWindow", u"\u05ea\u05d3\u05d9\u05e8\u05d5\u05ea:", None))
        self.restart_backup_warning.setText(QCoreApplication.translate("MainWindow", u"\u05d4\u05e9\u05d9\u05e0\u05d5\u05d9\u05d9\u05dd \u05d9\u05d9\u05e9\u05de\u05e8\u05d5 \u05dc\u05d0\u05d7\u05e8 \u05d4\u05e4\u05e2\u05dc\u05d4 \u05de\u05d7\u05d3\u05e9", None))
        self.restart_for_backup_btn.setText(QCoreApplication.translate("MainWindow", u"\u05d1\u05e6\u05e2 \u05db\u05e2\u05ea", None))
        self.quote_label.setText(QCoreApplication.translate("MainWindow", u"\"\u05d4\u05d0\u05d9\u05e8\u05d5\u05e2 \u05e9\u05ea\u05de\u05d9\u05d3 \u05d7\u05dc\u05de\u05ea\u05dd \u05e2\u05dc\u05d9\u05d5...\"", None))
        self.leads_head_label.setText(QCoreApplication.translate("MainWindow", u"\u05dc\u05d9\u05d3\u05d9\u05dd", None))
        self.previous_leads_btn.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.next_leads_btn.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.leads_page_number_label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.previous_events_btn.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.next_events_btn.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.events_page_number_label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.events_head_label.setText(QCoreApplication.translate("MainWindow", u"\u05d0\u05d9\u05e8\u05d5\u05e2\u05d9\u05dd", None))
    # retranslateUi

