from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import pyqtSlot
import sys


cls, wind = uic.loadUiType('E:\Python\DiopomatCalc\mwdDiopomat.ui')


class myWnd(cls, wind):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.statusBar.setStyleSheet("color : red")
        self.statusBar.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.statusBar.showMessage("ja")

    @pyqtSlot()
    def on_pushButton_clicked(self):
        print('button')
    
    # def on_pushButton_pressed(self):
    #     self.pushButton.hide()
      

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = myWnd()
    mainWin.show()
    sys.exit(app.exec_())