import h5py
import numpy as np
from scipy.signal import find_peaks


# Load dataset
file = h5py.File("data/part_1.mat", "r")
data = file["Part_1"]

print("Number of records in Part_1:", data.shape[0])


# Store processed data
all_ppg_windows = []
all_abp_windows = []
all_systolic_labels = []
all_diastolic_labels = []

window_size = 625

invalid_records = 0
flat_ppg_windows = 0
no_peak_windows = 0


# Process all records
for i in range(data.shape[0]):

    record_ref = data[i, 0]
    record = np.array(file[record_ref])

    ppg = record[:, 0]
    abp = record[:, 1]

    # Skip records with missing or invalid values
    if not np.all(np.isfinite(ppg)) or not np.all(np.isfinite(abp)):
        invalid_records += 1
        continue

    # Split signals into 5-second windows
    for start in range(0, len(ppg) - window_size + 1, window_size):

        end = start + window_size

        ppg_window = ppg[start:end]
        abp_window = abp[start:end]

        # Find systolic peaks and diastolic valleys
        peaks, _ = find_peaks(abp_window, distance=50)
        valleys, _ = find_peaks(-abp_window, distance=50)

        if len(peaks) == 0 or len(valleys) == 0:
            no_peak_windows += 1
            continue

        systolic = np.mean(abp_window[peaks])
        diastolic = np.mean(abp_window[valleys])

        # Normalize PPG
        ppg_mean = np.mean(ppg_window)
        ppg_std = np.std(ppg_window)

        if ppg_std == 0:
            flat_ppg_windows += 1
            continue

        normalized_ppg = (ppg_window - ppg_mean) / ppg_std

        # Store matching window and labels
        all_ppg_windows.append(normalized_ppg)
        all_abp_windows.append(abp_window)
        all_systolic_labels.append(systolic)
        all_diastolic_labels.append(diastolic)


# Convert to NumPy arrays
all_ppg_windows = np.array(all_ppg_windows)
all_abp_windows = np.array(all_abp_windows)
all_systolic_labels = np.array(all_systolic_labels)
all_diastolic_labels = np.array(all_diastolic_labels)


# Preprocessing results
print("\n--- Part 1 Preprocessing Results ---")

print("Records processed:", data.shape[0])
print("Invalid records skipped:", invalid_records)
print("Flat PPG windows skipped:", flat_ppg_windows)
print("Windows without peaks/valleys:", no_peak_windows)

print("Total valid examples:", len(all_ppg_windows))

print("PPG dataset shape:", all_ppg_windows.shape)
print("ABP dataset shape:", all_abp_windows.shape)
print("Systolic labels shape:", all_systolic_labels.shape)
print("Diastolic labels shape:", all_diastolic_labels.shape)


# Blood pressure range
print("\n--- Blood Pressure Range Check ---")

print("Lowest systolic:", np.min(all_systolic_labels))
print("Highest systolic:", np.max(all_systolic_labels))

print("Lowest diastolic:", np.min(all_diastolic_labels))
print("Highest diastolic:", np.max(all_diastolic_labels))


# Check extreme labels
print("\n--- Extreme BP Label Check ---")

print("Systolic below 70:",
      np.sum(all_systolic_labels < 70))

print("Systolic above 180:",
      np.sum(all_systolic_labels > 180))

print("Diastolic below 40:",
      np.sum(all_diastolic_labels < 40))

print("Diastolic above 120:",
      np.sum(all_diastolic_labels > 120))


# Check normalization
print("\n--- Normalization Check ---")

print("First window mean:",
      np.mean(all_ppg_windows[0]))

print("First window standard deviation:",
      np.std(all_ppg_windows[0]))


# Inspect an extreme DBP example
extreme_dbp = np.where(all_diastolic_labels > 120)[0]

if len(extreme_dbp) > 0:

    index = extreme_dbp[0]

    print("\n--- Example Extreme DBP Window ---")

    print("Window index:", index)
    print("Systolic:", all_systolic_labels[index])
    print("Diastolic:", all_diastolic_labels[index])

    print("ABP minimum:", np.min(all_abp_windows[index]))
    print("ABP maximum:", np.max(all_abp_windows[index]))


file.close()