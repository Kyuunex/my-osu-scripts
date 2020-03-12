#!/usr/bin/env python3
import os

base_dir = "D:/osu!/Songs/"

mapset_list = os.listdir(base_dir)

banned_extensions = [
    ".mp4",
    ".avi",
    ".flv",
    ".wmv",
]


for mapset in mapset_list:
    if mapset == "." or mapset == "..":
        continue
    full_mapset_dir = base_dir+mapset
    try:
        map_files = os.listdir(full_mapset_dir)
    except:
        map_files = []
    for map_file in map_files:
        for banned_ext in banned_extensions:
            if map_file.endswith(banned_ext):
                full_file_path = full_mapset_dir+"/"+map_file
                os.remove(full_file_path)
                print(full_file_path)

print("i am done")
