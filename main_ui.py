# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:/Users/Joel/Documents/Sparkle-HDF5-Extractor/main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("horsey.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout_8.addWidget(self.progressBar, 7, 0, 1, 3)
        self.pushButton_browse = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_browse.sizePolicy().hasHeightForWidth())
        self.pushButton_browse.setSizePolicy(sizePolicy)
        self.pushButton_browse.setObjectName(_fromUtf8("pushButton_browse"))
        self.gridLayout_8.addWidget(self.pushButton_browse, 1, 2, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout_8.addWidget(self.textEdit, 6, 0, 1, 3)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_8.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_file_name = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_file_name.setObjectName(_fromUtf8("lineEdit_file_name"))
        self.gridLayout_8.addWidget(self.lineEdit_file_name, 1, 0, 1, 2)
        self.horizontalLayout_polarity = QtGui.QHBoxLayout()
        self.horizontalLayout_polarity.setObjectName(_fromUtf8("horizontalLayout_polarity"))
        self.groupBox_polarity = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_polarity.setFont(font)
        self.groupBox_polarity.setFlat(True)
        self.groupBox_polarity.setObjectName(_fromUtf8("groupBox_polarity"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_polarity)
        self.gridLayout_4.setContentsMargins(-1, 5, -1, 5)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.radioButton_normal = QtGui.QRadioButton(self.groupBox_polarity)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.radioButton_normal.setFont(font)
        self.radioButton_normal.setChecked(True)
        self.radioButton_normal.setObjectName(_fromUtf8("radioButton_normal"))
        self.gridLayout_4.addWidget(self.radioButton_normal, 0, 0, 1, 1)
        self.radioButton_inverse = QtGui.QRadioButton(self.groupBox_polarity)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.radioButton_inverse.setFont(font)
        self.radioButton_inverse.setObjectName(_fromUtf8("radioButton_inverse"))
        self.gridLayout_4.addWidget(self.radioButton_inverse, 0, 1, 1, 1)
        self.horizontalLayout_polarity.addWidget(self.groupBox_polarity)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_polarity.addItem(spacerItem1)
        self.gridLayout_8.addLayout(self.horizontalLayout_polarity, 3, 0, 1, 2)
        self.horizontalLayout_threshold = QtGui.QHBoxLayout()
        self.horizontalLayout_threshold.setObjectName(_fromUtf8("horizontalLayout_threshold"))
        self.groupBox_threshold = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_threshold.setFont(font)
        self.groupBox_threshold.setFlat(True)
        self.groupBox_threshold.setObjectName(_fromUtf8("groupBox_threshold"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_threshold)
        self.gridLayout_6.setContentsMargins(-1, 5, -1, 5)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.pushButton_auto_threshold = QtGui.QPushButton(self.groupBox_threshold)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_auto_threshold.setFont(font)
        self.pushButton_auto_threshold.setObjectName(_fromUtf8("pushButton_auto_threshold"))
        self.gridLayout_6.addWidget(self.pushButton_auto_threshold, 0, 2, 1, 1)
        self.doubleSpinBox_threshold = QtGui.QDoubleSpinBox(self.groupBox_threshold)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.doubleSpinBox_threshold.setFont(font)
        self.doubleSpinBox_threshold.setDecimals(4)
        self.doubleSpinBox_threshold.setMaximum(100.0)
        self.doubleSpinBox_threshold.setSingleStep(0.001)
        self.doubleSpinBox_threshold.setObjectName(_fromUtf8("doubleSpinBox_threshold"))
        self.gridLayout_6.addWidget(self.doubleSpinBox_threshold, 0, 1, 1, 1)
        self.horizontalLayout_threshold.addWidget(self.groupBox_threshold)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_threshold.addItem(spacerItem2)
        self.gridLayout_8.addLayout(self.horizontalLayout_threshold, 4, 0, 1, 2)
        self.horizontalLayout_export = QtGui.QHBoxLayout()
        self.horizontalLayout_export.setObjectName(_fromUtf8("horizontalLayout_export"))
        self.groupBox_export = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_export.setFont(font)
        self.groupBox_export.setFlat(True)
        self.groupBox_export.setObjectName(_fromUtf8("groupBox_export"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_export)
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.checkBox_calibration = QtGui.QCheckBox(self.groupBox_export)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_calibration.setFont(font)
        self.checkBox_calibration.setObjectName(_fromUtf8("checkBox_calibration"))
        self.gridLayout_2.addWidget(self.checkBox_calibration, 0, 0, 1, 1)
        self.checkBox_spikes = QtGui.QCheckBox(self.groupBox_export)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_spikes.setFont(font)
        self.checkBox_spikes.setObjectName(_fromUtf8("checkBox_spikes"))
        self.gridLayout_2.addWidget(self.checkBox_spikes, 0, 1, 1, 1)
        self.checkBox_raw = QtGui.QCheckBox(self.groupBox_export)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_raw.setFont(font)
        self.checkBox_raw.setObjectName(_fromUtf8("checkBox_raw"))
        self.gridLayout_2.addWidget(self.checkBox_raw, 0, 2, 1, 1)
        self.horizontalLayout_export.addWidget(self.groupBox_export)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_export.addItem(spacerItem3)
        self.gridLayout_8.addLayout(self.horizontalLayout_export, 5, 0, 1, 2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.groupBox_test = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_test.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_test.setFont(font)
        self.groupBox_test.setFlat(True)
        self.groupBox_test.setObjectName(_fromUtf8("groupBox_test"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_test)
        self.gridLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.comboBox_test_num = QtGui.QComboBox(self.groupBox_test)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_test_num.sizePolicy().hasHeightForWidth())
        self.comboBox_test_num.setSizePolicy(sizePolicy)
        self.comboBox_test_num.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox_test_num.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_test_num.setFont(font)
        self.comboBox_test_num.setObjectName(_fromUtf8("comboBox_test_num"))
        self.gridLayout_3.addWidget(self.comboBox_test_num, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBox_test)
        self.groupBox_channel = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_channel.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_channel.setFont(font)
        self.groupBox_channel.setFlat(True)
        self.groupBox_channel.setObjectName(_fromUtf8("groupBox_channel"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_channel)
        self.gridLayout_5.setContentsMargins(-1, 5, -1, 5)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.comboBox_channel = QtGui.QComboBox(self.groupBox_channel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_channel.sizePolicy().hasHeightForWidth())
        self.comboBox_channel.setSizePolicy(sizePolicy)
        self.comboBox_channel.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox_channel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_channel.setFont(font)
        self.comboBox_channel.setObjectName(_fromUtf8("comboBox_channel"))
        self.gridLayout_5.addWidget(self.comboBox_channel, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBox_channel)
        self.groupBox_comments = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_comments.setFont(font)
        self.groupBox_comments.setFlat(True)
        self.groupBox_comments.setObjectName(_fromUtf8("groupBox_comments"))
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox_comments)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.lineEdit_comments = QtGui.QLineEdit(self.groupBox_comments)
        self.lineEdit_comments.setEnabled(True)
        self.lineEdit_comments.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_comments.setFont(font)
        self.lineEdit_comments.setReadOnly(True)
        self.lineEdit_comments.setObjectName(_fromUtf8("lineEdit_comments"))
        self.gridLayout_7.addWidget(self.lineEdit_comments, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBox_comments)
        self.gridLayout_8.addLayout(self.horizontalLayout_3, 2, 0, 1, 3)
        self.gridLayout.addLayout(self.gridLayout_8, 2, 0, 1, 1)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Sparkle HDF5 Extractor", None))
        self.pushButton_start.setText(_translate("MainWindow", "Start", None))
        self.pushButton_browse.setText(_translate("MainWindow", "Browse...", None))
        self.label.setText(_translate("MainWindow", "Open:", None))
        self.groupBox_polarity.setTitle(_translate("MainWindow", "Response Polarity ", None))
        self.radioButton_normal.setText(_translate("MainWindow", "Normal", None))
        self.radioButton_inverse.setText(_translate("MainWindow", "Inverse", None))
        self.groupBox_threshold.setTitle(_translate("MainWindow", "Threshold ", None))
        self.pushButton_auto_threshold.setText(_translate("MainWindow", "Estimate Threshold", None))
        self.doubleSpinBox_threshold.setSuffix(_translate("MainWindow", " V", None))
        self.groupBox_export.setTitle(_translate("MainWindow", "Export to CSV ", None))
        self.checkBox_calibration.setText(_translate("MainWindow", "Calibration", None))
        self.checkBox_spikes.setText(_translate("MainWindow", "Spike Times", None))
        self.checkBox_raw.setText(_translate("MainWindow", "Raw Data", None))
        self.groupBox_test.setTitle(_translate("MainWindow", "Test Number ", None))
        self.groupBox_channel.setTitle(_translate("MainWindow", "Channel ", None))
        self.groupBox_comments.setTitle(_translate("MainWindow", "Comments ", None))

