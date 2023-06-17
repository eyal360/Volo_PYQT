# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'event_windowVNMtMM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import event_window_icons_rc

class Ui_EventWindow(object):
    def setupUi(self, EventWindow):
        if not EventWindow.objectName():
            EventWindow.setObjectName(u"EventWindow")
        EventWindow.resize(1025, 927)
        EventWindow.setStyleSheet(u"background-color: rgb(137,236,218);\n"
"")
        self.centralwidget = QWidget(EventWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.upper_frame = QFrame(self.centralwidget)
        self.upper_frame.setObjectName(u"upper_frame")
        self.upper_frame.setGeometry(QRect(10, 10, 1001, 81))
        font = QFont()
        font.setPointSize(15)
        self.upper_frame.setFont(font)
        self.upper_frame.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"border-radius: 40px;")
        self.upper_frame.setFrameShape(QFrame.StyledPanel)
        self.upper_frame.setFrameShadow(QFrame.Raised)
        self.headline_label = QLabel(self.upper_frame)
        self.headline_label.setObjectName(u"headline_label")
        self.headline_label.setGeometry(QRect(280, -10, 701, 81))
        self.headline_label.setLayoutDirection(Qt.RightToLeft)
        self.headline_label.setAutoFillBackground(False)
        self.headline_label.setStyleSheet(u"color: rgb(151,186,172);\n"
"font: 63 42pt \"Segoe UI Semibold\";\n"
"border-radius: 40px;\n"
"\n"
"")
        self.headline_label.setScaledContents(True)
        self.headline_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.headline_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.event_clear_all_btn = QPushButton(self.upper_frame)
        self.event_clear_all_btn.setObjectName(u"event_clear_all_btn")
        self.event_clear_all_btn.setGeometry(QRect(10, 10, 71, 61))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semilight")
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(7)
        self.event_clear_all_btn.setFont(font1)
        self.event_clear_all_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.event_clear_all_btn.setMouseTracking(True)
        self.event_clear_all_btn.setFocusPolicy(Qt.ClickFocus)
        self.event_clear_all_btn.setStyleSheet(u"QPushButton {\n"
"	\n"
"	image: url(:/icons/misc/minus-icon-png.jpg);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semilight\";\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb( 255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(168,230,207);\n"
"}")
        self.event_collapse_all_btn = QPushButton(self.upper_frame)
        self.event_collapse_all_btn.setObjectName(u"event_collapse_all_btn")
        self.event_collapse_all_btn.setGeometry(QRect(10, 10, 71, 61))
        self.event_collapse_all_btn.setFont(font1)
        self.event_collapse_all_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.event_collapse_all_btn.setMouseTracking(True)
        self.event_collapse_all_btn.setFocusPolicy(Qt.ClickFocus)
        self.event_collapse_all_btn.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/misc/plus-icon.png);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semilight\";\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb( 255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(168,230,207);\n"
"}")
        self.event_folder_btn = QPushButton(self.centralwidget)
        self.event_folder_btn.setObjectName(u"event_folder_btn")
        self.event_folder_btn.setGeometry(QRect(10, 110, 101, 81))
        self.event_folder_btn.setFont(font1)
        self.event_folder_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.event_folder_btn.setMouseTracking(True)
        self.event_folder_btn.setFocusPolicy(Qt.ClickFocus)
        self.event_folder_btn.setStyleSheet(u"QPushButton {\n"
"	\n"
"	image: url(:/icons/misc/folder.png);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semilight\";\n"
"	border-radius: 40px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb( 255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(168,230,207);\n"
"}")
        self.client_details_btn = QPushButton(self.centralwidget)
        self.client_details_btn.setObjectName(u"client_details_btn")
        self.client_details_btn.setGeometry(QRect(860, 160, 151, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semibold")
        font2.setPointSize(15)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(7)
        self.client_details_btn.setFont(font2)
        self.client_details_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.client_details_btn.setMouseTracking(True)
        self.client_details_btn.setFocusPolicy(Qt.ClickFocus)
        self.client_details_btn.setStyleSheet(u"QPushButton {\n"
"	font: 63 15pt \"Segoe UI Semibold\";\n"
"	border-radius: 15px;	\n"
"	color: rgb(76, 77, 76);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb( 255, 255, 255);\n"
"	font: 63 17pt \"Segoe UI Semibold\";\n"
"}")
        self.event_details_btn = QPushButton(self.centralwidget)
        self.event_details_btn.setObjectName(u"event_details_btn")
        self.event_details_btn.setGeometry(QRect(860, 260, 151, 41))
        self.event_details_btn.setFont(font2)
        self.event_details_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.event_details_btn.setMouseTracking(True)
        self.event_details_btn.setFocusPolicy(Qt.ClickFocus)
        self.event_details_btn.setStyleSheet(u"QPushButton {\n"
"	font: 63 15pt \"Segoe UI Semibold\";\n"
"	border-radius: 15px;	\n"
"	color: rgb(76, 77, 76);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb( 255, 255, 255);\n"
"	font: 63 17pt \"Segoe UI Semibold\";\n"
"}")
        self.client_details_frame = QFrame(self.centralwidget)
        self.client_details_frame.setObjectName(u"client_details_frame")
        self.client_details_frame.setGeometry(QRect(240, 140, 611, 91))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.client_details_frame.sizePolicy().hasHeightForWidth())
        self.client_details_frame.setSizePolicy(sizePolicy)
        self.client_details_frame.setStyleSheet(u"background-color: rgb(137,236,218);\n"
"")
        self.client_details_frame.setFrameShape(QFrame.StyledPanel)
        self.client_details_frame.setFrameShadow(QFrame.Raised)
        self.client_detail_name1 = QLabel(self.client_details_frame)
        self.client_detail_name1.setObjectName(u"client_detail_name1")
        self.client_detail_name1.setGeometry(QRect(310, 0, 291, 21))
        self.client_detail_name1.setCursor(QCursor(Qt.ArrowCursor))
        self.client_detail_name1.setLayoutDirection(Qt.RightToLeft)
        self.client_detail_name1.setStyleSheet(u"font: 63 10pt \"Segoe UI Semibold\";\n"
"color: rgb(76, 77, 76);")
        self.client_detail_name1.setAlignment(Qt.AlignCenter)
        self.client_detail_name1.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.client_detail_phone1 = QLabel(self.client_details_frame)
        self.client_detail_phone1.setObjectName(u"client_detail_phone1")
        self.client_detail_phone1.setGeometry(QRect(310, 20, 291, 21))
        self.client_detail_phone1.setLayoutDirection(Qt.RightToLeft)
        self.client_detail_phone1.setStyleSheet(u"font: 63 10pt \"Segoe UI Semilight\";\n"
"color: rgb(76, 77, 76);")
        self.client_detail_phone1.setAlignment(Qt.AlignCenter)
        self.client_detail_phone1.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.client_detail_email1 = QLabel(self.client_details_frame)
        self.client_detail_email1.setObjectName(u"client_detail_email1")
        self.client_detail_email1.setGeometry(QRect(310, 60, 291, 31))
        self.client_detail_email1.setLayoutDirection(Qt.RightToLeft)
        self.client_detail_email1.setStyleSheet(u"font: 63 10pt \"Segoe UI Semilight\";\n"
"border-radius: 10px; 	\n"
"color: rgb(76, 77, 76);")
        self.client_detail_email1.setAlignment(Qt.AlignCenter)
        self.client_detail_email1.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.client_detail_address1 = QLabel(self.client_details_frame)
        self.client_detail_address1.setObjectName(u"client_detail_address1")
        self.client_detail_address1.setGeometry(QRect(310, 40, 291, 21))
        self.client_detail_address1.setLayoutDirection(Qt.RightToLeft)
        self.client_detail_address1.setStyleSheet(u"font: 63 10pt \"Segoe UI Semilight\";\n"
"color: rgb(76, 77, 76);\n"
"")
        self.client_detail_address1.setAlignment(Qt.AlignCenter)
        self.client_detail_address1.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.client_detail_phone2 = QLabel(self.client_details_frame)
        self.client_detail_phone2.setObjectName(u"client_detail_phone2")
        self.client_detail_phone2.setGeometry(QRect(10, 20, 291, 21))
        self.client_detail_phone2.setLayoutDirection(Qt.RightToLeft)
        self.client_detail_phone2.setStyleSheet(u"font: 63 10pt \"Segoe UI Semilight\";\n"
"color: rgb(76, 77, 76);")
        self.client_detail_phone2.setAlignment(Qt.AlignCenter)
        self.client_detail_phone2.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.client_detail_name2 = QLabel(self.client_details_frame)
        self.client_detail_name2.setObjectName(u"client_detail_name2")
        self.client_detail_name2.setGeometry(QRect(10, 0, 291, 21))
        self.client_detail_name2.setLayoutDirection(Qt.RightToLeft)
        self.client_detail_name2.setStyleSheet(u"font: 63 10pt \"Segoe UI Semibold\";\n"
"border-radius: 10px; 	\n"
"color: rgb(76, 77, 76);")
        self.client_detail_name2.setAlignment(Qt.AlignCenter)
        self.client_detail_name2.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.client_detail_email2 = QLabel(self.client_details_frame)
        self.client_detail_email2.setObjectName(u"client_detail_email2")
        self.client_detail_email2.setGeometry(QRect(10, 60, 291, 31))
        self.client_detail_email2.setLayoutDirection(Qt.RightToLeft)
        self.client_detail_email2.setStyleSheet(u"font: 63 10pt \"Segoe UI Semilight\";\n"
"border-radius: 10px; 	\n"
"color: rgb(76, 77, 76);")
        self.client_detail_email2.setAlignment(Qt.AlignCenter)
        self.client_detail_email2.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.client_detail_address2 = QLabel(self.client_details_frame)
        self.client_detail_address2.setObjectName(u"client_detail_address2")
        self.client_detail_address2.setGeometry(QRect(0, 40, 291, 21))
        self.client_detail_address2.setLayoutDirection(Qt.RightToLeft)
        self.client_detail_address2.setStyleSheet(u"font: 63 10pt \"Segoe UI Semilight\";\n"
"color: rgb(76, 77, 76);\n"
"")
        self.client_detail_address2.setAlignment(Qt.AlignCenter)
        self.client_detail_address2.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.event_detail_frame = QFrame(self.centralwidget)
        self.event_detail_frame.setObjectName(u"event_detail_frame")
        self.event_detail_frame.setGeometry(QRect(250, 240, 611, 111))
        self.event_detail_frame.setStyleSheet(u"background-color: rgb(137,236,218);")
        self.event_detail_frame.setFrameShape(QFrame.StyledPanel)
        self.event_detail_frame.setFrameShadow(QFrame.Raised)
        self.event_detail_contract = QLabel(self.event_detail_frame)
        self.event_detail_contract.setObjectName(u"event_detail_contract")
        self.event_detail_contract.setGeometry(QRect(250, 20, 351, 21))
        self.event_detail_contract.setLayoutDirection(Qt.RightToLeft)
        self.event_detail_contract.setStyleSheet(u"font: 63 10pt \"Segoe UI Semilight\";\n"
"color: rgb(76, 77, 76);")
        self.event_detail_contract.setAlignment(Qt.AlignCenter)
        self.event_detail_contract.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.event_detail_location = QLabel(self.event_detail_frame)
        self.event_detail_location.setObjectName(u"event_detail_location")
        self.event_detail_location.setGeometry(QRect(250, 40, 351, 21))
        self.event_detail_location.setLayoutDirection(Qt.RightToLeft)
        self.event_detail_location.setStyleSheet(u"font: 63 10pt \"Segoe UI Semilight\";\n"
"color: rgb(76, 77, 76);")
        self.event_detail_location.setAlignment(Qt.AlignCenter)
        self.event_detail_location.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.event_detail_name = QLabel(self.event_detail_frame)
        self.event_detail_name.setObjectName(u"event_detail_name")
        self.event_detail_name.setGeometry(QRect(250, 0, 351, 21))
        self.event_detail_name.setLayoutDirection(Qt.RightToLeft)
        self.event_detail_name.setStyleSheet(u"font: 63 10pt \"Segoe UI Semilight\";\n"
"border-radius: 10px; 	\n"
"color: rgb(76, 77, 76);")
        self.event_detail_name.setAlignment(Qt.AlignCenter)
        self.event_detail_name.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.event_detail_location_address = QLabel(self.event_detail_frame)
        self.event_detail_location_address.setObjectName(u"event_detail_location_address")
        self.event_detail_location_address.setGeometry(QRect(250, 60, 351, 31))
        self.event_detail_location_address.setLayoutDirection(Qt.RightToLeft)
        self.event_detail_location_address.setStyleSheet(u"font: 63 10pt \"Segoe UI Semilight\";\n"
"border-radius: 10px; 	\n"
"color: rgb(76, 77, 76);")
        self.event_detail_location_address.setAlignment(Qt.AlignCenter)
        self.event_detail_location_address.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.event_budget_text = QTextEdit(self.event_detail_frame)
        self.event_budget_text.setObjectName(u"event_budget_text")
        self.event_budget_text.setGeometry(QRect(40, 20, 161, 41))
        self.event_budget_text.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.event_budget_text.setAcceptDrops(False)
        self.event_budget_text.setLayoutDirection(Qt.RightToLeft)
        self.event_budget_text.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 20px;")
        self.event_budget_text.setFrameShape(QFrame.StyledPanel)
        self.event_budget_text.setFrameShadow(QFrame.Plain)
        self.event_budget_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.event_budget_text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.event_budget_text.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.event_budget_text.setTabChangesFocus(True)
        self.event_budget_text.setLineWrapMode(QTextEdit.WidgetWidth)
        self.event_budget_text.setOverwriteMode(False)
        self.event_budget_text.setTextInteractionFlags(Qt.TextEditorInteraction)
        self.event_budget_text.setPlaceholderText(u"     \u05ea\u05e7\u05e6\u05d9\u05d1 \u05d0\u05d9\u05e8\u05d5\u05e2")
        self.event_budget_label = QLabel(self.event_detail_frame)
        self.event_budget_label.setObjectName(u"event_budget_label")
        self.event_budget_label.setGeometry(QRect(70, 0, 101, 21))
        self.event_budget_label.setStyleSheet(u"QLabel {\n"
"	font: 63 11pt \"Segoe UI Semibold\";\n"
"	border-radius: 15px;	\n"
"	color: rgb(76, 77, 76);\n"
"}\n"
"")
        self.update_budget_btn = QPushButton(self.event_detail_frame)
        self.update_budget_btn.setObjectName(u"update_budget_btn")
        self.update_budget_btn.setGeometry(QRect(80, 60, 81, 31))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Semilight")
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(7)
        self.update_budget_btn.setFont(font3)
        self.update_budget_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.update_budget_btn.setMouseTracking(True)
        self.update_budget_btn.setFocusPolicy(Qt.ClickFocus)
        self.update_budget_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 170, 127);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 14pt \"Segoe UI Semilight\";\n"
"	border: 1px solid #090206;\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 170, 127);\n"
"	font: 63 15pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"}")
        self.payments_page_btn = QPushButton(self.centralwidget)
        self.payments_page_btn.setObjectName(u"payments_page_btn")
        self.payments_page_btn.setGeometry(QRect(780, 340, 71, 51))
        self.payments_page_btn.setFont(font1)
        self.payments_page_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.payments_page_btn.setMouseTracking(True)
        self.payments_page_btn.setFocusPolicy(Qt.ClickFocus)
        self.payments_page_btn.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/misc/supplier_payment_icon.png);\n"
"	font: 63 20pt \"Segoe UI Semilight\";\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.payments_page_btn_label = QLabel(self.centralwidget)
        self.payments_page_btn_label.setObjectName(u"payments_page_btn_label")
        self.payments_page_btn_label.setGeometry(QRect(780, 391, 71, 20))
        self.payments_page_btn_label.setStyleSheet(u"QLabel {\n"
"	font: 63 12pt \"Segoe UI Semibold\";\n"
"	border-radius: 15px;	\n"
"	color: rgb(76, 77, 76);\n"
"}\n"
"")
        self.payments_page_btn_label.setAlignment(Qt.AlignCenter)
        self.missions_page_btn = QPushButton(self.centralwidget)
        self.missions_page_btn.setObjectName(u"missions_page_btn")
        self.missions_page_btn.setGeometry(QRect(670, 340, 71, 51))
        self.missions_page_btn.setFont(font1)
        self.missions_page_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.missions_page_btn.setMouseTracking(True)
        self.missions_page_btn.setFocusPolicy(Qt.ClickFocus)
        self.missions_page_btn.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/misc/task-icon.jpg);\n"
"	font: 63 20pt \"Segoe UI Semilight\";\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.missions_page_btn_label = QLabel(self.centralwidget)
        self.missions_page_btn_label.setObjectName(u"missions_page_btn_label")
        self.missions_page_btn_label.setGeometry(QRect(669, 391, 71, 20))
        self.missions_page_btn_label.setStyleSheet(u"QLabel {\n"
"	font: 63 12pt \"Segoe UI Semibold\";\n"
"	border-radius: 15px;	\n"
"	color: rgb(76, 77, 76);\n"
"}\n"
"")
        self.missions_page_btn_label.setAlignment(Qt.AlignCenter)
        self.payments_btn_line = QFrame(self.centralwidget)
        self.payments_btn_line.setObjectName(u"payments_btn_line")
        self.payments_btn_line.setGeometry(QRect(790, 420, 50, 3))
        self.payments_btn_line.setStyleSheet(u"border: 2px solid #FFFFFF;\n"
"")
        self.payments_btn_line.setFrameShape(QFrame.HLine)
        self.payments_btn_line.setFrameShadow(QFrame.Sunken)
        self.events_stackedWidget = QStackedWidget(self.centralwidget)
        self.events_stackedWidget.setObjectName(u"events_stackedWidget")
        self.events_stackedWidget.setGeometry(QRect(0, 420, 1031, 501))
        self.events_stackedWidget.setStyleSheet(u"")
        self.files_page = QWidget()
        self.files_page.setObjectName(u"files_page")
        self.dragndrop_label = QLabel(self.files_page)
        self.dragndrop_label.setObjectName(u"dragndrop_label")
        self.dragndrop_label.setGeometry(QRect(560, 420, 241, 31))
        self.dragndrop_label.setStyleSheet(u"\n"
"	font: 63 14pt \"Segoe UI Semibold\";\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"")
        self.or_label = QLabel(self.files_page)
        self.or_label.setObjectName(u"or_label")
        self.or_label.setGeometry(QRect(360, 200, 31, 41))
        self.or_label.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.browser_btn = QPushButton(self.files_page)
        self.browser_btn.setObjectName(u"browser_btn")
        self.browser_btn.setGeometry(QRect(60, 200, 261, 51))
        self.browser_btn.setFont(font1)
        self.browser_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.browser_btn.setMouseTracking(True)
        self.browser_btn.setFocusPolicy(Qt.ClickFocus)
        self.browser_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(187,187,187);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid #090206;\n"
"	font: 63 20pt \"Segoe UI Semilight\";\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(170,170,170);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0,0,0);\n"
"}")
        self.events_stackedWidget.addWidget(self.files_page)
        self.missions_page = QWidget()
        self.missions_page.setObjectName(u"missions_page")
        self.missions_tablewidget = QTableWidget(self.missions_page)
        if (self.missions_tablewidget.columnCount() < 4):
            self.missions_tablewidget.setColumnCount(4)
        font4 = QFont()
        font4.setFamily(u"Segoe UI Semibold")
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font4);
        self.missions_tablewidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font4);
        self.missions_tablewidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font4);
        self.missions_tablewidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font4);
        self.missions_tablewidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.missions_tablewidget.setObjectName(u"missions_tablewidget")
        self.missions_tablewidget.setGeometry(QRect(10, 150, 1001, 261))
        sizePolicy.setHeightForWidth(self.missions_tablewidget.sizePolicy().hasHeightForWidth())
        self.missions_tablewidget.setSizePolicy(sizePolicy)
        self.missions_tablewidget.setMaximumSize(QSize(1090, 16777215))
        self.missions_tablewidget.setLayoutDirection(Qt.RightToLeft)
        self.missions_tablewidget.setFrameShape(QFrame.NoFrame)
        self.missions_tablewidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.missions_tablewidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.missions_tablewidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.missions_tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.missions_tablewidget.setAlternatingRowColors(True)
        self.missions_tablewidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.missions_tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.missions_tablewidget.setTextElideMode(Qt.ElideMiddle)
        self.missions_tablewidget.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.missions_tablewidget.setGridStyle(Qt.DashLine)
        self.mission_name_text = QTextEdit(self.missions_page)
        self.mission_name_text.setObjectName(u"mission_name_text")
        self.mission_name_text.setGeometry(QRect(310, 10, 661, 41))
        self.mission_name_text.setAcceptDrops(False)
        self.mission_name_text.setLayoutDirection(Qt.RightToLeft)
        self.mission_name_text.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border: 3px solid #6248F0;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.mission_name_text.setFrameShape(QFrame.StyledPanel)
        self.mission_name_text.setFrameShadow(QFrame.Plain)
        self.mission_name_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mission_name_text.setTabChangesFocus(True)
        self.mission_name_text.setLineWrapMode(QTextEdit.WidgetWidth)
        self.mission_name_text.setOverwriteMode(False)
        self.mission_name_text.setPlaceholderText(u"                                                          \u05e4\u05e8\u05d8\u05d9 \u05de\u05e9\u05d9\u05de\u05d4")
        self.delete_all_missions_btn = QPushButton(self.missions_page)
        self.delete_all_missions_btn.setObjectName(u"delete_all_missions_btn")
        self.delete_all_missions_btn.setGeometry(QRect(100, 450, 191, 41))
        self.delete_all_missions_btn.setFont(font1)
        self.delete_all_missions_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.delete_all_missions_btn.setMouseTracking(True)
        self.delete_all_missions_btn.setFocusPolicy(Qt.ClickFocus)
        self.delete_all_missions_btn.setStyleSheet(u"QPushButton {\n"
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
        self.update_mission_btn = QPushButton(self.missions_page)
        self.update_mission_btn.setObjectName(u"update_mission_btn")
        self.update_mission_btn.setGeometry(QRect(380, 110, 101, 31))
        self.update_mission_btn.setFont(font3)
        self.update_mission_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.update_mission_btn.setMouseTracking(True)
        self.update_mission_btn.setFocusPolicy(Qt.ClickFocus)
        self.update_mission_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255,223,128);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 14pt \"Segoe UI Semilight\";\n"
"	border-radius: 10px;\n"
"	border: 1px solid #009de2;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255,192,128);\n"
"	font: 63 16pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(234,206,41);\n"
"}")
        self.clear_mission_input_btn = QPushButton(self.missions_page)
        self.clear_mission_input_btn.setObjectName(u"clear_mission_input_btn")
        self.clear_mission_input_btn.setGeometry(QRect(620, 110, 101, 31))
        font5 = QFont()
        font5.setFamily(u"Segoe UI Semilight")
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(7)
        self.clear_mission_input_btn.setFont(font5)
        self.clear_mission_input_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.clear_mission_input_btn.setMouseTracking(True)
        self.clear_mission_input_btn.setFocusPolicy(Qt.ClickFocus)
        self.clear_mission_input_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(76, 77, 76);\n"
