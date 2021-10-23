import sys, os
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QDialogButtonBox, QLabel, QVBoxLayout, QMainWindow
from PyQt5.QtCore import pyqtSlot 
from PyQt5.QtGui import QIcon
from mydicom import LoadDCM, ProcessChart, PoreSize

#multifiles - to jest napisane z AGH

# Define function to import external files when using PyInstaller.
def resource_path(relative_path):
# Get absolute path to resource, works for dev and for PyInstaller
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS 
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("DioPomat !")
        QBtn = QDialogButtonBox.Close
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        # self.setWindowIcon(QIcon('icon.ico'))

class myMainWnd(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(myMainWnd, self).__init__(*args, **kwargs)
        path = resource_path("mwdDiopomat.ui")
        fileh = QtCore.QFile(path)
        fileh.open(QtCore.QFile.ReadOnly)
        uic.loadUi(fileh, self)
        fileh.close()
        
        path = resource_path('icon.png')
        self.setWindowIcon(QIcon(path))
        self.statusBar.setStyleSheet("color : red")
        self.statusBar.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.statusBar.showMessage("Diopomat: 1.01")
 

    @pyqtSlot()
    def on_pushButton_clicked(self):
        # me = DCMSlideClass()
        # me.nic()
        self.label.setText("The toggle state is")
        self.label.adjustSize()
        print('button')

        dlg = CustomDialog()  # If you pass self, the dialog will be centered over the main window as before.
        if dlg.exec_():
            print("Success!")
        else:
            print("Cancel!")
    
    # def on_pushButton_pressed(self):
    # self.pushButton.hide()

    @pyqtSlot()
    def on_actionImport_triggered(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Image DICOM (*.dcm)", options=options)

        PoreSize.ShowDCM(fileName)


    @pyqtSlot()
    def on_actionImport_data_triggered(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Image DICOM (*.dcm)", options=options)

        PoreSize.ShowDCM(fileName)
        
    def on_pushButton_Entered(self, QEvent):
        print('mouse')
        

    def mouseMoveEvent(self, event):
        print('mouse event')
        
    def wheelEvent(self, event):
        print('mouse wheel')

    # def eventFilter(self, object, event):
    #     print('even filtr')
    #     return False

#

if __name__ == "__main__":
    app = QApplication(sys.argv)
    print('Run program...')
    mainWin = myMainWnd()
    mainWin.show()
    sys.exit(app.exec_())


# import sys
# from PyQt5 import QtCore, QtWidgets
# from PyQt5.QtWidgets import QDialog, QMainWindow, QWidget, QPushButton, QAction, QFileDialog, QStatusBar, QLabel, QVBoxLayout
# from PyQt5.QtCore import QSize    
# from PyQt5.QtGui import QIcon, QWindow
# from mydicom import LoadDCM, ProcessChart, PoreSize
# # from PyQt5.uic import loadUiType


# boolLoadDCM = False
# filesDCM =[]


# class MainWindow(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         # self.setStyleSheet(appStyle)
#         self.w = None
#         self.initUI()

#     def initUI(self):
#         self.setMinimumSize(QSize(600, 300))    
#         self.setWindowTitle("DiopomatCalc") 
#         self.setWindowIcon(QIcon('icon.png'))

#         #Add statusbar
#         self.statusBar = QStatusBar()
#         self.setStatusBar(self.statusBar)
#         self.statusBar.setStyleSheet("background-color : grey")
#         self.statusBar.showMessage("this is status bar")
        

#         # Add button widget
#         pybutton = QPushButton('Pyqt', self)
#         # pybutton.clicked.connect(self.show_new_window)
#         pybutton.resize(100,32)
#         pybutton.move(130, 100)        
#         pybutton.setToolTip('This is a tooltip message.')  

#         # Create new action
#         newAction = QAction(QIcon('new.png'), '&New', self)        
#         newAction.setShortcut('Ctrl+N')
#         newAction.setStatusTip('New document')
#         newAction.triggered.connect(self.newCall)

#         # Create Import action
#         importAction = QAction(QIcon('import.png'), '&Import', self)        
#         importAction.setShortcut('Ctrl+I')
#         importAction.setStatusTip('Import dcm file')
#         importAction.triggered.connect(self.openCall)

#         # Create exit action
#         exitAction = QAction(QIcon('exit.png'), '&Exit', self)        
#         exitAction.setShortcut('Ctrl+Q')
#         exitAction.setStatusTip('Exit application')
#         exitAction.triggered.connect(self.exitCall)

#         # Create menu bar and add action
#         menuBar = self.menuBar()
#         fileMenu = menuBar.addMenu('&File')
#         fileMenu.addAction(newAction)
#         fileMenu.addAction(importAction)
#         fileMenu.addAction(exitAction)

#         # fileMenu = menuBar.addMenu('&View')
#         # fileMenu.addAction(exitAction)
#         self.setStyleSheet("""
#         QMenuBar {
#             background-color: rgb(49,49,49);
#             color: rgb(255,255,255);
#             border: 1px solid #000;
#         }

#         QMenuBar::item {
#             background-color: rgb(49,49,49);
#             color: rgb(255,255,255);
#         }

#         QMenuBar::item::selected {
#             background-color: rgb(30,30,30);
#         }

#         QMenu {
#             background-color: rgb(49,49,49);
#             color: rgb(255,255,255);
#             border: 1px solid #000;           
#         }

#         QMenu::item::selected {
#             background-color: rgb(30,30,30);
#         }
#     """)

#         # Create about action
#         aboutAction = QAction(QIcon('exit.png'), '&About', self)        
#         aboutAction.setShortcut('Ctrl+A')
#         aboutAction.setStatusTip('About...')
#         aboutAction.triggered.connect(self.exitCall)
#         aboutAction.triggered.connect(self.show_new_window)
        
#         aboutMenu = menuBar.addMenu('&About')
#         aboutMenu.addAction(aboutAction)

#     def openCall(self):
#         options = QFileDialog.Options()
#         options |= QFileDialog.DontUseNativeDialog
#         fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Image DICOM (*.dcm)", options=options)
#         if fileName:
#             print(fileName)

#         # filesDCM = PoreSize.LoadFileDCM(fileName)
#         PoreSize.ShowDCM(fileName)


#     def newCall(self):
#         print('New')

#     def exitCall(self):
#         print('Exit app')

#     def clickMethod(self):
#         print('PyQt')

#     def show_new_window(self, checked):
#         if self.w is None:
#             self.w = AnotherWindow()
#         self.w.show()


# class AnotherWindow(QDialog):
#     """
#     This "window" is a QWidget. If it has no parent, it
#     will appear as a free-floating window as we want.
#     """
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         self.setMinimumSize(QSize(600, 300))  
#         self.setWindowTitle("About") 
#         self.label = QLabel("Another Window")
#         layout.addWidget(self.label)
#         self.setLayout(layout)
#         pybutton = QPushButton('Pyqt', self)
#         # pybutton.clicked.connect(self.show_new_window)
#         pybutton.resize(100,32)
#         pybutton.move(130, 100)        
#         pybutton.setToolTip('This is a tooltip message.')  
#         self.setModal(True)
      

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     mainWin = MainWindow()
#     mainWin.show()
#     sys.exit(app.exec_())