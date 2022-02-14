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
    def __init__(self, titles):
        QtWidgets.QDialog.__init__(self)
        self.setFixedSize(960, 600)
        self.resolution = QtWidgets.QDesktopWidget().screenGeometry()
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
        self.editor.textChanged.connect(self.handleTextChanged)
        self.buttonOpen = QtWidgets.QPushButton('В pdf', self)
        self.buttonOpen.clicked.connect(self.topdf)
        self.buttonPrint = QtWidgets.QPushButton('Друкувати', self)
        self.buttonPrint.clicked.connect(self.handlePrint)
        self.buttonPreview = QtWidgets.QPushButton('Переглянути', self)
        self.buttonPreview.clicked.connect(self.handlePreview)
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self.editor, 0, 0, 1, 3)
        layout.addWidget(self.buttonOpen, 1, 0)
        layout.addWidget(self.buttonPrint, 1, 1)
        layout.addWidget(self.buttonPreview, 1, 2)
        self.handleTextChanged()

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
            else:
                printerd.setOrientation(QtPrintSupport.QPrinter.Portrait)
            printerd.setResolution(100)
            printerd.setPageSize(QtPrintSupport.QPrinter.A4)
            printerd.setPageMargins(30,20,10,20, QtPrintSupport.QPrinter.Millimeter)
            dialog = QtPrintSupport.QPrintDialog(printerd,self)
            dialog.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint)
            dialog.setWindowIcon(icon)
            doc.setPageSize(QtCore.QSizeF(printerd.pageRect().size()))
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
            printerd = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.ScreenResolution)
            printerd.setPageSize(QtPrintSupport.QPrinter.A4)
            if self.orient == 1:
                printerd.setOrientation(QtPrintSupport.QPrinter.Landscape)
            else:
                printerd.setOrientation(QtPrintSupport.QPrinter.Portrait)
            printerd.setResolution(100)
            printerd.setPageMargins(30,20,10,20, QtPrintSupport.QPrinter.Millimeter)
            dialog = QtPrintSupport.QPrintPreviewDialog(printerd,self)
            dialog.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint)
            dialog.setWindowIcon(icon)
            doc.setPageSize(QtCore.QSizeF(printerd.pageRect().size()))
            dialog.paintRequested.connect(doc.print_)
            dialog.exec_()

    def handleTextChanged(self):
        enable = not self.editor.document().isEmpty()
        self.buttonPrint.setEnabled(enable)
        self.buttonPreview.setEnabled(enable)

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
            html = open(location).read()
            doc.setHtml(html)
            if 'ANDROID_BOOTLOGO' in os.environ:
                pass
            else:
                printer = QtPrintSupport.QPrinter()
                printer.setOutputFileName(self.files)
                printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
                printer.setPageSize(QtPrintSupport.QPrinter.A4)
                if self.orient == 1:
                    printer.setOrientation(QtPrintSupport.QPrinter.Landscape)
                else:
                    printer.setOrientation(QtPrintSupport.QPrinter.Portrait)
                printer.setPageMargins(30, 20, 10, 20, QtPrintSupport.QPrinter.Millimeter)
                doc.setPageSize(QtCore.QSizeF(printer.pageRect().size()))
                doc.print_(printer)
