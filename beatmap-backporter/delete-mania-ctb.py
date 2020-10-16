#!/usr/bin/env python3
import os
import sys


class Beatmap:
    def __init__(self, file_path):
        self.file = open(file_path, "r+")

        # sections
        self.osu_file_format_version = 0
        self.general_section = {}
        self.editor_section = []
        self.metadata_section = []
        self.difficulty_section = {}
        self.events_section = []
        self.timing_points_section = []
        self.colours_section = []
        self.hit_objects_section = []

        self.parse()

    def parse(self):
        current_section = ""

        for line in self.file.readlines():
            if "osu file format v" in line:
                self.osu_file_format_version = int(line.replace("osu file format v", "")
                                                   .replace("\ufeff", "").replace("\x7f", "").strip())
                continue
            elif "[General]" in line:
                current_section = "[General]"
                continue
            elif "[Editor]" in line:
                current_section = "[Editor]"
                continue
            elif "[Metadata]" in line:
                current_section = "[Metadata]"
                continue
            elif "[Difficulty]" in line:
                current_section = "[Difficulty]"
                continue
            elif "[Events]" in line:
                current_section = "[Events]"
                continue
            elif "[TimingPoints]" in line:
                current_section = "[TimingPoints]"
                continue
            elif "[Colours]" in line:
                current_section = "[Colours]"
                continue
            elif "[HitObjects]" in line:
                current_section = "[HitObjects]"
                continue

            if not line.strip():
                continue
            line = line.strip()

            if current_section == "[General]":
                try:
                    general_stuff = line.split(": ")
                    self.general_section[general_stuff[0]] = general_stuff[1]
                except IndexError:
                    general_stuff = line.split(":")
                    self.general_section[general_stuff[0]] = general_stuff[1]
            elif current_section == "[Editor]":
                self.editor_section.append(line)
            elif current_section == "[Metadata]":
                self.metadata_section.append(line)
            elif current_section == "[Difficulty]":
                diff_stuff = line.split(":")
                self.difficulty_section[diff_stuff[0]] = diff_stuff[1]
            elif current_section == "[Events]":
                self.events_section.append(line)
            elif current_section == "[TimingPoints]":
                self.timing_points_section.append(line.split(","))
            elif current_section == "[Colours]":
                self.colours_section.append(line)
            elif current_section == "[HitObjects]":
                self.hit_objects_section.append(line)


del sys.argv[0]


def convert(file_to_convert):
    # print(file_to_convert)
    a = Beatmap(file_to_convert)
    try:
        if int(a.general_section['Mode']) > 0:
            os.remove(file_to_convert)
            print(file_to_convert)
    except KeyError:
        pass


if sys.argv:
    for beatmap_folder in os.listdir(" ".join(sys.argv)):
        if beatmap_folder == ".":
            continue
        if beatmap_folder == "..":
            continue

        for file in os.listdir(" ".join(sys.argv) + "/" + beatmap_folder):
            if file.endswith(".osu"):
                convert(" ".join(sys.argv) + "/" + beatmap_folder + "/" + file)
