import sys
import csv
import h5py
import json
import operator
import numpy as np

from PyQt4 import QtCore, QtGui
from main_ui import Ui_MainWindow
from itertools import islice, count


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.filename = ''
        self.threshold = 0
        self.h_file = h5py.File

        QtCore.QObject.connect(self.ui.pushButton_browse, QtCore.SIGNAL("clicked()"), self.browse)
        QtCore.QObject.connect(self.ui.pushButton_start, QtCore.SIGNAL("clicked()"), self.start)

    def browse(self):
        self.ui.comboBox_test_num.clear()

        QtGui.QFileDialog(self)
        self.filename = QtGui.QFileDialog.getOpenFileName()
        self.ui.lineEdit_file_name.setText(self.filename)

        # If the filename is not blank, attempt to extract test numbers and place them into the combobox
        if self.filename != '':
            self.h_file = h5py.File(unicode(self.filename), 'r')

            tests = {}
            for key in self.h_file.keys():
                if 'segment' in key:
                    for test in self.h_file[key].keys():
                        tests[test] = int(test.replace('test_', ''))

            sorted_tests = sorted(tests.items(), key=operator.itemgetter(1))

            for test in sorted_tests:
                self.ui.comboBox_test_num.addItem(test[0])

    def extract(self):
        filename = self.filename = self.ui.lineEdit_file_name.text()
        if filename != '':
            h_file = h5py.File(unicode(self.filename), 'r')

        # Check for extraction parameters
        if '.hdf5' in self.filename:
            pass
        else:
            self.ui.textEdit.append('Error: Must select a .hdf5 file.\n')
            return

        if not self.ui.checkBox_calibration.isChecked() and not self.ui.checkBox_spikes.isChecked() and not self.ui.checkBox_raw.isChecked():
            self.ui.textEdit.append('Error: Must select at least one type of export.\n')
            return

        if self.ui.doubleSpinBox_threshold.value() == 0:
            self.ui.textEdit.append('Warning: Threshold has a value of 0\n')

        # Display parameters
        self.ui.textEdit.append('File: ' + self.filename)
        self.ui.textEdit.append('Threshold: ' + str(self.ui.doubleSpinBox_threshold.value()) + ' V')
        self.ui.textEdit.append('Test: ' + self.ui.comboBox_test_num.currentText())
        threshold = self.ui.doubleSpinBox_threshold.value()
        extract_test = self.ui.comboBox_test_num.currentText()

        if self.ui.radioButton_normal.isChecked():
            self.ui.textEdit.append('Type: Normal')
            thresh_type = 'normal'
        elif self.ui.radioButton_inverse.isChecked():
            self.ui.textEdit.append('Type: Inverse')
            thresh_type = 'inverse'
        else:
            self.ui.textEdit.append('Type: Error')
            thresh_type = 'error'

        if self.ui.checkBox_calibration.isChecked():
            self.ui.textEdit.append('Export: Calibration')
            export_calibration = True
        else:
            export_calibration = False
        if self.ui.checkBox_spikes.isChecked():
            self.ui.textEdit.append('Export: Spike Times')
            export_spikes = True
        else:
            export_spikes = False
        if self.ui.checkBox_raw.isChecked():
            self.ui.textEdit.append('Export: Raw Data')
            export_raw = True
        else:
            export_raw = False

        self.ui.textEdit.append('')

        if export_calibration:
            for key in h_file.keys():
                # If key is a calibration
                if 'calibration' in key:
                    # print 'Cal:', key

                    temp_filename = filename.replace('.hdf5', '_') + key + '.csv'
                    try:
                        cal_file = open(temp_filename, 'wb')
                    except IOError, e:
                        self.ui.textEdit.append('Unable to open ' + get_file_name(temp_filename))
                        self.ui.textEdit.append('Error ' + str(e.errno) + ': ' + e.strerror + '\n')
                    cal_writer = csv.writer(cal_file)

                    cal_writer.writerow([key])
                    for dataSet in h_file[key].keys():
                        # print '    ', dataSet
                        cal_writer.writerow(['', dataSet])
                        for attr in h_file[key][dataSet].attrs.items():
                            # print '    ', '    ', attr[0], ' ', attr[1]
                            cal_writer.writerow(['', '', attr[0]])
                            cal_writer.writerow(['', '', '', attr[1]])

                    cal_file.close()
                    self.ui.textEdit.append(key + ' Complete')

        # Print all of the samples
        np.set_printoptions(threshold='nan')

        # --------------------------------------------------------------------------------------------------------------

        if export_spikes:
            if 'inverse' in thresh_type:
                stats_file_name = filename.replace('.hdf5', '_') + extract_test + '_inverse_spikes(' + str(threshold) + 'V).csv'
            else:
                stats_file_name = filename.replace('.hdf5', '_') + extract_test + '_spikes(' + str(threshold) + 'V).csv'

            try:
                stats_file = open(stats_file_name, 'wb')
            except IOError, e:
                self.ui.textEdit.append('Unable to open ' + get_file_name(stats_file_name))
                self.ui.textEdit.append('Error ' + str(e.errno) + ': ' + e.strerror + '\n')
            stats_writer = csv.writer(stats_file)

            stats_writer.writerow(['File', filename])
            stats_writer.writerow(['Test', extract_test])
            stats_writer.writerow(['Threshold', threshold])
            stats_writer.writerow(['Type', thresh_type])
            stats_writer.writerow([])
            stats_writer.writerow(
                ['Segment', 'Test', 'Trace', 'Rep', 'Channel', '', 'Spikes', 'First Spike (ms)', '',
                 'Spike Times (ms)'])
            stats_writer.writerow([])

        for key in h_file.keys():

            # If key is a segment
            if 'segment' in key:
                seg_sample_rate = h_file[key].attrs['samplerate_ad']

                for test in h_file[key].keys():
                    if test == extract_test:

                        if export_raw:
                            if 'inverse' in thresh_type:
                                temp_filename = filename.replace('.hdf5', '_') + key + '_' + test + '_raw.csv'
                            else:
                                temp_filename = filename.replace('.hdf5', '_') + key + '_' + test + '_raw.csv'
                            try:
                                seg_file = open(temp_filename, 'wb')
                            except IOError, e:
                                self.ui.textEdit.append('Unable to open ' + get_file_name(temp_filename))
                                self.ui.textEdit.append('Error ' + str(e.errno) + ': ' + e.strerror + '\n')
                            seg_writer = csv.writer(seg_file)

                        if len(h_file[key][test].value.shape) > 3:
                            no_chan = False
                            traces = h_file[key][test].value.shape[0]
                            reps = h_file[key][test].value.shape[1]
                            channels = h_file[key][test].value.shape[2]
                            samples = h_file[key][test].value.shape[3]
                        else:
                            no_chan = True
                            traces = h_file[key][test].value.shape[0]
                            reps = h_file[key][test].value.shape[1]
                            channels = 1
                            samples = h_file[key][test].value.shape[2]

                        print no_chan

                        # Measured in seconds
                        window_duration = samples / seg_sample_rate
                        sample_length = window_duration / samples
                        # Convert to ms
                        sample_length_ms = sample_length * 1000
                        for trace in islice(count(1), traces):

                            # ----------------------------------------------------------------------------------

                            if key.replace('/', '') in h_file and 'stim' in h_file[key][test].attrs:
                                stimuli = json.loads(h_file[key][test].attrs['stim'])
                                stimulus = stimuli[trace - 1]
                                fs = stimulus['samplerate_da']
                            else:
                                fs = seg_sample_rate

                            # ----------------------------------------------------------------------------------

                            for rep in islice(count(1), reps):
                                for channel in islice(count(1), channels):
                                    if export_raw:

                                        if no_chan:
                                            seg_writer.writerow(
                                                [key.replace('segment_', 'seg_'), test, 'trace_' + str(trace),
                                                'rep_' + str(rep), 'chan_' + str(channel), ''] +
                                                h_file[key][test].value[trace - 1, rep - 1, :].tolist())
                                        else:
                                            seg_writer.writerow(
                                                [key.replace('segment_', 'seg_'), test, 'trace_' + str(trace),
                                                'rep_' + str(rep), 'chan_' + str(channel), ''] +
                                                h_file[key][test].value[trace - 1, rep - 1, channel - 1, :].tolist())

                                    if no_chan:
                                        signal = h_file[key][test].value[trace - 1, rep - 1, :]
                                    else:
                                        signal = h_file[key][test].value[trace - 1, rep - 1, channel - 1, :]

                                    if 'inverse' in thresh_type:
                                        signal[:] = [i * -1 for i in signal]

                                    spike_times = get_spike_times(signal, threshold, fs)
                                    spike_times[:] = [i * 1000 for i in spike_times]
                                    spike_count = len(spike_times)

                                    if spike_count == 0:
                                        first_spike = float('nan')
                                    else:
                                        first_spike = spike_times[0]

                                    if export_spikes:
                                        stats_writer.writerow(
                                            [key.replace('segment_', 'seg_'), test, 'trace_' + str(trace),
                                             'rep_' + str(rep), 'chan_' + str(channel), '', spike_count,
                                             first_spike, ''] + spike_times)

                                    reps_percent = (float(rep)) / reps
                                    traces_percent = (float(trace) - 1 + reps_percent) / traces
                                    string = test + ' {:7.2%}'.format(
                                        traces_percent) + ' ... ' + 'trace_{} {:4.0%}'.format(
                                        trace, reps_percent) + ' ... ' + 'rep_{}'.format(rep)

                                    self.ui.progressBar.setValue(traces_percent * 100)
                                    self.ui.textEdit.append(string)
                                    self.update()
                                    QtGui.qApp.processEvents()

                        if export_raw:
                            seg_file.close()
                        self.ui.textEdit.append(test + ' Complete\n')

        if export_spikes:
            stats_file.close()

        self.ui.textEdit.append('Extraction Complete\n')
        import subprocess

        explorer_open = 'explorer /root, ' + get_folder_path(str(filename))
        subprocess.Popen(explorer_open)

    def start(self):

        self.ui.progressBar.reset()
        QtCore.QTimer.singleShot(0, self.extract)


