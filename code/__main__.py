import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QMenuBar, QMenu, QToolBar, QStatusBar
from PyQt6.QtGui import QAction, QIcon

class Window(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("DiOPMatCALC")
        self.resize(400, 200)
        self.centralWidget = QLabel("Hello, World")
        self.centralWidget.setAlignment(Qt.Alignment.AlignCenter)
        self.setCentralWidget(self.centralWidget)
        self.setWindowIcon(QIcon('icon.png'))
        self._createActions()
        self._createToolBars()
        self._createstatusBar()
        self._createMenuBar()
        self.offset = None

    def _createMenuBar(self):
        menuBar = self.menuBar()
        # self.addToolBar("File")
        #  menuBar.setMovable(FALSE)
        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        # fileMenu.addAction(self.saveAction)
        # fileMenu.addAction(self.exitAction)

    def _createActions(self):
        # Creating action using the first constructor
        self.newAction = QAction(self)
        self.newAction.setText("&New")
        # Creating actions using the second constructor
        self.openAction = QAction("&Exit", self)
        #self.openAction.setText("&New")
        # self.saveAction = QAction("&Save", self)
        #self.exitAction = QAction("&Exit", self)
        # self.copyAction = QAction("&Copy", self)
        # self.pasteAction = QAction("&Paste", self)
        # self.cutAction = QAction("C&ut", self)
        # self.helpContentAction = QAction("&Help Content", self)
        # self.aboutAction = QAction("&About", self)

    def _createToolBars(self):
#         Using a title
        fileToolBar = self.addToolBar("File")
        fileToolBar.setMovable(False)
#         Using a QToolBar object
        editToolBar = QToolBar("Edit", self)
#         self.addToolBar(editToolBar)
#        Using a QToolBar object and a toolbar area
        helpToolBar = QToolBar("Help", self)
#         self.addToolBar(Qt.LeftToolBarArea, helpToolBar)

    def _createstatusBar(self):
        self.statusBar().showMessage('Message in statusbar.')
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
    