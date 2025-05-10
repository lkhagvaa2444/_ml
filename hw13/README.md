# Isolation Forest - Anomaly Detection (Exercise 13)

This project demonstrates an **unsupervised machine learning algorithm** called **Isolation Forest**. It is designed to detect anomalies by randomly isolating data points using tree structures.

## Overview
- Anomalies (outliers) are easier to isolate than normal data.
- The algorithm builds multiple random trees and measures how deep a point is isolated.
- Shallow isolation = likely anomaly.

## Files
- `main.py`: Runs the model and visualizes results with matplotlib.

## How to Run
```bash
python main.py
