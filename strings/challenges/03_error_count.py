import re

log = """
[1.11] ERROR: device failed to start
[1.12] ERROR: timeout waiting for response
[1.13] WARNING: low battery
[1.14] PANIC: unrecoverable error
[1.15] device fail detected
[1.16] timeout on bus
"""
count = {
    "error" : len(re.findall(r'error', log, re.IGNORECASE)),
    "fail" : len(re.findall(r'fail', log, re.IGNORECASE)),
    "timeout" : len(re.findall(r'timeout', log, re.IGNORECASE)),
    "panic" : len(re.findall(r'panic', log, re.IGNORECASE))
}
sorted_counts = sorted(count.items(), key=lambda x: x[1], reverse=True)

for keyword, count in sorted_counts[:3]:
    print(f"{keyword}: {count}")



