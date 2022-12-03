# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_windows.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTextBrowser,
    QToolBar, QVBoxLayout, QWidget)
from GUI.ui_windows_extr import CheckComBox,CustomPlot

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(623, 498)
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        self.action_export = QAction(MainWindow)
        self.action_export.setObjectName(u"action_export")
        self.action_stm = QAction(MainWindow)
        self.action_stm.setObjectName(u"action_stm")
        self.action_stop = QAction(MainWindow)
        self.action_stop.setObjectName(u"action_stop")
        self.action_setpath = QAction(MainWindow)
        self.action_setpath.setObjectName(u"action_setpath")
        self.action_Acc = QAction(MainWindow)
        self.action_Acc.setObjectName(u"action_Acc")
        self.actionGyr = QAction(MainWindow)
        self.actionGyr.setObjectName(u"actionGyr")
        self.action_footfre = QAction(MainWindow)
        self.action_footfre.setObjectName(u"action_footfre")
        self.actionmean_Fz = QAction(MainWindow)
        self.actionmean_Fz.setObjectName(u"actionmean_Fz")
        self.action_GRF = QAction(MainWindow)
        self.action_GRF.setObjectName(u"action_GRF")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_startscan = QPushButton(self.centralwidget)
        self.pushButton_startscan.setObjectName(u"pushButton_startscan")

        self.horizontalLayout_2.addWidget(self.pushButton_startscan)

        self.pushButton_stopscan = QPushButton(self.centralwidget)
        self.pushButton_stopscan.setObjectName(u"pushButton_stopscan")

        self.horizontalLayout_2.addWidget(self.pushButton_stopscan)

        self.pushButton_refresh = QPushButton(self.centralwidget)
        self.pushButton_refresh.setObjectName(u"pushButton_refresh")

        self.horizontalLayout_2.addWidget(self.pushButton_refresh)

        self.comboBox_dotlist = CheckComBox(self.centralwidget)
        self.comboBox_dotlist.setObjectName(u"comboBox_dotlist")

        self.horizontalLayout_2.addWidget(self.comboBox_dotlist)

        self.pushButton_connect = QPushButton(self.centralwidget)
        self.pushButton_connect.setObjectName(u"pushButton_connect")

        self.horizontalLayout_2.addWidget(self.pushButton_connect)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 5)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.graphicsView_acc = CustomPlot(self.centralwidget)
        self.graphicsView_acc.setObjectName(u"graphicsView_acc")

        self.horizontalLayout.addWidget(self.graphicsView_acc)

        self.graphicsView_gyr = CustomPlot(self.centralwidget)
        self.graphicsView_gyr.setObjectName(u"graphicsView_gyr")

        self.horizontalLayout.addWidget(self.graphicsView_gyr)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_measuretime = QLineEdit(self.centralwidget)
        self.lineEdit_measuretime.setObjectName(u"lineEdit_measuretime")

        self.horizontalLayout_3.addWidget(self.lineEdit_measuretime)

        self.comboBox_meauremode = QComboBox(self.centralwidget)
        self.comboBox_meauremode.addItem("")
        self.comboBox_meauremode.addItem("")
        self.comboBox_meauremode.addItem("")
        self.comboBox_meauremode.addItem("")
        self.comboBox_meauremode.addItem("")
        self.comboBox_meauremode.addItem("")
        self.comboBox_meauremode.addItem("")
        self.comboBox_meauremode.addItem("")
        self.comboBox_meauremode.addItem("")
        self.comboBox_meauremode.addItem("")
        self.comboBox_meauremode.addItem("")
        self.comboBox_meauremode.addItem("")
        self.comboBox_meauremode.addItem("")
        self.comboBox_meauremode.addItem("")
        self.comboBox_meauremode.addItem("")
        self.comboBox_meauremode.addItem("")
        self.comboBox_meauremode.addItem("")
        self.comboBox_meauremode.addItem("")
        self.comboBox_meauremode.setObjectName(u"comboBox_meauremode")

        self.horizontalLayout_3.addWidget(self.comboBox_meauremode)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 5)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(13, 37, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy1)
        self.textBrowser.setMinimumSize(QSize(599, 0))

        self.verticalLayout.addWidget(self.textBrowser)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 20)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 3)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 623, 22))
        self.menu_edit = QMenu(self.menuBar)
        self.menu_edit.setObjectName(u"menu_edit")
        self.menu_2 = QMenu(self.menuBar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menuBar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_analsys = QMenu(self.menuBar)
        self.menu_analsys.setObjectName(u"menu_analsys")
        self.menuRUN = QMenu(self.menu_analsys)
        self.menuRUN.setObjectName(u"menuRUN")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(MainWindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar_2)
        self.toolBar_3 = QToolBar(MainWindow)
        self.toolBar_3.setObjectName(u"toolBar_3")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar_3)

        self.menuBar.addAction(self.menu_edit.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu_3.menuAction())
        self.menuBar.addAction(self.menu_analsys.menuAction())
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.action_open)
        self.menu_edit.addAction(self.action_export)
        self.menu_3.addAction(self.action_Acc)
        self.menu_3.addAction(self.actionGyr)
        self.menu_3.addAction(self.action_GRF)
        self.menu_analsys.addAction(self.menuRUN.menuAction())
        self.menuRUN.addAction(self.action_footfre)
        self.menuRUN.addAction(self.actionmean_Fz)
        self.toolBar.addAction(self.action_setpath)
        self.toolBar_2.addAction(self.action_stm)
        self.toolBar_3.addAction(self.action_stop)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"XD GRF PRE", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.action_export.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.action_stm.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u6d4b\u8bd5", None))
        self.action_stop.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u6d4b\u8bd5", None))
        self.action_setpath.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u8def\u5f84", None))
        self.action_Acc.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u901f\u5ea6", None))
        self.actionGyr.setText(QCoreApplication.translate("MainWindow", u"\u89d2\u901f\u5ea6", None))
        self.action_footfre.setText(QCoreApplication.translate("MainWindow", u"_footfre", None))
        self.actionmean_Fz.setText(QCoreApplication.translate("MainWindow", u"mean_Fz", None))
        self.action_GRF.setText(QCoreApplication.translate("MainWindow", u"_GRF", None))
        self.pushButton_startscan.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u8bbe\u5907", None))
        self.pushButton_stopscan.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u626b\u63cf", None))
        self.pushButton_refresh.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        self.pushButton_connect.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5", None))
        self.lineEdit_measuretime.setText(QCoreApplication.translate("MainWindow", u"input measure time (s)", None))
        self.comboBox_meauremode.setItemText(0, QCoreApplication.translate("MainWindow", u"RateQuantities", None))
        self.comboBox_meauremode.setItemText(1, QCoreApplication.translate("MainWindow", u"HighFidelitywMag", None))
        self.comboBox_meauremode.setItemText(2, QCoreApplication.translate("MainWindow", u"ExtendedQuaternion", None))
        self.comboBox_meauremode.setItemText(3, QCoreApplication.translate("MainWindow", u"CompleteQuaternion", None))
        self.comboBox_meauremode.setItemText(4, QCoreApplication.translate("MainWindow", u"OrientationEuler", None))
        self.comboBox_meauremode.setItemText(5, QCoreApplication.translate("MainWindow", u"OrientationQuaternion", None))
        self.comboBox_meauremode.setItemText(6, QCoreApplication.translate("MainWindow", u"FreeAcceleration", None))
        self.comboBox_meauremode.setItemText(7, QCoreApplication.translate("MainWindow", u"ExtendedEuler", None))
        self.comboBox_meauremode.setItemText(8, QCoreApplication.translate("MainWindow", u"CompleteEuler", None))
        self.comboBox_meauremode.setItemText(9, QCoreApplication.translate("MainWindow", u"HighFidelity", None))
        self.comboBox_meauremode.setItemText(10, QCoreApplication.translate("MainWindow", u"DeltaQuantitieswMag", None))
        self.comboBox_meauremode.setItemText(11, QCoreApplication.translate("MainWindow", u"DeltaQuantities", None))
        self.comboBox_meauremode.setItemText(12, QCoreApplication.translate("MainWindow", u"RateQuantitieswMag", None))
        self.comboBox_meauremode.setItemText(13, QCoreApplication.translate("MainWindow", u"CustomMode1", None))
        self.comboBox_meauremode.setItemText(14, QCoreApplication.translate("MainWindow", u"CustomMode2", None))
        self.comboBox_meauremode.setItemText(15, QCoreApplication.translate("MainWindow", u"CustomMode3", None))
        self.comboBox_meauremode.setItemText(16, QCoreApplication.translate("MainWindow", u"CustomMode4", None))
        self.comboBox_meauremode.setItemText(17, QCoreApplication.translate("MainWindow", u"CustomMode5", None))

        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">---------------------------------log---------------------------------</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.menu_edit.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u89c6\u56fe", None))
        self.menu_analsys.setTitle(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97", None))
        self.menuRUN.setTitle(QCoreApplication.translate("MainWindow", u"RUN", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
        self.toolBar_3.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_3", None))
    # retranslateUi