"	font: 63 10pt \"Segoe UI Semilight\";\n"
"	border-radius: 10px;\n"
"	border: 1px solid #009de2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255,255,255);\n"
"	font: 63 11pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255,255,255);\n"
"}")
        self.mission_single_select_delete_no_btn = QPushButton(self.missions_page)
        self.mission_single_select_delete_no_btn.setObjectName(u"mission_single_select_delete_no_btn")
        self.mission_single_select_delete_no_btn.setGeometry(QRect(660, 460, 71, 31))
        self.mission_single_select_delete_no_btn.setFont(font3)
        self.mission_single_select_delete_no_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.mission_single_select_delete_no_btn.setMouseTracking(True)
        self.mission_single_select_delete_no_btn.setFocusPolicy(Qt.ClickFocus)
        self.mission_single_select_delete_no_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(165,212,106);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 14pt \"Segoe UI Semilight\";\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(62,178,101);\n"
"	font: 63 16pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(45,127,72);\n"
"}")
        self.missions_delete_all_warning = QLabel(self.missions_page)
        self.missions_delete_all_warning.setObjectName(u"missions_delete_all_warning")
        self.missions_delete_all_warning.setGeometry(QRect(20, 420, 341, 31))
        self.missions_delete_all_warning.setCursor(QCursor(Qt.ArrowCursor))
        self.missions_delete_all_warning.setStyleSheet(u"font: 16pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border: 1px solid #e38c8c;\n"
"")
        self.missions_delete_all_warning.setLineWidth(0)
        self.missions_delete_all_warning.setScaledContents(False)
        self.missions_delete_all_warning.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.mission_single_select_delete_label = QLabel(self.missions_page)
        self.mission_single_select_delete_label.setObjectName(u"mission_single_select_delete_label")
        self.mission_single_select_delete_label.setGeometry(QRect(820, 460, 201, 31))
        self.mission_single_select_delete_label.setStyleSheet(u"font: 63 12pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.add_mission_btn = QPushButton(self.missions_page)
        self.add_mission_btn.setObjectName(u"add_mission_btn")
        self.add_mission_btn.setGeometry(QRect(500, 110, 101, 31))
        self.add_mission_btn.setFont(font3)
        self.add_mission_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.add_mission_btn.setMouseTracking(True)
        self.add_mission_btn.setFocusPolicy(Qt.ClickFocus)
        self.add_mission_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(165,212,106);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 14pt \"Segoe UI Semilight\";\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(62,178,101);\n"
"	font: 63 16pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(45,127,72);\n"
"}")
        self.status_combobox = QComboBox(self.missions_page)
        self.status_combobox.addItem("")
        self.status_combobox.addItem("")
        self.status_combobox.addItem("")
        self.status_combobox.setObjectName(u"status_combobox")
        self.status_combobox.setGeometry(QRect(20, 10, 141, 31))
        self.status_combobox.setAcceptDrops(False)
        self.status_combobox.setLayoutDirection(Qt.RightToLeft)
        self.status_combobox.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border: 1px solid #090206;\n"
"background-color: rgb(255,223,128);\n"
"border-radius: 10px;")
        self.status_combobox.setEditable(False)
        self.missions_all_select_delete_label = QLabel(self.missions_page)
        self.missions_all_select_delete_label.setObjectName(u"missions_all_select_delete_label")
        self.missions_all_select_delete_label.setGeometry(QRect(170, 460, 201, 31))
        self.missions_all_select_delete_label.setStyleSheet(u"font: 63 12pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.missions_all_select_delete_yes_btn = QPushButton(self.missions_page)
        self.missions_all_select_delete_yes_btn.setObjectName(u"missions_all_select_delete_yes_btn")
        self.missions_all_select_delete_yes_btn.setGeometry(QRect(90, 460, 71, 31))
        self.missions_all_select_delete_yes_btn.setFont(font3)
        self.missions_all_select_delete_yes_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.missions_all_select_delete_yes_btn.setMouseTracking(True)
        self.missions_all_select_delete_yes_btn.setFocusPolicy(Qt.ClickFocus)
        self.missions_all_select_delete_yes_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(227,140,140);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 14pt \"Segoe UI Semilight\";\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(223,66,66);\n"
"	font: 63 16pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(221,9,9);\n"
"}")
        self.delete_selection_mission_btn = QPushButton(self.missions_page)
        self.delete_selection_mission_btn.setObjectName(u"delete_selection_mission_btn")
        self.delete_selection_mission_btn.setGeometry(QRect(750, 450, 191, 41))
        self.delete_selection_mission_btn.setFont(font1)
        self.delete_selection_mission_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.delete_selection_mission_btn.setMouseTracking(True)
        self.delete_selection_mission_btn.setFocusPolicy(Qt.ClickFocus)
        self.delete_selection_mission_btn.setStyleSheet(u"QPushButton {\n"
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
        self.mission_delete_selection_warning = QLabel(self.missions_page)
        self.mission_delete_selection_warning.setObjectName(u"mission_delete_selection_warning")
        self.mission_delete_selection_warning.setGeometry(QRect(670, 420, 341, 31))
        self.mission_delete_selection_warning.setCursor(QCursor(Qt.ArrowCursor))
        self.mission_delete_selection_warning.setStyleSheet(u"font: 16pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border: 1px solid #e38c8c;\n"
"")
        self.mission_delete_selection_warning.setLineWidth(0)
        self.mission_delete_selection_warning.setScaledContents(False)
        self.mission_delete_selection_warning.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.missions_excel_warning = QLabel(self.missions_page)
        self.missions_excel_warning.setObjectName(u"missions_excel_warning")
        self.missions_excel_warning.setGeometry(QRect(410, 420, 211, 21))
        self.missions_excel_warning.setCursor(QCursor(Qt.ArrowCursor))
        self.missions_excel_warning.setStyleSheet(u"font: 10pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.missions_excel_warning.setLineWidth(0)
        self.missions_excel_warning.setScaledContents(False)
        self.missions_excel_warning.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.mission_single_select_delete_yes_btn = QPushButton(self.missions_page)
        self.mission_single_select_delete_yes_btn.setObjectName(u"mission_single_select_delete_yes_btn")
        self.mission_single_select_delete_yes_btn.setGeometry(QRect(740, 460, 71, 31))
        self.mission_single_select_delete_yes_btn.setFont(font3)
        self.mission_single_select_delete_yes_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.mission_single_select_delete_yes_btn.setMouseTracking(True)
        self.mission_single_select_delete_yes_btn.setFocusPolicy(Qt.ClickFocus)
        self.mission_single_select_delete_yes_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(227,140,140);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 14pt \"Segoe UI Semilight\";\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(223,66,66);\n"
"	font: 63 16pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(221,9,9);\n"
"}")
        self.mission_notes_text = QTextEdit(self.missions_page)
        self.mission_notes_text.setObjectName(u"mission_notes_text")
        self.mission_notes_text.setGeometry(QRect(10, 60, 991, 41))
        self.mission_notes_text.setAcceptDrops(False)
        self.mission_notes_text.setLayoutDirection(Qt.RightToLeft)
        self.mission_notes_text.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border: 1px solid #090206;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.mission_notes_text.setFrameShape(QFrame.StyledPanel)
        self.mission_notes_text.setFrameShadow(QFrame.Plain)
        self.mission_notes_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mission_notes_text.setTabChangesFocus(True)
        self.mission_notes_text.setLineWrapMode(QTextEdit.WidgetWidth)
        self.mission_notes_text.setOverwriteMode(False)
        self.mission_notes_text.setPlaceholderText(u"                                                                                              \u05d4\u05e2\u05e8\u05d5\u05ea")
        self.missions_all_select_delete_no_btn = QPushButton(self.missions_page)
        self.missions_all_select_delete_no_btn.setObjectName(u"missions_all_select_delete_no_btn")
        self.missions_all_select_delete_no_btn.setGeometry(QRect(10, 460, 71, 31))
        self.missions_all_select_delete_no_btn.setFont(font3)
        self.missions_all_select_delete_no_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.missions_all_select_delete_no_btn.setMouseTracking(True)
        self.missions_all_select_delete_no_btn.setFocusPolicy(Qt.ClickFocus)
        self.missions_all_select_delete_no_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(165,212,106);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 14pt \"Segoe UI Semilight\";\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(62,178,101);\n"
"	font: 63 16pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(45,127,72);\n"
"}")
        self.mission_due_text = QTextEdit(self.missions_page)
        self.mission_due_text.setObjectName(u"mission_due_text")
        self.mission_due_text.setGeometry(QRect(180, 10, 111, 41))
        self.mission_due_text.setAcceptDrops(False)
        self.mission_due_text.setLayoutDirection(Qt.RightToLeft)
        self.mission_due_text.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border: 1px solid #090206;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.mission_due_text.setFrameShape(QFrame.StyledPanel)
        self.mission_due_text.setFrameShadow(QFrame.Plain)
        self.mission_due_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mission_due_text.setTabChangesFocus(True)
        self.mission_due_text.setLineWrapMode(QTextEdit.WidgetWidth)
        self.mission_due_text.setOverwriteMode(False)
        self.mission_due_text.setPlaceholderText(u"      \u05ea\u05d2\"\u05d1")
        self.missions_export_excel_btn = QPushButton(self.missions_page)
        self.missions_export_excel_btn.setObjectName(u"missions_export_excel_btn")
        self.missions_export_excel_btn.setGeometry(QRect(460, 440, 91, 61))
        self.missions_export_excel_btn.setFont(font1)
        self.missions_export_excel_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.missions_export_excel_btn.setMouseTracking(True)
        self.missions_export_excel_btn.setFocusPolicy(Qt.ClickFocus)
        self.missions_export_excel_btn.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/misc/round_excel.png);\n"
"	font: 63 20pt \"Segoe UI Semilight\";\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb( 255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(168,230,207);\n"
"}")
        self.edit_mission_btn = QPushButton(self.missions_page)
        self.edit_mission_btn.setObjectName(u"edit_mission_btn")
        self.edit_mission_btn.setGeometry(QRect(380, 110, 101, 31))
        self.edit_mission_btn.setFont(font3)
        self.edit_mission_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.edit_mission_btn.setMouseTracking(True)
        self.edit_mission_btn.setFocusPolicy(Qt.ClickFocus)
        self.edit_mission_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255,223,128);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 14pt \"Segoe UI Semilight\";\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255,192,128);\n"
"	font: 63 16pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(234,206,41);\n"
"}")
        self.events_stackedWidget.addWidget(self.missions_page)
        self.missions_all_select_delete_label.raise_()
        self.missions_all_select_delete_yes_btn.raise_()
        self.mission_single_select_delete_yes_btn.raise_()
        self.missions_tablewidget.raise_()
        self.mission_name_text.raise_()
        self.delete_all_missions_btn.raise_()
        self.update_mission_btn.raise_()
        self.clear_mission_input_btn.raise_()
        self.mission_single_select_delete_no_btn.raise_()
        self.missions_delete_all_warning.raise_()
        self.mission_single_select_delete_label.raise_()
        self.add_mission_btn.raise_()
        self.status_combobox.raise_()
        self.delete_selection_mission_btn.raise_()
        self.mission_delete_selection_warning.raise_()
        self.missions_excel_warning.raise_()
        self.mission_notes_text.raise_()
        self.missions_all_select_delete_no_btn.raise_()
        self.mission_due_text.raise_()
        self.missions_export_excel_btn.raise_()
        self.edit_mission_btn.raise_()
        self.payments_page = QWidget()
        self.payments_page.setObjectName(u"payments_page")
        self.payments_export_excel_btn = QPushButton(self.payments_page)
        self.payments_export_excel_btn.setObjectName(u"payments_export_excel_btn")
        self.payments_export_excel_btn.setGeometry(QRect(460, 440, 91, 61))
        self.payments_export_excel_btn.setFont(font1)
        self.payments_export_excel_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.payments_export_excel_btn.setMouseTracking(True)
        self.payments_export_excel_btn.setFocusPolicy(Qt.ClickFocus)
        self.payments_export_excel_btn.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/misc/round_excel.png);\n"
