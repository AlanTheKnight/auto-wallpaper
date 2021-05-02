import subprocess
import os
import time
import toml
from typing import List


with open(os.path.join(os.environ.get("HOME"), ".wallpapers.toml"), "r") as f:
    config = toml.load(f)
FOLDER = config['folder']


def set_wallpaper(wall: str):
    command = config['commands']['set'] + " '" + wall + "'"
    subprocess.Popen(["/bin/bash", "-c", command])


def get_current_wallpaper() -> str:
    return subprocess.check_output(
        ["/bin/bash", "-c", config['commands']['get']]).decode("utf-8").strip()


def filename_to_time(filename: str):
    hours, minutes = map(int, filename.split(".")[0].split(":"))
    return int(hours) * 60 + int(minutes)


def examine_folder() -> dict:
    *_, filenames = list(os.walk(FOLDER))[0]
    folder = [(filename_to_time(i), i) for i in filenames]
    folder.sort(key=lambda x: x[0])
    return folder


def get_filename_to_change():
    folder = examine_folder()
    ct = time.localtime()
    ct = ct.tm_hour * 60 + ct.tm_min
    if ct < folder[0][0]:
        return folder[-1][1]
    for i in range(1, len(folder)):
        if folder[i-1][0] <= ct < folder[i][0]:
            return folder[i-1][1]
    return folder[-1][1]


if __name__ == "__main__":
    while True:
        filename = get_filename_to_change()
        if os.path.basename(get_current_wallpaper()[1:-1]) != filename:
            set_wallpaper(os.path.join(FOLDER, filename))
        time.sleep(60) # Check for new wallpaper every 60 seconds
