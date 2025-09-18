import re

log = """
[12345.67] kernel panic - not syncing: Fatal exception
[12345.89] Oops: 0002 [#1] SMP
[12346.00] kernel panic - not syncing: Fatal exception
[12346.13] Oops: 0003 [#2] SMP
"""

kernel_panic_count = len(re.findall(r'kernel panic', log, re.IGNORECASE))
oops_count = len(re.findall(r'oops', log, re.IGNORECASE))

print("Kernel Panic Count:", kernel_panic_count)
print("Oops Count:", oops_count)