"	font: 63 20pt \"Segoe UI Semilight\";\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb( 255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(168,230,207);\n"
"}")
        self.supplier_service_text = QTextEdit(self.payments_page)
        self.supplier_service_text.setObjectName(u"supplier_service_text")
        self.supplier_service_text.setGeometry(QRect(540, 10, 221, 41))
        self.supplier_service_text.setAcceptDrops(False)
#if QT_CONFIG(whatsthis)
        self.supplier_service_text.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.supplier_service_text.setLayoutDirection(Qt.RightToLeft)
        self.supplier_service_text.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border: 3px solid #6248F0;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.supplier_service_text.setFrameShape(QFrame.StyledPanel)
        self.supplier_service_text.setFrameShadow(QFrame.Plain)
        self.supplier_service_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.supplier_service_text.setTabChangesFocus(True)
        self.supplier_service_text.setLineWrapMode(QTextEdit.WidgetWidth)
        self.supplier_service_text.setOverwriteMode(False)
        self.supplier_service_text.setPlaceholderText(u"            \u05e1\u05d5\u05d2 \u05e9\u05d9\u05e8\u05d5\u05ea")
        self.suppliers_combobox = QComboBox(self.payments_page)
        self.suppliers_combobox.addItem("")
        self.suppliers_combobox.addItem("")
        self.suppliers_combobox.addItem("")
        self.suppliers_combobox.setObjectName(u"suppliers_combobox")
        self.suppliers_combobox.setGeometry(QRect(770, 50, 241, 41))
        sizePolicy.setHeightForWidth(self.suppliers_combobox.sizePolicy().hasHeightForWidth())
        self.suppliers_combobox.setSizePolicy(sizePolicy)
        self.suppliers_combobox.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(whatsthis)
        self.suppliers_combobox.setWhatsThis(u"<html><head/><body><p align=\"center\">\u05d1\u05d7\u05e8 \u05e1\u05e4\u05e7</p></body></html>")
#endif // QT_CONFIG(whatsthis)
        self.suppliers_combobox.setLayoutDirection(Qt.RightToLeft)
        self.suppliers_combobox.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border: 3px solid #6248F0;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.suppliers_combobox.setInsertPolicy(QComboBox.InsertAtBottom)
        self.suppliers_combobox.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.suppliers_combobox.setDuplicatesEnabled(False)
        self.add_payment_btn = QPushButton(self.payments_page)
        self.add_payment_btn.setObjectName(u"add_payment_btn")
        self.add_payment_btn.setGeometry(QRect(10, 20, 101, 31))
        self.add_payment_btn.setFont(font3)
        self.add_payment_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.add_payment_btn.setMouseTracking(True)
        self.add_payment_btn.setFocusPolicy(Qt.ClickFocus)
        self.add_payment_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(165,212,106);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 14pt \"Segoe UI Semilight\";\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(62,178,101);\n"
"	font: 63 16pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(45,127,72);\n"
"}")
        self.supplier_advance_text = QTextEdit(self.payments_page)
        self.supplier_advance_text.setObjectName(u"supplier_advance_text")
        self.supplier_advance_text.setGeometry(QRect(230, 60, 141, 41))
        self.supplier_advance_text.setAcceptDrops(False)
        self.supplier_advance_text.setLayoutDirection(Qt.RightToLeft)
        self.supplier_advance_text.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border: 1px solid #090206;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.supplier_advance_text.setFrameShape(QFrame.StyledPanel)
        self.supplier_advance_text.setFrameShadow(QFrame.Plain)
        self.supplier_advance_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.supplier_advance_text.setTabChangesFocus(True)
        self.supplier_advance_text.setLineWrapMode(QTextEdit.WidgetWidth)
        self.supplier_advance_text.setOverwriteMode(False)
        self.supplier_advance_text.setPlaceholderText(u"\u05de\u05e7\u05d3\u05de\u05d4 (\u05e8\u05e9\u05d5\u05ea)")
        self.update_payment_btn = QPushButton(self.payments_page)
        self.update_payment_btn.setObjectName(u"update_payment_btn")
        self.update_payment_btn.setGeometry(QRect(10, 70, 101, 31))
        self.update_payment_btn.setFont(font3)
        self.update_payment_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.update_payment_btn.setMouseTracking(True)
        self.update_payment_btn.setFocusPolicy(Qt.ClickFocus)
        self.update_payment_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255,223,128);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 14pt \"Segoe UI Semilight\";\n"
"	border-radius: 10px;\n"
"	border: 1px solid #009de2;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255,192,128);\n"
"	font: 63 16pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(234,206,41);\n"
"}")
        self.advance_checkbox = QCheckBox(self.payments_page)
        self.advance_checkbox.setObjectName(u"advance_checkbox")
        self.advance_checkbox.setGeometry(QRect(140, 60, 81, 41))
        self.advance_checkbox.setStyleSheet(u"font: 63 12pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.clear_payment_text_btn = QPushButton(self.payments_page)
        self.clear_payment_text_btn.setObjectName(u"clear_payment_text_btn")
        self.clear_payment_text_btn.setGeometry(QRect(10, 120, 101, 31))
        self.clear_payment_text_btn.setFont(font5)
        self.clear_payment_text_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.clear_payment_text_btn.setMouseTracking(True)
        self.clear_payment_text_btn.setFocusPolicy(Qt.ClickFocus)
        self.clear_payment_text_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(76, 77, 76);\n"
"	font: 63 10pt \"Segoe UI Semilight\";\n"
"	border-radius: 10px;\n"
"	border: 1px solid #009de2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255,255,255);\n"
"	font: 63 11pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255,255,255);\n"
"}")
        self.payments_tablewidget = QTableWidget(self.payments_page)
        if (self.payments_tablewidget.columnCount() < 7):
            self.payments_tablewidget.setColumnCount(7)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font4);
        self.payments_tablewidget.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFont(font4);
        self.payments_tablewidget.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFont(font4);
        self.payments_tablewidget.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFont(font4);
        self.payments_tablewidget.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFont(font4);
        self.payments_tablewidget.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFont(font4);
        self.payments_tablewidget.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFont(font4);
        self.payments_tablewidget.setHorizontalHeaderItem(6, __qtablewidgetitem10)
        self.payments_tablewidget.setObjectName(u"payments_tablewidget")
        self.payments_tablewidget.setGeometry(QRect(10, 160, 1001, 251))
        sizePolicy.setHeightForWidth(self.payments_tablewidget.sizePolicy().hasHeightForWidth())
        self.payments_tablewidget.setSizePolicy(sizePolicy)
        self.payments_tablewidget.setMaximumSize(QSize(1090, 16777215))
        self.payments_tablewidget.setLayoutDirection(Qt.RightToLeft)
        self.payments_tablewidget.setFrameShape(QFrame.NoFrame)
        self.payments_tablewidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.payments_tablewidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.payments_tablewidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.payments_tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.payments_tablewidget.setAlternatingRowColors(True)
        self.payments_tablewidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.payments_tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.payments_tablewidget.setTextElideMode(Qt.ElideMiddle)
        self.payments_tablewidget.setGridStyle(Qt.DashLine)
        self.payments_excel_warning = QLabel(self.payments_page)
        self.payments_excel_warning.setObjectName(u"payments_excel_warning")
        self.payments_excel_warning.setGeometry(QRect(410, 420, 211, 21))
        self.payments_excel_warning.setCursor(QCursor(Qt.ArrowCursor))
        self.payments_excel_warning.setStyleSheet(u"font: 10pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.payments_excel_warning.setLineWidth(0)
        self.payments_excel_warning.setScaledContents(False)
        self.payments_excel_warning.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.supplier_tip_text = QTextEdit(self.payments_page)
        self.supplier_tip_text.setObjectName(u"supplier_tip_text")
        self.supplier_tip_text.setGeometry(QRect(270, 110, 101, 41))
        self.supplier_tip_text.setAcceptDrops(False)
        self.supplier_tip_text.setLayoutDirection(Qt.RightToLeft)
        self.supplier_tip_text.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border: 1px solid #090206;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.supplier_tip_text.setFrameShape(QFrame.StyledPanel)
        self.supplier_tip_text.setFrameShadow(QFrame.Plain)
        self.supplier_tip_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.supplier_tip_text.setTabChangesFocus(True)
        self.supplier_tip_text.setLineWrapMode(QTextEdit.WidgetWidth)
        self.supplier_tip_text.setOverwriteMode(False)
        self.supplier_tip_text.setPlaceholderText(u"      \u05d8\u05d9\u05e4")
        self.supplier_details_text = QTextEdit(self.payments_page)
        self.supplier_details_text.setObjectName(u"supplier_details_text")
        self.supplier_details_text.setGeometry(QRect(380, 60, 381, 91))
        self.supplier_details_text.setAcceptDrops(False)
#if QT_CONFIG(whatsthis)
        self.supplier_details_text.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.supplier_details_text.setLayoutDirection(Qt.RightToLeft)
        self.supplier_details_text.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border: 1px solid #090206;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.supplier_details_text.setFrameShape(QFrame.StyledPanel)
        self.supplier_details_text.setFrameShadow(QFrame.Plain)
        self.supplier_details_text.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.supplier_details_text.setTabChangesFocus(True)
        self.supplier_details_text.setLineWrapMode(QTextEdit.WidgetWidth)
        self.supplier_details_text.setOverwriteMode(False)
        self.supplier_details_text.setPlaceholderText(u"                         \u05e4\u05e8\u05d8\u05d9\u05dd \u05e0\u05d5\u05e1\u05e4\u05d9\u05dd")
        self.delete_selection_payment_btn = QPushButton(self.payments_page)
        self.delete_selection_payment_btn.setObjectName(u"delete_selection_payment_btn")
        self.delete_selection_payment_btn.setGeometry(QRect(750, 450, 191, 41))
        self.delete_selection_payment_btn.setFont(font1)
        self.delete_selection_payment_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.delete_selection_payment_btn.setMouseTracking(True)
        self.delete_selection_payment_btn.setFocusPolicy(Qt.ClickFocus)
        self.delete_selection_payment_btn.setStyleSheet(u"QPushButton {\n"
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
        self.delete_all_payments_btn = QPushButton(self.payments_page)
        self.delete_all_payments_btn.setObjectName(u"delete_all_payments_btn")
        self.delete_all_payments_btn.setGeometry(QRect(100, 450, 191, 41))
        self.delete_all_payments_btn.setFont(font1)
        self.delete_all_payments_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.delete_all_payments_btn.setMouseTracking(True)
        self.delete_all_payments_btn.setFocusPolicy(Qt.ClickFocus)
        self.delete_all_payments_btn.setStyleSheet(u"QPushButton {\n"
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
        self.payment_delete_selection_warning = QLabel(self.payments_page)
        self.payment_delete_selection_warning.setObjectName(u"payment_delete_selection_warning")
        self.payment_delete_selection_warning.setGeometry(QRect(670, 420, 341, 31))
        self.payment_delete_selection_warning.setCursor(QCursor(Qt.ArrowCursor))
        self.payment_delete_selection_warning.setStyleSheet(u"font: 16pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border: 1px solid #e38c8c;\n"
"")
        self.payment_delete_selection_warning.setLineWidth(0)
        self.payment_delete_selection_warning.setScaledContents(False)
        self.payment_delete_selection_warning.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.payment_single_select_delete_no_btn = QPushButton(self.payments_page)
        self.payment_single_select_delete_no_btn.setObjectName(u"payment_single_select_delete_no_btn")
        self.payment_single_select_delete_no_btn.setGeometry(QRect(660, 460, 71, 31))
        self.payment_single_select_delete_no_btn.setFont(font3)
        self.payment_single_select_delete_no_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.payment_single_select_delete_no_btn.setMouseTracking(True)
        self.payment_single_select_delete_no_btn.setFocusPolicy(Qt.ClickFocus)
        self.payment_single_select_delete_no_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(165,212,106);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 14pt \"Segoe UI Semilight\";\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(62,178,101);\n"
"	font: 63 16pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(45,127,72);\n"
"}")
        self.payment_delete_all_warning = QLabel(self.payments_page)
        self.payment_delete_all_warning.setObjectName(u"payment_delete_all_warning")
        self.payment_delete_all_warning.setGeometry(QRect(20, 420, 341, 31))
        self.payment_delete_all_warning.setCursor(QCursor(Qt.ArrowCursor))
        self.payment_delete_all_warning.setStyleSheet(u"font: 16pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border: 1px solid #e38c8c;\n"
"")
        self.payment_delete_all_warning.setLineWidth(0)
        self.payment_delete_all_warning.setScaledContents(False)
        self.payment_delete_all_warning.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.payment_single_select_delete_yes_btn = QPushButton(self.payments_page)
        self.payment_single_select_delete_yes_btn.setObjectName(u"payment_single_select_delete_yes_btn")
        self.payment_single_select_delete_yes_btn.setGeometry(QRect(740, 460, 71, 31))
        self.payment_single_select_delete_yes_btn.setFont(font3)
        self.payment_single_select_delete_yes_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.payment_single_select_delete_yes_btn.setMouseTracking(True)
        self.payment_single_select_delete_yes_btn.setFocusPolicy(Qt.ClickFocus)
        self.payment_single_select_delete_yes_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(227,140,140);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 14pt \"Segoe UI Semilight\";\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(223,66,66);\n"
"	font: 63 16pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(221,9,9);\n"
"}")
        self.payment_single_select_delete_label = QLabel(self.payments_page)
        self.payment_single_select_delete_label.setObjectName(u"payment_single_select_delete_label")
        self.payment_single_select_delete_label.setGeometry(QRect(820, 460, 201, 31))
        self.payment_single_select_delete_label.setStyleSheet(u"font: 63 12pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.payments_all_select_delete_no_btn = QPushButton(self.payments_page)
        self.payments_all_select_delete_no_btn.setObjectName(u"payments_all_select_delete_no_btn")
        self.payments_all_select_delete_no_btn.setGeometry(QRect(10, 460, 71, 31))
        self.payments_all_select_delete_no_btn.setFont(font3)
        self.payments_all_select_delete_no_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.payments_all_select_delete_no_btn.setMouseTracking(True)
        self.payments_all_select_delete_no_btn.setFocusPolicy(Qt.ClickFocus)
        self.payments_all_select_delete_no_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(165,212,106);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 14pt \"Segoe UI Semilight\";\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(62,178,101);\n"
"	font: 63 16pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(45,127,72);\n"
"}")
        self.payments_all_select_delete_label = QLabel(self.payments_page)
        self.payments_all_select_delete_label.setObjectName(u"payments_all_select_delete_label")
        self.payments_all_select_delete_label.setGeometry(QRect(170, 460, 201, 31))
        self.payments_all_select_delete_label.setStyleSheet(u"font: 63 12pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.payments_all_select_delete_yes_btn = QPushButton(self.payments_page)
        self.payments_all_select_delete_yes_btn.setObjectName(u"payments_all_select_delete_yes_btn")
        self.payments_all_select_delete_yes_btn.setGeometry(QRect(90, 460, 71, 31))
        self.payments_all_select_delete_yes_btn.setFont(font3)
        self.payments_all_select_delete_yes_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.payments_all_select_delete_yes_btn.setMouseTracking(True)
        self.payments_all_select_delete_yes_btn.setFocusPolicy(Qt.ClickFocus)
        self.payments_all_select_delete_yes_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(227,140,140);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 14pt \"Segoe UI Semilight\";\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(223,66,66);\n"
"	font: 63 16pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(221,9,9);\n"
"}")
        self.service_mendatory_label = QLabel(self.payments_page)
        self.service_mendatory_label.setObjectName(u"service_mendatory_label")
        self.service_mendatory_label.setGeometry(QRect(760, 0, 51, 31))
        self.service_mendatory_label.setStyleSheet(u"font: 11pt \"Segoe UI Semibold\";\n"
"color: rgb(239, 64, 64);")
        self.supplier_mendatory_label = QLabel(self.payments_page)
        self.supplier_mendatory_label.setObjectName(u"supplier_mendatory_label")
        self.supplier_mendatory_label.setGeometry(QRect(950, 20, 51, 20))
        self.supplier_mendatory_label.setStyleSheet(u"font: 11pt \"Segoe UI Semibold\";\n"
"color: rgb(239, 64, 64);")
        self.seperator_2 = QFrame(self.payments_page)
        self.seperator_2.setObjectName(u"seperator_2")
        self.seperator_2.setGeometry(QRect(120, 40, 20, 91))
        self.seperator_2.setFrameShape(QFrame.VLine)
        self.seperator_2.setFrameShadow(QFrame.Sunken)
        self.edit_payment_btn = QPushButton(self.payments_page)
        self.edit_payment_btn.setObjectName(u"edit_payment_btn")
        self.edit_payment_btn.setGeometry(QRect(10, 70, 101, 31))
        self.edit_payment_btn.setFont(font3)
        self.edit_payment_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.edit_payment_btn.setMouseTracking(True)
        self.edit_payment_btn.setFocusPolicy(Qt.ClickFocus)
        self.edit_payment_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255,223,128);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 14pt \"Segoe UI Semilight\";\n"