def get_folder_path(path):
    edit_path = path.replace('/', '\\')
    split_list = edit_path.split('\\')
    new_path = ''
    for item in split_list[:-1]:
        new_path = new_path + item + '\\'
    return new_path


def get_file_name(path):
    edit_path = path.replace('/', '\\')
    split_list = edit_path.split('\\')
    return split_list[-1]


def get_spike_times(signal, threshold, fs):
    times = []
    over, = np.where(signal > float(threshold))
    segments, = np.where(np.diff(over) > 1)

    if len(over) > 1:
        if len(segments) == 0:
            segments = [0, len(over) - 1]
        else:
            # add end points to sections for looping
            if segments[0] != 0:
                segments = np.insert(segments, [0], [0])
            else:
                # first point in singleton
                times.append(float(over[0]) / fs)
                if 1 not in segments:
                    # make sure that first point is in there
                    segments[0] = 1
            if segments[-1] != len(over) - 1:
                segments = np.insert(segments, [len(segments)], [len(over) - 1])
            else:
                times.append(float(over[-1]) / fs)

        for iseg in range(1, len(segments)):
            if segments[iseg] - segments[iseg - 1] == 1:
                # only single point over threshold
                idx = over[segments[iseg]]
            else:
                segments[0] = segments[0] - 1
                # find maximum of continuous set over max
                idx = over[segments[iseg - 1] + 1] + np.argmax(
                    signal[over[segments[iseg - 1] + 1]:over[segments[iseg]]])
            times.append(float(idx) / fs)
    elif len(over) == 1:
        times.append(float(over[0]) / fs)

    if len(times) > 0:
        refract = 0.002
        times_refract = []
        times_refract.append(times[0])
        for i in range(1, len(times)):
            if times_refract[-1] + refract <= times[i]:
                times_refract.append(times[i])
        return times_refract
    else:
        return times


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
