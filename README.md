# BMP180 Sensor Simulation & Analysis 

## Overview
This project is a **digital twin** and diagnostic tool designed to simulate and analyze data from a BMP180 barometric pressure sensor. It models real-world environmental noise and sensor faults to test the reliability of anomaly detection algorithms.

![Diagnostic Report](./sensor_diagnostic_report.png)

## Features
- **Telemetry Simulation:** Generates synthetic temperature and altitude data with modeled Gaussian noise and random "fault" jumps.
- **State-Tracking Anomaly Detection:** Identifies velocity spikes ( > 1cm/s) and thermal variances outside the standard operating range (20°C - 24°C).
- **Automated Accuracy Reporting:** Calculates real-time reliability percentages for both sensors.
- **Diagnostic Visualizations:** Generates a dual-paneled report using Matplotlib with high-visibility fault markers.

## Technical Implementation
- **Data Engineering:** Utilizes Python's `csv` module for persistent data storage between simulation and analysis phases.
- **Signal Processing:** Implemented `numpy` arrays for efficient data handling and visualization.
- **Modular Architecture:** Split into separate simulation, analysis, and visualization modules to ensure maintainability.

## Related Projects
### [Physical Altitude Threshold Detector] ([https://github.com/yourusername/arduino-altitude-threshold-detector)](https://github.com/faeezali/BMP180-Sensor-Simulation-Analysis)
This Python simulation acts as a **Digital Twin** for my physical Arduino prototype. While the Arduino handles real-time hardware interrupts and LED alerts, this Python suite provides the diagnostic pipeline needed to analyze telemetry logs and refine the threshold logic used in the field.
