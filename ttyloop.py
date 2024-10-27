import subprocess
import time
while True:
    time.sleep(5)
    subprocess.run(['bash', 'shells/t4.sh'])
    time.sleep(5)
    subprocess.run(['bash', 'shells/t6.sh'])
    time.sleep(5)
    subprocess.run(['bash', 'shells/t2.sh'])
    time.sleep(5)
    subprocess.run(['bash', 'shells/t5.sh'])
    time.sleep(5)
    subprocess.run(['bash', 'shells/t1.sh'])
    time.sleep(5)
    subprocess.run(['bash', 'shells/t3.sh'])