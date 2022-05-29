# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets

class MyWindow(QtWidgets.QWidget):
    def uise (self):
        QtWidgets.QWidget.__init__(self)
        self.resize(300, 100)
    def closeEvent(self, e):
        result = QtWidgets.QMessageBox.question(self, "Подтверждение закрытия окна",
                                                "Вы действительно хотите закрыть окно?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
            QtWidgets.QWidget.closeEvent(self, e)
        else:
            e.ignore()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.uise()
    window.show()
    sys.exit(app.exec_())