# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(345, 406)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(345, 390))
        MainWindow.setMaximumSize(QtCore.QSize(9999, 9999))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 321, 351))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_username = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lbl_username.setObjectName("lbl_username")
        self.verticalLayout_2.addWidget(self.lbl_username)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txt_username = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.txt_username.setText("")
        self.txt_username.setObjectName("txt_username")
        self.horizontalLayout.addWidget(self.txt_username)
        self.btn_load = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_load.setObjectName("btn_load")
        self.horizontalLayout.addWidget(self.btn_load)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.cb_com = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.cb_com.setObjectName("cb_com")
        self.verticalLayout.addWidget(self.cb_com)
        self.cb_cur = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.cb_cur.setObjectName("cb_cur")
        self.verticalLayout.addWidget(self.cb_cur)
        self.cb_pla = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.cb_pla.setObjectName("cb_pla")
        self.verticalLayout.addWidget(self.cb_pla)
        self.cb_dro = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.cb_dro.setObjectName("cb_dro")
        self.verticalLayout.addWidget(self.cb_dro)
        self.cb_hol = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.cb_hol.setObjectName("cb_hol")
        self.verticalLayout.addWidget(self.cb_hol)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_2)
        self.textBrowser.setPlaceholderText("")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.btn_toAni = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_toAni.setObjectName("btn_toAni")
        self.verticalLayout_2.addWidget(self.btn_toAni)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.progressBar.setEnabled(True)
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 100)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 345, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAuthorize_Account = QtWidgets.QAction(MainWindow)
        self.actionAuthorize_Account.setCheckable(False)
        self.actionAuthorize_Account.setChecked(False)
        self.actionAuthorize_Account.setObjectName("actionAuthorize_Account")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RandToAni"))
        self.lbl_username.setText(_translate("MainWindow", "Randaris Username"))
        self.txt_username.setPlaceholderText(_translate("MainWindow", "username"))
        self.btn_load.setText(_translate("MainWindow", "Load"))
        self.cb_com.setText(_translate("MainWindow", "Completed"))
        self.cb_cur.setText(_translate("MainWindow", "Currently watching"))
        self.cb_pla.setText(_translate("MainWindow", "Plan to watch"))
        self.cb_dro.setText(_translate("MainWindow", "Dropped"))
        self.cb_hol.setText(_translate("MainWindow", "On Hold"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btn_toAni.setText(_translate("MainWindow", "load to AniList"))
        self.actionAuthorize_Account.setText(_translate("MainWindow", "Authorize Account"))
