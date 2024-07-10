#!/usr/bin/env python3
#ChatGPT4 written code for plotting IR signals

import matplotlib.pyplot as plt
import numpy as np
import sys

def parse_timing(timing_str):
    if 'ms' in timing_str:
        return float(timing_str.replace('ms', ''))
    elif 'us' in timing_str:
        return float(timing_str.replace('us', '')) / 1000  # Convert microseconds to milliseconds
    else:
        raise ValueError("Unknown timing unit in " + timing_str)

def read_signal_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    signals = []
    for line in lines:
        parts = line.strip().split(',')
        modulation = parts[0].strip()
        wavelength = parts[1].strip()
        title = parts[2].strip()
        repetitions = int(parts[3].strip())
        timings = [parse_timing(parts[i].strip()) for i in range(4, len(parts))]
        signals.append((modulation, wavelength, title, repetitions, timings))
    return signals

def plot_signals(signals, output_file):
    plt.figure(figsize=(15, len(signals) * 3))
    for i, (modulation, wavelength, title, repetitions, timings) in enumerate(signals, 1):
        initial_off = timings[0] if timings else 0
        total_timings = [initial_off] + timings * repetitions
        
        times = [0]  # Start the first time at zero
        signal = [0]  # Start with an 'off' state

        # Build time and signal arrays
        for t in total_timings:
            current_time = times[-1]
            times.append(current_time + t)
            # Toggle signal state
            signal.append(1 - signal[-1])  # Toggle between 0 and 1

        # Ensure the last toggle reverts to 'off' if it ends on 'on'
        if signal[-1] == 1:
            times.append(times[-1] + total_timings[0])  # Use the first on period duration
            signal.append(0)

        ax = plt.subplot(len(signals), 1, i)
        ax.step(times, signal, where='post')
        full_title = f"{title} - Modulation: {modulation}, Wavelength: {wavelength}"
        ax.set_title(full_title)
        ax.set_ylabel('On/Off')
        ax.set_xlabel('Time (ms)')
        ax.grid(True)

        # Annotate each transition with duration, skip the first added period
        for j in range(2, len(times)):  # Start from 2 to skip the first off period label
            duration = times[j] - times[j - 1]
            mid_point = (times[j] + times[j - 1]) / 2
            ax.annotate(f'{duration:.2f} ms', (mid_point, 0.5), textcoords="offset points",
                        xytext=(0,10), ha='center', color='blue')  # Color matched to the trace line

    plt.tight_layout()
    plt.savefig(output_file, format='png')
    plt.show()

import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script_name.py input_filename.txt output_filename.png")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    signals = read_signal_file(input_filename)
    plot_signals(signals, output_filename)