import re

log = """
[22.1] usb 1-1: USB disconnect, device number 2
[22.3] usb 1-1: new full-speed USB device number 3 using xhci_hcd
[22.5] usb 2-1: reset high-speed USB device number 4 using ehci-pci
"""
line= log.strip().split('\n')
for i in line:
    if (re.search(r'USB disconnect', i,re.IGNORECASE)) or (re.search(r'new full-speed USB device', i,re.IGNORECASE)):
        print(i)