"	border-radius: 10px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255,192,128);\n"
"	font: 63 16pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(234,206,41);\n"
"}")
        self.category_combobox = QComboBox(self.payments_page)
        self.category_combobox.addItem("")
        self.category_combobox.addItem("")
        self.category_combobox.addItem("")
        self.category_combobox.addItem("")
        self.category_combobox.addItem("")
        self.category_combobox.addItem("")
        self.category_combobox.addItem("")
        self.category_combobox.addItem("")
        self.category_combobox.addItem("")
        self.category_combobox.addItem("")
        self.category_combobox.addItem("")
        self.category_combobox.addItem("")
        self.category_combobox.setObjectName(u"category_combobox")
        self.category_combobox.setGeometry(QRect(770, 100, 241, 41))
        sizePolicy.setHeightForWidth(self.category_combobox.sizePolicy().hasHeightForWidth())
        self.category_combobox.setSizePolicy(sizePolicy)
        self.category_combobox.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(whatsthis)
        self.category_combobox.setWhatsThis(u"<html><head/><body><p align=\"center\">\u05d1\u05d7\u05e8 \u05e7\u05d8\u05d2\u05d5\u05e8\u05d9\u05d4</p></body></html>")
#endif // QT_CONFIG(whatsthis)
        self.category_combobox.setLayoutDirection(Qt.RightToLeft)
        self.category_combobox.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border: 1px solid #090206;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.category_combobox.setEditable(True)
        self.category_combobox.setInsertPolicy(QComboBox.InsertAtBottom)
        self.category_combobox.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.category_combobox.setDuplicatesEnabled(False)
        self.guest_num_input = QTextEdit(self.payments_page)
        self.guest_num_input.setObjectName(u"guest_num_input")
        self.guest_num_input.setGeometry(QRect(230, 10, 141, 41))
        self.guest_num_input.setAcceptDrops(False)
        self.guest_num_input.setLayoutDirection(Qt.RightToLeft)
        self.guest_num_input.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border: 3px solid #be7efb;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.guest_num_input.setFrameShape(QFrame.StyledPanel)
        self.guest_num_input.setFrameShadow(QFrame.Plain)
        self.guest_num_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.guest_num_input.setTabChangesFocus(True)
        self.guest_num_input.setLineWrapMode(QTextEdit.WidgetWidth)
        self.guest_num_input.setOverwriteMode(False)
        self.guest_num_input.setPlaceholderText(u"  \u05db\u05de\u05d5\u05ea \u05de\u05d5\u05d6\u05de\u05e0\u05d9\u05dd")
        self.supplier_price_text = QTextEdit(self.payments_page)
        self.supplier_price_text.setObjectName(u"supplier_price_text")
        self.supplier_price_text.setGeometry(QRect(380, 10, 151, 41))
        self.supplier_price_text.setAcceptDrops(False)
        self.supplier_price_text.setLayoutDirection(Qt.RightToLeft)
        self.supplier_price_text.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border: 1px solid #090206;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.supplier_price_text.setFrameShape(QFrame.StyledPanel)
        self.supplier_price_text.setFrameShadow(QFrame.Plain)
        self.supplier_price_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.supplier_price_text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.supplier_price_text.setTabChangesFocus(True)
        self.supplier_price_text.setLineWrapMode(QTextEdit.WidgetWidth)
        self.supplier_price_text.setOverwriteMode(False)
        self.supplier_price_text.setPlaceholderText(u"\u05de\u05d7\u05d9\u05e8 \u05db\u05d5\u05dc\u05dc \u05de\u05e2\"\u05de")
        self.events_stackedWidget.addWidget(self.payments_page)
        self.payments_tablewidget.raise_()
        self.payments_all_select_delete_label.raise_()
        self.payment_single_select_delete_yes_btn.raise_()
        self.payment_single_select_delete_label.raise_()
        self.payments_export_excel_btn.raise_()
        self.supplier_service_text.raise_()
        self.add_payment_btn.raise_()
        self.supplier_advance_text.raise_()
        self.update_payment_btn.raise_()
        self.advance_checkbox.raise_()
        self.clear_payment_text_btn.raise_()
        self.payments_excel_warning.raise_()
        self.suppliers_combobox.raise_()
        self.supplier_tip_text.raise_()
        self.supplier_details_text.raise_()
        self.payments_all_select_delete_yes_btn.raise_()
        self.payments_all_select_delete_no_btn.raise_()
        self.payment_delete_selection_warning.raise_()
        self.payment_single_select_delete_no_btn.raise_()
        self.delete_all_payments_btn.raise_()
        self.payment_delete_all_warning.raise_()
        self.delete_selection_payment_btn.raise_()
        self.service_mendatory_label.raise_()
        self.supplier_mendatory_label.raise_()
        self.seperator_2.raise_()
        self.edit_payment_btn.raise_()
        self.category_combobox.raise_()
        self.guest_num_input.raise_()
        self.supplier_price_text.raise_()
        self.files_page_btn_label = QLabel(self.centralwidget)
        self.files_page_btn_label.setObjectName(u"files_page_btn_label")
        self.files_page_btn_label.setGeometry(QRect(560, 391, 61, 20))
        self.files_page_btn_label.setStyleSheet(u"QLabel {\n"
"	font: 63 12pt \"Segoe UI Semibold\";\n"
"	border-radius: 15px;	\n"
"	color: rgb(76, 77, 76);\n"
"}\n"
"")
        self.files_page_btn = QPushButton(self.centralwidget)
        self.files_page_btn.setObjectName(u"files_page_btn")
        self.files_page_btn.setGeometry(QRect(560, 340, 71, 51))
        self.files_page_btn.setFont(font1)
        self.files_page_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.files_page_btn.setMouseTracking(True)
        self.files_page_btn.setFocusPolicy(Qt.ClickFocus)
        self.files_page_btn.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/misc/add_files_icon.png);\n"
