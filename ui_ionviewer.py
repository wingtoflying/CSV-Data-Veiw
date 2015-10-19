# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IonViewer.ui'
#
# Created: Mon Oct 19 15:33:32 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1035, 714)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.listWidget = QtGui.QListWidget(self.splitter_2)
        self.listWidget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.listWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.splitter = QtGui.QSplitter(self.splitter_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.mplwidget_up = MatplotlibWidget(self.splitter)
        self.mplwidget_up.setObjectName(_fromUtf8("mplwidget_up"))
        self.mplwidget_down = MatplotlibWidget(self.splitter)
        self.mplwidget_down.setObjectName(_fromUtf8("mplwidget_down"))
        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1035, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSetting = QtGui.QMenu(self.menubar)
        self.menuSetting.setObjectName(_fromUtf8("menuSetting"))
        self.menuCopy = QtGui.QMenu(self.menubar)
        self.menuCopy.setObjectName(_fromUtf8("menuCopy"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_File = QtGui.QAction(MainWindow)
        self.actionLoad_File.setObjectName(_fromUtf8("actionLoad_File"))
        self.actionLoad_Folder = QtGui.QAction(MainWindow)
        self.actionLoad_Folder.setObjectName(_fromUtf8("actionLoad_Folder"))
        self.actionClean_Load_File = QtGui.QAction(MainWindow)
        self.actionClean_Load_File.setObjectName(_fromUtf8("actionClean_Load_File"))
        self.actionRange = QtGui.QAction(MainWindow)
        self.actionRange.setObjectName(_fromUtf8("actionRange"))
        self.actionColorMapSettingDialog = QtGui.QAction(MainWindow)
        self.actionColorMapSettingDialog.setObjectName(_fromUtf8("actionColorMapSettingDialog"))
        self.actionNormalize_by_DV = QtGui.QAction(MainWindow)
        self.actionNormalize_by_DV.setObjectName(_fromUtf8("actionNormalize_by_DV"))
        self.actionCopy_Image = QtGui.QAction(MainWindow)
        self.actionCopy_Image.setObjectName(_fromUtf8("actionCopy_Image"))
        self.actionCopy_Slice = QtGui.QAction(MainWindow)
        self.actionCopy_Slice.setObjectName(_fromUtf8("actionCopy_Slice"))
        self.menuFile.addAction(self.actionLoad_File)
        self.menuFile.addAction(self.actionLoad_Folder)
        self.menuFile.addAction(self.actionClean_Load_File)
        self.menuSetting.addAction(self.actionColorMapSettingDialog)
        self.menuCopy.addAction(self.actionCopy_Image)
        self.menuCopy.addAction(self.actionCopy_Slice)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuCopy.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Ion Viewer", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting", None))
        self.menuCopy.setTitle(_translate("MainWindow", "Copy", None))
        self.actionLoad_File.setText(_translate("MainWindow", "Load File", None))
        self.actionLoad_Folder.setText(_translate("MainWindow", "Load Folder", None))
        self.actionClean_Load_File.setText(_translate("MainWindow", "Clean Load File", None))
        self.actionRange.setText(_translate("MainWindow", "Range", None))
        self.actionColorMapSettingDialog.setText(_translate("MainWindow", "Color Map", None))
        self.actionNormalize_by_DV.setText(_translate("MainWindow", "Normalize by DV", None))
        self.actionCopy_Image.setText(_translate("MainWindow", "Copy Image", None))
        self.actionCopy_Slice.setText(_translate("MainWindow", "Copy Slice", None))

from matplotlibwidget import MatplotlibWidget
