def detect_anomalies(data):
    insights = []

    if len(data) < 2:
        return insights

    CPU_SPIKE = 20
    MEM_SPIKE = 15
    DISK_SPIKE = 10

    prev = data[-2]
    curr = data[-1]

    cpu_diff = float(curr["CPU%"]) - float(prev["CPU%"])
    mem_diff = float(curr["Memory%"]) - float(prev["Memory%"])
    disk_diff = float(curr["Disk%"]) - float(prev["Disk%"])

    timestamp = curr["Timestamp"]

    if cpu_diff >= CPU_SPIKE:
        insights.append(f"⚠ CPU spiked by {cpu_diff:.1f}% at {timestamp}")

    if mem_diff >= MEM_SPIKE:
        insights.append(f"⚠ Memory spiked by {mem_diff:.1f}% at {timestamp}")

    if disk_diff >= DISK_SPIKE:
        insights.append(f"⚠ Disk usage spiked by {disk_diff:.1f}% at {timestamp}")

    return insights


def performance_mode(latest):
    cpu = float(latest["CPU%"])
    mem = float(latest["Memory%"])

    if cpu < 30 and mem < 40:
        return "🟢 Idle"
    elif cpu > 70 or mem > 70:
        return "🔴 Under Stress"
    else:
        return "🟡 Normal"
