# -*- coding: utf-8 -*-

# Форма для створення списку обліку
import sys
import os
import tempfile
import pickle
from WrData import Datas
import Profs_rc
import WrData
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormO(object):
    pathtemp = tempfile.gettempdir() + "/Proftemp"
    _translate = QtCore.QCoreApplication.translate
    def setupUi(self, FormO):
        with open(self.pathtemp + "/Profs.dbsp", "r")as f:
            self.files = f.read()
            f.close()
        self.baza = self.LoadsDB()
        self.list_ov = self.baza["prof_ov"]
        del self.list_ov[0]
        FormO.setObjectName("FormO")
        FormO.setFixedSize(554, 196)
        self.resolution = QtWidgets.QDesktopWidget().screenGeometry()
        FormO.move(int((self.resolution.width() / 2)) - int((FormO.frameSize().width() / 2)),
                   int((self.resolution.height()) / 2) - int((FormO.frameSize().height() / 2)))
        FormO.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        FormO.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/Profico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormO.setWindowIcon(icon)
        FormO.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(FormO)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.pushButton_2 = QtWidgets.QPushButton(FormO)
        self.pushButton_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_10.addWidget(self.pushButton_2, 10, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(FormO)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_10.addWidget(self.pushButton_4, 10, 3, 1, 1)
        self.comboBox = QtWidgets.QComboBox(FormO)
        self.comboBox.setObjectName("comboBox")
        for i in range(len(self.list_ov)):
            self.comboBox.addItem("")
        self.gridLayout_10.addWidget(self.comboBox, 8, 1, 1, 3)
        self.label_Image = QtWidgets.QLabel(FormO)
        self.label_Image.setStyleSheet("")
        self.label_Image.setText("")
        self.label_Image.setPixmap(QtGui.QPixmap(":/image/Books2.png"))
        self.label_Image.setScaledContents(False)
        self.label_Image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Image.setObjectName("label_Image")
        self.gridLayout_10.addWidget(self.label_Image, 0, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(FormO)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.gridLayout_10.addWidget(self.label_1, 2, 0, 1, 1)
        self.label_title = QtWidgets.QLabel(FormO)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.gridLayout_10.addWidget(self.label_title, 0, 1, 1, 3)
        self.label_2 = QtWidgets.QLabel(FormO)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_10.addWidget(self.label_2, 8, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(FormO)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_10.addWidget(self.pushButton, 2, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(FormO)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_10.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.line_11 = QtWidgets.QFrame(FormO)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.line_11.setFont(font)
        self.line_11.setStyleSheet("")
        self.line_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_11.setLineWidth(5)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setObjectName("line_11")
        self.gridLayout_10.addWidget(self.line_11, 1, 0, 1, 4)
        self.line_12 = QtWidgets.QFrame(FormO)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.line_12.setFont(font)
        self.line_12.setStyleSheet("")
        self.line_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_12.setLineWidth(6)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setObjectName("line_12")
        self.gridLayout_10.addWidget(self.line_12, 7, 0, 1, 4)
        self.line = QtWidgets.QFrame(FormO)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout_10.addWidget(self.line, 9, 0, 1, 4)
        self.verticalLayout.addLayout(self.gridLayout_10)

        self.retranslateUi(FormO)
        self.pushButton_2.clicked.connect(self.DelO)
        self.pushButton_4.clicked.connect(lambda: self.Close(FormO))
        self.pushButton.clicked.connect(lambda: self.CreateOB())
        self.comboBox.activated.connect(self.combo_chosen)
        QtCore.QMetaObject.connectSlotsByName(FormO)
        FormO.setTabOrder(self.lineEdit, self.pushButton)
        FormO.setTabOrder(self.pushButton, self.comboBox)
        FormO.setTabOrder(self.comboBox, self.pushButton_2)
        FormO.setTabOrder(self.pushButton_2, self.pushButton_4)

    def retranslateUi(self, FormO):
        self._translate = QtCore.QCoreApplication.translate
        FormO.setWindowTitle(self._translate("FormO", "Створення бази обліку"))
        self.pushButton_2.setText(self._translate("FormO", "Видалити"))
        self.pushButton_4.setText(self._translate("FormO", "Закрити"))
        for i in range(len(self.list_ov)):
            self.comboBox.setItemText(i, self._translate("Form", "{0}".format(self.list_ov[i])))
        self.label_1.setText(self._translate("FormO", "Облік"))
        self.label_title.setText(self._translate("FormO", "ПРОФІЛЬ"))
        self.label_2.setText(self._translate("FormO", "Перегляд "))
        self.pushButton.setText(self._translate("FormO", "ДОДАТИ"))

    def Close(self, forms):
        forms.close()
        os.remove(self.pathtemp + "/1")

    def CreateOB(self):
        self.prf = self.lineEdit.text()
        if self.prf != "" or self.prf != " ":
            with open(self.files, "rb") as f:
                self.dbs = pickle.load(f)
                f.close()
            self.list_ov = self.dbs["prof_ov"]
            self.list_ov.append(self.prf)
            self.dbs["prof_ov"] = self.list_ov
            with open(self.files, "wb") as f:
                pickle.dump(self.dbs, f)
                f.close()
        self.lineEdit.clear()
        self.Upcombo()

    def LoadsDB(self):
        with open(self.files, "rb") as f:
            self.dbs = pickle.load(f)
            f.close()
        return self.dbs

    def Writedb(self, db):
        with open(self.files, "wb") as f:
            pickle.dump(db, f)
            f.close()


    def combo_chosen(self):
        self.texts = self.comboBox.currentText()
        self.pushButton_2.setEnabled(True)

    def DelO(self):
        self.baza = self.LoadsDB()
        self.list_ov = self.baza["prof_ov"]
        self.list_ov.remove(self.texts)
        self.baza["prof_ov"] = self.list_ov
        self.Writedb(db=self.baza)
        self.Upcombo()

    def Upcombo(self):
        self.comboBox.clear()
        self.baza = WrData.Datas().Roblik(files=self.files)
        self.list_ov = self.baza["prof_ov"]
        del self.list_ov[0]
        for i in range(len(self.list_ov)):
            self.comboBox.addItem("")
        for i in range(len(self.list_ov)):
            self.comboBox.setItemText(i, self._translate("Form", "{0}".format(self.list_ov[i])))
        self.comboBox.update()
