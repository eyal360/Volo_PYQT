# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lead_windowgevvtz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import event_window_icons_rc

class Ui_LeadWindow(object):
    def setupUi(self, LeadWindow):
        if not LeadWindow.objectName():
            LeadWindow.setObjectName(u"LeadWindow")
        LeadWindow.resize(1025, 837)
        LeadWindow.setStyleSheet(u"background-color: rgb(196,213,242);")
        self.centralwidget = QWidget(LeadWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lead_folder_label = QLabel(self.centralwidget)
        self.lead_folder_label.setObjectName(u"lead_folder_label")
        self.lead_folder_label.setGeometry(QRect(870, 130, 151, 31))
        self.lead_folder_label.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(224, 153, 94);\n"
"	font: 63 14pt \"Segoe UI Semibold\";\n"
"	border: 1px solid #090206;\n"
"	border-radius: 15px;	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.contact_email_label = QLabel(self.centralwidget)
        self.contact_email_label.setObjectName(u"contact_email_label")
        self.contact_email_label.setGeometry(QRect(630, 180, 51, 41))
        self.contact_email_label.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.dragndrop_label = QLabel(self.centralwidget)
        self.dragndrop_label.setObjectName(u"dragndrop_label")
        self.dragndrop_label.setGeometry(QRect(580, 800, 241, 31))
        self.dragndrop_label.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(187,187,187);\n"
"	font: 63 14pt \"Segoe UI Semibold\";\n"
"	border: 1px solid #090206;\n"
"	border-radius: 15px;	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.left_line = QFrame(self.centralwidget)
        self.left_line.setObjectName(u"left_line")
        self.left_line.setGeometry(QRect(160, 680, 16, 161))
        self.left_line.setFrameShape(QFrame.VLine)
        self.left_line.setFrameShadow(QFrame.Sunken)
        self.upper_line = QFrame(self.centralwidget)
        self.upper_line.setObjectName(u"upper_line")
        self.upper_line.setGeometry(QRect(50, 230, 951, 20))
        self.upper_line.setFrameShape(QFrame.HLine)
        self.upper_line.setFrameShadow(QFrame.Sunken)
        self.wine_icon = QLabel(self.centralwidget)
        self.wine_icon.setObjectName(u"wine_icon")
        self.wine_icon.setGeometry(QRect(20, 20, 71, 101))
        self.wine_icon.setStyleSheet(u"image: url(:/icons/misc/wine.png);")
        self.contact_email = QLabel(self.centralwidget)
        self.contact_email.setObjectName(u"contact_email")
        self.contact_email.setGeometry(QRect(310, 180, 321, 41))
        self.contact_email.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border:1px solid #090206;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.lead_tablewidget = QTableWidget(self.centralwidget)
        if (self.lead_tablewidget.columnCount() < 4):
            self.lead_tablewidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.lead_tablewidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.lead_tablewidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.lead_tablewidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.lead_tablewidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.lead_tablewidget.setObjectName(u"lead_tablewidget")
        self.lead_tablewidget.setGeometry(QRect(280, 310, 501, 301))
        self.lead_tablewidget.setMaximumSize(QSize(881, 16777215))
        self.lead_tablewidget.setLayoutDirection(Qt.RightToLeft)
        self.lead_tablewidget.setFrameShape(QFrame.NoFrame)
        self.lead_tablewidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.lead_tablewidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lead_tablewidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.bottom_line = QFrame(self.centralwidget)
        self.bottom_line.setObjectName(u"bottom_line")
        self.bottom_line.setGeometry(QRect(170, 670, 721, 20))
        self.bottom_line.setFrameShape(QFrame.HLine)
        self.bottom_line.setFrameShadow(QFrame.Sunken)
        self.contact_phone = QLabel(self.centralwidget)
        self.contact_phone.setObjectName(u"contact_phone")
        self.contact_phone.setGeometry(QRect(50, 180, 161, 41))
        self.contact_phone.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border:1px solid #090206;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.or_label = QLabel(self.centralwidget)
        self.or_label.setObjectName(u"or_label")
        self.or_label.setGeometry(QRect(490, 740, 31, 41))
        self.or_label.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.contact_name = QLabel(self.centralwidget)
        self.contact_name.setObjectName(u"contact_name")
        self.contact_name.setGeometry(QRect(710, 180, 161, 41))
        self.contact_name.setStyleSheet(u"font: 12pt \"Segoe UI Semilight\";\n"
"border:1px solid #090206;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.lead_open_missions_btn = QPushButton(self.centralwidget)
        self.lead_open_missions_btn.setObjectName(u"lead_open_missions_btn")
        self.lead_open_missions_btn.setGeometry(QRect(220, 250, 261, 41))
        font = QFont()
        font.setFamily(u"Segoe UI Semilight")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.lead_open_missions_btn.setFont(font)
        self.lead_open_missions_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.lead_open_missions_btn.setMouseTracking(True)
        self.lead_open_missions_btn.setFocusPolicy(Qt.ClickFocus)
        self.lead_open_missions_btn.setStyleSheet(u"QPushButton { \n"
"	background-color: rgb(255,255,255);	\n"
"	color: rgb(255,204,0);\n"
"	font: 63 15pt \"Segoe UI Semilight\";\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	font: 63 15pt \"Segoe UI Semilight\";\n"
"	background-color: rgb(255,204,0);\n"
"	color: rgb(255,255,255);	\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	font: 63 15pt \"Segoe UI Semibold\";\n"
"}")
        self.contact_name_label = QLabel(self.centralwidget)
        self.contact_name_label.setObjectName(u"contact_name_label")
        self.contact_name_label.setGeometry(QRect(880, 180, 101, 41))
        self.contact_name_label.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.contact_phone_label = QLabel(self.centralwidget)
        self.contact_phone_label.setObjectName(u"contact_phone_label")
        self.contact_phone_label.setGeometry(QRect(220, 180, 61, 41))
        self.contact_phone_label.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.lead_folder_btn = QPushButton(self.centralwidget)
        self.lead_folder_btn.setObjectName(u"lead_folder_btn")
        self.lead_folder_btn.setGeometry(QRect(890, 20, 111, 101))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semilight")
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(7)
        self.lead_folder_btn.setFont(font1)
        self.lead_folder_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.lead_folder_btn.setMouseTracking(True)
        self.lead_folder_btn.setFocusPolicy(Qt.ClickFocus)
        self.lead_folder_btn.setStyleSheet(u"QPushButton {\n"
"	\n"
"	image: url(:/icons/misc/folder.png);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 20pt \"Segoe UI Semilight\";\n"
"	border-radius: 35px;\n"
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
        self.right_line = QFrame(self.centralwidget)
        self.right_line.setObjectName(u"right_line")
        self.right_line.setGeometry(QRect(880, 680, 16, 161))
        self.right_line.setFrameShape(QFrame.VLine)
        self.right_line.setFrameShadow(QFrame.Sunken)
        self.lead_close_missions_btn = QPushButton(self.centralwidget)
        self.lead_close_missions_btn.setObjectName(u"lead_close_missions_btn")
        self.lead_close_missions_btn.setGeometry(QRect(500, 250, 341, 41))
        self.lead_close_missions_btn.setFont(font)
        self.lead_close_missions_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.lead_close_missions_btn.setMouseTracking(True)
        self.lead_close_missions_btn.setFocusPolicy(Qt.ClickFocus)
        self.lead_close_missions_btn.setStyleSheet(u"QPushButton { \n"
"	background-color: rgb(255,255,255);	\n"
"	color: rgb(221,9,9);\n"
"	font: 63 15pt \"Segoe UI Semilight\";\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	font: 63 15pt \"Segoe UI Semilight\";\n"
"	background-color: rgb(221,9,9);\n"
"	color: rgb(255,255,255);	\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	font: 63 15pt \"Segoe UI Semibold\";\n"
"}")
        self.lead_date_label = QLabel(self.centralwidget)
        self.lead_date_label.setObjectName(u"lead_date_label")
        self.lead_date_label.setGeometry(QRect(400, 110, 161, 41))
        self.lead_date_label.setStyleSheet(u"font: 14pt \"Segoe UI Semibold\";\n"
"border:1px solid #090206;\n"
"color: rgb(196,197,242);\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.browser_btn = QPushButton(self.centralwidget)
        self.browser_btn.setObjectName(u"browser_btn")
        self.browser_btn.setGeometry(QRect(200, 740, 261, 41))
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
        self.dragndrop_list = QListWidget(self.centralwidget)
        QListWidgetItem(self.dragndrop_list)
        QListWidgetItem(self.dragndrop_list)
        QListWidgetItem(self.dragndrop_list)
        QListWidgetItem(self.dragndrop_list)
        QListWidgetItem(self.dragndrop_list)
        self.dragndrop_list.setObjectName(u"dragndrop_list")
        self.dragndrop_list.setGeometry(QRect(545, 700, 311, 111))
        self.dragndrop_list.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.dragndrop_list.setStyleSheet(u"font: 14pt \"Segoe UI Semilight\";\n"
"border: 1px solid #090206;\n"
"background-color: rgb(255,255,255);\n"
"border-radius: 20px;")
        self.dragndrop_list.setFrameShape(QFrame.NoFrame)
        self.dragndrop_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.dragndrop_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.dragndrop_list.setFlow(QListView.TopToBottom)
        self.dragndrop_list.setViewMode(QListView.ListMode)
        self.dragndrop_list.setModelColumn(0)
        self.dragndrop_list.setItemAlignment(Qt.AlignCenter|Qt.AlignHCenter|Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dragndrop_list.setSortingEnabled(False)
        self.upper_frame = QFrame(self.centralwidget)
        self.upper_frame.setObjectName(u"upper_frame")
        self.upper_frame.setGeometry(QRect(100, 20, 751, 101))
        font2 = QFont()
        font2.setPointSize(15)
        self.upper_frame.setFont(font2)
        self.upper_frame.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"border-radius: 40px;")
        self.upper_frame.setFrameShape(QFrame.StyledPanel)
        self.upper_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.upper_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.upper_frame_header_btn = QPushButton(self.upper_frame)
        self.upper_frame_header_btn.setObjectName(u"upper_frame_header_btn")
        font3 = QFont()
        font3.setFamily(u"Segoe UI Semibold")
        font3.setPointSize(42)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(7)
        self.upper_frame_header_btn.setFont(font3)
        self.upper_frame_header_btn.setCursor(QCursor(Qt.ArrowCursor))
        self.upper_frame_header_btn.setMouseTracking(True)
        self.upper_frame_header_btn.setFocusPolicy(Qt.ClickFocus)
        self.upper_frame_header_btn.setAutoFillBackground(False)
        self.upper_frame_header_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(196,197,242);\n"
"	font: 63 42pt \"Segoe UI Semibold\";\n"
"	border-radius: 30px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.upper_frame_header_btn)

        LeadWindow.setCentralWidget(self.centralwidget)
        self.lead_folder_label.raise_()
        self.contact_email_label.raise_()
        self.left_line.raise_()
        self.upper_line.raise_()
        self.wine_icon.raise_()
        self.contact_email.raise_()
        self.lead_tablewidget.raise_()
        self.bottom_line.raise_()
        self.contact_phone.raise_()
        self.or_label.raise_()
        self.contact_name.raise_()
        self.lead_open_missions_btn.raise_()
        self.contact_name_label.raise_()
        self.contact_phone_label.raise_()
        self.lead_folder_btn.raise_()
        self.right_line.raise_()
        self.lead_close_missions_btn.raise_()
        self.browser_btn.raise_()
        self.dragndrop_list.raise_()
        self.upper_frame.raise_()
        self.lead_date_label.raise_()
        self.dragndrop_label.raise_()

        self.retranslateUi(LeadWindow)

        QMetaObject.connectSlotsByName(LeadWindow)
    # setupUi

    def retranslateUi(self, LeadWindow):
        LeadWindow.setWindowTitle(QCoreApplication.translate("LeadWindow", u"MainWindow", None))
        self.lead_folder_label.setText(QCoreApplication.translate("LeadWindow", u"\u05ea\u05d9\u05e7\u05d9\u05d9\u05d4 \u05d0\u05d9\u05e9\u05d9\u05ea", None))
        self.contact_email_label.setText(QCoreApplication.translate("LeadWindow", u"\u05de\u05d9\u05d9\u05dc", None))
        self.dragndrop_label.setText(QCoreApplication.translate("LeadWindow", u"\u05e0\u05d9\u05ea\u05df \u05dc\u05d2\u05e8\u05d5\u05e8 \u05dc\u05db\u05d0\u05df \u05e7\u05d1\u05e6\u05d9\u05dd", None))
        self.wine_icon.setText("")
        self.contact_email.setText(QCoreApplication.translate("LeadWindow", u"<html><head/><body><p align=\"center\">miriamkogan84@gmail.com</p></body></html>", None))
        ___qtablewidgetitem = self.lead_tablewidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("LeadWindow", u"\u05de\u05e9\u05d9\u05de\u05d4", None));
        ___qtablewidgetitem1 = self.lead_tablewidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("LeadWindow", u"\u05ea\u05d0\u05e8\u05d9\u05da \u05dc\u05d1\u05d9\u05e6\u05d5\u05e2", None));
        ___qtablewidgetitem2 = self.lead_tablewidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("LeadWindow", u"\u05e1\u05d8\u05d0\u05d8\u05d5\u05e1", None));
        ___qtablewidgetitem3 = self.lead_tablewidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("LeadWindow", u"\u05d4\u05e2\u05e8\u05d5\u05ea", None));
        self.contact_phone.setText(QCoreApplication.translate("LeadWindow", u"<html><head/><body><p align=\"center\">054-6215532</p></body></html>", None))
        self.or_label.setText(QCoreApplication.translate("LeadWindow", u"\u05d0\u05d5 ", None))
        self.contact_name.setText(QCoreApplication.translate("LeadWindow", u"<html><head/><body><p align=\"center\">\u05de\u05e8\u05d9\u05dd \u05e7\u05d5\u05d2\u05df</p></body></html>", None))
        self.lead_open_missions_btn.setText(QCoreApplication.translate("LeadWindow", u"\u05de\u05e9\u05d9\u05de\u05d5\u05ea \u05e4\u05ea\u05d5\u05d7\u05d5\u05ea - 10", None))
        self.contact_name_label.setText(QCoreApplication.translate("LeadWindow", u"\u05d0\u05d9\u05e9 \u05e7\u05e9\u05e8", None))
        self.contact_phone_label.setText(QCoreApplication.translate("LeadWindow", u"\u05d8\u05dc\u05e4\u05d5\u05df", None))
