# -*- coding: utf-8 -*-

import os
import sys
import tempfile
from PyQt5 import QtCore, QtGui, QtWidgets

if 'ANDROID_BOOTLOGO' in os.environ:
    pass
else:
    from PyQt5 import QtPrintSupport
import Profs_rc

class Window(QtWidgets.QWidget):
    pathtemp = tempfile.gettempdir() + "/Proftemp"
    orient = 0
    cur = 0
    def __init__(self, titles):
        QtWidgets.QDialog.__init__(self)
        self.setFixedSize(960, 600)
        self.resolution = QtWidgets.QDesktopWidget().screenGeometry()
        if 'ANDROID_BOOTLOGO' in os.environ:
            self.move(int((self.resolution.width() / 2) - (self.frameSize().width() / 2)), int(0))
        else:
            self.move(int((self.resolution.width() / 2) - (self.frameSize().width() / 2)),
                          int((self.resolution.height() / 2) - (self.frameSize().height() / 2)))
        self.activateWindow()
        self.setWindowTitle(self.tr(titles))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/Profico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setWindowIcon(icon)
        self.editor = QtWidgets.QTextEdit(self)
        self.editor.setReadOnly(True)
        self.editor.setLineWrapMode(self.editor.WidgetWidth)
        self.editor.textChanged.connect(self.handleTextChanged)
        self.buttonOpen = QtWidgets.QPushButton('В pdf', self)
        self.buttonOpen.setAutoDefault(True)
        self.buttonOpen.clicked.connect(self.topdf)
        self.buttonPrint = QtWidgets.QPushButton('Друкувати', self)
        self.buttonPrint.setAutoDefault(True)
        self.buttonPrint.clicked.connect(self.handlePrint)
        self.buttonPreview = QtWidgets.QPushButton('Переглянути', self)
        self.buttonPreview.setAutoDefault(True)
        self.buttonPreview.clicked.connect(self.handlePreview)
        self.buttonCurs = QtWidgets.QPushButton('Включити курсор', self)
        self.buttonCurs.setAutoDefault(True)
        self.buttonCurs.clicked.connect(self.hirCurs)
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self.editor, 0, 0, 1, 4)
        layout.addWidget(self.buttonCurs,1, 0)
        layout.addWidget(self.buttonOpen, 1, 1)
        layout.addWidget(self.buttonPrint, 1, 2)
        layout.addWidget(self.buttonPreview, 1, 3)
        self.handleTextChanged()
        self.setTabOrder(self.buttonCurs,self.buttonPreview)
        self.setTabOrder(self.buttonPreview, self.buttonPrint)
        self.setTabOrder(self.buttonPrint, self.buttonOpen)
        self.setTabOrder(self.buttonOpen, self.editor)

    def hirCurs(self):
        if self.cur == 0:
            self.buttonCurs.setText("Виключити курсор")
            self.editor.setReadOnly(False)
            self.cur = 1
        else:
            self.buttonCurs.setText("Включити курсор")
            self.editor.setReadOnly(True)
            self.cur = 0

    def handleOpen(self, orent):
        self.orient = orent
        path = self.pathtemp + "/_temp.html"
        info = QtCore.QFileInfo(path)
        f = open(path, "r")
        text = f.read()
        f.close()
        if info.completeSuffix() == 'html':
            self.editor.setHtml(text)
        else:
            self.editor.setPlainText(text)

    def handlePrint(self):
        location = self.pathtemp + "/_temp.html"
        with open(location,"w") as f:
            f.write(self.editor.document().toHtml())
            f.close()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/Profico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        doc = QtGui.QTextDocument()
        location = self.pathtemp + "/_temp.html"
        html = open(location).read()
        doc.setHtml(html)
        if 'ANDROID_BOOTLOGO' in os.environ:
            pass
        else:
            printerd = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
            if self.orient == 1:
                printerd.setOrientation(QtPrintSupport.QPrinter.Landscape)
                printerd.setResolution(300)
                printerd.setPageMargins(30,10,10,20, QtPrintSupport.QPrinter.Millimeter)
                printerd.setPageSize(QtPrintSupport.QPrinter.A4)
                sizes = QtCore.QSizeF(794, 1123)
            else:
                printerd.setOrientation(QtPrintSupport.QPrinter.Portrait)
                printerd.setResolution(300)
                printerd.setPageMargins(30,10,10,20, QtPrintSupport.QPrinter.Millimeter)
                printerd.setPageSize(QtPrintSupport.QPrinter.A4)
                sizes = QtCore.QSizeF(794, 1123)
            dialog = QtPrintSupport.QPrintDialog(printerd,self)
            dialog.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint)
            dialog.setWindowIcon(icon)
            doc.setPageSize(sizes)
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                doc.print_(dialog.printer())

    def handlePreview(self):
        location = self.pathtemp + "/_temp.html"
        with open(location,"w") as f:
            f.write(self.editor.document().toHtml())
            f.close()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/Profico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        doc = QtGui.QTextDocument()
        location = self.pathtemp + "/_temp.html"
        html = open(location).read()
        doc.setHtml(html)
        if 'ANDROID_BOOTLOGO' in os.environ:
            pass
        else:
            printerd = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.PrinterResolution)
            if self.orient == 1:
                printerd.setOrientation(QtPrintSupport.QPrinter.Landscape)
                printerd.setResolution(300)
                printerd.setPageSize(QtPrintSupport.QPrinter.A4)
                printerd.setPageMargins(30,10,10,20, QtPrintSupport.QPrinter.Millimeter)
                sizes = QtCore.QSizeF(1123, 794)
            else:
                printerd.setOrientation(QtPrintSupport.QPrinter.Portrait)
                printerd.setResolution(300)
                printerd.setPageSize(QtPrintSupport.QPrinter.A4)
                printerd.setPageMargins(30,10,10,20, QtPrintSupport.QPrinter.Millimeter)
                sizes = QtCore.QSizeF(794, 1123)
            dialog = QtPrintSupport.QPrintPreviewDialog(printerd,self)
            dialog.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint)
            dialog.setWindowIcon(icon)
            doc.setPageSize(sizes)
            dialog.paintRequested.connect(doc.print_)
            dialog.exec_()

    def handleTextChanged(self):
        enable = not self.editor.document().isEmpty()
        self.buttonPrint.setEnabled(enable)
        self.buttonPreview.setEnabled(enable)
        self.buttonOpen.setEnabled(enable)

    def topdf(self):
        if sys.platform == 'win32':
            self.sevs = os.environ['USERPROFILE'] + "/Documents"
        if sys.platform == 'linux':
            self.sevs = os.environ['HOME']
        self.files = QtWidgets.QFileDialog.getSaveFileName(self, "Зберегти дані", self.sevs, "PDF (*.pdf)")
        self.files = self.files[0]
        if self.files != "":
            doc = QtGui.QTextDocument()
            location = self.pathtemp + "/_temp.html"
            with open(location, "w") as f:
                f.write(self.editor.document().toHtml())
                f.close()
            html = open(location).read()
            doc.setHtml(html)
            if 'ANDROID_BOOTLOGO' in os.environ:
                pass
            else:
                printer = QtPrintSupport.QPrinter()
                printer.setOutputFileName(self.files)
                printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
                if self.orient == 1:
                    printer.setOrientation(QtPrintSupport.QPrinter.Landscape)
                    printer.setResolution(300)
                    printer.setPageSize(QtPrintSupport.QPrinter.A4)
                    printer.setPageMargins(30, 10, 10, 20, QtPrintSupport.QPrinter.Millimeter)
                    sizes = QtCore.QSizeF(1123, 794)
                else:
                    printer.setOrientation(QtPrintSupport.QPrinter.Portrait)
                    printer.setResolution(300)
                    printer.setPageSize(QtPrintSupport.QPrinter.A4)
                    printer.setPageMargins(30, 10, 10, 20, QtPrintSupport.QPrinter.Millimeter)
                    sizes = QtCore.QSizeF(794, 1123)
                doc.setPageSize(sizes)
                doc.print_(printer)
