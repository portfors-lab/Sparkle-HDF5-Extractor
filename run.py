import sys
import csv
import h5py
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
        self.ui.comboBox_test_num.addItem('All Tests')

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
            self.ui.textEdit.append('Error: Threshold has a value of 0')

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
                    cal_file = open(temp_filename, 'wb')
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

        if export_spikes or export_raw:
            data_dict = {}
            first_spike_dict = {}
            spike_count_dict = {}
            spike_times_dict = {}

            if 'All Tests' in extract_test:
                stats_file_name = filename.replace('.hdf5', '_') + 'spikes.csv'

                stats_file = open(stats_file_name, 'wb')
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

                # Convert all tests
                key_count = -1
                key_total = len(h_file.keys())

                for key in h_file.keys():
                    key_count += 1

                    # If key is a segment
                    if 'segment' in key:
                        # print 'Seg:', key

                        seg_sample_rate = h_file[key].attrs['samplerate_ad']

                        test_count = -1
                        test_total = len(h_file[key].keys())

                        for test in h_file[key].keys():
                            test_count += 1

                            if export_raw:
                                temp_filename = filename + key + '_' + test + '_raw.csv'
                                seg_file = open(temp_filename, 'wb')
                                seg_writer = csv.writer(seg_file)

                                seg_writer.writerow([key.replace('segment_', 'seg_'), ''])
                                seg_writer.writerow(['', test])

                            traces = h_file[key][test].value.shape[0]
                            reps = h_file[key][test].value.shape[1]
                            channels = h_file[key][test].value.shape[2]
                            samples = h_file[key][test].value.shape[3]

                            # Measured in seconds
                            window_duration = samples / seg_sample_rate
                            sample_length = window_duration / samples
                            # Convert to ms
                            sample_length_ms = sample_length * 1000
                            for trace in islice(count(1), traces):
                                # print '    ', '    ', trace
                                if export_raw:
                                    seg_writer.writerow(['', '', 'trace_' + str(trace)])
                                for rep in islice(count(1), reps):
                                    # print '    ', '    ', '    ', rep
                                    if export_raw:
                                        seg_writer.writerow(['', '', '', 'rep_' + str(rep)])
                                    for channel in islice(count(1), channels):
                                        if export_raw:
                                            seg_writer.writerow(['', '', '', '', 'chan_' + str(channel)])
                                            seg_writer.writerow(
                                                ['', '', '', '', ''] + h_file[key][test].value[trace - 1, rep - 1,
                                                                       channel - 1,
                                                                       :].tolist())

                                        data_key = str(test) + '_trace_' + str(trace) + '_rep_' + str(
                                            rep) + '_chan_' + str(
                                            channel)
                                        data_dict[data_key] = h_file[key][test].value[trace - 1, rep - 1, channel - 1,
                                                              :].tolist()

                                        first_spike = False
                                        spike_size = 0
                                        spike_num = 0
                                        spike_count = 0
                                        sample_num = 0
                                        prev_volt = 0
                                        spike_times = []
                                        for sample in data_dict[data_key]:
                                            sample_num += 1

                                            if 'inverse' in thresh_type:
                                                # inverse threshold type
                                                if sample <= threshold:
                                                    if spike_size > sample:
                                                        spike_size = sample
                                                        spike_num = sample_num

                                                if sample > threshold:
                                                    if prev_volt <= threshold:
                                                        # spike just ended
                                                        if (spike_num * sample_length_ms) not in spike_times:
                                                            spike_count += 1
                                                            spike_times.append(spike_num * sample_length_ms)

                                                            if first_spike is False:
                                                                first_spike = True
                                                                first_spike_dict[
                                                                    data_key] = spike_num * sample_length_ms

                                                            spike_size = 0

                                                if (sample_num == len(data_dict[data_key])) and (sample <= threshold):
                                                    # spike just ended
                                                    spike_count += 1
                                                    spike_times.append(spike_num * sample_length_ms)

                                                    if first_spike is False:
                                                        first_spike = True
                                                        first_spike_dict[data_key] = spike_num * sample_length_ms

                                                    spike_size = 0
                                            else:
                                                # normal threshold type
                                                if sample >= threshold:
                                                    if spike_size < sample:
                                                        spike_size = sample
                                                        spike_num = sample_num

                                                if sample < threshold:
                                                    if prev_volt >= threshold:
                                                        # spike just ended
                                                        if (spike_num * sample_length_ms) not in spike_times:
                                                            spike_count += 1
                                                            spike_times.append(spike_num * sample_length_ms)

                                                            if first_spike is False:
                                                                first_spike = True
                                                                first_spike_dict[
                                                                    data_key] = spike_num * sample_length_ms

                                                            spike_size = 0

                                                if (sample_num == len(data_dict[data_key])) and (sample >= threshold):
                                                    # spike just ended
                                                    spike_count += 1
                                                    spike_times.append(spike_num * sample_length_ms)

                                                    if first_spike is False:
                                                        first_spike = True
                                                        first_spike_dict[data_key] = spike_num * sample_length_ms

                                                    spike_size = 0

                                            prev_volt = sample

                                        if data_key not in first_spike_dict:
                                            first_spike_dict[data_key] = float('nan')

                                        spike_count_dict[data_key] = spike_count
                                        spike_times_dict[data_key] = spike_times

                                        stats_writer.writerow(
                                            [key.replace('segment_', 'seg_'), test, 'trace_' + str(trace),
                                             'rep_' + str(rep),
                                             'chan_' + str(channel), '', spike_count_dict[data_key],
                                             first_spike_dict[data_key],
                                             ''] + spike_times_dict[data_key])

                                        reps_percent = (float(rep)) / reps
                                        traces_percent = (float(trace) - 1 + reps_percent) / traces
                                        tests_percent = (float(test_count) + traces_percent) / test_total
                                        segs_percent = (float(key_count) + tests_percent) / key_total
                                        string = 'Total ' + '{:7.2%}'.format(segs_percent) + ' ... ' + key.replace(
                                            'segment_', 'seg_') + '{:4.0%}'.format(
                                            tests_percent) + ' ... ' + test + '{:4.0%}'.format(
                                            traces_percent) + ' ... ' + 'trace_{} {:4.0%}'.format(trace,
                                            reps_percent) + ' ... ' + 'rep_{}'.format(rep)

                                        self.ui.progressBar.setValue(segs_percent * 100)
                                        self.ui.textEdit.append(string)
                                        self.update()
                                        QtGui.qApp.processEvents()

                                        # print dataKey
                                        # print 'spikeCount: ', spikeCountDict[dataKey]
                                        # print 'firstSpike: ', firstSpikeDict[dataKey]
                                        # print 'spikeTimes: ', spikeTimesDict[dataKey], '\n'

                            if export_raw:
                                seg_file.close()
                            self.ui.textEdit.append(test + ' Complete\n')

                    print ''

            else:
                stats_file_name = filename.replace('.hdf5', '_') + extract_test + '_spikes.csv'

                stats_file = open(stats_file_name, 'wb')
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
                        # print 'Seg:', key

                        seg_sample_rate = h_file[key].attrs['samplerate_ad']

                        for test in h_file[key].keys():
                            if test == extract_test:

                                if export_raw:
                                    temp_filename = filename.replace('.hdf5', '_') + key + '_' + test + '_raw.csv'
                                    seg_file = open(temp_filename, 'wb')
                                    seg_writer = csv.writer(seg_file)

                                    seg_writer.writerow([key.replace('segment_', 'seg_'), ''])
                                    seg_writer.writerow(['', test])

                                traces = h_file[key][test].value.shape[0]
                                reps = h_file[key][test].value.shape[1]
                                channels = h_file[key][test].value.shape[2]
                                samples = h_file[key][test].value.shape[3]

                                # Measured in seconds
                                window_duration = samples / seg_sample_rate
                                sample_length = window_duration / samples
                                # Convert to ms
                                sample_length_ms = sample_length * 1000
                                for trace in islice(count(1), traces):
                                    # print '    ', '    ', trace
                                    if export_raw:
                                        seg_writer.writerow(['', '', 'trace_' + str(trace)])
                                    for rep in islice(count(1), reps):
                                        # print '    ', '    ', '    ', rep
                                        if export_raw:
                                            seg_writer.writerow(['', '', '', 'rep_' + str(rep)])
                                        for channel in islice(count(1), channels):
                                            if export_raw:
                                                seg_writer.writerow(['', '', '', '', 'chan_' + str(channel)])
                                                seg_writer.writerow(
                                                    ['', '', '', '', ''] + h_file[key][test].value[trace - 1, rep - 1,
                                                                           channel - 1, :].tolist())

                                            data_key = str(test) + '_trace_' + str(trace) + '_rep_' + str(
                                                rep) + '_chan_' + str(
                                                channel)
                                            data_dict[data_key] = h_file[key][test].value[trace - 1, rep - 1,
                                                                  channel - 1,
                                                                  :].tolist()

                                            first_spike = False
                                            spike_size = 0
                                            spike_num = 0
                                            spike_count = 0
                                            sample_num = 0
                                            prev_volt = 0
                                            spike_times = []
                                            for sample in data_dict[data_key]:
                                                sample_num += 1

                                                if 'inverse' in thresh_type:
                                                    # inverse threshold type
                                                    if sample <= threshold:
                                                        if spike_size > sample:
                                                            spike_size = sample
                                                            spike_num = sample_num

                                                    if sample > threshold:
                                                        if prev_volt <= threshold:
                                                            # spike just ended
                                                            if (spike_num * sample_length_ms) not in spike_times:
                                                                spike_count += 1
                                                                spike_times.append(spike_num * sample_length_ms)

                                                                if first_spike is False:
                                                                    first_spike = True
                                                                    first_spike_dict[
                                                                        data_key] = spike_num * sample_length_ms

                                                                spike_size = 0

                                                    if (sample_num == len(data_dict[data_key])) and (
                                                                sample <= threshold):
                                                        # spike just ended
                                                        spike_count += 1
                                                        spike_times.append(spike_num * sample_length_ms)

                                                        if first_spike is False:
                                                            first_spike = True
                                                            first_spike_dict[data_key] = spike_num * sample_length_ms

                                                        spike_size = 0
                                                else:
                                                    # normal threshold type
                                                    if sample >= threshold:
                                                        if spike_size < sample:
                                                            spike_size = sample
                                                            spike_num = sample_num

                                                    if sample < threshold:
                                                        if prev_volt >= threshold:
                                                            # spike just ended
                                                            if (spike_num * sample_length_ms) not in spike_times:
                                                                spike_count += 1
                                                                spike_times.append(spike_num * sample_length_ms)

                                                                if first_spike is False:
                                                                    first_spike = True
                                                                    first_spike_dict[
                                                                        data_key] = spike_num * sample_length_ms

                                                                spike_size = 0

                                                    if (sample_num == len(data_dict[data_key])) and (
                                                                sample >= threshold):
                                                        # spike just ended
                                                        spike_count += 1
                                                        spike_times.append(spike_num * sample_length_ms)

                                                        if first_spike is False:
                                                            first_spike = True
                                                            first_spike_dict[data_key] = spike_num * sample_length_ms

                                                        spike_size = 0

                                                prev_volt = sample

                                            if data_key not in first_spike_dict:
                                                first_spike_dict[data_key] = float('nan')

                                            spike_count_dict[data_key] = spike_count
                                            spike_times_dict[data_key] = spike_times

                                            stats_writer.writerow(
                                                [key.replace('segment_', 'seg_'), test, 'trace_' + str(trace),
                                                 'rep_' + str(rep),
                                                 'chan_' + str(channel), '', spike_count_dict[data_key],
                                                 first_spike_dict[data_key],
                                                 ''] + spike_times_dict[data_key])

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

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
