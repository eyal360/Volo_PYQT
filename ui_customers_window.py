# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customers_windowbdEUsp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import client_window_icon_rc
import dialog_rc

class Ui_CustomersWindow(object):
    def setupUi(self, CustomersWindow):
        if not CustomersWindow.objectName():
            CustomersWindow.setObjectName(u"CustomersWindow")
        CustomersWindow.resize(1107, 866)
        CustomersWindow.setStyleSheet(u"background-color: rgb(186,225,255);")
        self.centralwidget = QWidget(CustomersWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.customers_tablewidget = QTableWidget(self.centralwidget)
        if (self.customers_tablewidget.columnCount() < 9):
            self.customers_tablewidget.setColumnCount(9)
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font);
        self.customers_tablewidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font);
        self.customers_tablewidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font);
        self.customers_tablewidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font);
        self.customers_tablewidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font);
        self.customers_tablewidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        font1.setKerning(False)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFont(font1);
        self.customers_tablewidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFont(font);
        self.customers_tablewidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFont(font);
        self.customers_tablewidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFont(font);
        self.customers_tablewidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.customers_tablewidget.setObjectName(u"customers_tablewidget")
        self.customers_tablewidget.setGeometry(QRect(10, 430, 1091, 331))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customers_tablewidget.sizePolicy().hasHeightForWidth())
        self.customers_tablewidget.setSizePolicy(sizePolicy)
        self.customers_tablewidget.setMaximumSize(QSize(1100, 1000))
        font2 = QFont()
        font2.setPointSize(9)
        self.customers_tablewidget.setFont(font2)
        self.customers_tablewidget.setLayoutDirection(Qt.RightToLeft)
        self.customers_tablewidget.setAutoFillBackground(False)
        self.customers_tablewidget.setStyleSheet(u"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: rgb(255,255,255);\n"
"    width: 18px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(196, 213, 242);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(151, 152, 186);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(151, 152, 186);\n"
"	height: 15px;\n"
""
                        "	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background-color: rgb(255,255,255);\n"
"    width: 18px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: rgb(196, 213, 242);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
" 	border: none;\n"
"	background-color: rgb(151, 152, 186);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-ri"
                        "ght-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;   \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"	background: none;\n"
"\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"	background: none;\n"
"\n"
"}\n"
"")
        self.customers_tablewidget.setFrameShape(QFrame.NoFrame)
        self.customers_tablewidget.setMidLineWidth(0)
        self.customers_tablewidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.customers_tablewidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.customers_tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.customers_tablewidget.setTabKeyNavigation(True)
        self.customers_tablewidget.setProperty("showDropIndicator", False)
        self.customers_tablewidget.setDragEnabled(False)
        self.customers_tablewidget.setDragDropOverwriteMode(False)
        self.customers_tablewidget.setAlternatingRowColors(True)
        self.customers_tablewidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.customers_tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.customers_tablewidget.setTextElideMode(Qt.ElideMiddle)
        self.customers_tablewidget.setGridStyle(Qt.DashLine)
        self.delete_all_clients_btn = QPushButton(self.centralwidget)
        self.delete_all_clients_btn.setObjectName(u"delete_all_clients_btn")
        self.delete_all_clients_btn.setGeometry(QRect(60, 800, 261, 51))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Semilight")
        font3.setPointSize(20)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(7)
        self.delete_all_clients_btn.setFont(font3)
        self.delete_all_clients_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.delete_all_clients_btn.setMouseTracking(True)
        self.delete_all_clients_btn.setFocusPolicy(Qt.ClickFocus)
        self.delete_all_clients_btn.setStyleSheet(u"QPushButton {\n"
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
        self.event_date_input = QTextEdit(self.centralwidget)
        self.event_date_input.setObjectName(u"event_date_input")
        self.event_date_input.setGeometry(QRect(520, 120, 161, 41))
        self.event_date_input.setLayoutDirection(Qt.RightToLeft)
        self.event_date_input.setStyleSheet(u"font: 11pt \"Segoe UI Semilight\";\n"
"border: 1px solid #090206;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.event_date_input.setFrameShape(QFrame.StyledPanel)
        self.event_date_input.setFrameShadow(QFrame.Plain)
        self.event_date_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.event_date_input.setAutoFormatting(QTextEdit.AutoAll)
        self.event_date_input.setTabChangesFocus(True)
        self.event_date_input.setLineWrapMode(QTextEdit.WidgetWidth)
        self.event_date_input.setOverwriteMode(False)
        self.contact2_name_input = QTextEdit(self.centralwidget)
        self.contact2_name_input.setObjectName(u"contact2_name_input")
        self.contact2_name_input.setGeometry(QRect(860, 280, 191, 41))
        self.contact2_name_input.setLayoutDirection(Qt.RightToLeft)
        self.contact2_name_input.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border: 1px solid #090206;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.contact2_name_input.setFrameShape(QFrame.StyledPanel)
        self.contact2_name_input.setFrameShadow(QFrame.Plain)
        self.contact2_name_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.contact2_name_input.setTabChangesFocus(True)
        self.contact2_name_input.setLineWrapMode(QTextEdit.WidgetWidth)
        self.contact2_name_input.setOverwriteMode(False)
        self.customers_export_excel_btn = QPushButton(self.centralwidget)
        self.customers_export_excel_btn.setObjectName(u"customers_export_excel_btn")
        self.customers_export_excel_btn.setGeometry(QRect(500, 790, 101, 71))
        self.customers_export_excel_btn.setFont(font3)
        self.customers_export_excel_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.customers_export_excel_btn.setMouseTracking(True)
        self.customers_export_excel_btn.setFocusPolicy(Qt.ClickFocus)
        self.customers_export_excel_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(186,225,255);\n"
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
        self.event_name_input = QTextEdit(self.centralwidget)
        self.event_name_input.setObjectName(u"event_name_input")
        self.event_name_input.setGeometry(QRect(690, 120, 211, 41))
        self.event_name_input.setLayoutDirection(Qt.RightToLeft)
        self.event_name_input.setStyleSheet(u"font: 11pt \"Segoe UI Semilight\";\n"
"border: 3px solid #6248F0;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.event_name_input.setInputMethodHints(Qt.ImhMultiLine)
        self.event_name_input.setFrameShape(QFrame.StyledPanel)
        self.event_name_input.setFrameShadow(QFrame.Plain)
        self.event_name_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.event_name_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.event_name_input.setAutoFormatting(QTextEdit.AutoAll)
        self.event_name_input.setTabChangesFocus(True)
        self.event_name_input.setLineWrapMode(QTextEdit.WidgetWidth)
        self.event_name_input.setOverwriteMode(False)
        self.contact1_phone_input = QTextEdit(self.centralwidget)
        self.contact1_phone_input.setObjectName(u"contact1_phone_input")
        self.contact1_phone_input.setGeometry(QRect(370, 230, 141, 41))
        self.contact1_phone_input.setLayoutDirection(Qt.RightToLeft)
        self.contact1_phone_input.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border: 1px solid #090206;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.contact1_phone_input.setFrameShape(QFrame.StyledPanel)
        self.contact1_phone_input.setFrameShadow(QFrame.Plain)
        self.contact1_phone_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.contact1_phone_input.setTabChangesFocus(True)
        self.contact1_phone_input.setLineWrapMode(QTextEdit.WidgetWidth)
        self.contact1_phone_input.setOverwriteMode(False)
        self.rate_input = QTextEdit(self.centralwidget)
        self.rate_input.setObjectName(u"rate_input")
        self.rate_input.setGeometry(QRect(390, 120, 111, 41))
        self.rate_input.setLayoutDirection(Qt.RightToLeft)
        self.rate_input.setStyleSheet(u"font: 11pt \"Segoe UI Semilight\";\n"
"border: 1px solid #090206;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.rate_input.setFrameShape(QFrame.StyledPanel)
        self.rate_input.setFrameShadow(QFrame.Plain)
        self.rate_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rate_input.setAutoFormatting(QTextEdit.AutoAll)
        self.rate_input.setTabChangesFocus(False)
        self.rate_input.setLineWrapMode(QTextEdit.WidgetWidth)
        self.rate_input.setOverwriteMode(False)
        self.upper_frame = QFrame(self.centralwidget)
        self.upper_frame.setObjectName(u"upper_frame")
        self.upper_frame.setGeometry(QRect(10, 10, 1081, 101))
        font4 = QFont()
        font4.setPointSize(15)
        self.upper_frame.setFont(font4)
        self.upper_frame.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"border-radius: 40px;")
        self.upper_frame.setFrameShape(QFrame.StyledPanel)
        self.upper_frame.setFrameShadow(QFrame.Raised)
        self.upper_frame_header_btn = QPushButton(self.upper_frame)
        self.upper_frame_header_btn.setObjectName(u"upper_frame_header_btn")
        self.upper_frame_header_btn.setGeometry(QRect(280, 10, 531, 79))
        font5 = QFont()
        font5.setFamily(u"Segoe UI Semibold")
        font5.setPointSize(42)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(7)
        self.upper_frame_header_btn.setFont(font5)
        self.upper_frame_header_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.upper_frame_header_btn.setMouseTracking(True)
        self.upper_frame_header_btn.setFocusPolicy(Qt.ClickFocus)
        self.upper_frame_header_btn.setAutoFillBackground(False)
        self.upper_frame_header_btn.setStyleSheet(u"QPushButton {\n"
"\n"
"	color: rgb(167,202,229);\n"
"	font: 63 42pt \"Segoe UI Semibold\";\n"
"	border-radius: 30px;\n"
"}\n"
"")
        self.label = QLabel(self.upper_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(740, -20, 131, 141))
        self.label.setStyleSheet(u"image: url(:/icons/logo/Pheonix.ico);\n"
"")
        self.contact1_email_input = QTextEdit(self.centralwidget)
        self.contact1_email_input.setObjectName(u"contact1_email_input")
        self.contact1_email_input.setGeometry(QRect(50, 230, 311, 41))
        self.contact1_email_input.setLayoutDirection(Qt.RightToLeft)
        self.contact1_email_input.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border: 1px solid #090206;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.contact1_email_input.setFrameShape(QFrame.StyledPanel)
        self.contact1_email_input.setFrameShadow(QFrame.Plain)
        self.contact1_email_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.contact1_email_input.setTabChangesFocus(True)
        self.contact1_email_input.setLineWrapMode(QTextEdit.WidgetWidth)
        self.contact1_email_input.setOverwriteMode(False)
        self.add_client_btn = QPushButton(self.centralwidget)
        self.add_client_btn.setObjectName(u"add_client_btn")
        self.add_client_btn.setGeometry(QRect(790, 360, 261, 51))
        self.add_client_btn.setFont(font3)
        self.add_client_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.add_client_btn.setMouseTracking(True)
        self.add_client_btn.setFocusPolicy(Qt.ClickFocus)
        self.add_client_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(165,212,106);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semilight\";\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(62,178,101);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(45,127,72);\n"
"}")
        self.contract_checkbox = QCheckBox(self.centralwidget)
        self.contract_checkbox.setObjectName(u"contract_checkbox")
        self.contract_checkbox.setGeometry(QRect(230, 120, 141, 41))
        self.contract_checkbox.setLayoutDirection(Qt.RightToLeft)
        self.contract_checkbox.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.contact2_email_input = QTextEdit(self.centralwidget)
        self.contact2_email_input.setObjectName(u"contact2_email_input")
        self.contact2_email_input.setGeometry(QRect(50, 280, 311, 41))
        self.contact2_email_input.setLayoutDirection(Qt.RightToLeft)
        self.contact2_email_input.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border: 1px solid #090206;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.contact2_email_input.setFrameShape(QFrame.StyledPanel)
        self.contact2_email_input.setFrameShadow(QFrame.Plain)
        self.contact2_email_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.contact2_email_input.setTabChangesFocus(True)
        self.contact2_email_input.setLineWrapMode(QTextEdit.WidgetWidth)
        self.contact2_email_input.setOverwriteMode(False)
        self.contact1_address_input = QTextEdit(self.centralwidget)
        self.contact1_address_input.setObjectName(u"contact1_address_input")
        self.contact1_address_input.setGeometry(QRect(520, 230, 331, 41))
        self.contact1_address_input.setLayoutDirection(Qt.RightToLeft)
        self.contact1_address_input.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border: 1px solid #090206;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.contact1_address_input.setFrameShape(QFrame.StyledPanel)
        self.contact1_address_input.setFrameShadow(QFrame.Plain)
        self.contact1_address_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.contact1_address_input.setTabChangesFocus(True)
        self.contact1_address_input.setLineWrapMode(QTextEdit.WidgetWidth)
        self.contact1_address_input.setOverwriteMode(False)
        self.contact1_address_input.setPlaceholderText(u"                    \u05db\u05ea\u05d5\u05d1\u05ea \u05de\u05dc\u05d0\u05d4")
        self.delete_selection_client_btn = QPushButton(self.centralwidget)
        self.delete_selection_client_btn.setObjectName(u"delete_selection_client_btn")
        self.delete_selection_client_btn.setGeometry(QRect(800, 800, 261, 51))
        self.delete_selection_client_btn.setFont(font3)
        self.delete_selection_client_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.delete_selection_client_btn.setMouseTracking(True)
        self.delete_selection_client_btn.setFocusPolicy(Qt.ClickFocus)
        self.delete_selection_client_btn.setStyleSheet(u"QPushButton {\n"
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
        self.contact2_address_input = QTextEdit(self.centralwidget)
        self.contact2_address_input.setObjectName(u"contact2_address_input")
        self.contact2_address_input.setGeometry(QRect(520, 280, 331, 41))
        self.contact2_address_input.setLayoutDirection(Qt.RightToLeft)
        self.contact2_address_input.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border: 1px solid #090206;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.contact2_address_input.setFrameShape(QFrame.StyledPanel)
        self.contact2_address_input.setFrameShadow(QFrame.Plain)
        self.contact2_address_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.contact2_address_input.setTabChangesFocus(True)
        self.contact2_address_input.setLineWrapMode(QTextEdit.WidgetWidth)
        self.contact2_address_input.setOverwriteMode(False)
        self.contact2_address_input.setPlaceholderText(u"                    \u05db\u05ea\u05d5\u05d1\u05ea \u05de\u05dc\u05d0\u05d4")
        self.clear_client_fields_btn = QPushButton(self.centralwidget)
        self.clear_client_fields_btn.setObjectName(u"clear_client_fields_btn")
        self.clear_client_fields_btn.setGeometry(QRect(60, 360, 261, 51))
        self.clear_client_fields_btn.setFont(font3)
        self.clear_client_fields_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.clear_client_fields_btn.setMouseTracking(True)
        self.clear_client_fields_btn.setFocusPolicy(Qt.ClickFocus)
        self.clear_client_fields_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(76, 77, 76);\n"
"	font: 63 20pt \"Segoe UI Semilight\";\n"
"	border-radius: 20px;\n"
"	border: 1px solid #009de2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255,255,255);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(76, 77, 76);\n"
"}")
        self.main_item_seperator_line = QFrame(self.centralwidget)
        self.main_item_seperator_line.setObjectName(u"main_item_seperator_line")
        self.main_item_seperator_line.setGeometry(QRect(60, 340, 991, 20))
        self.main_item_seperator_line.setFrameShape(QFrame.HLine)
        self.main_item_seperator_line.setFrameShadow(QFrame.Sunken)
        self.contact2_phone_input = QTextEdit(self.centralwidget)
        self.contact2_phone_input.setObjectName(u"contact2_phone_input")
        self.contact2_phone_input.setGeometry(QRect(370, 280, 141, 41))
        self.contact2_phone_input.setLayoutDirection(Qt.RightToLeft)
        self.contact2_phone_input.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border: 1px solid #090206;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.contact2_phone_input.setFrameShape(QFrame.StyledPanel)
        self.contact2_phone_input.setFrameShadow(QFrame.Plain)
        self.contact2_phone_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.contact2_phone_input.setTabChangesFocus(True)
        self.contact2_phone_input.setLineWrapMode(QTextEdit.WidgetWidth)
        self.contact2_phone_input.setOverwriteMode(False)
        self.edit_client_btn = QPushButton(self.centralwidget)
        self.edit_client_btn.setObjectName(u"edit_client_btn")
        self.edit_client_btn.setGeometry(QRect(430, 360, 261, 51))
        self.edit_client_btn.setFont(font3)
        self.edit_client_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.edit_client_btn.setMouseTracking(True)
        self.edit_client_btn.setFocusPolicy(Qt.ClickFocus)
        self.edit_client_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255,223,128);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semilight\";\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255,192,128);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(234,206,41);\n"
"}")
        self.contact1_name_input = QTextEdit(self.centralwidget)
        self.contact1_name_input.setObjectName(u"contact1_name_input")
        self.contact1_name_input.setGeometry(QRect(860, 230, 191, 41))
        self.contact1_name_input.setLayoutDirection(Qt.RightToLeft)
        self.contact1_name_input.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border: 3px solid #6248F0;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.contact1_name_input.setFrameShape(QFrame.StyledPanel)
        self.contact1_name_input.setFrameShadow(QFrame.Plain)
        self.contact1_name_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.contact1_name_input.setTabChangesFocus(True)
        self.contact1_name_input.setLineWrapMode(QTextEdit.WidgetWidth)
        self.contact1_name_input.setOverwriteMode(False)
        self.event_location_input = QTextEdit(self.centralwidget)
        self.event_location_input.setObjectName(u"event_location_input")
        self.event_location_input.setGeometry(QRect(710, 170, 281, 41))
        self.event_location_input.setLayoutDirection(Qt.RightToLeft)
        self.event_location_input.setStyleSheet(u"font: 11pt \"Segoe UI Semilight\";\n"
"border: 1px solid #090206;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.event_location_input.setFrameShape(QFrame.StyledPanel)
        self.event_location_input.setFrameShadow(QFrame.Plain)
        self.event_location_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.event_location_input.setAutoFormatting(QTextEdit.AutoAll)
        self.event_location_input.setTabChangesFocus(True)
        self.event_location_input.setLineWrapMode(QTextEdit.WidgetWidth)
        self.event_location_input.setOverwriteMode(False)
        self.event_location_address_input = QTextEdit(self.centralwidget)
        self.event_location_address_input.setObjectName(u"event_location_address_input")
        self.event_location_address_input.setGeometry(QRect(220, 170, 481, 41))
        self.event_location_address_input.setLayoutDirection(Qt.RightToLeft)
        self.event_location_address_input.setStyleSheet(u"font: 11pt \"Segoe UI Semilight\";\n"
"border: 1px solid #090206;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.event_location_address_input.setFrameShape(QFrame.StyledPanel)
        self.event_location_address_input.setFrameShadow(QFrame.Plain)
        self.event_location_address_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.event_location_address_input.setTabChangesFocus(True)
        self.event_location_address_input.setLineWrapMode(QTextEdit.WidgetWidth)
        self.event_location_address_input.setOverwriteMode(False)
        self.update_client_btn = QPushButton(self.centralwidget)
        self.update_client_btn.setObjectName(u"update_client_btn")
        self.update_client_btn.setGeometry(QRect(410, 360, 311, 51))
        font6 = QFont()
        font6.setFamily(u"Segoe UI Semibold")
        font6.setPointSize(20)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(7)
        self.update_client_btn.setFont(font6)
        self.update_client_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.update_client_btn.setMouseTracking(True)
        self.update_client_btn.setFocusPolicy(Qt.ClickFocus)
        self.update_client_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255,223,128);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semibold\";\n"
"	border-radius: 20px;\n"
"	border: 2px solid #009de2;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255,192,128);\n"
"	font: 63 24pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(234,206,41);\n"
"}")
        self.event_mendatory_label = QLabel(self.centralwidget)
        self.event_mendatory_label.setObjectName(u"event_mendatory_label")
        self.event_mendatory_label.setGeometry(QRect(900, 120, 51, 31))
        self.event_mendatory_label.setStyleSheet(u"font: 11pt \"Segoe UI Semibold\";\n"
"color: rgb(239, 64, 64);")
        self.contact_mendatory_label = QLabel(self.centralwidget)
        self.contact_mendatory_label.setObjectName(u"contact_mendatory_label")
        self.contact_mendatory_label.setGeometry(QRect(1050, 230, 51, 31))
        self.contact_mendatory_label.setStyleSheet(u"font: 11pt \"Segoe UI Semibold\";\n"
"color: rgb(239, 64, 64);")
        self.delete_selection_warning = QLabel(self.centralwidget)
        self.delete_selection_warning.setObjectName(u"delete_selection_warning")
        self.delete_selection_warning.setGeometry(QRect(750, 770, 341, 31))
        self.delete_selection_warning.setCursor(QCursor(Qt.BlankCursor))
        self.delete_selection_warning.setStyleSheet(u"font: 16pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border: 1px solid #e38c8c;\n"
"")
        self.delete_selection_warning.setLineWidth(0)
        self.delete_selection_warning.setScaledContents(False)
        self.delete_selection_warning.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.delete_all_warning = QLabel(self.centralwidget)
        self.delete_all_warning.setObjectName(u"delete_all_warning")
        self.delete_all_warning.setGeometry(QRect(20, 770, 341, 31))
        self.delete_all_warning.setCursor(QCursor(Qt.BlankCursor))
        self.delete_all_warning.setStyleSheet(u"font: 16pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border: 1px solid #e38c8c;\n"
"")
        self.delete_all_warning.setLineWidth(0)
        self.delete_all_warning.setScaledContents(False)
        self.delete_all_warning.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.excel_warning = QLabel(self.centralwidget)
        self.excel_warning.setObjectName(u"excel_warning")
        self.excel_warning.setGeometry(QRect(430, 760, 261, 31))
        self.excel_warning.setCursor(QCursor(Qt.BlankCursor))
        self.excel_warning.setStyleSheet(u"font: 16pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.excel_warning.setLineWidth(0)
        self.excel_warning.setScaledContents(False)
        self.excel_warning.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lead_check = QRadioButton(self.centralwidget)
        self.lead_check.setObjectName(u"lead_check")
        self.lead_check.setGeometry(QRect(1010, 120, 71, 41))
        self.lead_check.setLayoutDirection(Qt.LeftToRight)
        self.lead_check.setAutoFillBackground(False)
        self.lead_check.setStyleSheet(u"background-color: rgb(196,197,242);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 15pt \"Segoe UI Semibold\";\n"
"border-radius: 20px;")
        self.editing_state_label = QLabel(self.centralwidget)
        self.editing_state_label.setObjectName(u"editing_state_label")
        self.editing_state_label.setGeometry(QRect(850, 40, 231, 41))
        self.editing_state_label.setCursor(QCursor(Qt.ArrowCursor))
        self.editing_state_label.setStyleSheet(u"font: 16pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(137,236,218);\n"
"border-radius: 20px;\n"
"")
        self.editing_state_label.setLineWidth(0)
        self.editing_state_label.setScaledContents(False)
        self.editing_state_label.setAlignment(Qt.AlignCenter)
        self.single_select_delete_label = QLabel(self.centralwidget)
        self.single_select_delete_label.setObjectName(u"single_select_delete_label")
        self.single_select_delete_label.setGeometry(QRect(900, 820, 201, 31))
        self.single_select_delete_label.setStyleSheet(u"font: 63 12pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.single_select_delete_yes_btn = QPushButton(self.centralwidget)
        self.single_select_delete_yes_btn.setObjectName(u"single_select_delete_yes_btn")
        self.single_select_delete_yes_btn.setGeometry(QRect(820, 820, 71, 31))
        font7 = QFont()
        font7.setFamily(u"Segoe UI Semilight")
        font7.setPointSize(14)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setWeight(7)
        self.single_select_delete_yes_btn.setFont(font7)
        self.single_select_delete_yes_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.single_select_delete_yes_btn.setMouseTracking(True)
        self.single_select_delete_yes_btn.setFocusPolicy(Qt.ClickFocus)
        self.single_select_delete_yes_btn.setStyleSheet(u"QPushButton {\n"
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
        self.single_select_delete_no_btn = QPushButton(self.centralwidget)
        self.single_select_delete_no_btn.setObjectName(u"single_select_delete_no_btn")
        self.single_select_delete_no_btn.setGeometry(QRect(740, 820, 71, 31))
        self.single_select_delete_no_btn.setFont(font7)
        self.single_select_delete_no_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.single_select_delete_no_btn.setMouseTracking(True)
        self.single_select_delete_no_btn.setFocusPolicy(Qt.ClickFocus)
        self.single_select_delete_no_btn.setStyleSheet(u"QPushButton {\n"
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
        self.all_select_delete_no_btn = QPushButton(self.centralwidget)
        self.all_select_delete_no_btn.setObjectName(u"all_select_delete_no_btn")
        self.all_select_delete_no_btn.setGeometry(QRect(10, 820, 71, 31))
        self.all_select_delete_no_btn.setFont(font7)
        self.all_select_delete_no_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.all_select_delete_no_btn.setMouseTracking(True)
        self.all_select_delete_no_btn.setFocusPolicy(Qt.ClickFocus)
        self.all_select_delete_no_btn.setStyleSheet(u"QPushButton {\n"
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
        self.all_select_delete_yes_btn = QPushButton(self.centralwidget)
        self.all_select_delete_yes_btn.setObjectName(u"all_select_delete_yes_btn")
        self.all_select_delete_yes_btn.setGeometry(QRect(90, 820, 71, 31))
        self.all_select_delete_yes_btn.setFont(font7)
        self.all_select_delete_yes_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.all_select_delete_yes_btn.setMouseTracking(True)
        self.all_select_delete_yes_btn.setFocusPolicy(Qt.ClickFocus)
        self.all_select_delete_yes_btn.setStyleSheet(u"QPushButton {\n"
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
        self.all_select_delete_label = QLabel(self.centralwidget)
        self.all_select_delete_label.setObjectName(u"all_select_delete_label")
        self.all_select_delete_label.setGeometry(QRect(170, 820, 201, 31))
        self.all_select_delete_label.setStyleSheet(u"font: 63 12pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.event_place_combobox = QComboBox(self.centralwidget)
        self.event_place_combobox.addItem("")
        self.event_place_combobox.addItem("")
        self.event_place_combobox.addItem("")
        self.event_place_combobox.addItem("")
        self.event_place_combobox.setObjectName(u"event_place_combobox")
        self.event_place_combobox.setGeometry(QRect(30, 170, 181, 41))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.event_place_combobox.sizePolicy().hasHeightForWidth())
        self.event_place_combobox.setSizePolicy(sizePolicy1)
        self.event_place_combobox.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(whatsthis)
        self.event_place_combobox.setWhatsThis(u"<html><head/><body><p align=\"center\">\u05d1\u05d7\u05e8 \u05e1\u05d5\u05d2 \u05d0\u05d9\u05e8\u05d5\u05e2</p></body></html>")
#endif // QT_CONFIG(whatsthis)
        self.event_place_combobox.setLayoutDirection(Qt.RightToLeft)
        self.event_place_combobox.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border: 1px solid #090206;\n"
"background-color: rgb(255,255,255);")
        self.event_place_combobox.setEditable(True)
        self.event_place_combobox.setInsertPolicy(QComboBox.InsertAtBottom)
        self.event_place_combobox.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.event_place_combobox.setMinimumContentsLength(0)
        self.event_place_combobox.setDuplicatesEnabled(False)
        self.excel_warning_2 = QLabel(self.centralwidget)
        self.excel_warning_2.setObjectName(u"excel_warning_2")
        self.excel_warning_2.setGeometry(QRect(60, 140, 121, 21))
        self.excel_warning_2.setCursor(QCursor(Qt.BlankCursor))
        self.excel_warning_2.setStyleSheet(u"font: 14pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.excel_warning_2.setLineWidth(0)
        self.excel_warning_2.setScaledContents(False)
        self.excel_warning_2.setAlignment(Qt.AlignCenter)
        CustomersWindow.setCentralWidget(self.centralwidget)
        self.event_location_input.raise_()
        self.event_location_address_input.raise_()
        self.customers_tablewidget.raise_()
        self.event_date_input.raise_()
        self.contact2_name_input.raise_()
        self.customers_export_excel_btn.raise_()
        self.event_name_input.raise_()
        self.contact1_phone_input.raise_()
        self.rate_input.raise_()
        self.upper_frame.raise_()
        self.contact1_email_input.raise_()
        self.add_client_btn.raise_()
        self.contract_checkbox.raise_()
        self.contact2_email_input.raise_()
        self.contact1_address_input.raise_()
        self.contact2_address_input.raise_()
        self.clear_client_fields_btn.raise_()
        self.main_item_seperator_line.raise_()
        self.contact2_phone_input.raise_()
        self.edit_client_btn.raise_()
        self.contact1_name_input.raise_()
        self.update_client_btn.raise_()
        self.event_mendatory_label.raise_()
        self.contact_mendatory_label.raise_()
        self.delete_selection_warning.raise_()
        self.delete_all_warning.raise_()
        self.excel_warning.raise_()
        self.lead_check.raise_()
        self.editing_state_label.raise_()
        self.single_select_delete_label.raise_()
        self.single_select_delete_yes_btn.raise_()
        self.single_select_delete_no_btn.raise_()
        self.delete_selection_client_btn.raise_()
        self.all_select_delete_no_btn.raise_()
        self.all_select_delete_yes_btn.raise_()
        self.all_select_delete_label.raise_()
        self.delete_all_clients_btn.raise_()
        self.event_place_combobox.raise_()
        self.excel_warning_2.raise_()

        self.retranslateUi(CustomersWindow)

        QMetaObject.connectSlotsByName(CustomersWindow)
    # setupUi

    def retranslateUi(self, CustomersWindow):
        CustomersWindow.setWindowTitle(QCoreApplication.translate("CustomersWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.customers_tablewidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CustomersWindow", u"\u05d0\u05d9\u05e8\u05d5\u05e2", None));
        ___qtablewidgetitem1 = self.customers_tablewidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CustomersWindow", u"\u05de\u05d5\u05e2\u05d3", None));
        ___qtablewidgetitem2 = self.customers_tablewidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("CustomersWindow", u"\u05e9\u05dd", None));
        ___qtablewidgetitem3 = self.customers_tablewidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("CustomersWindow", u"\u05db\u05ea\u05d5\u05d1\u05ea", None));
        ___qtablewidgetitem4 = self.customers_tablewidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("CustomersWindow", u"\u05d8\u05dc\u05e4\u05d5\u05df", None));
        ___qtablewidgetitem5 = self.customers_tablewidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("CustomersWindow", u"\u05de\u05d9\u05d9\u05dc", None));
        ___qtablewidgetitem6 = self.customers_tablewidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("CustomersWindow", u"\u05d7\u05d5\u05d6\u05d4", None));
        ___qtablewidgetitem7 = self.customers_tablewidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("CustomersWindow", u"\u05ea\u05e2\u05e8\u05d9\u05e3", None));
        ___qtablewidgetitem8 = self.customers_tablewidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("CustomersWindow", u"\u05d0\u05d5\u05dc\u05dd", None));
        self.delete_all_clients_btn.setText(QCoreApplication.translate("CustomersWindow", u"\u05de\u05d7\u05e7 \u05d4\u05db\u05d5\u05dc", None))
        self.event_date_input.setHtml(QCoreApplication.translate("CustomersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.event_date_input.setPlaceholderText(QCoreApplication.translate("CustomersWindow", u"      \u05de\u05d5\u05e2\u05d3 \u05d4\u05d0\u05d9\u05e8\u05d5\u05e2", None))
#if QT_CONFIG(tooltip)
        self.contact2_name_input.setToolTip(QCoreApplication.translate("CustomersWindow", u"<html><head/><body><p>\u05d0\u05d9\u05e9 \u05e7\u05e9\u05e8 \u05e8\u05d0\u05e9\u05d9</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.contact2_name_input.setMarkdown("")
        self.contact2_name_input.setHtml(QCoreApplication.translate("CustomersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.contact2_name_input.setPlaceholderText(QCoreApplication.translate("CustomersWindow", u"  \u05e9\u05dd \u05d0\u05d9\u05e9 \u05e7\u05e9\u05e8 \u05e0\u05d5\u05e1\u05e3", None))
#if QT_CONFIG(tooltip)
        self.customers_export_excel_btn.setToolTip(QCoreApplication.translate("CustomersWindow", u"<html><head/><body><p align=\"center\">\u05d9\u05d9\u05e6\u05d5\u05d0 \u05d8\u05d1\u05dc\u05ea \u05dc\u05e7\u05d5\u05d7\u05d5\u05ea</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.customers_export_excel_btn.setWhatsThis(QCoreApplication.translate("CustomersWindow", u"<html><head/><body><p align=\"center\">\u05d9\u05d9\u05e6\u05d5\u05d0 \u05d8\u05d1\u05dc\u05ea \u05dc\u05e7\u05d5\u05d7\u05d5\u05ea</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.customers_export_excel_btn.setText("")
#if QT_CONFIG(tooltip)
        self.event_name_input.setToolTip(QCoreApplication.translate("CustomersWindow", u"<html><head/><body><p align=\"center\">\u05d4\u05db\u05e0\u05e1 \u05e9\u05dd \u05d0\u05d9\u05e8\u05d5\u05e2 (\u05e9\u05d3\u05d4 \u05d7\u05d5\u05d1\u05d4)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.event_name_input.setWhatsThis(QCoreApplication.translate("CustomersWindow", u"<html><head/><body><p align=\"center\">\u05d4\u05db\u05e0\u05e1 \u05e9\u05dd \u05d0\u05d9\u05e8\u05d5\u05e2 (\u05e9\u05d3\u05d4 \u05d7\u05d5\u05d1\u05d4)</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.event_name_input.setHtml(QCoreApplication.translate("CustomersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.event_name_input.setPlaceholderText(QCoreApplication.translate("CustomersWindow", u"  \u05e9\u05dd \u05d4\u05d0\u05d9\u05e8\u05d5\u05e2 (\u05e9\u05d3\u05d4 \u05d7\u05d5\u05d1\u05d4)", None))
        self.contact1_phone_input.setHtml(QCoreApplication.translate("CustomersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.contact1_phone_input.setPlaceholderText(QCoreApplication.translate("CustomersWindow", u"        \u05d8\u05dc\u05e4\u05d5\u05df", None))
        self.rate_input.setHtml(QCoreApplication.translate("CustomersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.rate_input.setPlaceholderText(QCoreApplication.translate("CustomersWindow", u"     \u05ea\u05e2\u05e8\u05d9\u05e3", None))
        self.upper_frame_header_btn.setText(QCoreApplication.translate("CustomersWindow", u"\u05e0\u05d9\u05d4\u05d5\u05dc \u05dc\u05e7\u05d5\u05d7\u05d5\u05ea", None))
        self.label.setText("")
        self.contact1_email_input.setHtml(QCoreApplication.translate("CustomersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.contact1_email_input.setPlaceholderText(QCoreApplication.translate("CustomersWindow", u"                        \u05d0\u05d9\u05de\u05d9\u05d9\u05dc", None))
        self.add_client_btn.setText(QCoreApplication.translate("CustomersWindow", u"\u05d4\u05d5\u05e1\u05e3 \u05dc\u05e7\u05d5\u05d7 ", None))
#if QT_CONFIG(tooltip)
        self.contract_checkbox.setToolTip(QCoreApplication.translate("CustomersWindow", u"<html><head/><body><p align=\"center\">\u05e1\u05de\u05df \u05d0\u05dd \u05e0\u05d7\u05ea\u05dd \u05d7\u05d5\u05d6\u05d4</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.contract_checkbox.setWhatsThis(QCoreApplication.translate("CustomersWindow", u"<html><head/><body><p align=\"center\">\u05e1\u05de\u05df \u05d0\u05dd \u05e0\u05d7\u05ea\u05dd \u05d7\u05d5\u05d6\u05d4</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.contract_checkbox.setText(QCoreApplication.translate("CustomersWindow", u"\u05e0\u05d7\u05ea\u05dd \u05d7\u05d5\u05d6\u05d4", None))
        self.contact2_email_input.setHtml(QCoreApplication.translate("CustomersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.contact2_email_input.setPlaceholderText(QCoreApplication.translate("CustomersWindow", u"                        \u05d0\u05d9\u05de\u05d9\u05d9\u05dc", None))
        self.contact1_address_input.setHtml(QCoreApplication.translate("CustomersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.delete_selection_client_btn.setText(QCoreApplication.translate("CustomersWindow", u"\u05de\u05d7\u05e7 \u05d1\u05d7\u05d9\u05e8\u05d4", None))
        self.contact2_address_input.setHtml(QCoreApplication.translate("CustomersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.clear_client_fields_btn.setText(QCoreApplication.translate("CustomersWindow", u"\u05e0\u05e7\u05d4 \u05d4\u05db\u05d5\u05dc", None))
        self.contact2_phone_input.setHtml(QCoreApplication.translate("CustomersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.contact2_phone_input.setPlaceholderText(QCoreApplication.translate("CustomersWindow", u"        \u05d8\u05dc\u05e4\u05d5\u05df", None))
        self.edit_client_btn.setText(QCoreApplication.translate("CustomersWindow", u"\u05e2\u05e8\u05d5\u05da \u05e4\u05e8\u05d8\u05d9 \u05dc\u05e7\u05d5\u05d7 ", None))
#if QT_CONFIG(tooltip)
        self.contact1_name_input.setToolTip(QCoreApplication.translate("CustomersWindow", u"<html><head/><body><p align=\"center\">\u05d4\u05db\u05e0\u05e1 \u05d0\u05d9\u05e9 \u05e7\u05e9\u05e8 \u05e8\u05d0\u05e9\u05d9 (\u05e9\u05d3\u05d4 \u05d7\u05d5\u05d1\u05d4)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.contact1_name_input.setWhatsThis(QCoreApplication.translate("CustomersWindow", u"<html><head/><body><p align=\"center\">\u05d4\u05db\u05e0\u05e1 \u05d0\u05d9\u05e9 \u05e7\u05e9\u05e8 \u05e8\u05d0\u05e9\u05d9 (\u05e9\u05d3\u05d4 \u05d7\u05d5\u05d1\u05d4)</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.contact1_name_input.setMarkdown("")
        self.contact1_name_input.setHtml(QCoreApplication.translate("CustomersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.contact1_name_input.setPlaceholderText(QCoreApplication.translate("CustomersWindow", u" \u05e9\u05dd \u05d0\u05d9\u05e9 \u05e7\u05e9\u05e8 (\u05d7\u05d5\u05d1\u05d4)", None))
        self.event_location_input.setHtml(QCoreApplication.translate("CustomersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.event_location_input.setPlaceholderText(QCoreApplication.translate("CustomersWindow", u"                  \u05e9\u05dd \u05d4\u05d0\u05d5\u05dc\u05dd", None))
        self.event_location_address_input.setHtml(QCoreApplication.translate("CustomersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.event_location_address_input.setPlaceholderText(QCoreApplication.translate("CustomersWindow", u"                                    \u05db\u05ea\u05d5\u05d1\u05ea \u05d4\u05d0\u05d5\u05dc\u05dd", None))
        self.update_client_btn.setText(QCoreApplication.translate("CustomersWindow", u"\u05e2\u05d3\u05db\u05df \u05dc\u05e7\u05d5\u05d7", None))
        self.event_mendatory_label.setText(QCoreApplication.translate("CustomersWindow", u"\u05d7\u05d5\u05d1\u05d4*", None))
        self.contact_mendatory_label.setText(QCoreApplication.translate("CustomersWindow", u"\u05d7\u05d5\u05d1\u05d4*", None))
        self.delete_selection_warning.setText(QCoreApplication.translate("CustomersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semibold'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; color:#ef4040;\">!\u05dc\u05d0\u05d7\u05e8 \u05e4\u05e2\u05d5\u05dc\u05d4 \u05d6\u05d5 \u05dc\u05d0 \u05e0\u05d9\u05ea\u05df \u05dc\u05e9\u05d7\u05d6\u05e8 \u05d0\u05ea \u05d4\u05de\u05d9\u05d3\u05e2</span></p></body></html>", None))
        self.delete_all_warning.setText(QCoreApplication.translate("CustomersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semibold'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; color:#ef4040;\">!\u05dc\u05d0\u05d7\u05e8 \u05e4\u05e2\u05d5\u05dc\u05d4 \u05d6\u05d5 \u05dc\u05d0 \u05e0\u05d9\u05ea\u05df \u05dc\u05e9\u05d7\u05d6\u05e8 \u05d0\u05ea \u05d4\u05de\u05d9\u05d3\u05e2</span></p></body></html>", None))
        self.excel_warning.setText(QCoreApplication.translate("CustomersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semibold'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; color:#ef4040;\">\u05d4\u05e7\u05d5\u05d1\u05e5 \u05d1\u05e9\u05d9\u05de\u05d5\u05e9 - \u05dc\u05d0 \u05e0\u05d9\u05ea\u05df \u05dc\u05e9\u05de\u05d5\u05e8</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lead_check.setToolTip(QCoreApplication.translate("CustomersWindow", u"<html><head/><body><p align=\"center\">\u05dc\u05e1\u05de\u05df \u05d0\u05dd \u05de\u05d3\u05d5\u05d1\u05e8 \u05d1\u05dc\u05d9\u05d3</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lead_check.setWhatsThis(QCoreApplication.translate("CustomersWindow", u"<html><head/><body><p align=\"center\">\u05dc\u05e1\u05de\u05df \u05d0\u05dd \u05de\u05d3\u05d5\u05d1\u05e8 \u05d1\u05dc\u05d9\u05d3</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lead_check.setText(QCoreApplication.translate("CustomersWindow", u"\u05dc\u05d9\u05d3", None))
        self.editing_state_label.setText(QCoreApplication.translate("CustomersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semibold'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u05de\u05e6\u05d1 \u05d4\u05d5\u05e1\u05e4\u05ea \u05d0\u05d9\u05e8\u05d5\u05e2</p></body></html>", None))
        self.single_select_delete_label.setText(QCoreApplication.translate("CustomersWindow", u"\u05d4\u05d0\u05dd \u05dc\u05de\u05d7\u05d5\u05e7 \u05dc\u05e6\u05de\u05d9\u05ea\u05d5\u05ea?", None))
        self.single_select_delete_yes_btn.setText(QCoreApplication.translate("CustomersWindow", u"\u05db\u05df", None))
        self.single_select_delete_no_btn.setText(QCoreApplication.translate("CustomersWindow", u"\u05dc\u05d0", None))
        self.all_select_delete_no_btn.setText(QCoreApplication.translate("CustomersWindow", u"\u05dc\u05d0", None))
        self.all_select_delete_yes_btn.setText(QCoreApplication.translate("CustomersWindow", u"\u05db\u05df", None))
        self.all_select_delete_label.setText(QCoreApplication.translate("CustomersWindow", u"\u05d4\u05d0\u05dd \u05dc\u05de\u05d7\u05d5\u05e7 \u05dc\u05e6\u05de\u05d9\u05ea\u05d5\u05ea?", None))
        self.event_place_combobox.setItemText(0, QCoreApplication.translate("CustomersWindow", u"\u05d0\u05d9\u05e8\u05d5\u05e2 \u05d1\u05d0\u05d5\u05dc\u05dd", None))
        self.event_place_combobox.setItemText(1, QCoreApplication.translate("CustomersWindow", u"\u05d0\u05d9\u05e8\u05d5\u05e2 \u05d1\u05d2\u05df", None))
        self.event_place_combobox.setItemText(2, QCoreApplication.translate("CustomersWindow", u"\u05d0\u05d9\u05e8\u05d5\u05e2 \u05d1\u05d8\u05d1\u05e2", None))
        self.event_place_combobox.setItemText(3, QCoreApplication.translate("CustomersWindow", u"\u05d0\u05d9\u05e8\u05d5\u05e2 \u05d1 {\u05d7\u05d5\u05e4\u05e9\u05d9}", None))

#if QT_CONFIG(tooltip)
        self.event_place_combobox.setToolTip(QCoreApplication.translate("CustomersWindow", u"<html><head/><body><p align=\"center\">\u05d1\u05d7\u05e8 \u05e1\u05d5\u05d2 \u05d0\u05d9\u05e8\u05d5\u05e2</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.event_place_combobox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.event_place_combobox.setCurrentText(QCoreApplication.translate("CustomersWindow", u"\u05d0\u05d9\u05e8\u05d5\u05e2 \u05d1\u05d0\u05d5\u05dc\u05dd", None))
        self.event_place_combobox.setPlaceholderText(QCoreApplication.translate("CustomersWindow", u"\u05e1\u05d5\u05d2 \u05d4\u05d0\u05d9\u05e8\u05d5\u05e2", None))
        self.excel_warning_2.setText(QCoreApplication.translate("CustomersWindow", u"\u05e1\u05d5\u05d2 \u05d0\u05d9\u05e8\u05d5\u05e2", None))
    # retranslateUi

