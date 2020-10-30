#!/usr/bin/env python3
import os 
import shutil 

songs_directory = "/mnt/ti/games/x86/osu-stable/Songs/" # use / slashes and make these end with slash

list_of_all_mapsets = os.listdir(songs_directory)
for mapset_folder in list_of_all_mapsets:
    if mapset_folder == "." or mapset_folder == "..":
        continue
    
    if not " " in mapset_folder:
        continue

    a_list = mapset_folder.split(" ")

    mapset_id = a_list[0]

    if not mapset_id.isdigit():
        continue

    mapset_folder_full_path = songs_directory + mapset_folder + "/"

    mapset_folder_new_path = songs_directory + mapset_id + "/"

    try:
        shutil.move(mapset_folder_full_path, mapset_folder_new_path)
    except Exception as e:
        print("Errored: " + mapset_folder_full_path + "\n")
        print(e)


print("I am done owo")