#if QT_CONFIG(tooltip)
        self.lead_folder_btn.setToolTip(QCoreApplication.translate("LeadWindow", u"<html><head/><body><p>\u05dc\u05d7\u05e5 \u05dc\u05e4\u05ea\u05d9\u05d7\u05ea \u05ea\u05d9\u05e7\u05d9\u05d9\u05d4 \u05d0\u05d9\u05e9\u05d9\u05ea</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lead_folder_btn.setWhatsThis(QCoreApplication.translate("LeadWindow", u"<html><head/><body><p>\u05dc\u05d7\u05e5 \u05dc\u05e4\u05ea\u05d9\u05d7\u05ea \u05ea\u05d9\u05e7\u05d9\u05d9\u05d4 \u05d0\u05d9\u05e9\u05d9\u05ea</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lead_folder_btn.setText("")
        self.lead_close_missions_btn.setText(QCoreApplication.translate("LeadWindow", u"\u05de\u05e9\u05d9\u05de\u05d5\u05ea \u05dc\u05d7\u05d5\u05d3\u05e9 \u05d4\u05e7\u05e8\u05d5\u05d1 - 3", None))
        self.lead_date_label.setText(QCoreApplication.translate("LeadWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">11/11/2021</span></p></body></html>", None))
        self.browser_btn.setText(QCoreApplication.translate("LeadWindow", u"\u05dc\u05d1\u05d7\u05d5\u05e8 \u05e7\u05d1\u05e6\u05d9\u05dd", None))

        __sortingEnabled = self.dragndrop_list.isSortingEnabled()
        self.dragndrop_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.dragndrop_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("LeadWindow", u"file_number_1", None));
        ___qlistwidgetitem1 = self.dragndrop_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("LeadWindow", u"\u05de\u05e1\u05de\u05da \u05d7\u05d3\u05e9", None));
        ___qlistwidgetitem2 = self.dragndrop_list.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("LeadWindow", u"\u05d7\u05d5\u05d6\u05d4 \u05d7\u05ea\u05d5\u05e0\u05d4 \u05d0\u05d9\u05d9\u05dc \u05d5\u05de\u05d9\u05e8\u05d9", None));
        ___qlistwidgetitem3 = self.dragndrop_list.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("LeadWindow", u"\u05d7\u05d5\u05d6\u05d4 \u05de\u05d5\u05dc \u05e1\u05e4\u05e7 \u05e4\u05d9\u05e6\u05d5\u05d7\u05d9\u05dd", None));
        ___qlistwidgetitem4 = self.dragndrop_list.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("LeadWindow", u"\u05d4\u05e1\u05db\u05de\u05d9\u05dd \u05e2\u05dd \u05d4\u05d5\u05e8\u05d9\u05dd \u05e9\u05dc \u05e9\u05dc\u05de\u05d4", None));
        self.dragndrop_list.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(tooltip)
        self.dragndrop_list.setToolTip(QCoreApplication.translate("LeadWindow", u"<html><head/><body><p>\u05d2\u05e8\u05d5\u05e8 \u05dc\u05db\u05d0\u05df \u05e7\u05d1\u05e6\u05d9\u05dd</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.dragndrop_list.setWhatsThis(QCoreApplication.translate("LeadWindow", u"<html><head/><body><p>\u05d2\u05e8\u05d5\u05e8 \u05dc\u05db\u05d0\u05df \u05e7\u05d1\u05e6\u05d9\u05dd</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.upper_frame_header_btn.setText(QCoreApplication.translate("LeadWindow", u"\u05d4\u05d7\u05ea\u05d5\u05e0\u05d4 \u05e9\u05dc \u05d0\u05d9\u05d9\u05dc \u05d5\u05de\u05d9\u05e8\u05d9", None))
    # retranslateUi

