# calculator/export_tools.py - Data export functionality
# Exports data to CSV.

import csv
import os

def export_to_csv(data, filename="performance_data.csv"):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)
    print(f"Data exported to {filename}"")
