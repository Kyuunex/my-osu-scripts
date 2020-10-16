#!/usr/bin/env python3
import sys


class Beatmap:
    def __init__(self, file_path):
        self.file = open(file_path, "r+")

        # sections
        self.general_section = []
        self.editor_section = []
        self.metadata_section = []
        self.difficulty_section = {}
        self.events_section = []
        self.timing_points_section = []
        self.colours_section = []
        self.hitobjects_section = []

    def convert_timing_points(self):
        new_timing_points = []
        print("this works")
        base_bpm = 0
        for current_timing_point in self.timing_points_section:
            t11, t12, t13, t14, t15, t16, t17, t18 = current_timing_point
            # t11, t12, t13, t14, t15, t16, t17, t18 = current_timing_point.split(",")

            if t17 == "1":
                base_bpm = float(t12)
                new_timing_points.append([t11, t12, t13, t14, t15, t16, t17, t18])
            elif t17 == "0":
                nt = str(round(base_bpm * (abs(float(t12)) / 100), 3))
                new_timing_points.append([t11, nt, t13, t14, t15, t16, "1", t18])

        self.timing_points_section = new_timing_points

    def convert_diff_settings(self):
        new_difficulty_settings = {}
        for difficulty_line in self.difficulty_section.items():
            diff_setting = difficulty_line[0]

            if diff_setting == "ApproachRate":
                diff_setting = "OverallDifficulty"

            new_difficulty_settings[diff_setting] = str(int(float(difficulty_line[1])))

        self.difficulty_section = new_difficulty_settings

    def parse(self):
        current_section = ""

        for line in self.file.readlines():
            if "[General]" in line:
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
                self.general_section.append(line)
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
                self.hitobjects_section.append(line)

    def print_timing_points(self):
        for tp in self.timing_points_section:
            print(tp)
        for tp in self.metadata_section:
            print(tp)

    def save_file(self, save_file=None):
        if save_file:
            output_file = open(save_file, "w+")
        else:
            output_file = self.file

        output_file.write("osu file format v14")
        output_file.write("\n")
        output_file.write("\n")

        output_file.write("[General]")
        output_file.write("\n")
        for general_line in self.general_section:
            output_file.write(general_line)
            output_file.write("\n")
        output_file.write("\n")
        output_file.write("\n")

        output_file.write("[Editor]")
        output_file.write("\n")
        for editor_line in self.editor_section:
            output_file.write(editor_line)
            output_file.write("\n")
        output_file.write("\n")
        output_file.write("\n")

        output_file.write("[Metadata]")
        output_file.write("\n")
        for metadata_line in self.metadata_section:
            output_file.write(metadata_line)
            output_file.write("\n")
        output_file.write("\n")
        output_file.write("\n")

        output_file.write("[Difficulty]")
        output_file.write("\n")
        for difficulty_line in self.difficulty_section.items():
            output_file.write(":".join(difficulty_line))
            output_file.write("\n")
        output_file.write("\n")
        output_file.write("\n")

        output_file.write("[Events]")
        output_file.write("\n")
        for event_line in self.events_section:
            output_file.write(event_line)
            output_file.write("\n")
        output_file.write("\n")
        output_file.write("\n")

        output_file.write("[TimingPoints]")
        output_file.write("\n")
        for timing_point_line in self.timing_points_section:
            output_file.write(",".join(timing_point_line))
            output_file.write("\n")
        output_file.write("\n")
        output_file.write("\n")

        output_file.write("[Colours]")
        output_file.write("\n")
        for colours_line in self.colours_section:
            output_file.write(colours_line)
            output_file.write("\n")
        output_file.write("\n")
        output_file.write("\n")

        output_file.write("[HitObjects]")
        output_file.write("\n")
        for hitobjects_line in self.hitobjects_section:
            output_file.write(hitobjects_line)
            output_file.write("\n")
        output_file.write("\n")
        output_file.write("\n")

        output_file.close()
        print("File saved!")

del sys.argv[0]

a = Beatmap(" ".join(sys.argv))
a.parse()
a.convert_timing_points()
a.convert_diff_settings()
a.print_timing_points()
a.save_file()

print("saving file as "+" ".join(sys.argv))
