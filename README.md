# Sparkle-HDF5-Extractor
Extract data from sparkle .hdf5 files into .csv files

![alt tag](https://raw.githubusercontent.com/portfors-lab/Sparkle-HDF5-Extractor/master/SparkleHDF5Extractor.png "Main Window")
======

### Instructions:
1. Select a Sparkle .hdf5 file by typing in the absolute path or searching for it with the “Browse” button.
2. Choose the test number and channel you wish to extract the raw data from.
3. Select either normal or inverse to determine how you want the data configured while calculating spikes.
4. Select a voltage threshold to be used while calculating spikes.
5. Choose what you wish to have exported.
6. Calibration: The calibration parameters used in the test.
7. Stimulus: The stimulus parameters used in the test.
8. Spike Times: The spike times for the selected test based on your threshold.
9. Raw Data: Each voltage value for every time point captured during the test. (Caution: Can create large files)
10. Press “Start” to begin extraction.

### TODO:
* Add Sparkle HDF5e Extractor features to Sparkle Analysis
