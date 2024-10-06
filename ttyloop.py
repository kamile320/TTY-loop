import subprocess
import time
while True:
    time.sleep(8)
    subprocess.run(['bash', 't4.sh'])
    time.sleep(8)
    subprocess.run(['bash', 't6.sh'])
    time.sleep(8)
    subprocess.run(['bash', 't2.sh'])
    time.sleep(8)
    subprocess.run(['bash', 't5.sh'])
    time.sleep(8)
    subprocess.run(['bash', 't1.sh'])
    time.sleep(8)
    subprocess.run(['bash', 't3.sh'])