"	font: 63 20pt \"Segoe UI Semilight\";\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.cosmetic_label = QLabel(self.centralwidget)
        self.cosmetic_label.setObjectName(u"cosmetic_label")
        self.cosmetic_label.setGeometry(QRect(1004, 420, 21, 20))
        self.mission_mendatory_label = QLabel(self.centralwidget)
        self.mission_mendatory_label.setObjectName(u"mission_mendatory_label")
        self.mission_mendatory_label.setGeometry(QRect(970, 430, 51, 21))
        self.mission_mendatory_label.setStyleSheet(u"font: 11pt \"Segoe UI Semibold\";\n"
"color: rgb(239, 64, 64);")
        self.budget_status_label = QLabel(self.centralwidget)
        self.budget_status_label.setObjectName(u"budget_status_label")
        self.budget_status_label.setGeometry(QRect(230, 80, 580, 31))
        self.budget_status_label.setStyleSheet(u"font: 13pt \"Segoe UI Semibold\";\n"
"color: rgb(151,186,172);\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 15px;")
        self.budget_status_label.setAlignment(Qt.AlignCenter)
        self.budget_status_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.event_date_label = QLabel(self.centralwidget)
        self.event_date_label.setObjectName(u"event_date_label")
        self.event_date_label.setGeometry(QRect(90, 30, 201, 41))
        self.event_date_label.setStyleSheet(u"font: 16pt \"Segoe UI Semibold\";\n"
"\n"
"color: rgb(151,186,172);\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.event_date_label.setAlignment(Qt.AlignCenter)
        self.event_date_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.event_folder_label = QLabel(self.centralwidget)
        self.event_folder_label.setObjectName(u"event_folder_label")
        self.event_folder_label.setGeometry(QRect(110, 140, 141, 31))
        self.event_folder_label.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(224, 153, 94);\n"
"	font: 63 12pt \"Segoe UI Semibold\";\n"
"	\n"
"	border-radius: 15px;	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.adding_btn = QPushButton(self.centralwidget)
        self.adding_btn.setObjectName(u"adding_btn")
        self.adding_btn.setGeometry(QRect(860, 360, 151, 41))
        self.adding_btn.setFont(font2)
        self.adding_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.adding_btn.setMouseTracking(True)
        self.adding_btn.setFocusPolicy(Qt.ClickFocus)
        self.adding_btn.setStyleSheet(u"QPushButton {\n"
"	font: 63 15pt \"Segoe UI Semibold\";\n"
"	border-radius: 15px;	\n"
"	color: rgb(76, 77, 76);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(236,211,175);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(168,230,207);\n"
"	font: 63 17pt \"Segoe UI Semibold\";\n"
"}")
        self.files_btn_line = QFrame(self.centralwidget)
        self.files_btn_line.setObjectName(u"files_btn_line")
        self.files_btn_line.setGeometry(QRect(570, 420, 50, 3))
        self.files_btn_line.setStyleSheet(u"border: 2px solid #FFFFFF;\n"
"")
        self.files_btn_line.setFrameShape(QFrame.HLine)
        self.files_btn_line.setFrameShadow(QFrame.Sunken)
        self.missions_btn_line = QFrame(self.centralwidget)
        self.missions_btn_line.setObjectName(u"missions_btn_line")
        self.missions_btn_line.setGeometry(QRect(680, 420, 50, 3))
        self.missions_btn_line.setStyleSheet(u"border: 2px solid #FFFFFF;\n"
"")
        self.missions_btn_line.setFrameShape(QFrame.HLine)
        self.missions_btn_line.setFrameShadow(QFrame.Sunken)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(280, 230, 580, 3))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(280, 340, 580, 3))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.event_excel_btn = QPushButton(self.centralwidget)
        self.event_excel_btn.setObjectName(u"event_excel_btn")
        self.event_excel_btn.setGeometry(QRect(10, 190, 101, 91))
        self.event_excel_btn.setFont(font1)
        self.event_excel_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.event_excel_btn.setMouseTracking(True)
        self.event_excel_btn.setFocusPolicy(Qt.ClickFocus)
        self.event_excel_btn.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/misc/round_excel.png);	\n"
"	font: 63 20pt \"Segoe UI Semilight\";\n"
"	border-radius: 45px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb( 255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(168,230,207);\n"
"}")
        self.event_excel_label = QLabel(self.centralwidget)
        self.event_excel_label.setObjectName(u"event_excel_label")
        self.event_excel_label.setGeometry(QRect(110, 220, 141, 31))
        self.event_excel_label.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(8, 116, 59);\n"
"	font: 63 12pt \"Segoe UI Semibold\";\n"
"	\n"
"	border-radius: 15px;	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.event_delete_btn = QPushButton(self.centralwidget)
        self.event_delete_btn.setObjectName(u"event_delete_btn")
        self.event_delete_btn.setGeometry(QRect(10, 280, 101, 91))
        self.event_delete_btn.setFont(font1)
        self.event_delete_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.event_delete_btn.setMouseTracking(True)
        self.event_delete_btn.setFocusPolicy(Qt.ClickFocus)
        self.event_delete_btn.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/misc/garbage.png);\n"
"	font: 63 20pt \"Segoe UI Semilight\";\n"
"	border-radius: 45px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb( 255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(168,230,207);\n"
"}")
        self.event_delete_label = QLabel(self.centralwidget)
        self.event_delete_label.setObjectName(u"event_delete_label")
        self.event_delete_label.setGeometry(QRect(110, 310, 141, 31))
        self.event_delete_label.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(2, 155, 197);\n"
"	font: 63 12pt \"Segoe UI Semibold\";\n"
"	\n"
"	border-radius: 15px;	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.delete_warning_label = QLabel(self.centralwidget)
        self.delete_warning_label.setObjectName(u"delete_warning_label")
        self.delete_warning_label.setGeometry(QRect(100, 350, 201, 71))
        self.delete_warning_label.setStyleSheet(u"font: 10pt \"Segoe UI Semibold\";\n"
"color: rgb(239, 64, 64);")
        EventWindow.setCentralWidget(self.centralwidget)
        self.client_details_frame.raise_()
        self.upper_frame.raise_()
        self.event_folder_btn.raise_()
        self.client_details_btn.raise_()
        self.event_details_btn.raise_()
        self.event_detail_frame.raise_()
        self.payments_page_btn.raise_()
        self.payments_page_btn_label.raise_()
        self.missions_page_btn.raise_()
        self.missions_page_btn_label.raise_()
        self.events_stackedWidget.raise_()
        self.files_page_btn_label.raise_()
        self.files_page_btn.raise_()
        self.cosmetic_label.raise_()
        self.budget_status_label.raise_()
        self.event_date_label.raise_()
        self.event_folder_label.raise_()
        self.adding_btn.raise_()
        self.payments_btn_line.raise_()
        self.missions_btn_line.raise_()
        self.files_btn_line.raise_()
        self.mission_mendatory_label.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.event_excel_btn.raise_()
        self.event_excel_label.raise_()
        self.event_delete_btn.raise_()
        self.event_delete_label.raise_()
        self.delete_warning_label.raise_()

        self.retranslateUi(EventWindow)

        self.events_stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(EventWindow)
    # setupUi

    def retranslateUi(self, EventWindow):
        EventWindow.setWindowTitle(QCoreApplication.translate("EventWindow", u"MainWindow", None))
        self.headline_label.setText(QCoreApplication.translate("EventWindow", u"\u05d4\u05d7\u05ea\u05d5\u05e0\u05d4 \u05e9\u05dc \u05d0\u05d9\u05d9\u05dc \u05d5\u05de\u05d9\u05e8\u05d9", None))
