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
        # Parse timings with units
        timings = []
        for part in parts[2:]:
            value, unit = part[:-2].strip(), part[-2:].strip()
            if unit == 'ms':
                timings.append(float(value))
            elif unit == 'us':
                timings.append(float(value) / 1000)  # Convert microseconds to milliseconds
        signals.append((modulation, repetitions, timings))
    return signals

def plot_signals(signals, output_file):
    plt.figure(figsize=(15, len(signals) * 2))
    for i, (modulation, repetitions, timings) in enumerate(signals, 1):
        # Add an initial off period equal to the first on period for visual clarity
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
