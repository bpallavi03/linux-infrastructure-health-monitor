from flask import Flask, render_template
import csv
from analyze_metrics import detect_anomalies,performance_mode

app = Flask(__name__)

CSV_FILE = "system_metrics.csv"

def load_data():
    with open(CSV_FILE) as f:
        return list(csv.DictReader(f))

def calculate_health(latest):
    cpu = float(latest["CPU%"])
    mem = float(latest["Memory%"])
    disk = float(latest["Disk%"])

    health = 100 - (cpu * 0.4 + mem * 0.4 + disk * 0.2)
    return max(0, min(100, round(health, 1)))

@app.route("/")
def dashboard():
    data = load_data()
    insights = detect_anomalies(data)

    latest = data[-1]
    health_score = calculate_health(latest)
    mode = performance_mode(latest)

    return render_template(
        "index.html",
        data=data,
        insights=insights,
        health=health_score,
        mode=mode  
    )

if __name__ == "__main__":
    app.run(debug=True)
