import psutil
import csv
from datetime import datetime
import os

CSV_FILE = "system_metrics.csv"

file_exists = os.path.isfile(CSV_FILE)

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage("/")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(CSV_FILE, "a", newline="") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(["Timestamp", "CPU%", "Memory%", "Disk%"])
    writer.writerow([timestamp, cpu, memory.percent, disk.percent])

print(f"Metrics collected at {timestamp}")
