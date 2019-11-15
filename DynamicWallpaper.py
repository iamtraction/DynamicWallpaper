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
    WALLPAPER_PACK_PATH += "{0}".format(WALLPAPER_PACK)

if not os.path.isdir(WALLPAPER_PACK_PATH):
    print("The specified wallpaper pack - {0} - doesn't exist.".format(WALLPAPER_PACK))
    input("\nPress Enter to exit...")
    exit(1)

while True:
    now = datetime.datetime.now()
    set_wall(now.hour)
    time.sleep(5)
