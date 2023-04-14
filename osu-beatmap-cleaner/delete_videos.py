#!/usr/bin/env python3

import os
import sys

if not len(sys.argv) == 2:
    print("Pass in the location to your Songs folder as the only argument")
    exit()

base_dir = sys.argv[1]

mapset_list = os.listdir(base_dir)

banned_extensions = [
    ".mp4",
    ".avi",
    ".flv",
    ".wmv",
    ".m4v",
]

if not (base_dir.endswith("/") or base_dir.endswith("\\")):
    base_dir += "/"

print("Deleting videos from subdirectories of ", base_dir)
print(f"Found {len(mapset_list)-2} mapsets")

input("Press Enter to continue...")

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
            if map_file.lower().endswith(banned_ext):
                full_file_path = full_mapset_dir+"/"+map_file
                os.remove(full_file_path)
                print(full_file_path)

print("i am done")
