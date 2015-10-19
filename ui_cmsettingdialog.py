# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CmSettingDialog.ui'
#
# Created: Mon Oct 19 12:56:29 2015
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

class Ui_DialogColorMapSetting(object):
    def setupUi(self, DialogColorMapSetting):
        DialogColorMapSetting.setObjectName(_fromUtf8("DialogColorMapSetting"))
        DialogColorMapSetting.resize(398, 325)
        DialogColorMapSetting.setSizeGripEnabled(False)
        self.gridLayout = QtGui.QGridLayout(DialogColorMapSetting)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(DialogColorMapSetting)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)
        self.frame = QtGui.QFrame(DialogColorMapSetting)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_gamma = QtGui.QLineEdit(self.frame)
        self.lineEdit_gamma.setObjectName(_fromUtf8("lineEdit_gamma"))
        self.horizontalLayout.addWidget(self.lineEdit_gamma)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(DialogColorMapSetting)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.radioButtonCmGray = QtGui.QRadioButton(self.groupBox)
        self.radioButtonCmGray.setObjectName(_fromUtf8("radioButtonCmGray"))
        self.gridLayout_2.addWidget(self.radioButtonCmGray, 0, 0, 1, 1)
        self.radioButtonCmJet = QtGui.QRadioButton(self.groupBox)
        self.radioButtonCmJet.setObjectName(_fromUtf8("radioButtonCmJet"))
        self.gridLayout_2.addWidget(self.radioButtonCmJet, 0, 1, 1, 1)
        self.radioButtonCmHot = QtGui.QRadioButton(self.groupBox)
        self.radioButtonCmHot.setObjectName(_fromUtf8("radioButtonCmHot"))
        self.gridLayout_2.addWidget(self.radioButtonCmHot, 1, 0, 1, 1)
        self.radioButtonCmSpectral = QtGui.QRadioButton(self.groupBox)
        self.radioButtonCmSpectral.setObjectName(_fromUtf8("radioButtonCmSpectral"))
        self.gridLayout_2.addWidget(self.radioButtonCmSpectral, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)

        self.retranslateUi(DialogColorMapSetting)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogColorMapSetting.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogColorMapSetting.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogColorMapSetting)

    def retranslateUi(self, DialogColorMapSetting):
        DialogColorMapSetting.setWindowTitle(_translate("DialogColorMapSetting", "Color Map Setting", None))
        self.frame.setToolTip(_translate("DialogColorMapSetting", "Lower for enhance small signal difference, higher for enghance large signal difference", None))
        self.label.setText(_translate("DialogColorMapSetting", "Color Map Gamma :             ", None))
        self.groupBox.setTitle(_translate("DialogColorMapSetting", "Color Map Type", None))
        self.radioButtonCmGray.setText(_translate("DialogColorMapSetting", "Gray", None))
        self.radioButtonCmJet.setText(_translate("DialogColorMapSetting", "Jet", None))
        self.radioButtonCmHot.setText(_translate("DialogColorMapSetting", "Hot", None))
        self.radioButtonCmSpectral.setText(_translate("DialogColorMapSetting", "Spectral", None))

