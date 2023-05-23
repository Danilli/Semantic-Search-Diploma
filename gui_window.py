# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTextBrowser,
    QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(889, 655)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Noto Sans SC;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 10, 91, 31))
        self.label.setStyleSheet(u"color: rgb(200,120,90);\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(80, 60, 91, 31))
        self.label_8.setStyleSheet(u"color: rgb(200,120,90);\n"
"font-weight: bold;\n"
"font-size: 11pt;")
        self.title_frame = QFrame(self.centralwidget)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setGeometry(QRect(80, 190, 491, 181))
        self.title_frame.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.verticalLayout_2 = QVBoxLayout(self.title_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title1 = QLabel(self.title_frame)
        self.title1.setObjectName(u"title1")

        self.verticalLayout_2.addWidget(self.title1)

        self.title2 = QLabel(self.title_frame)
        self.title2.setObjectName(u"title2")

        self.verticalLayout_2.addWidget(self.title2)

        self.title3 = QLabel(self.title_frame)
        self.title3.setObjectName(u"title3")

        self.verticalLayout_2.addWidget(self.title3)

        self.title4 = QLabel(self.title_frame)
        self.title4.setObjectName(u"title4")

        self.verticalLayout_2.addWidget(self.title4)

        self.title5 = QLabel(self.title_frame)
        self.title5.setObjectName(u"title5")

        self.verticalLayout_2.addWidget(self.title5)

        self.Find = QPushButton(self.centralwidget)
        self.Find.setObjectName(u"Find")
        self.Find.setGeometry(QRect(750, 110, 91, 31))
        self.Find.setStyleSheet(u"QPushButton:pressed{\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,50);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/search_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Find.setIcon(icon)
        self.Rel_frames = QFrame(self.centralwidget)
        self.Rel_frames.setObjectName(u"Rel_frames")
        self.Rel_frames.setGeometry(QRect(640, 190, 81, 181))
        self.Rel_frames.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.verticalLayout_3 = QVBoxLayout(self.Rel_frames)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.rel1 = QLabel(self.Rel_frames)
        self.rel1.setObjectName(u"rel1")

        self.verticalLayout_3.addWidget(self.rel1)

        self.rel2 = QLabel(self.Rel_frames)
        self.rel2.setObjectName(u"rel2")

        self.verticalLayout_3.addWidget(self.rel2)

        self.rel3 = QLabel(self.Rel_frames)
        self.rel3.setObjectName(u"rel3")

        self.verticalLayout_3.addWidget(self.rel3)

        self.rel4 = QLabel(self.Rel_frames)
        self.rel4.setObjectName(u"rel4")

        self.verticalLayout_3.addWidget(self.rel4)

        self.rel5 = QLabel(self.Rel_frames)
        self.rel5.setObjectName(u"rel5")

        self.verticalLayout_3.addWidget(self.rel5)

        self.queryLine = QLineEdit(self.centralwidget)
        self.queryLine.setObjectName(u"queryLine")
        self.queryLine.setGeometry(QRect(170, 10, 681, 31))
        self.keywordsLine = QLineEdit(self.centralwidget)
        self.keywordsLine.setObjectName(u"keywordsLine")
        self.keywordsLine.setGeometry(QRect(170, 60, 681, 31))
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(570, 150, 79, 31))
        self.label_19.setStyleSheet(u"font: 700 11pt \"Segoe Print\";")
        self.FileText = QTextBrowser(self.centralwidget)
        self.FileText.setObjectName(u"FileText")
        self.FileText.setGeometry(QRect(90, 400, 721, 241))
        self.FileText.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 61, 71))
        self.label_2.setPixmap(QPixmap(u":/icons/icons/travel_icon.svg"))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 400, 51, 81))
        self.label_9.setPixmap(QPixmap(u":/icons/icons/description_icon.svg"))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 190, 31, 181))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: italic 12pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: italic 12pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: italic 12pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: italic 12pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: italic 12pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.label_7)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(730, 190, 81, 181))
        self.verticalLayout_4 = QVBoxLayout(self.widget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.View1 = QPushButton(self.widget1)
        self.View1.setObjectName(u"View1")
        self.View1.setStyleSheet(u"QPushButton:pressed{\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,50);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/visibility_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.View1.setIcon(icon1)

        self.verticalLayout_4.addWidget(self.View1)

        self.View2 = QPushButton(self.widget1)
        self.View2.setObjectName(u"View2")
        self.View2.setStyleSheet(u"QPushButton:pressed{\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,50);\n"
"}")
        self.View2.setIcon(icon1)

        self.verticalLayout_4.addWidget(self.View2)

        self.View3 = QPushButton(self.widget1)
        self.View3.setObjectName(u"View3")
        self.View3.setStyleSheet(u"QPushButton:pressed{\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,50);\n"
"}")
        self.View3.setIcon(icon1)

        self.verticalLayout_4.addWidget(self.View3)

        self.View4 = QPushButton(self.widget1)
        self.View4.setObjectName(u"View4")
        self.View4.setStyleSheet(u"QPushButton:pressed{\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,50);\n"
"}")
        self.View4.setIcon(icon1)

        self.verticalLayout_4.addWidget(self.View4)

        self.View5 = QPushButton(self.widget1)
        self.View5.setObjectName(u"View5")
        self.View5.setStyleSheet(u"QPushButton:pressed{\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,50);\n"
"}")
        self.View5.setIcon(icon1)

        self.verticalLayout_4.addWidget(self.View5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0434\u0443\u0441\u042f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Your query: ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Keywords:", None))
        self.title1.setText("")
        self.title2.setText("")
        self.title3.setText("")
        self.title4.setText("")
        self.title5.setText("")
        self.Find.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.rel1.setText("")
        self.rel2.setText("")
        self.rel3.setText("")
        self.rel4.setText("")
        self.rel5.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Relevanse:", None))
        self.label_2.setText("")
        self.label_9.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"1:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"2:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"3:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"4:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"5:", None))
        self.View1.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.View2.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.View3.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.View4.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.View5.setText(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi

