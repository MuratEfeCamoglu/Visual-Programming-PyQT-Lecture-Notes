# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(495, 269)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_sayi1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sayi1.setGeometry(QtCore.QRect(40, 60, 47, 14))
        self.lbl_sayi1.setObjectName("lbl_sayi1")
        self.lbl_sayi2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sayi2.setGeometry(QtCore.QRect(40, 90, 47, 14))
        self.lbl_sayi2.setObjectName("lbl_sayi2")
        self.txt_sayi1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_sayi1.setGeometry(QtCore.QRect(110, 60, 181, 20))
        self.txt_sayi1.setObjectName("txt_sayi1")
        self.txt_sayi2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_sayi2.setGeometry(QtCore.QRect(110, 90, 181, 20))
        self.txt_sayi2.setObjectName("txt_sayi2")
        self.btn_topla = QtWidgets.QPushButton(self.centralwidget)
        self.btn_topla.setGeometry(QtCore.QRect(110, 130, 75, 23))
        self.btn_topla.setObjectName("btn_topla")
        self.btn_cikarma = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cikarma.setGeometry(QtCore.QRect(190, 130, 75, 23))
        self.btn_cikarma.setObjectName("btn_cikarma")
        self.btn_carpma = QtWidgets.QPushButton(self.centralwidget)
        self.btn_carpma.setGeometry(QtCore.QRect(270, 130, 75, 23))
        self.btn_carpma.setObjectName("btn_carpma")
        self.btn_bolme = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bolme.setGeometry(QtCore.QRect(350, 130, 75, 23))
        self.btn_bolme.setObjectName("btn_bolme")
        self.lbl_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sonuc.setGeometry(QtCore.QRect(110, 180, 301, 31))
        self.lbl_sonuc.setObjectName("lbl_sonuc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 495, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_sayi1.setText(_translate("MainWindow", "Sayi1 : "))
        self.lbl_sayi2.setText(_translate("MainWindow", "Sayi 2 : "))
        self.btn_topla.setText(_translate("MainWindow", "Toplam"))
        self.btn_cikarma.setText(_translate("MainWindow", "Cikarma"))
        self.btn_carpma.setText(_translate("MainWindow", "Carpma"))
        self.btn_bolme.setText(_translate("MainWindow", "Bolme"))
        self.lbl_sonuc.setText(_translate("MainWindow", "Sonuc : "))
