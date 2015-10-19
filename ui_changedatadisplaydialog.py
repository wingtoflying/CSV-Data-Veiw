# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChangeDataDisplayDialog.ui'
#
# Created: Mon Oct 19 15:04:24 2015
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

class Ui_DialogChangeDataRange(object):
    def setupUi(self, DialogChangeDataRange):
        DialogChangeDataRange.setObjectName(_fromUtf8("DialogChangeDataRange"))
        DialogChangeDataRange.resize(567, 214)
        self.verticalLayout = QtGui.QVBoxLayout(DialogChangeDataRange)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(DialogChangeDataRange)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_i_start = QtGui.QLineEdit(self.frame)
        self.lineEdit_i_start.setObjectName(_fromUtf8("lineEdit_i_start"))
        self.horizontalLayout.addWidget(self.lineEdit_i_start)
        self.label_i_max = QtGui.QLabel(self.frame)
        self.label_i_max.setObjectName(_fromUtf8("label_i_max"))
        self.horizontalLayout.addWidget(self.label_i_max)
        self.lineEdit_i_end = QtGui.QLineEdit(self.frame)
        self.lineEdit_i_end.setObjectName(_fromUtf8("lineEdit_i_end"))
        self.horizontalLayout.addWidget(self.lineEdit_i_end)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(DialogChangeDataRange)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_j_start = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_j_start.setObjectName(_fromUtf8("lineEdit_j_start"))
        self.horizontalLayout_2.addWidget(self.lineEdit_j_start)
        self.label_j_max = QtGui.QLabel(self.frame_2)
        self.label_j_max.setObjectName(_fromUtf8("label_j_max"))
        self.horizontalLayout_2.addWidget(self.label_j_max)
        self.lineEdit_j_end = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_j_end.setObjectName(_fromUtf8("lineEdit_j_end"))
        self.horizontalLayout_2.addWidget(self.lineEdit_j_end)
        self.verticalLayout.addWidget(self.frame_2)
        self.buttonBox = QtGui.QDialogButtonBox(DialogChangeDataRange)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogChangeDataRange)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogChangeDataRange.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogChangeDataRange.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogChangeDataRange)

    def retranslateUi(self, DialogChangeDataRange):
        DialogChangeDataRange.setWindowTitle(_translate("DialogChangeDataRange", "Change Data Display Range", None))
        self.label.setText(_translate("DialogChangeDataRange", "Display row data  from  (minimum 0):     ", None))
        self.label_i_max.setText(_translate("DialogChangeDataRange", "to (maximun 10)", None))
        self.label_3.setText(_translate("DialogChangeDataRange", "Display column data  from  (minimum 0):", None))
        self.label_j_max.setText(_translate("DialogChangeDataRange", "to (maximun 10)", None))

