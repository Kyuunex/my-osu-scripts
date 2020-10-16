#!/usr/bin/env python3
import os
import sys
from .beatmapbackporter import Beatmap


del sys.argv[0]


def convert(file_to_convert):
    # print(file_to_convert)
    a = Beatmap(file_to_convert)
    if a.general_section['Mode'] > 0:
        os.remove(file_to_convert)
        print(file_to_convert)


if sys.argv:
    for beatmap_folder in os.listdir(" ".join(sys.argv)):
        if beatmap_folder == ".":
            continue
        if beatmap_folder == "..":
            continue

        for file in os.listdir(" ".join(sys.argv) + "/" + beatmap_folder):
            if file.endswith(".osu"):
                convert(" ".join(sys.argv) + "/" + beatmap_folder + "/" + file)
