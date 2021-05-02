# Auto-wallpaper

Python script made to automatically change wallpapers depending on current time

## How to use

1. Copy the repository
2. Create file ``.wallpapers.toml`` in your ``~`` directory (see configuration files for different DEs)
3. Install requirements: ```pip3 install -r requirements.txt```
4. Add ```sh -c 'python3 <path to wallpapers.py>'```
5. Restart your computer and enjoy.

## GNOME

```toml
folder = "<full path to folder with images>"

[commands]
set = "gsettings set org.gnome.desktop.background picture-uri"
get = "gsettings get org.gnome.desktop.background picture-uri"
```

## Cinnamon

```toml
folder = "<full path to folder with images>"

[commands]
set = "gsettings set org.cinnamon.desktop.background picture-uri"
get = "gsettings get org.cinnamon.desktop.background picture-uri"
```
