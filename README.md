# DynamicWallpaper
DynamicWallpaper is a Python script that you can run in the background to
automatically change Windows wallpaper throught the day, every hour.

It's like the macOS dynamic wallpapers introduced in Mojave.

## DynamicWallpaper Packs
A DynamicWallpaper Pack is a collection of 24 wallpapers (representing 24 hours
of the day) named as `00.jpg`, `01.jpg`, `02.jpg`, ... , `23.jpg`.
Every collection should be inside a directory whose name is the pack's name.
And all the packs should be inside the `packs` directory.

One pack has already been provided, called `Clock`. You can use that or make
your own as per the instructions above. Feel free to contribute your amazing
DynamicWallpaper Packs by making a pull request.

## Usage
- Clone/Download this repository.
- Run the `DynamicWallpaper.py` script.

## Tips & Tricks

### Run at startup
To run DynamicWallpaper at startup, follow these steps:
- Go to the **Startup** directory:
  `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`
- Create a shortcut to the `DynamicWallpaper.py` script.

### Auto select wallpaper pack
To automatically select a DynamicWallpaper Pack at start, follow these steps:
- Right-Click on the `DynamicWallpaper.py` script's shortcut.
- Go to **Properties**.
- In the **Target** text box, add the name of your DynamicWallpaper Pack at the
  end - right after `...\DynamicWallpaper.py` - separated by a space.

  Example: `...\DynamicWallpaper.py Clock`

> If you liked this project, please give this repository a **Star** :star:
