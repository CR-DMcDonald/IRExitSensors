#!/usr/bin/env python3
#ChatGPT4 written code for plotting IR signals

import matplotlib.pyplot as plt
import numpy as np

def read_signal_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    signals = []
    for line in lines:
        parts = line.strip().split(',')
        modulation = parts[0].strip()
        repetitions = int(parts[1].strip())
        timings = [float(x) for x in parts[2:]]
        signals.append((modulation, repetitions, timings))
    return signals

def plot_signals(signals, output_file):
    plt.figure(figsize=(15, len(signals) * 2))
    for i, (modulation, repetitions, timings) in enumerate(signals, 1):
        total_timings = timings * repetitions
        times = [0]  # Start the first time at zero
        signal = []

        # Build time and signal arrays
        for t in total_timings:
            current_time = times[-1]
            times.append(current_time + t)
            # Toggle signal state
            if len(signal) % 2 == 0:  # If even, we are at a 'low' state
                signal.extend([1])  # Turn signal on
            else:
                signal.extend([0])  # Turn signal off

        # Ensure that signal and times match by appending the last state if necessary
        if len(times) == len(signal) + 1:
            signal.append(signal[-1])

        ax = plt.subplot(len(signals), 1, i)
        ax.step(times, signal, where='post')
        ax.set_title(f'Signal Modulation: {modulation}')
        ax.set_ylabel('On/Off')
        ax.set_xlabel('Time (ms)')
        ax.grid(True)
    
    plt.tight_layout()
    plt.savefig(output_file, format='png')
    plt.show()

# Example usage:
signals = read_signal_file('input_signals.txt')
plot_signals(signals, 'output_signal_diagram.png')
