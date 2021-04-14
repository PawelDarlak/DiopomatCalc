import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore



cls, wind = uic.loadUiType('E:\Python\DiopomatCalc\mwdDiopomat.ui')


class myMainWnd(cls, wind):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.statusBar.setStyleSheet("color : red")
        self.statusBar.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.statusBar.showMessage("ja")
        self.pushButton.installEventFilter(self)
 

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.label.setText("The toggle state is")
        self.label.adjustSize()
        print('button')
    
    # def on_pushButton_pressed(self):
    #     self.pushButton.hide()

    @pyqtSlot()
    def on_actionOpen_triggered(self):
        self.label.setText("Dupa")
        self.label.adjustSize()
        print('open')

    def on_pushButton_Entered(self, QEvent):
        print('mouse')

    def mouseMoveEvent(self, event):
        print('mouse event')
        
    def wheelEvent(self, event):
        print('mouse wheel')

    # def eventFilter(self, object, event):
    #     print('even filtr')
    #     return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = myMainWnd()
    mainWin.show()
    sys.exit(app.exec_())