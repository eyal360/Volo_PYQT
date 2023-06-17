# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'suppliers_windowUztZuV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import client_window_icon_rc

class Ui_SuppliersWindow(object):
    def setupUi(self, SuppliersWindow):
        if not SuppliersWindow.objectName():
            SuppliersWindow.setObjectName(u"SuppliersWindow")
        SuppliersWindow.resize(1107, 866)
        SuppliersWindow.setStyleSheet(u"background-color: rgb(255,211,182);")
        self.centralwidget = QWidget(SuppliersWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.upper_frame = QFrame(self.centralwidget)
        self.upper_frame.setObjectName(u"upper_frame")
        self.upper_frame.setGeometry(QRect(10, 10, 1091, 101))
        font = QFont()
        font.setPointSize(15)
        self.upper_frame.setFont(font)
        self.upper_frame.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"border-radius: 40px;")
        self.upper_frame.setFrameShape(QFrame.StyledPanel)
        self.upper_frame.setFrameShadow(QFrame.Raised)
        self.upper_frame_header_btn = QPushButton(self.upper_frame)
        self.upper_frame_header_btn.setObjectName(u"upper_frame_header_btn")
        self.upper_frame_header_btn.setGeometry(QRect(270, 11, 536, 79))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(42)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(7)
        self.upper_frame_header_btn.setFont(font1)
        self.upper_frame_header_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.upper_frame_header_btn.setMouseTracking(True)
        self.upper_frame_header_btn.setFocusPolicy(Qt.ClickFocus)
        self.upper_frame_header_btn.setAutoFillBackground(False)
        self.upper_frame_header_btn.setStyleSheet(u"QPushButton {\n"
"\n"
"	color: rgb(255,170,165);\n"
"	font: 63 42pt \"Segoe UI Semibold\";\n"
"	border-radius: 30px;\n"
"}\n"
"")
        self.label = QLabel(self.upper_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(730, -10, 131, 131))
        self.label.setStyleSheet(u"image: url(:/icons/logo/Pheonix.ico);")
        self.company_name_input = QTextEdit(self.centralwidget)
        self.company_name_input.setObjectName(u"company_name_input")
        self.company_name_input.setGeometry(QRect(610, 140, 441, 41))
        self.company_name_input.setLayoutDirection(Qt.RightToLeft)
        self.company_name_input.setStyleSheet(u"font: 11pt \"Segoe UI Semilight\";\n"
"border: 3px solid #6248F0;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.company_name_input.setFrameShape(QFrame.StyledPanel)
        self.company_name_input.setFrameShadow(QFrame.Plain)
        self.company_name_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.company_name_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.company_name_input.setTabChangesFocus(True)
        self.company_name_input.setOverwriteMode(False)
        self.edit_supplier_btn = QPushButton(self.centralwidget)
        self.edit_supplier_btn.setObjectName(u"edit_supplier_btn")
        self.edit_supplier_btn.setGeometry(QRect(410, 340, 261, 51))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semilight")
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(7)
        self.edit_supplier_btn.setFont(font2)
        self.edit_supplier_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.edit_supplier_btn.setMouseTracking(True)
        self.edit_supplier_btn.setFocusPolicy(Qt.ClickFocus)
        self.edit_supplier_btn.setStyleSheet(u"QPushButton {\n"
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
        self.main_item_seperator_line = QFrame(self.centralwidget)
        self.main_item_seperator_line.setObjectName(u"main_item_seperator_line")
        self.main_item_seperator_line.setGeometry(QRect(40, 190, 1021, 20))
        self.main_item_seperator_line.setFrameShape(QFrame.HLine)
        self.main_item_seperator_line.setFrameShadow(QFrame.Sunken)
        self.delete_all_suppliers_btn = QPushButton(self.centralwidget)
        self.delete_all_suppliers_btn.setObjectName(u"delete_all_suppliers_btn")
        self.delete_all_suppliers_btn.setGeometry(QRect(50, 800, 261, 51))
        self.delete_all_suppliers_btn.setFont(font2)
        self.delete_all_suppliers_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.delete_all_suppliers_btn.setMouseTracking(True)
        self.delete_all_suppliers_btn.setFocusPolicy(Qt.ClickFocus)
        self.delete_all_suppliers_btn.setStyleSheet(u"QPushButton {\n"
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
        self.arrangment_checkbox = QCheckBox(self.centralwidget)
        self.arrangment_checkbox.setObjectName(u"arrangment_checkbox")
        self.arrangment_checkbox.setGeometry(QRect(40, 140, 91, 41))
        self.arrangment_checkbox.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.company_address_input = QTextEdit(self.centralwidget)
        self.company_address_input.setObjectName(u"company_address_input")
        self.company_address_input.setGeometry(QRect(150, 140, 451, 41))
        self.company_address_input.setLayoutDirection(Qt.RightToLeft)
        self.company_address_input.setStyleSheet(u"font: 11pt \"Segoe UI Semilight\";\n"
"border: 1px solid #090206;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.company_address_input.setFrameShape(QFrame.StyledPanel)
        self.company_address_input.setFrameShadow(QFrame.Plain)
        self.company_address_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.company_address_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.company_address_input.setTabChangesFocus(True)
        self.company_address_input.setOverwriteMode(False)
        self.suppliers_tablewidget = QTableWidget(self.centralwidget)
        if (self.suppliers_tablewidget.columnCount() < 6):
            self.suppliers_tablewidget.setColumnCount(6)
        font3 = QFont()
        font3.setFamily(u"Segoe UI Semibold")
        font3.setPointSize(12)
        font3.setStyleStrategy(QFont.PreferDefault)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font3);
        __qtablewidgetitem.setBackground(QColor(0, 0, 0));
        self.suppliers_tablewidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font4 = QFont()
        font4.setFamily(u"Segoe UI Semibold")
        font4.setPointSize(12)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font4);
        self.suppliers_tablewidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font4);
        self.suppliers_tablewidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font4);
        self.suppliers_tablewidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font4);
        self.suppliers_tablewidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFont(font4);
        self.suppliers_tablewidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.suppliers_tablewidget.setObjectName(u"suppliers_tablewidget")
        self.suppliers_tablewidget.setGeometry(QRect(30, 410, 1051, 351))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.suppliers_tablewidget.sizePolicy().hasHeightForWidth())
        self.suppliers_tablewidget.setSizePolicy(sizePolicy)
        self.suppliers_tablewidget.setMaximumSize(QSize(1060, 16777215))
        self.suppliers_tablewidget.setBaseSize(QSize(50, 0))
        self.suppliers_tablewidget.setLayoutDirection(Qt.RightToLeft)
        self.suppliers_tablewidget.setStyleSheet(u"/* VERTICAL SCROLLBAR */\n"
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
        self.suppliers_tablewidget.setFrameShape(QFrame.NoFrame)
        self.suppliers_tablewidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.suppliers_tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.suppliers_tablewidget.setProperty("showDropIndicator", False)
        self.suppliers_tablewidget.setDragDropOverwriteMode(False)
        self.suppliers_tablewidget.setAlternatingRowColors(True)
        self.suppliers_tablewidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.suppliers_tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.suppliers_tablewidget.setTextElideMode(Qt.ElideMiddle)
        self.suppliers_tablewidget.setGridStyle(Qt.DashLine)
        self.clear_supplier_fields_btn = QPushButton(self.centralwidget)
        self.clear_supplier_fields_btn.setObjectName(u"clear_supplier_fields_btn")
        self.clear_supplier_fields_btn.setGeometry(QRect(50, 340, 261, 51))
        self.clear_supplier_fields_btn.setFont(font2)
        self.clear_supplier_fields_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.clear_supplier_fields_btn.setMouseTracking(True)
        self.clear_supplier_fields_btn.setFocusPolicy(Qt.ClickFocus)
        self.clear_supplier_fields_btn.setStyleSheet(u"QPushButton {\n"
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
        self.suppliers_export_excel_btn = QPushButton(self.centralwidget)
        self.suppliers_export_excel_btn.setObjectName(u"suppliers_export_excel_btn")
        self.suppliers_export_excel_btn.setGeometry(QRect(530, 790, 91, 71))
        self.suppliers_export_excel_btn.setFont(font2)
        self.suppliers_export_excel_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.suppliers_export_excel_btn.setMouseTracking(True)
        self.suppliers_export_excel_btn.setFocusPolicy(Qt.ClickFocus)
        self.suppliers_export_excel_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255,211,182);	\n"
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
        self.details_input = QTextEdit(self.centralwidget)
        self.details_input.setObjectName(u"details_input")
        self.details_input.setGeometry(QRect(40, 210, 371, 121))
        self.details_input.setLayoutDirection(Qt.RightToLeft)
        self.details_input.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border: 1px solid #090206;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.details_input.setFrameShape(QFrame.StyledPanel)
        self.details_input.setFrameShadow(QFrame.Plain)
        self.details_input.setTabChangesFocus(True)
        self.details_input.setLineWrapMode(QTextEdit.WidgetWidth)
        self.details_input.setOverwriteMode(False)
        self.delete_selection_supplier_btn = QPushButton(self.centralwidget)
        self.delete_selection_supplier_btn.setObjectName(u"delete_selection_supplier_btn")
        self.delete_selection_supplier_btn.setGeometry(QRect(800, 800, 261, 51))
        self.delete_selection_supplier_btn.setFont(font2)
        self.delete_selection_supplier_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.delete_selection_supplier_btn.setMouseTracking(True)
        self.delete_selection_supplier_btn.setFocusPolicy(Qt.ClickFocus)
        self.delete_selection_supplier_btn.setStyleSheet(u"QPushButton {\n"
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
        self.add_supplier_btn = QPushButton(self.centralwidget)
        self.add_supplier_btn.setObjectName(u"add_supplier_btn")
        self.add_supplier_btn.setGeometry(QRect(760, 340, 261, 51))
        self.add_supplier_btn.setFont(font2)
        self.add_supplier_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.add_supplier_btn.setMouseTracking(True)
        self.add_supplier_btn.setFocusPolicy(Qt.ClickFocus)
        self.add_supplier_btn.setStyleSheet(u"QPushButton {\n"
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
        self.contact1_name_input = QTextEdit(self.centralwidget)
        self.contact1_name_input.setObjectName(u"contact1_name_input")
        self.contact1_name_input.setGeometry(QRect(860, 220, 191, 41))
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
        self.contact2_phone_input = QTextEdit(self.centralwidget)
        self.contact2_phone_input.setObjectName(u"contact2_phone_input")
        self.contact2_phone_input.setGeometry(QRect(710, 270, 141, 41))
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
        self.contact1_email_input = QTextEdit(self.centralwidget)
        self.contact1_email_input.setObjectName(u"contact1_email_input")
        self.contact1_email_input.setGeometry(QRect(420, 220, 281, 41))
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
        self.contact2_email_input = QTextEdit(self.centralwidget)
        self.contact2_email_input.setObjectName(u"contact2_email_input")
        self.contact2_email_input.setGeometry(QRect(420, 270, 281, 41))
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
        self.contact2_name_input = QTextEdit(self.centralwidget)
        self.contact2_name_input.setObjectName(u"contact2_name_input")
        self.contact2_name_input.setGeometry(QRect(860, 270, 191, 41))
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
        self.contact1_phone_input = QTextEdit(self.centralwidget)
        self.contact1_phone_input.setObjectName(u"contact1_phone_input")
        self.contact1_phone_input.setGeometry(QRect(710, 220, 141, 41))
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
        self.update_supplier_btn = QPushButton(self.centralwidget)
        self.update_supplier_btn.setObjectName(u"update_supplier_btn")
        self.update_supplier_btn.setGeometry(QRect(390, 340, 311, 51))
        font5 = QFont()
        font5.setFamily(u"Segoe UI Semibold")
        font5.setPointSize(20)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(7)
        self.update_supplier_btn.setFont(font5)
        self.update_supplier_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.update_supplier_btn.setMouseTracking(True)
        self.update_supplier_btn.setFocusPolicy(Qt.ClickFocus)
        self.update_supplier_btn.setStyleSheet(u"QPushButton {\n"
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
        self.contact_mendatory_label = QLabel(self.centralwidget)
        self.contact_mendatory_label.setObjectName(u"contact_mendatory_label")
        self.contact_mendatory_label.setGeometry(QRect(1050, 220, 51, 31))
        self.contact_mendatory_label.setStyleSheet(u"font: 11pt \"Segoe UI Semibold\";\n"
"color: rgb(239, 64, 64);")
        self.company_mendatory_label = QLabel(self.centralwidget)
        self.company_mendatory_label.setObjectName(u"company_mendatory_label")
        self.company_mendatory_label.setGeometry(QRect(1050, 140, 51, 31))
        self.company_mendatory_label.setStyleSheet(u"font: 11pt \"Segoe UI Semibold\";\n"
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
        self.delete_all_warning.setGeometry(QRect(10, 770, 341, 31))
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
        self.excel_warning.setGeometry(QRect(450, 760, 261, 31))
        self.excel_warning.setCursor(QCursor(Qt.BlankCursor))
        self.excel_warning.setStyleSheet(u"font: 16pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.excel_warning.setLineWidth(0)
        self.excel_warning.setScaledContents(False)
        self.excel_warning.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.single_select_delete_yes_btn = QPushButton(self.centralwidget)
        self.single_select_delete_yes_btn.setObjectName(u"single_select_delete_yes_btn")
        self.single_select_delete_yes_btn.setGeometry(QRect(820, 820, 71, 31))
        font6 = QFont()
        font6.setFamily(u"Segoe UI Semilight")
        font6.setPointSize(14)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(7)
        self.single_select_delete_yes_btn.setFont(font6)
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
        self.single_select_delete_label = QLabel(self.centralwidget)
        self.single_select_delete_label.setObjectName(u"single_select_delete_label")
        self.single_select_delete_label.setGeometry(QRect(900, 820, 201, 31))
        self.single_select_delete_label.setStyleSheet(u"font: 63 12pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.single_select_delete_no_btn = QPushButton(self.centralwidget)
        self.single_select_delete_no_btn.setObjectName(u"single_select_delete_no_btn")
        self.single_select_delete_no_btn.setGeometry(QRect(740, 820, 71, 31))
        self.single_select_delete_no_btn.setFont(font6)
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
        self.all_select_delete_label = QLabel(self.centralwidget)
        self.all_select_delete_label.setObjectName(u"all_select_delete_label")
        self.all_select_delete_label.setGeometry(QRect(170, 820, 201, 31))
        self.all_select_delete_label.setStyleSheet(u"font: 63 12pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.all_select_delete_yes_btn = QPushButton(self.centralwidget)
        self.all_select_delete_yes_btn.setObjectName(u"all_select_delete_yes_btn")
        self.all_select_delete_yes_btn.setGeometry(QRect(90, 820, 71, 31))
        self.all_select_delete_yes_btn.setFont(font6)
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
        self.all_select_delete_no_btn = QPushButton(self.centralwidget)
        self.all_select_delete_no_btn.setObjectName(u"all_select_delete_no_btn")
        self.all_select_delete_no_btn.setGeometry(QRect(10, 820, 71, 31))
        self.all_select_delete_no_btn.setFont(font6)
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
        SuppliersWindow.setCentralWidget(self.centralwidget)
        self.upper_frame.raise_()
        self.company_name_input.raise_()
        self.edit_supplier_btn.raise_()
        self.main_item_seperator_line.raise_()
        self.arrangment_checkbox.raise_()
        self.company_address_input.raise_()
        self.suppliers_tablewidget.raise_()
        self.clear_supplier_fields_btn.raise_()
        self.suppliers_export_excel_btn.raise_()
        self.details_input.raise_()
        self.add_supplier_btn.raise_()
        self.contact1_name_input.raise_()
        self.contact2_phone_input.raise_()
        self.contact1_email_input.raise_()
        self.contact2_email_input.raise_()
        self.contact2_name_input.raise_()
        self.contact1_phone_input.raise_()
        self.update_supplier_btn.raise_()
        self.contact_mendatory_label.raise_()
        self.company_mendatory_label.raise_()
        self.delete_selection_warning.raise_()
        self.delete_all_warning.raise_()
        self.excel_warning.raise_()
        self.single_select_delete_yes_btn.raise_()
        self.single_select_delete_label.raise_()
        self.single_select_delete_no_btn.raise_()
        self.delete_selection_supplier_btn.raise_()
        self.all_select_delete_label.raise_()
        self.all_select_delete_yes_btn.raise_()
        self.all_select_delete_no_btn.raise_()
        self.delete_all_suppliers_btn.raise_()

        self.retranslateUi(SuppliersWindow)

        QMetaObject.connectSlotsByName(SuppliersWindow)
    # setupUi

    def retranslateUi(self, SuppliersWindow):
        SuppliersWindow.setWindowTitle(QCoreApplication.translate("SuppliersWindow", u"MainWindow", None))
        self.upper_frame_header_btn.setText(QCoreApplication.translate("SuppliersWindow", u"\u05e0\u05d9\u05d4\u05d5\u05dc \u05e1\u05e4\u05e7\u05d9\u05dd", None))
        self.label.setText("")
        self.company_name_input.setHtml(QCoreApplication.translate("SuppliersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.company_name_input.setPlaceholderText(QCoreApplication.translate("SuppliersWindow", u"                       \u05e9\u05dd \u05d4\u05d7\u05d1\u05e8\u05d4 (\u05e9\u05d3\u05d4 \u05d7\u05d5\u05d1\u05d4)", None))
        self.edit_supplier_btn.setText(QCoreApplication.translate("SuppliersWindow", u"\u05e2\u05e8\u05d5\u05da \u05e4\u05e8\u05d8\u05d9 \u05e1\u05e4\u05e7 ", None))
        self.delete_all_suppliers_btn.setText(QCoreApplication.translate("SuppliersWindow", u"\u05de\u05d7\u05e7 \u05d4\u05db\u05d5\u05dc", None))
        self.arrangment_checkbox.setText(QCoreApplication.translate("SuppliersWindow", u"\u05d4\u05e1\u05d3\u05e8", None))
        self.company_address_input.setHtml(QCoreApplication.translate("SuppliersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.company_address_input.setPlaceholderText(QCoreApplication.translate("SuppliersWindow", u"                                 \u05db\u05ea\u05d5\u05d1\u05ea \u05d4\u05d7\u05d1\u05e8\u05d4", None))
        ___qtablewidgetitem = self.suppliers_tablewidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SuppliersWindow", u"\u05d7\u05d1\u05e8\u05d4", None));
        ___qtablewidgetitem1 = self.suppliers_tablewidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SuppliersWindow", u"\u05e9\u05dd \u05e1\u05e4\u05e7", None));
        ___qtablewidgetitem2 = self.suppliers_tablewidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SuppliersWindow", u"\u05d8\u05dc\u05e4\u05d5\u05df", None));
        ___qtablewidgetitem3 = self.suppliers_tablewidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SuppliersWindow", u"\u05d0\u05d9\u05de\u05d9\u05d9\u05dc", None));
        ___qtablewidgetitem4 = self.suppliers_tablewidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("SuppliersWindow", u"\u05d4\u05e1\u05d3\u05e8", None));
        ___qtablewidgetitem5 = self.suppliers_tablewidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("SuppliersWindow", u"\u05e4\u05e8\u05d8\u05d9\u05dd \u05e0\u05d5\u05e1\u05e4\u05d9\u05dd", None));
        self.clear_supplier_fields_btn.setText(QCoreApplication.translate("SuppliersWindow", u"\u05e0\u05e7\u05d4 \u05d4\u05db\u05d5\u05dc", None))
#if QT_CONFIG(tooltip)
        self.suppliers_export_excel_btn.setToolTip(QCoreApplication.translate("SuppliersWindow", u"<html><head/><body><p align=\"center\">\u05d9\u05d9\u05e6\u05d5\u05d0 \u05d8\u05d1\u05dc\u05ea \u05e1\u05e4\u05e7\u05d9\u05dd</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.suppliers_export_excel_btn.setWhatsThis(QCoreApplication.translate("SuppliersWindow", u"<html><head/><body><p align=\"center\">\u05d9\u05d9\u05e6\u05d5\u05d0 \u05d8\u05d1\u05dc\u05ea \u05e1\u05e4\u05e7\u05d9\u05dd</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.suppliers_export_excel_btn.setText("")
        self.details_input.setHtml(QCoreApplication.translate("SuppliersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.details_input.setPlaceholderText(QCoreApplication.translate("SuppliersWindow", u"                        \u05e4\u05e8\u05d8\u05d9\u05dd \u05e0\u05d5\u05e1\u05e4\u05d9\u05dd", None))
        self.delete_selection_supplier_btn.setText(QCoreApplication.translate("SuppliersWindow", u"\u05de\u05d7\u05e7 \u05d1\u05d7\u05d9\u05e8\u05d4", None))
        self.add_supplier_btn.setText(QCoreApplication.translate("SuppliersWindow", u"\u05d4\u05d5\u05e1\u05e3 \u05e1\u05e4\u05e7 ", None))
#if QT_CONFIG(tooltip)
        self.contact1_name_input.setToolTip(QCoreApplication.translate("SuppliersWindow", u"<html><head/><body><p align=\"center\">\u05d4\u05db\u05e0\u05e1 \u05d0\u05d9\u05e9 \u05e7\u05e9\u05e8 \u05e8\u05d0\u05e9\u05d9 (\u05e9\u05d3\u05d4 \u05d7\u05d5\u05d1\u05d4)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.contact1_name_input.setWhatsThis(QCoreApplication.translate("SuppliersWindow", u"<html><head/><body><p align=\"center\">\u05d4\u05db\u05e0\u05e1 \u05d0\u05d9\u05e9 \u05e7\u05e9\u05e8 \u05e8\u05d0\u05e9\u05d9 (\u05e9\u05d3\u05d4 \u05d7\u05d5\u05d1\u05d4)</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.contact1_name_input.setMarkdown("")
        self.contact1_name_input.setHtml(QCoreApplication.translate("SuppliersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.contact1_name_input.setPlaceholderText(QCoreApplication.translate("SuppliersWindow", u" \u05e9\u05dd \u05d0\u05d9\u05e9 \u05e7\u05e9\u05e8 (\u05d7\u05d5\u05d1\u05d4)", None))
        self.contact2_phone_input.setHtml(QCoreApplication.translate("SuppliersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.contact2_phone_input.setPlaceholderText(QCoreApplication.translate("SuppliersWindow", u"        \u05d8\u05dc\u05e4\u05d5\u05df", None))
        self.contact1_email_input.setHtml(QCoreApplication.translate("SuppliersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.contact1_email_input.setPlaceholderText(QCoreApplication.translate("SuppliersWindow", u"                      \u05d0\u05d9\u05de\u05d9\u05d9\u05dc", None))
        self.contact2_email_input.setHtml(QCoreApplication.translate("SuppliersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.contact2_email_input.setPlaceholderText(QCoreApplication.translate("SuppliersWindow", u"                      \u05d0\u05d9\u05de\u05d9\u05d9\u05dc", None))
#if QT_CONFIG(tooltip)
        self.contact2_name_input.setToolTip(QCoreApplication.translate("SuppliersWindow", u"<html><head/><body><p>\u05d0\u05d9\u05e9 \u05e7\u05e9\u05e8 \u05e8\u05d0\u05e9\u05d9</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.contact2_name_input.setMarkdown("")
        self.contact2_name_input.setHtml(QCoreApplication.translate("SuppliersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.contact2_name_input.setPlaceholderText(QCoreApplication.translate("SuppliersWindow", u"  \u05e9\u05dd \u05d0\u05d9\u05e9 \u05e7\u05e9\u05e8 \u05e0\u05d5\u05e1\u05e3", None))
        self.contact1_phone_input.setHtml(QCoreApplication.translate("SuppliersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semilight'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.contact1_phone_input.setPlaceholderText(QCoreApplication.translate("SuppliersWindow", u"        \u05d8\u05dc\u05e4\u05d5\u05df", None))
        self.update_supplier_btn.setText(QCoreApplication.translate("SuppliersWindow", u"\u05e2\u05d3\u05db\u05df \u05e1\u05e4\u05e7", None))
        self.contact_mendatory_label.setText(QCoreApplication.translate("SuppliersWindow", u"\u05d7\u05d5\u05d1\u05d4*", None))
        self.company_mendatory_label.setText(QCoreApplication.translate("SuppliersWindow", u"\u05d7\u05d5\u05d1\u05d4*", None))
        self.delete_selection_warning.setText(QCoreApplication.translate("SuppliersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semibold'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; color:#ef4040;\">!\u05dc\u05d0\u05d7\u05e8 \u05e4\u05e2\u05d5\u05dc\u05d4 \u05d6\u05d5 \u05dc\u05d0 \u05e0\u05d9\u05ea\u05df \u05dc\u05e9\u05d7\u05d6\u05e8 \u05d0\u05ea \u05d4\u05de\u05d9\u05d3\u05e2</span></p></body></html>", None))
        self.delete_all_warning.setText(QCoreApplication.translate("SuppliersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semibold'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; color:#ef4040;\">!\u05dc\u05d0\u05d7\u05e8 \u05e4\u05e2\u05d5\u05dc\u05d4 \u05d6\u05d5 \u05dc\u05d0 \u05e0\u05d9\u05ea\u05df \u05dc\u05e9\u05d7\u05d6\u05e8 \u05d0\u05ea \u05d4\u05de\u05d9\u05d3\u05e2</span></p></body></html>", None))
        self.excel_warning.setText(QCoreApplication.translate("SuppliersWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semibold'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; color:#ef4040;\">\u05d4\u05e7\u05d5\u05d1\u05e5 \u05d1\u05e9\u05d9\u05de\u05d5\u05e9 - \u05dc\u05d0 \u05e0\u05d9\u05ea\u05df \u05dc\u05e9\u05de\u05d5\u05e8</span></p></body></html>", None))
        self.single_select_delete_yes_btn.setText(QCoreApplication.translate("SuppliersWindow", u"\u05db\u05df", None))
        self.single_select_delete_label.setText(QCoreApplication.translate("SuppliersWindow", u"\u05d4\u05d0\u05dd \u05dc\u05de\u05d7\u05d5\u05e7 \u05dc\u05e6\u05de\u05d9\u05ea\u05d5\u05ea?", None))
        self.single_select_delete_no_btn.setText(QCoreApplication.translate("SuppliersWindow", u"\u05dc\u05d0", None))
        self.all_select_delete_label.setText(QCoreApplication.translate("SuppliersWindow", u"\u05d4\u05d0\u05dd \u05dc\u05de\u05d7\u05d5\u05e7 \u05dc\u05e6\u05de\u05d9\u05ea\u05d5\u05ea?", None))
        self.all_select_delete_yes_btn.setText(QCoreApplication.translate("SuppliersWindow", u"\u05db\u05df", None))
        self.all_select_delete_no_btn.setText(QCoreApplication.translate("SuppliersWindow", u"\u05dc\u05d0", None))
    # retranslateUi