#if QT_CONFIG(tooltip)
        self.event_clear_all_btn.setToolTip(QCoreApplication.translate("EventWindow", u"<html><head/><body><p>\u05dc\u05d7\u05e5 \u05dc\u05e4\u05ea\u05d9\u05d7\u05ea \u05ea\u05d9\u05e7\u05d9\u05d9\u05d4 \u05d0\u05d9\u05e9\u05d9\u05ea</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.event_clear_all_btn.setWhatsThis(QCoreApplication.translate("EventWindow", u"<html><head/><body><p>\u05dc\u05d7\u05e5 \u05dc\u05e4\u05ea\u05d9\u05d7\u05ea \u05ea\u05d9\u05e7\u05d9\u05d9\u05d4 \u05d0\u05d9\u05e9\u05d9\u05ea</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.event_clear_all_btn.setText("")
#if QT_CONFIG(tooltip)
        self.event_collapse_all_btn.setToolTip(QCoreApplication.translate("EventWindow", u"<html><head/><body><p>\u05dc\u05d7\u05e5 \u05dc\u05e4\u05ea\u05d9\u05d7\u05ea \u05ea\u05d9\u05e7\u05d9\u05d9\u05d4 \u05d0\u05d9\u05e9\u05d9\u05ea</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.event_collapse_all_btn.setWhatsThis(QCoreApplication.translate("EventWindow", u"<html><head/><body><p>\u05dc\u05d7\u05e5 \u05dc\u05e4\u05ea\u05d9\u05d7\u05ea \u05ea\u05d9\u05e7\u05d9\u05d9\u05d4 \u05d0\u05d9\u05e9\u05d9\u05ea</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.event_collapse_all_btn.setText("")
#if QT_CONFIG(tooltip)
        self.event_folder_btn.setToolTip(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\">\u05dc\u05d7\u05e5 \u05dc\u05e4\u05ea\u05d9\u05d7\u05ea \u05ea\u05d9\u05e7\u05d9\u05d9\u05d4 \u05d0\u05d9\u05e9\u05d9\u05ea</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.event_folder_btn.setWhatsThis(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\">\u05dc\u05d7\u05e5 \u05dc\u05e4\u05ea\u05d9\u05d7\u05ea \u05ea\u05d9\u05e7\u05d9\u05d9\u05d4 \u05d0\u05d9\u05e9\u05d9\u05ea</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.event_folder_btn.setText("")
#if QT_CONFIG(tooltip)
        self.client_details_btn.setToolTip(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u05d4\u05e6\u05d2 \u05e4\u05e8\u05d8\u05d9 \u05d0\u05e0\u05e9\u05d9 \u05e7\u05e9\u05e8 \u05dc\u05d0\u05d9\u05e8\u05d5\u05e2</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.client_details_btn.setWhatsThis(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u05d4\u05e6\u05d2 \u05e4\u05e8\u05d8\u05d9 \u05d0\u05e0\u05e9\u05d9 \u05e7\u05e9\u05e8 \u05dc\u05d0\u05d9\u05e8\u05d5\u05e2</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.client_details_btn.setText(QCoreApplication.translate("EventWindow", u"\u05d0\u05d9\u05e9 \u05e7\u05e9\u05e8", None))
#if QT_CONFIG(tooltip)
        self.event_details_btn.setToolTip(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u05d4\u05e6\u05d2 \u05e4\u05e8\u05d8\u05d9 \u05d0\u05d9\u05e8\u05d5\u05e2</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.event_details_btn.setWhatsThis(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u05d4\u05e6\u05d2 \u05e4\u05e8\u05d8\u05d9 \u05d0\u05d9\u05e8\u05d5\u05e2</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.event_details_btn.setText(QCoreApplication.translate("EventWindow", u"\u05e4\u05e8\u05d8\u05d9 \u05d0\u05d9\u05e8\u05d5\u05e2", None))
        self.client_detail_name1.setText("")
        self.client_detail_phone1.setText("")
        self.client_detail_address1.setText("")
        self.client_detail_phone2.setText("")
        self.client_detail_name2.setText("")
        self.client_detail_email2.setText("")
        self.client_detail_address2.setText("")
        self.event_detail_contract.setText("")
        self.event_detail_location.setText("")
        self.event_detail_name.setText("")
        self.event_detail_location_address.setText("")
#if QT_CONFIG(tooltip)
        self.event_budget_text.setToolTip(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\">\u05d4\u05db\u05e0\u05e1 \u05ea\u05e7\u05e6\u05d9\u05d1 \u05d0\u05d9\u05e8\u05d5\u05e2</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.event_budget_text.setWhatsThis(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\">\u05d4\u05db\u05e0\u05e1 \u05ea\u05e7\u05e6\u05d9\u05d1 \u05d0\u05d9\u05e8\u05d5\u05e2</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.event_budget_text.setHtml(QCoreApplication.translate("EventWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.event_budget_label.setText(QCoreApplication.translate("EventWindow", u"\u05ea\u05e7\u05e6\u05d9\u05d1 \u05d0\u05d9\u05e8\u05d5\u05e2", None))
#if QT_CONFIG(tooltip)
        self.update_budget_btn.setToolTip(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u05dc\u05d7\u05e5 \u05dc\u05e2\u05d3\u05db\u05d5\u05df \u05d4\u05ea\u05e7\u05e6\u05d9\u05d1</span></p><p align=\"center\"><span style=\" font-size:12pt;\">\u05dc\u05d0\u05d7\u05e8 \u05de\u05db\u05df \u05d9\u05e9 \u05dc\u05e2\u05d3\u05db\u05df \u05d0\u05ea \u05de\u05d0\u05d2\u05e8 \u05d4\u05de\u05d9\u05d3\u05e2 \u05d1\u05de\u05e1\u05da \u05d4\u05e8\u05d0\u05e9\u05d9</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.update_budget_btn.setWhatsThis(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u05dc\u05d7\u05e5 \u05dc\u05e2\u05d3\u05db\u05d5\u05df \u05d4\u05ea\u05e7\u05e6\u05d9\u05d1</span></p><p align=\"center\"><span style=\" font-size:12pt;\">\u05dc\u05d0\u05d7\u05e8 \u05de\u05db\u05df \u05d9\u05e9 \u05dc\u05e2\u05d3\u05db\u05df \u05d0\u05ea \u05de\u05d0\u05d2\u05e8 \u05d4\u05de\u05d9\u05d3\u05e2 \u05d1\u05de\u05e1\u05da \u05d4\u05e8\u05d0\u05e9\u05d9</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.update_budget_btn.setText(QCoreApplication.translate("EventWindow", u"\u05e2\u05d3\u05db\u05df", None))
#if QT_CONFIG(tooltip)
        self.payments_page_btn.setToolTip(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\">\u05d4\u05d5\u05e1\u05e3 \u05ea\u05e9\u05dc\u05d5\u05dd</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.payments_page_btn.setWhatsThis(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\">\u05d4\u05d5\u05e1\u05e3 \u05ea\u05e9\u05dc\u05d5\u05dd</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.payments_page_btn.setText("")
        self.payments_page_btn_label.setText(QCoreApplication.translate("EventWindow", u"\u05ea\u05e9\u05dc\u05d5\u05dd", None))
#if QT_CONFIG(tooltip)
        self.missions_page_btn.setToolTip(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\">\u05d4\u05d5\u05e1\u05e3 \u05de\u05e9\u05d9\u05de\u05d4</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.missions_page_btn.setWhatsThis(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\">\u05d4\u05d5\u05e1\u05e3 \u05de\u05e9\u05d9\u05de\u05d4</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.missions_page_btn.setText("")
        self.missions_page_btn_label.setText(QCoreApplication.translate("EventWindow", u"\u05de\u05e9\u05d9\u05de\u05d4", None))
        self.dragndrop_label.setText(QCoreApplication.translate("EventWindow", u"\u05e0\u05d9\u05ea\u05df \u05dc\u05d2\u05e8\u05d5\u05e8 \u05dc\u05db\u05d0\u05df \u05e7\u05d1\u05e6\u05d9\u05dd", None))
        self.or_label.setText(QCoreApplication.translate("EventWindow", u"\u05d0\u05d5 ", None))
        self.browser_btn.setText(QCoreApplication.translate("EventWindow", u"\u05dc\u05d1\u05d7\u05d5\u05e8 \u05e7\u05d1\u05e6\u05d9\u05dd", None))
        ___qtablewidgetitem = self.missions_tablewidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("EventWindow", u"\u05de\u05e9\u05d9\u05de\u05d4", None));
        ___qtablewidgetitem1 = self.missions_tablewidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("EventWindow", u"\u05ea\u05d0\u05e8\u05d9\u05da \u05dc\u05d1\u05d9\u05e6\u05d5\u05e2", None));
        ___qtablewidgetitem2 = self.missions_tablewidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("EventWindow", u"\u05e1\u05d8\u05d0\u05d8\u05d5\u05e1", None));
        ___qtablewidgetitem3 = self.missions_tablewidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("EventWindow", u"\u05d4\u05e2\u05e8\u05d5\u05ea", None));
        self.mission_name_text.setHtml(QCoreApplication.translate("EventWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.delete_all_missions_btn.setText(QCoreApplication.translate("EventWindow", u"\u05de\u05d7\u05e7 \u05d4\u05db\u05d5\u05dc", None))
        self.update_mission_btn.setText(QCoreApplication.translate("EventWindow", u"\u05e2\u05d3\u05db\u05df", None))
        self.clear_mission_input_btn.setText(QCoreApplication.translate("EventWindow", u"\u05e0\u05e7\u05d4 \u05d4\u05db\u05d5\u05dc", None))
        self.mission_single_select_delete_no_btn.setText(QCoreApplication.translate("EventWindow", u"\u05dc\u05d0", None))
        self.missions_delete_all_warning.setText(QCoreApplication.translate("EventWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semibold'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; color:#ef4040;\">!\u05dc\u05d0\u05d7\u05e8 \u05e4\u05e2\u05d5\u05dc\u05d4 \u05d6\u05d5 \u05dc\u05d0 \u05e0\u05d9\u05ea\u05df \u05dc\u05e9\u05d7\u05d6\u05e8 \u05d0\u05ea \u05d4\u05de\u05d9\u05d3\u05e2</span></p></body></html>", None))
        self.mission_single_select_delete_label.setText(QCoreApplication.translate("EventWindow", u"\u05d4\u05d0\u05dd \u05dc\u05de\u05d7\u05d5\u05e7 \u05dc\u05e6\u05de\u05d9\u05ea\u05d5\u05ea?", None))
        self.add_mission_btn.setText(QCoreApplication.translate("EventWindow", u"\u05d4\u05d5\u05e1\u05e4\u05d4", None))
        self.status_combobox.setItemText(0, QCoreApplication.translate("EventWindow", u"\u05d1\u05ea\u05d4\u05dc\u05d9\u05da", None))
        self.status_combobox.setItemText(1, QCoreApplication.translate("EventWindow", u"\u05d1\u05d5\u05e6\u05e2", None))
        self.status_combobox.setItemText(2, QCoreApplication.translate("EventWindow", u"\u05dc\u05d0 \u05e8\u05dc\u05d5\u05d5\u05e0\u05d8\u05d9", None))

        self.status_combobox.setCurrentText("")
        self.status_combobox.setPlaceholderText(QCoreApplication.translate("EventWindow", u"\u05e1\u05d8\u05d0\u05d8\u05d5\u05e1", None))
        self.missions_all_select_delete_label.setText(QCoreApplication.translate("EventWindow", u"\u05d4\u05d0\u05dd \u05dc\u05de\u05d7\u05d5\u05e7 \u05dc\u05e6\u05de\u05d9\u05ea\u05d5\u05ea?", None))
        self.missions_all_select_delete_yes_btn.setText(QCoreApplication.translate("EventWindow", u"\u05db\u05df", None))
        self.delete_selection_mission_btn.setText(QCoreApplication.translate("EventWindow", u"\u05de\u05d7\u05e7 \u05d1\u05d7\u05d9\u05e8\u05d4", None))
        self.mission_delete_selection_warning.setText(QCoreApplication.translate("EventWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semibold'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; color:#ef4040;\">!\u05dc\u05d0\u05d7\u05e8 \u05e4\u05e2\u05d5\u05dc\u05d4 \u05d6\u05d5 \u05dc\u05d0 \u05e0\u05d9\u05ea\u05df \u05dc\u05e9\u05d7\u05d6\u05e8 \u05d0\u05ea \u05d4\u05de\u05d9\u05d3\u05e2</span></p></body></html>", None))
        self.missions_excel_warning.setText(QCoreApplication.translate("EventWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semibold'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#ef4040;\">\u05d4\u05e7\u05d5\u05d1\u05e5 \u05d1\u05e9\u05d9\u05de\u05d5\u05e9 - \u05dc\u05d0 \u05e0\u05d9\u05ea\u05df \u05dc\u05e9\u05de\u05d5\u05e8</span></p></body></html>", None))
        self.mission_single_select_delete_yes_btn.setText(QCoreApplication.translate("EventWindow", u"\u05db\u05df", None))
        self.mission_notes_text.setHtml(QCoreApplication.translate("EventWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.missions_all_select_delete_no_btn.setText(QCoreApplication.translate("EventWindow", u"\u05dc\u05d0", None))
        self.mission_due_text.setHtml(QCoreApplication.translate("EventWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.missions_export_excel_btn.setToolTip(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\">\u05d9\u05d9\u05e6\u05d0 \u05de\u05e9\u05d9\u05de\u05d5\u05ea \u05dc\u05e7\u05d5\u05d1\u05e5 \u05d0\u05e7\u05e1\u05dc</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.missions_export_excel_btn.setWhatsThis(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\">\u05d9\u05d9\u05e6\u05d0 \u05de\u05e9\u05d9\u05de\u05d5\u05ea \u05dc\u05e7\u05d5\u05d1\u05e5 \u05d0\u05e7\u05e1\u05dc</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.missions_export_excel_btn.setText("")
        self.edit_mission_btn.setText(QCoreApplication.translate("EventWindow", u"\u05e2\u05e8\u05d5\u05da", None))
#if QT_CONFIG(tooltip)
        self.payments_export_excel_btn.setToolTip(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\">\u05d9\u05d9\u05e6\u05d0 \u05ea\u05e9\u05dc\u05d5\u05de\u05d9\u05dd \u05dc\u05e7\u05d5\u05d1\u05e5 \u05d0\u05e7\u05e1\u05dc</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.payments_export_excel_btn.setWhatsThis(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\">\u05d9\u05d9\u05e6\u05d0 \u05ea\u05e9\u05dc\u05d5\u05de\u05d9\u05dd \u05dc\u05e7\u05d5\u05d1\u05e5 \u05d0\u05e7\u05e1\u05dc</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.payments_export_excel_btn.setText("")
        self.supplier_service_text.setHtml(QCoreApplication.translate("EventWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.suppliers_combobox.setItemText(0, QCoreApplication.translate("EventWindow", u"\u05d1\u05d7\u05e8 \u05e1\u05e4\u05e7", None))
        self.suppliers_combobox.setItemText(1, QCoreApplication.translate("EventWindow", u"\u05de\u05d7\u05d9\u05e8 \u05de\u05e0\u05d4 - \u05d0\u05d5\u05dc\u05dd", None))
        self.suppliers_combobox.setItemText(2, QCoreApplication.translate("EventWindow", u"\u05d0\u05d7\u05e8", None))

#if QT_CONFIG(tooltip)
        self.suppliers_combobox.setToolTip(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\">\u05d1\u05d7\u05e8 \u05e1\u05e4\u05e7</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.suppliers_combobox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.suppliers_combobox.setCurrentText("")
        self.suppliers_combobox.setPlaceholderText(QCoreApplication.translate("EventWindow", u"\u05d1\u05d7\u05e8 \u05e1\u05e4\u05e7", None))
        self.add_payment_btn.setText(QCoreApplication.translate("EventWindow", u"\u05d4\u05d5\u05e1\u05e4\u05d4", None))
        self.supplier_advance_text.setHtml(QCoreApplication.translate("EventWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.update_payment_btn.setText(QCoreApplication.translate("EventWindow", u"\u05e2\u05d3\u05db\u05df", None))
        self.advance_checkbox.setText(QCoreApplication.translate("EventWindow", u"\u05e9\u05d5\u05dc\u05de\u05d4", None))
        self.clear_payment_text_btn.setText(QCoreApplication.translate("EventWindow", u"\u05e0\u05e7\u05d4 \u05d4\u05db\u05d5\u05dc", None))
        ___qtablewidgetitem4 = self.payments_tablewidget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("EventWindow", u"\u05e9\u05d9\u05e8\u05d5\u05ea", None));
        ___qtablewidgetitem5 = self.payments_tablewidget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("EventWindow", u"\u05e1\u05e4\u05e7", None));
        ___qtablewidgetitem6 = self.payments_tablewidget.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("EventWindow", u"\u05de\u05d7\u05d9\u05e8", None));
        ___qtablewidgetitem7 = self.payments_tablewidget.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("EventWindow", u"\u05de\u05e7\u05d3\u05de\u05d4", None));
        ___qtablewidgetitem8 = self.payments_tablewidget.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("EventWindow", u"\u05dc\u05ea\u05e9\u05dc\u05d5\u05dd", None));
        ___qtablewidgetitem9 = self.payments_tablewidget.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("EventWindow", u"\u05d8\u05d9\u05e4", None));
        ___qtablewidgetitem10 = self.payments_tablewidget.horizontalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("EventWindow", u"\u05e4\u05e8\u05d8\u05d9\u05dd \u05e0\u05d5\u05e1\u05e4\u05d9\u05dd", None));
        self.payments_excel_warning.setText(QCoreApplication.translate("EventWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semibold'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#ef4040;\">\u05d4\u05e7\u05d5\u05d1\u05e5 \u05d1\u05e9\u05d9\u05de\u05d5\u05e9 - \u05dc\u05d0 \u05e0\u05d9\u05ea\u05df \u05dc\u05e9\u05de\u05d5\u05e8</span></p></body></html>", None))
        self.supplier_tip_text.setHtml(QCoreApplication.translate("EventWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.supplier_details_text.setHtml(QCoreApplication.translate("EventWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.delete_selection_payment_btn.setText(QCoreApplication.translate("EventWindow", u"\u05de\u05d7\u05e7 \u05d1\u05d7\u05d9\u05e8\u05d4", None))
        self.delete_all_payments_btn.setText(QCoreApplication.translate("EventWindow", u"\u05de\u05d7\u05e7 \u05d4\u05db\u05d5\u05dc", None))
        self.payment_delete_selection_warning.setText(QCoreApplication.translate("EventWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semibold'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; color:#ef4040;\">!\u05dc\u05d0\u05d7\u05e8 \u05e4\u05e2\u05d5\u05dc\u05d4 \u05d6\u05d5 \u05dc\u05d0 \u05e0\u05d9\u05ea\u05df \u05dc\u05e9\u05d7\u05d6\u05e8 \u05d0\u05ea \u05d4\u05de\u05d9\u05d3\u05e2</span></p></body></html>", None))
        self.payment_single_select_delete_no_btn.setText(QCoreApplication.translate("EventWindow", u"\u05dc\u05d0", None))
        self.payment_delete_all_warning.setText(QCoreApplication.translate("EventWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semibold'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; color:#ef4040;\">!\u05dc\u05d0\u05d7\u05e8 \u05e4\u05e2\u05d5\u05dc\u05d4 \u05d6\u05d5 \u05dc\u05d0 \u05e0\u05d9\u05ea\u05df \u05dc\u05e9\u05d7\u05d6\u05e8 \u05d0\u05ea \u05d4\u05de\u05d9\u05d3\u05e2</span></p></body></html>", None))
        self.payment_single_select_delete_yes_btn.setText(QCoreApplication.translate("EventWindow", u"\u05db\u05df", None))
        self.payment_single_select_delete_label.setText(QCoreApplication.translate("EventWindow", u"\u05d4\u05d0\u05dd \u05dc\u05de\u05d7\u05d5\u05e7 \u05dc\u05e6\u05de\u05d9\u05ea\u05d5\u05ea?", None))
        self.payments_all_select_delete_no_btn.setText(QCoreApplication.translate("EventWindow", u"\u05dc\u05d0", None))
        self.payments_all_select_delete_label.setText(QCoreApplication.translate("EventWindow", u"\u05d4\u05d0\u05dd \u05dc\u05de\u05d7\u05d5\u05e7 \u05dc\u05e6\u05de\u05d9\u05ea\u05d5\u05ea?", None))
        self.payments_all_select_delete_yes_btn.setText(QCoreApplication.translate("EventWindow", u"\u05db\u05df", None))
        self.service_mendatory_label.setText(QCoreApplication.translate("EventWindow", u"\u05d7\u05d5\u05d1\u05d4*", None))
        self.supplier_mendatory_label.setText(QCoreApplication.translate("EventWindow", u"\u05d7\u05d5\u05d1\u05d4*", None))
        self.edit_payment_btn.setText(QCoreApplication.translate("EventWindow", u"\u05e2\u05e8\u05d5\u05da", None))
        self.category_combobox.setItemText(0, QCoreApplication.translate("EventWindow", u"\u05d1\u05d7\u05e8 \u05e7\u05d8\u05d2\u05d5\u05e8\u05d9\u05d4", None))
        self.category_combobox.setItemText(1, QCoreApplication.translate("EventWindow", u"\u05d4\u05e4\u05e7\u05d4", None))
        self.category_combobox.setItemText(2, QCoreApplication.translate("EventWindow", u"\u05de\u05e7\u05d5\u05dd \u05d4\u05d0\u05d9\u05e8\u05d5\u05e2", None))
        self.category_combobox.setItemText(3, QCoreApplication.translate("EventWindow", u"\u05d7\u05d5\u05e4\u05d4 \u05d5\u05e8\u05d1\u05e0\u05d5\u05ea", None))
        self.category_combobox.setItemText(4, QCoreApplication.translate("EventWindow", u"\u05d0\u05d8\u05e8\u05e7\u05e6\u05d9\u05d5\u05ea", None))
        self.category_combobox.setItemText(5, QCoreApplication.translate("EventWindow", u"\u05d4\u05e1\u05e2\u05d5\u05ea - \u05d0\u05d9\u05e8\u05d5\u05e2", None))
        self.category_combobox.setItemText(6, QCoreApplication.translate("EventWindow", u"\u05d7\u05ea\u05df", None))
        self.category_combobox.setItemText(7, QCoreApplication.translate("EventWindow", u"\u05db\u05dc\u05d4", None))
        self.category_combobox.setItemText(8, QCoreApplication.translate("EventWindow", u"\u05d4\u05d3\u05e4\u05e1\u05d5\u05ea", None))
        self.category_combobox.setItemText(9, QCoreApplication.translate("EventWindow", u"\u05de\u05d5\u05d6\u05d9\u05e7\u05d4", None))
        self.category_combobox.setItemText(10, QCoreApplication.translate("EventWindow", u"\u05d0\u05d7\u05e8", None))
        self.category_combobox.setItemText(11, QCoreApplication.translate("EventWindow", u"\u05de\u05ea\u05e0\u05d5\u05ea", None))

#if QT_CONFIG(tooltip)
        self.category_combobox.setToolTip(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\">\u05d1\u05d7\u05e8 \u05e7\u05d8\u05d2\u05d5\u05e8\u05d9\u05d4</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.category_combobox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.category_combobox.setCurrentText(QCoreApplication.translate("EventWindow", u"\u05d1\u05d7\u05e8 \u05e7\u05d8\u05d2\u05d5\u05e8\u05d9\u05d4", None))
        self.category_combobox.setPlaceholderText(QCoreApplication.translate("EventWindow", u"\u05d1\u05d7\u05e8 \u05e7\u05d8\u05d2\u05d5\u05e8\u05d9\u05d4", None))
        self.guest_num_input.setHtml(QCoreApplication.translate("EventWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.supplier_price_text.setHtml(QCoreApplication.translate("EventWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.files_page_btn_label.setText(QCoreApplication.translate("EventWindow", u"\u05e7\u05d1\u05e6\u05d9\u05dd", None))
#if QT_CONFIG(tooltip)
        self.files_page_btn.setToolTip(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\">\u05d4\u05d5\u05e1\u05e3 \u05e7\u05d1\u05e6\u05d9\u05dd</p><p align=\"center\"><span style=\" font-size:12pt;\">\u05dc\u05d0\u05d7\u05e8 \u05d4\u05d5\u05e1\u05e4\u05d4 \u05e0\u05d9\u05ea\u05df \u05dc\u05d2\u05e9\u05ea \u05d3\u05e8\u05da &quot;\u05ea\u05d9\u05e7\u05d9\u05d9\u05d4 \u05d0\u05d9\u05e9\u05d9\u05ea&quot;</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.files_page_btn.setWhatsThis(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\">\u05d4\u05d5\u05e1\u05e3 \u05e7\u05d1\u05e6\u05d9\u05dd</p><p align=\"center\"><span style=\" font-size:12pt;\">\u05dc\u05d0\u05d7\u05e8 \u05d4\u05d5\u05e1\u05e4\u05d4 \u05e0\u05d9\u05ea\u05df \u05dc\u05d2\u05e9\u05ea \u05d3\u05e8\u05da &quot;\u05ea\u05d9\u05e7\u05d9\u05d9\u05d4 \u05d0\u05d9\u05e9\u05d9\u05ea&quot;</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.files_page_btn.setText("")
        self.cosmetic_label.setText("")
        self.mission_mendatory_label.setText(QCoreApplication.translate("EventWindow", u"\u05d7\u05d5\u05d1\u05d4*", None))
        self.event_date_label.setText(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">\u29bf\u29bf</span></p></body></html>", None))
        self.event_folder_label.setText(QCoreApplication.translate("EventWindow", u" \u05ea\u05d9\u05e7\u05d9\u05d9\u05d4 \u05d0\u05d9\u05e9\u05d9\u05ea", None))
        self.adding_btn.setText(QCoreApplication.translate("EventWindow", u"\u05d4\u05d5\u05e1\u05e4\u05d4", None))
#if QT_CONFIG(tooltip)
        self.event_excel_btn.setToolTip(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\">\u05d9\u05d9\u05e6\u05d0 \u05ea\u05e9\u05dc\u05d5\u05de\u05d9\u05dd \u05d5\u05de\u05e9\u05d9\u05de\u05d5\u05ea \u05dc\u05e7\u05d5\u05d1\u05e5 \u05d0\u05e7\u05e1\u05dc</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.event_excel_btn.setWhatsThis(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\">\u05d9\u05d9\u05e6\u05d0 \u05ea\u05e9\u05dc\u05d5\u05de\u05d9\u05dd \u05d5\u05de\u05e9\u05d9\u05de\u05d5\u05ea \u05dc\u05e7\u05d5\u05d1\u05e5 \u05d0\u05e7\u05e1\u05dc</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.event_excel_btn.setText("")
        self.event_excel_label.setText(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\">\u05de\u05d9\u05d3\u05e2 \u05e2\u05dc \u05d0\u05d9\u05e8\u05d5\u05e2</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.event_delete_btn.setToolTip(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\">\u05de\u05d7\u05e7 \u05d0\u05d9\u05e8\u05d5\u05e2 \u05d5\u05d0\u05e0\u05e9\u05d9 \u05e7\u05e9\u05e8 \u05d4\u05de\u05e9\u05d5\u05d9\u05d9\u05db\u05d9\u05dd \u05d0\u05dc\u05d9\u05d5</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.event_delete_btn.setWhatsThis(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\">\u05de\u05d7\u05e7 \u05d0\u05d9\u05e8\u05d5\u05e2 \u05d5\u05d0\u05e0\u05e9\u05d9 \u05e7\u05e9\u05e8 \u05d4\u05de\u05e9\u05d5\u05d9\u05d9\u05db\u05d9\u05dd \u05d0\u05dc\u05d9\u05d5</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.event_delete_btn.setText("")
        self.event_delete_label.setText(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\">\u05de\u05d7\u05e7 \u05d0\u05d9\u05e8\u05d5\u05e2</p></body></html>", None))
        self.delete_warning_label.setText(QCoreApplication.translate("EventWindow", u"<html><head/><body><p align=\"center\">\u05d1\u05d7\u05d9\u05e8\u05d4 \u05d6\u05d5 \u05ea\u05de\u05d7\u05d5\u05e7 \u05d2\u05dd \u05d0\u05ea <br/>\u05d0\u05e0\u05e9\u05d9 \u05d4\u05e7\u05e9\u05e8 \u05de\u05de\u05d0\u05d2\u05e8 \u05d4\u05de\u05d9\u05d3\u05e2<br/><span style=\" font-size:12pt; color:#ff0000;\">\u05dc\u05d7\u05e5 \u05e9\u05d5\u05d1 \u05dc\u05de\u05d7\u05d9\u05e7\u05d4</span></p></body></html>", None))
    # retranslateUi

