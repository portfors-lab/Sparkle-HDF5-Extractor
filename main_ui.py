# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:/Users/Joel/Documents/Sparkle-HDF5-Extractor/main.ui'
#
# Created: Thu Oct 15 15:32:44 2015
#      by: PyQt4 UI code generator 4.10.4
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
        MainWindow.setEnabled(True)
        MainWindow.resize(420, 500)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_start = QtGui.QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName(_fromUtf8("pushButton_start"))
        self.horizontalLayout_2.addWidget(self.pushButton_start)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.lineEdit_file_name = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_file_name.setObjectName(_fromUtf8("lineEdit_file_name"))
        self.horizontalLayout_7.addWidget(self.lineEdit_file_name)
        self.pushButton_browse = QtGui.QPushButton(self.centralwidget)
        self.pushButton_browse.setObjectName(_fromUtf8("pushButton_browse"))
        self.horizontalLayout_7.addWidget(self.pushButton_browse)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.comboBox_test_num = QtGui.QComboBox(self.centralwidget)
        self.comboBox_test_num.setObjectName(_fromUtf8("comboBox_test_num"))
        self.comboBox_test_num.addItem(_fromUtf8(""))
        self.horizontalLayout_10.addWidget(self.comboBox_test_num)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.doubleSpinBox_threshold = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_threshold.setDecimals(4)
        self.doubleSpinBox_threshold.setMaximum(100.0)
        self.doubleSpinBox_threshold.setSingleStep(0.001)
        self.doubleSpinBox_threshold.setObjectName(_fromUtf8("doubleSpinBox_threshold"))
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_threshold)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.radioButton_normal = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_normal.setChecked(True)
        self.radioButton_normal.setObjectName(_fromUtf8("radioButton_normal"))
        self.horizontalLayout_8.addWidget(self.radioButton_normal)
        self.radioButton_inverse = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_inverse.setObjectName(_fromUtf8("radioButton_inverse"))
        self.horizontalLayout_8.addWidget(self.radioButton_inverse)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.checkBox_calibration = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_calibration.setObjectName(_fromUtf8("checkBox_calibration"))
        self.horizontalLayout_11.addWidget(self.checkBox_calibration)
        self.checkBox_spikes = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_spikes.setObjectName(_fromUtf8("checkBox_spikes"))
        self.horizontalLayout_11.addWidget(self.checkBox_spikes)
        self.checkBox_raw = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_raw.setObjectName(_fromUtf8("checkBox_raw"))
        self.horizontalLayout_11.addWidget(self.checkBox_raw)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_3.addWidget(self.textEdit)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_3.addWidget(self.progressBar)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.Title = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setObjectName(_fromUtf8("Title"))
        self.horizontalLayout.addWidget(self.Title)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Sparkle to CSV", None))
        self.pushButton_start.setText(_translate("MainWindow", "Start", None))
        self.label.setText(_translate("MainWindow", "Open:", None))
        self.pushButton_browse.setText(_translate("MainWindow", "Browse...", None))
        self.label_3.setText(_translate("MainWindow", "Test Number:", None))
        self.comboBox_test_num.setItemText(0, _translate("MainWindow", "All Tests", None))
        self.label_5.setText(_translate("MainWindow", "Threshold:", None))
        self.doubleSpinBox_threshold.setSuffix(_translate("MainWindow", " V", None))
        self.label_2.setText(_translate("MainWindow", "Threshold Type:", None))
        self.radioButton_normal.setText(_translate("MainWindow", "Normal", None))
        self.radioButton_inverse.setText(_translate("MainWindow", "Inverse", None))
        self.label_4.setText(_translate("MainWindow", "Export to CSV:", None))
        self.checkBox_calibration.setText(_translate("MainWindow", "Calibration", None))
        self.checkBox_spikes.setText(_translate("MainWindow", "Spike Times", None))
        self.checkBox_raw.setText(_translate("MainWindow", "Raw Data", None))
        self.Title.setText(_translate("MainWindow", "Sparkle HDF5 Extractor", None))

