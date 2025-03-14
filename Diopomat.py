import sys, os
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QDialogButtonBox, QLabel, QVBoxLayout, QMainWindow
from PyQt5.QtCore import pyqtSlot 
from PyQt5.QtGui import QIcon
from mydicom import LoadDCM, ProcessChart, PoreSize
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
        try:
            path = resource_path("mwdDiopomat.ui")
            fileh = QtCore.QFile(path)
            fileh.open(QtCore.QFile.ReadOnly)
            uic.loadUi(fileh, self)
            fileh.close()
        except Exception as e:
            logging.error(f"Failed to load UI file: {e}")
        
        try:
            path = resource_path('icon.png')
            self.setWindowIcon(QIcon(path))
        except Exception as e:
            logging.error(f"Failed to set window icon: {e}")

        self.statusBar.setStyleSheet("color : red")
        self.statusBar.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.statusBar.showMessage("Diopomat: 1.01")
 
    @pyqtSlot()
    def on_pushButton_clicked(self):
        # me = DCMSlideClass()
        # me.nic()
        self.FileName.setText("The toggle state is")
        self.FileName.adjustSize()
        logging.info('Button clicked')
        
        self.FileNamelineEdit.setText("dupa")

        dlg = CustomDialog()  # If you pass self, the dialog will be centered over the main window as before.
        if dlg.exec_():
            logging.info("Dialog accepted")
        else:
            logging.info("Dialog rejected")
    
    # def on_pushButton_pressed(self):
    # self.pushButton.hide()

    @pyqtSlot()
    def on_actionImport_triggered(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Image DICOM (*.dcm)", options=options)
        if fileName:
            try:
                PoreSize.ShowDCM(fileName)
                logging.info(f"Imported file: {fileName}")
            except Exception as e:
                logging.error(f"Failed to import file: {e}")

    @pyqtSlot()
    def on_actionImport_data_triggered(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Image DICOM (*.dcm)", options=options)
        if fileName:
            try:
                PoreSize.ShowDCM(fileName)
                logging.info(f"Imported data file: {fileName}")
            except Exception as e:
                logging.error(f"Failed to import data file: {e}")
        
    def on_pushButton_Entered(self, QEvent):
        logging.info('Mouse entered button area')
        

    def mouseMoveEvent(self, event):
        logging.info('Mouse move event')
        
    def wheelEvent(self, event):
        logging.info('Mouse wheel event')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    logging.info('Run program...')
    mainWin = myMainWnd()
    mainWin.show()
    sys.exit(app.exec_())

