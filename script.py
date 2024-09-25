# Functioning code backup
# %%
import random
import math
import numpy as np
import matplotlib as plt
import matplotlib_inline as plt
import matplotlib.pyplot as plt
file_name = "pmt1_165v_all.txt"
# Load data from file
all_data = []
with open(file_name, 'r') as file:
    for line in file:
        data = [float(val) for val in line.split()]
        all_data.append(data)
# Print the total number of values in a single row (assuming all rows have the same length)
total_values = len(all_data[0])
print(f"Total number of values in each waveform: {total_values}")
# Find the top value from each waveform
all_top = [max(row) for row in all_data]
print(f"Number of top values: {len(all_top)}")
print(f"top values: {all_top}")  # Print top values as a sample
print()
print(f"For file {file_name}")
# Histogram of top values
plt.figure(figsize=(12, 6))
plt.hist(all_top, bins=150, range=(-5, 50))
plt.xlabel("Amplitude (mV)")
plt.ylabel("Frequency")
plt.title("Histogram of Top Amplitudes from All Waveforms")
plt.show()
# Histogram of top values
plt.figure(figsize=(12, 6))
plt.hist(all_top, bins=150, range=(-5, 50))
plt.xlabel("Amplitude (mV)")
plt.ylabel("Frequency")
plt.title("Histogram of Top Amplitudes from All Waveforms, zoomed")
# Set y-axis range
plt.ylim(0, 30)  # Desired range
plt.show()
