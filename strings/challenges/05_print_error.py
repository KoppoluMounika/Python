import re

log = """
[10.00] Starting system
[10.05] Initializing drivers
[10.10] ERROR: Device not found
[10.15] Trying next device
[10.20] ERROR: Timeout waiting for response
[10.25] Reboot recommended
"""
line= log.strip().split('\n')
for i in range (len(line)):
    if (re.search(r'ERROR', line[i],re.IGNORECASE)):
        print(line[i-1])
        print(line[i])
        print(line[i+1])
        print()
    