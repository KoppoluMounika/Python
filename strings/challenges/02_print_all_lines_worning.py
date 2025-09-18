import re

log = """
[100.123] INFO: Booting Linux
[100.456] WARNING: Low memory detected
[101.000] WARNING: CPU load high
[101.555] INFO: Boot complete
"""
line= log.strip().split('\n')
for i in line:
    if re.search(r'WARNING', i,re.IGNORECASE):
        print(i)


