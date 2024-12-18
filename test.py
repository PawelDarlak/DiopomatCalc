# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import QObject, pyqtSlot

# class Ui_MainWindow( QObject):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(482, 600)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
#         self.gridLayout.setObjectName("gridLayout")
#         self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
#         self.tabWidget.setObjectName("tabWidget")
#         self.tab = QtWidgets.QWidget()
#         self.tab.setObjectName("tab")
#         self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
#         self.gridLayout_2.setObjectName("gridLayout_2")
#         self.horizontalLayout = QtWidgets.QHBoxLayout()
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.clearButton = QtWidgets.QPushButton(self.tab)
#         self.clearButton.setObjectName("clearButton")
#         self.horizontalLayout.addWidget(self.clearButton)
#         self.EAXlineEdit = QtWidgets.QLineEdit(self.tab)
#         self.EAXlineEdit.setObjectName("EAXlineEdit")
#         self.horizontalLayout.addWidget(self.EAXlineEdit)
#         self.label = QtWidgets.QLabel(self.tab)
#         self.label.setObjectName("label")
#         self.horizontalLayout.addWidget(self.label)
#         spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
#         self.horizontalLayout.addItem(spacerItem)
#         self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
#         self.tabWidget.addTab(self.tab, "")
#         self.tab_2 = QtWidgets.QWidget()
#         self.tab_2.setObjectName("tab_2")
#         self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
#         self.gridLayout_4.setObjectName("gridLayout_4")
#         self.textEdit = QtWidgets.QTextEdit(self.tab_2)
#         self.textEdit.setObjectName("textEdit")
#         self.gridLayout_4.addWidget(self.textEdit, 0, 0, 1, 1)
#         self.gridLayout_3 = QtWidgets.QGridLayout()
#         self.gridLayout_3.setObjectName("gridLayout_3")
#         self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
#         self.horizontalLayout_2.setObjectName("horizontalLayout_2")
#         self.pushButton = QtWidgets.QPushButton(self.tab_2)
#         self.pushButton.setObjectName("pushButton")
#         self.horizontalLayout_2.addWidget(self.pushButton)
#         spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
#         self.horizontalLayout_2.addItem(spacerItem1)
#         self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.horizontalLayout_2.addWidget(self.pushButton_2)
#         self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
#         self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)
#         self.tabWidget.addTab(self.tab_2, "")
#         self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 482, 22))
#         self.menubar.setObjectName("menubar")
#         self.menuFile = QtWidgets.QMenu(self.menubar)
#         self.menuFile.setObjectName("menuFile")
#         self.menuQuit = QtWidgets.QMenu(self.menubar)
#         self.menuQuit.setObjectName("menuQuit")
#         self.menuHelp = QtWidgets.QMenu(self.menubar)
#         self.menuHelp.setObjectName("menuHelp")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#         self.actionSave_Program = QtWidgets.QAction(MainWindow)
#         self.actionSave_Program.setObjectName("actionSave_Program")
#         self.actionLoad_Program = QtWidgets.QAction(MainWindow)
#         self.actionLoad_Program.setObjectName("actionLoad_Program")
#         self.menuFile.addAction(self.actionSave_Program)
#         self.menuFile.addAction(self.actionLoad_Program)
#         self.menubar.addAction(self.menuFile.menuAction())
#         self.menubar.addAction(self.menuQuit.menuAction())
#         self.menubar.addAction(self.menuHelp.menuAction())

#         self.retranslateUi(MainWindow)
#         self.tabWidget.setCurrentIndex(1)
#         self.clearButton.clicked.connect(self.EAXlineEdit.clear)
#         self.pushButton_2.clicked.connect( self.addRandomTextSlot)
#         self.pushButton.clicked.connect(self.textEdit.clear)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)

#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.clearButton.setText(_translate("MainWindow", "Clear"))
#         self.label.setText(_translate("MainWindow", "EAX"))
#         self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Processor"))
#         self.pushButton.setText(_translate("MainWindow", "Clear"))
#         self.pushButton_2.setText(_translate("MainWindow", "Random Text"))
#         self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Memory"))
#         self.menuFile.setTitle(_translate("MainWindow", "File"))
#         self.menuQuit.setTitle(_translate("MainWindow", "Quit"))
#         self.menuHelp.setTitle(_translate("MainWindow", "Help"))
#         self.actionSave_Program.setText(_translate("MainWindow", "Save Program"))
#         self.actionLoad_Program.setText(_translate("MainWindow", "Load Program"))

#     @pyqtSlot( )
#     def addRandomTextSlot( self ):
#         self.textEdit.insertPlainText( "Hello World!" )

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())


# 
# 
#  import matplotlib.pyplot as plt
# import matplotlib.transforms as mtransforms

# fig, ax = plt.subplots()
# ax.plot(range(10))
# ax.set_yticks((2, 5, 7))
# labels = ax.set_yticklabels(('really, really, really', 'long', 'labels'))

# def on_draw(event):
#     bboxes = []
#     for label in labels:
#         bbox = label.get_window_extent()
#         # the figure transform goes from relative coords->pixels and we
#         # want the inverse of that
#         bboxi = bbox.transformed(fig.transFigure.inverted())
#         bboxes.append(bboxi)
#     # the bbox that bounds all the bboxes, again in relative figure coords
#     bbox = mtransforms.Bbox.union(bboxes)
#     if fig.subplotpars.left < bbox.width:
#         # we need to move it over
#         fig.subplots_adjust(left=1.1*bbox.width)  # pad a little
#         fig.canvas.draw()

# fig.canvas.mpl_connect('draw_event', on_draw)

# plt.show()

# import matplotlib.pyplot as plt
# import pydicom
# from pydicom.data import get_testdata_files
# filename = "C855020546.dcm"
# import numpy as np


# ds = pydicom.dcmread(filename)

# if 'SamplesPerPixel' not in ds:
#     ds.SamplesPerPixel = 1

# array  = ds.pixel_array

# plt.imshow(array, cmap=plt.cm.bone)
# plt.show()