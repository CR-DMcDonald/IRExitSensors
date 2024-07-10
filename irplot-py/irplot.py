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

def format_timing_value(t):
    if t * 1000 % 1000 == 0:  # Check if it's a whole number when expressed in microseconds
        return f"{int(t * 1000)}us"  # Avoid decimal places if it's an exact number of microseconds
    elif t < 1.0:
        return f"{t * 1000:.1f}us"  # Show as microseconds if less than 1 millisecond
    # if a number large than 1ms but has us precision then convert to us
    else:
        return f"{t:.3f}ms"


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
    label_offset_on = -30  # Vertical offset for 'on' period labels, above the line
    label_offset_off = 28  # Vertical offset for 'off' period labels, below the line

    plt.figure(figsize=(15, len(signals) * 4))
    unique_periods = {}
    period_count = 1

    for i, (modulation, wavelength, title, repetitions, timings) in enumerate(signals, 1):
        initial_off = timings[0] if timings else 0
        total_timings = [initial_off] + timings * repetitions

        times = [0]
        signal = [0]

        for t in total_timings:
            current_time = times[-1]
            times.append(current_time + t)
            signal.append(1 - signal[-1])
            period_key = format_timing_value(t)
            if period_key not in unique_periods:
                unique_periods[period_key] = f"p{period_count}"
                period_count += 1

        if signal[-1] == 1:
            times.append(times[-1] + total_timings[0])
            signal.append(0)

        ax = plt.subplot(len(signals), 1, i)
        ax.step(times, signal, where='post', color='darkred')
        ax.set_title(f"{title} - Modulation: {modulation}, Wavelength: {wavelength}")
        ax.set_ylabel('On/Off')
        ax.set_xlabel('Time (ms)')
        ax.grid(True)

        for j in range(2, len(times)):
            duration = times[j] - times[j - 1]
            mid_point = (times[j] + times[j - 1]) / 2
            label = unique_periods[format_timing_value(duration)]
            if signal[j] == 0:
                ypos = signal[j-1] - 0.1  # Below the line
                yoffset = label_offset_off
                va = 'top'
            else:
                ypos = signal[j-1] + 0.1  # Above the line
                yoffset = label_offset_on
                va = 'bottom'
            ax.annotate(label, (mid_point, ypos), textcoords="offset points",
                        xytext=(0, yoffset), ha='center', va=va, color='darkred', fontsize=8)

    plt.figtext(0.1, 0.01, '   '.join([f"{v}: {k}" for k, v in unique_periods.items()]), horizontalalignment='left')
    plt.tight_layout()
    plt.savefig(output_file, format='png')
    plt.show()




if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script_name.py input_filename.csv output_filename.png")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    signals = read_signal_file(input_filename)
    plot_signals(signals, output_filename)