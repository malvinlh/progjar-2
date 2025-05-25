import subprocess
import time
from datetime import datetime

# Tentukan waktu target (24 jam format)
target_time_str = "02:40:00"
target_time = datetime.strptime(target_time_str, "%H:%M:%S").time()

print(f"time_client.py will run at exactly {target_time_str}")

# Tunggu sampai waktu sistem sesuai
while True:
    now = datetime.now().time()
    if now >= target_time:
        break
    time.sleep(0.5)

# Jalankan time_client.py
subprocess.run(["python3", "time_client.py"])

print(f"time_client.py executed at {target_time_str}")