import time
import subprocess
import re
import os

TARGET = os.getenv("PING_TARGET", "8.8.8.8")
INTERVAL = int(os.getenv("PING_INTERVAL", "30"))
LOG_FILE = "/data/ping.log"

def ping():
    try:
        res = subprocess.run(
            ["ping", "-c", "1", "-W", "1", TARGET],
            capture_output=True, text=True, timeout=2
        )
        match = re.search(r"time=([0-9.]+) ms", res.stdout)
        return float(match.group(1)) if match else None
    except:
        return None

while True:
    latency = ping()
    timestamp = time.time()
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} {latency if latency is not None else 'null'}\n")
    # 只保留最近 24 小時 (約 2880 行，避免檔案太大)
    # 簡單清理：保留最後 3000 行
    with open(LOG_FILE, "r") as f:
        lines = f.readlines()
    if len(lines) > 3000:
        with open(LOG_FILE, "w") as f:
            f.writelines(lines[-3000:])
    time.sleep(INTERVAL)