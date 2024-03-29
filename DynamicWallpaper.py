"""
DynamicWallpaper is a Python script that you can run in the background to
automatically change Windows wallpaper throught the day, every hour.

Author: Sankarsan Kampa
License: GPLv3
"""

import ctypes
import datetime
import os
import sys
import time


SPI_SETDESKWALLPAPER = 20
WALLPAPER_PACK = None
WALLPAPER_PACK_PATH = "./packs/"


def set_wall(index):
    index = str(index)
    index = index if len(index) > 1 else "0{0}".format(index)

    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, "{0}/{1}/{2}.jpg".format(os.path.dirname(os.path.realpath(__file__)), WALLPAPER_PACK_PATH, index), 0)


if len(sys.argv) > 1:
    WALLPAPER_PACK = " ".join(sys.argv[1:])
else:
    WALLPAPER_PACK = input("Please enter the DynamicWallpaper pack: ")

WALLPAPER_PACK_PATH += "{0}".format(WALLPAPER_PACK)

if not os.path.isdir(WALLPAPER_PACK_PATH):
    print("The specified wallpaper pack - {0} - doesn't exist.".format(WALLPAPER_PACK))
    input("\nPress Enter to exit...")
    exit(1)

print("DynamicWallpaper - {0} - is running...".format(WALLPAPER_PACK))
print("\n\n")
print("If you've any suggestions or you're facing any issues, feel free to open a ticket here:")
print("https://github.com/k3rn31p4nic/DynamicWallpaper/issues")

while True:
    now = datetime.datetime.now()
    set_wall(now.hour)
    time.sleep(5)
