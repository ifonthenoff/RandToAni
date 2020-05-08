# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(280, 150)
        Dialog.setMinimumSize(QtCore.QSize(280, 150))
        Dialog.setMaximumSize(QtCore.QSize(280, 150))
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 261, 133))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.btn_url = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_url.setObjectName("btn_url")
        self.horizontalLayout_3.addWidget(self.btn_url)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.textBrowser_dialog = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser_dialog.setReadOnly(False)
        self.textBrowser_dialog.setObjectName("textBrowser_dialog")
        self.verticalLayout.addWidget(self.textBrowser_dialog)
        self.btn_save = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_save.setObjectName("btn_save")
        self.verticalLayout.addWidget(self.btn_save)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Authorize API Client"))
        self.label.setText(_translate("Dialog", "Copy authorization token to textbox"))
        self.btn_url.setText(_translate("Dialog", "Open Url"))
        self.textBrowser_dialog.setPlaceholderText(_translate("Dialog", "paste token here"))
        self.btn_save.setText(_translate("Dialog", "Save"))
