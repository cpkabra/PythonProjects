
#@author Neel Patel
#@file GoogleMapsPinning.py

import webbrowser as wb
import sys, pyperclip


maps_address = "https://www.google.com/maps/place/"
if len(sys.argv) > 1:
    maps_address.join(sys.argv[1:])
else:
    maps_address += pyperclip.paste()
wb.open(maps_address)
