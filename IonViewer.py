import sys
import os
from PyQt4 import QtGui
from PyQt4 import QtCore
import matplotlib
from enum import Enum
from ui_ionviewer import Ui_MainWindow
from ui_cmsettingdialog import Ui_DialogColorMapSetting
from ui_changedatadisplaydialog import Ui_DialogChangeDataRange
import numpy as np
import skimage.exposure


class DataRangeShowSettingDialog(QtGui.QDialog, Ui_DialogChangeDataRange):

    def __init__(self, data_range, current_range, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.data_range = data_range
        self.label_i_max.setText("to (maximun %d)" % data_range[1])
        self.label_j_max.setText("to (maximun %d)" % data_range[3])
        self.lineEdit_i_start.setText(str(current_range[0]))
        self.lineEdit_i_end.setText(str(current_range[1]))
        self.lineEdit_j_start.setText(str(current_range[2]))
        self.lineEdit_j_end.setText(str(current_range[3]))
        self.custom_range = list(current_range)

    def accept(self):
        outrange_message = ''
        lineEdit_i_start = self.lineEdit_i_start.text()
        lineEdit_i_end = self.lineEdit_i_end.text()
        lineEdit_j_start = self.lineEdit_j_start.text()
        lineEdit_j_end = self.lineEdit_j_end.text()
        if not DataRangeShowSettingDialog.is_int(lineEdit_i_start):
            outrange_message += 'i start must be interger'
        else:
            if int(lineEdit_i_start) < 0:
                outrange_message += 'i start must larger than 0'
        if not DataRangeShowSettingDialog.is_int(lineEdit_j_start):
            outrange_message += 'j start must be interger'
        else:
            if int(lineEdit_j_start) < 0:
                outrange_message += 'j start must larger than 0'
        if not DataRangeShowSettingDialog.is_int(lineEdit_i_end):
            outrange_message += 'i end must be interger'
        else:
            if int(lineEdit_i_end) > self.data_range[1]:
                outrange_message += 'i end is larger than data'
            if int(lineEdit_i_end) < int(lineEdit_i_start):
                outrange_message += 'i end must larger than i start'
        if not DataRangeShowSettingDialog.is_int(lineEdit_j_end):
            outrange_message += 'i end must be interger'
        else:
            if int(lineEdit_j_end) > self.data_range[3]:
                outrange_message += 'j end is larger than data'
            if int(lineEdit_j_end) < int(lineEdit_j_start):
                outrange_message += 'j end must larger than j start'
        if outrange_message == '':
            # anything setting is correct
            self.custom_range[0] = int(self.lineEdit_i_start.text())
            self.custom_range[1] = int(self.lineEdit_i_end.text())
            self.custom_range[2] = int(self.lineEdit_j_start.text())
            self.custom_range[3] = int(self.lineEdit_j_end.text())
            QtGui.QDialog.accept(self)
#            return self.custom_range, QtGui.QDialog.Accepted
        else:
            QtGui.QMessageBox.information(self, u'ERROR', outrange_message)

    @staticmethod
    def is_int(s):
        try:
            int(s)
            return True
        except ValueError:
            return False


class IonItem(QtGui.QWidget):

    range_change_signal = QtCore.pyqtSignal()

    def __init__(self, filename, parent=None):
        # super(IonItem, self).__init__(parent)
        super(QtGui.QWidget, self).__init__(parent)
        self.loadcsv(str(filename))
        qdir = QtCore.QDir(filename)
        if qdir.isRelative():
            self.display_name = filename
        else:
            self.display_name = qdir.dirName()
        self.label = QtGui.QLabel()
        self.label.setText(self.display_name)
        print self.display_name
        self.layout = QtGui.QHBoxLayout()
        self.layout.addWidget(self.label, 0)
        self.setLayout(self.layout)
        self.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.action_change_range = QtGui.QAction('Change Range', self)
        self.action_change_range.triggered.connect(self.change_range_action)
        self.addAction(self.action_change_range)

    def loadcsv(self, filename):
        #  load data and set initial range to maximun data size
        filename = str(filename)
        rough = np.genfromtxt(filename, delimiter=',')
        self.cv = rough[1:, 0]
        self.dv = rough[0, 1:]
        self.data = rough[1:, 1:]
#        self.r_i = (0, self.data.shape[0])
#        self.r_j = (0, self.data.shape[1])
        self.data_range = (0, self.data.shape[0], 0, self.data.shape[1])
        self.data_show_range = list(self.data_range)

    def change_range(self, new_r):
        # new_r : x0 x1, y0, y1
        if (new_r[0] < 0 or new_r[3] > self.data.shape[1] or new_r[2] < 0
                or new_r[1] > self.data.shape[0] or new_r[0] > new_r[1] or
                new_r[2] > new_r[3]):
            raise ValueError('Range Setting Error')
        self.data_show_range = new_r
        self.range_change_signal.emit()

    def change_range_action(self):
        print 'Change Range'
        dialog = DataRangeShowSettingDialog(self.data_range,
                                            self.data_show_range, self)
        isOK = dialog.exec_()
        print isOK
        if isOK:
            self.change_range(dialog.custom_range)


class CMType(Enum):
    jet = 0
    gray = 1
    hot = 2
    spectral = 3


class CmSettingDialog(QtGui.QDialog, Ui_DialogColorMapSetting):

    def __init__(self, setting_data, change_cm_fun, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.cmtype = setting_data['cm_type']
        self.gamma = setting_data['gamma']
        self.setCMType_to_ratiobutton()
        self.lineEdit_gamma.setText(str(self.gamma))
        self.chang_cm_fun = change_cm_fun  # fucntion input (cmtype, gamma)

    def accept(self):
        # overload QDialog accept function
        # check gamma text is available
        if CmSettingDialog.is_float(self.lineEdit_gamma.text()):
            gamma = float(self.lineEdit_gamma.text())
            if 0 >= gamma:
                QtGui.QMessageBox.information(self, "ERROR",
                                              "Gamma must > 0")
                return False
        else:
            QtGui.QMessageBox.information(self, u'ERROR',
                                          u'Gamma must be float')
            return False
        # set setting
        self.cmtype = self.getCMType_from_ratiobutton()
        self.gamma = float(self.lineEdit_gamma.text())
        self.chang_cm_fun(self.cmtype, self.gamma)
        QtGui.QDialog.accept(self)

    def getCMType_from_ratiobutton(self):
        if self.radioButtonCmGray.isChecked():
            return CMType.gray
        elif self.radioButtonCmJet.isChecked():
            return CMType.jet
        elif self.radioButtonCmHot.isChecked():
            return CMType.hot
        elif self.radioButtonCmSpectral.isChecked():
            return CMType.spectral
        else:
            raise ValueError("Haven't select any cm type")

    def setCMType_to_ratiobutton(self):
        if self.cmtype == CMType.jet:
            self.radioButtonCmJet.setChecked(True)
        elif self.cmtype == CMType.gray:
            self.radioButtonCmGray.setChecked(True)
        elif self.cmtype == CMType.hot:
            self.radioButtonCmHot.setChecked(True)
        elif self.cmtype == CMType.spectral:
            self.radioButtonCmSpectral.setChecked(True)

    @staticmethod
    def is_float(s):
        try:
            float(s)
            return True
        except ValueError:
            return False


class IonViewer(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.listWidget.itemSelectionChanged.connect(self.selected_change)
        self.listWidget.clear()
        self.last_select_item = None
        self.actionLoad_File.triggered.connect(self.load_file_dialog)
        self.actionLoad_File.setShortcut('Ctrl+O')
        self.actionLoad_Folder.triggered.connect(
            self.load_file_in_floder_dialog)
        self.actionCopy_Image.triggered.connect(self.copy_mpl_up)
        self.actionCopy_Slice.triggered.connect(self.copy_mpl_down)
        self.actionColorMapSettingDialog.triggered.connect(
            self.action_show_cm_setting_dialog)
        self.actionClean_Load_File.triggered.connect(
            self.clean_loaded_file_list)
        load_setting = dict()
        self.visual_enhance = dict()
        self.displayDV = 0
        self.display_data = None
        self.click_cid = None
        self.im = None
        self.init_mouse_click()
        self.first_time_draw = True
        self.show_j_at_mpl_down = 0
        self.mpl_up_vline = None

        self.state_bar = QtGui.QStatusBar(self)
        self.splitter.addWidget(self.state_bar)
        self.statusbar.hide()

        self.qsettings = QtCore.QSettings('settings.ini',
                                          QtCore.QSettings.IniFormat)
        self.qsettings.setFallbacksEnabled(False)
        self.read_file_path = self.qsettings.value('filePath', '\home',
                                                   type=unicode)
        load_setting['gamma'] = self.qsettings.value('Gamma', 1, type=float)
        qsetting_cm_type_name = self.qsettings.value('cm_type', 'jet',
                                                     type=unicode)
        qsetting_cm_type = [n for n in CMType if n.name ==
                            qsetting_cm_type_name][0]
        load_setting['cm_type'] = qsetting_cm_type
        self.visual_enhance['HE'] = self.qsettings.value('Enhance_HE', False,
                                                         type=bool)
        self.actionHistogram_Equlaization.setChecked(
            self.visual_enhance['HE'])
        self.actionHistogram_Equlaization.triggered.connect(
            self.actionHistogram_Equlaization_change)
        # set cm
        self.cm = matplotlib.cm.get_cmap(load_setting['cm_type'].name)
        self.cm.set_gamma(load_setting['gamma'])
        # initial dialog with qsetting data
        self.cm_dialog = CmSettingDialog(load_setting, self.change_cm, self)

        self.setAcceptDrops(True)

    def closeEvent(self, e):
        # overwrite closeEvent for add save setting
        print 'Save setting'
        self.qsettings.setValue('filePath', self.read_file_path)
        self.qsettings.setValue('Gamma', self.cm_dialog.gamma)
        self.qsettings.setValue('cm_type', self.cm_dialog.cmtype.name)
        self.qsettings.setValue('Enhance_HE', self.visual_enhance['HE'])
        e.accept()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            for url in event.mimeData().urls():
                fname = str(url.toLocalFile())
                if 'csv' in fname:
                    self.loadfile(fname)
        else:
            event.setDropAction(QtCore.Qt.MoveAction)
            super(IonViewer, self).dropEvent(event)

    def actionHistogram_Equlaization_change(self, e):
        self.visual_enhance['HE'] =\
            self.actionHistogram_Equlaization.isChecked()
        self.selected_change()  # force redraw

    def loadfile(self, filename):
        print "Enter Load File Function  "
        new_item = IonItem(filename)
        qt_list_item = QtGui.QListWidgetItem(self.listWidget)
        qt_list_item.setSizeHint(new_item.sizeHint())
        self.listWidget.addItem(qt_list_item)
        self.listWidget.setItemWidget(qt_list_item, new_item)
#        self.show_img_up(new_item)

        # for test change cm
#        self.change_cm(CMType.gray, 2)

    def selected_change(self):
        print 'Select change'
        if self.last_select_item is not None:
            print "Disconnect change range signal from old item"
            print type(self.last_select_item)
            self.last_select_item.range_change_signal.disconnect(
                self.selcted_item_range_change)
        list_item = self.listWidget.currentItem()
        item = self.listWidget.itemWidget(list_item)
        self.show_img_up(item)
        item.range_change_signal.connect(self.selcted_item_range_change)
        self.last_select_item = item
        self.mpl_down_display(self.show_j_at_mpl_down)

    def selcted_item_range_change(self):
        print "Redraw range changed item"
        self.show_img_up(self.last_select_item)

    def change_cm(self, cm_type, gamma):
        print "Change CM with %s %f" % (cm_type.name, gamma)
        self.cm = matplotlib.cm.get_cmap(cm_type.name)
        self.cm.set_gamma(gamma)
        if self.im is not None:
            self.im.set_cmap(self.cm)
            self.im.autoscale()
            self.mplwidget_up.figure.canvas.draw()

    def action_show_cm_setting_dialog(self):
        self.cm_dialog.show()

    def init_mouse_click(self):
        def click_up(event):
            if self.display_data is not None and event.button == 1:
                cor_ax0 = self.mplwidget_up.axes.transAxes.inverted().\
                    transform((event.x, event.y))
                inAxis0 = 0 <= cor_ax0[0] < 1 and 0 <= cor_ax0[1] < 1
                if inAxis0:
                    dv_p = event.xdata
#                    data_j = int((dv_p - self.dv_r[0])/(self.dv_r[1] -
#                                 self.dv_r[0])*self.display_data.shape[1])
                    print 'Draw mpl down'
                    self.show_j_at_mpl_down = dv_p
                    self.mpl_down_display(dv_p)
                else:
                    pass

        def mouse_move(event):
            if self.display_data is not None:
                if event.inaxes:
                    cv_p = event.ydata
                    dv_p = event.xdata
                    data_i = int((cv_p - self.cv_r[0])/(self.cv_r[1] -
                                 self.cv_r[0])*self.display_data.shape[0])
                    data_j = int((dv_p - self.dv_r[0])/(self.dv_r[1] -
                                 self.dv_r[0])*self.display_data.shape[1])
                    ion_p = self.display_data[data_i, data_j]
                    self.state_bar.showMessage(" cv %d pv %d ion: %f" %
                                               (data_i, data_j, ion_p))
                else:
                    self.state_bar.clearMessage()
        self.click_cid = self.mplwidget_up.figure.canvas.mpl_connect(
            'button_press_event', click_up)
        self.movie_cid = self.mplwidget_up.figure.canvas.mpl_connect(
            'motion_notify_event', mouse_move)

    def mpl_down_display(self, dv_p):
        self.mplwidget_down.axes.cla()
        data_j = int((dv_p - self.dv_r[0])/(self.dv_r[1] -
                     self.dv_r[0])*self.display_data.shape[1])
        data_j = min(data_j, self.display_data.shape[1]-1)
        self.mplwidget_down.axes.plot(self.display_cv,
                                      self.display_data[:, data_j])
        self.mplwidget_down.axes.set_xlabel('CV')
        self.mplwidget_down.axes.set_ylabel('ion current')
        self.mplwidget_down.show()
        self.mplwidget_down.figure.canvas.draw()
        self.mpl_up_vline.set_xdata(self.show_j_at_mpl_down)
        self.mplwidget_up.figure.canvas.draw()

    def enhance_before_show(self, data):
        if self.visual_enhance['HE']:
            data = data/data.max()
            data_eq = skimage.exposure.equalize_hist(data)
            return data_eq
        return data

    def show_img_up(self, item):
        self.mplwidget_up.axes.cla()
        r_i = item.data_show_range[:2]
        r_j = item.data_show_range[2:]
        self.display_data = item.data[r_i[0]:r_i[1],
                                      r_j[0]:r_j[1]].copy()
        self.display_cv = item.cv[r_i[0]:r_i[1]]
        self.display_dv = item.cv[r_j[0]:r_j[1]]
        self.cv_r = item.cv[r_i[0]], item.cv[r_i[1] - 1]
        self.dv_r = item.dv[r_j[0]], item.dv[r_j[1] - 1]
        refine_data = self.enhance_before_show(self.display_data)
        self.im = self.mplwidget_up.axes.imshow(refine_data,
                                                interpolation='none',
                                                extent=list(self.dv_r +
                                                            self.cv_r),
                                                cmap=self.cm,
                                                aspect='auto')
        axes = self.mplwidget_up.axes
        if self.show_j_at_mpl_down == r_j[0]:
            self.show_j_at_mpl_down = (r_j[0] + r_j[1])/2
        self.mpl_up_vline = axes.axvline(x=self.show_j_at_mpl_down, c='r')
        axes.set_xlabel('DV')
        axes.set_ylabel('CV')
        if self.first_time_draw:
            self.cbar = self.mplwidget_up.figure.colorbar(self.im)
            self.first_time_draw = False
        else:
            self.im.autoscale()
            self.cbar.update_bruteforce(self.im)
        self.mplwidget_up.figure.canvas.updateGeometry()
#        self.mpl_up_vline = axes.axvline(x=20, c='r')
#        self.mplwidget_up.show()
        self.mplwidget_up.figure.canvas.draw()
#        QtGui.QMessageBox.information(self, "message", "Click111")

    def load_file_dialog(self):
        print "Load File Dialog Trigger  " + str(self.last_select_item)
        path = self.read_file_path
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                                                  path, 'csv file (*.csv)')
        if fname != u'':
            self.loadfile(fname)
            qdir = QtCore.QDir(fname)
            self.read_file_path = qdir.path()
            # record filepath for open same folder next time
            print self.read_file_path

    def load_file_in_floder_dialog(self):
        print "Load Folder Dialog Trigger"
        path = self.read_file_path
        folder = QtGui.QFileDialog.getExistingDirectory(self, 'Select Foler',
                                                        path)
        if folder != u'':
            file_list = os.listdir(folder)
            for fname in file_list:
                if 'csv' in fname:
                    self.loadfile(fname)
                    qdir = QtCore.QDir(fname)
                    self.read_file_path = qdir.path()

    def clean_loaded_file_list(self):
        print "Clean loaded file"
        self.listWidget.clear()  # must call before clean last_select_item
        if self.last_select_item is not None:
            print "Disconnect change range signal from old item for clean"
            self.last_select_item.range_change_signal.disconnect(
                self.selcted_item_range_change)
            self.last_select_item = None
        self.mplwidget_up.axes.cla()
        self.mpl_up_vline = None
        self.mplwidget_up.figure.canvas.draw()
        self.mplwidget_down.axes.cla()
        self.mplwidget_down.figure.canvas.draw()

    def copy_mpl_up(self):
        pixmap = QtGui.QPixmap.grabWidget(self.mplwidget_up)
        QtGui.QApplication.clipboard().setPixmap(pixmap)

    def copy_mpl_down(self):
        pixmap = QtGui.QPixmap.grabWidget(self.mplwidget_down)
        QtGui.QApplication.clipboard().setPixmap(pixmap)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = IonViewer()
    window.show()
#    window.loadfile('test_matrix.csv')
#    window.loadfile('test_matrix2.csv')
    sys.exit(app.exec_())
