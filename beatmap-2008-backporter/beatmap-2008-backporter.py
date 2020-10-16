#!/usr/bin/env python3
import os
import sys


class Beatmap:
    def __init__(self, file_path):
        self.file = open(file_path, "r+")

        # sections
        self.osu_file_format_version = 0
        self.general_section = []
        self.editor_section = []
        self.metadata_section = []
        self.difficulty_section = {}
        self.events_section = []
        self.timing_points_section = []
        self.colours_section = []
        self.hit_objects_section = []

    def parse(self):
        current_section = ""

        for line in self.file.readlines():
            if "osu file format v" in line:
                self.osu_file_format_version = int(line.replace("osu file format v", "").strip())
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
                self.hit_objects_section.append(line)

    def save_file(self, save_file=None):
        output_buffer = f"osu file format v{str(self.osu_file_format_version)}"
        output_buffer += "\n"
        output_buffer += "\n"

        output_buffer += "[General]"
        output_buffer += "\n"
        for general_line in self.general_section:
            output_buffer += general_line
            output_buffer += "\n"
        output_buffer += "\n"

        output_buffer += "[Editor]"
        output_buffer += "\n"
        for editor_line in self.editor_section:
            output_buffer += editor_line
            output_buffer += "\n"
        output_buffer += "\n"

        output_buffer += "[Metadata]"
        output_buffer += "\n"
        for metadata_line in self.metadata_section:
            output_buffer += metadata_line
            output_buffer += "\n"
        output_buffer += "\n"

        output_buffer += "[Difficulty]"
        output_buffer += "\n"
        for difficulty_line in self.difficulty_section.items():
            output_buffer += ":".join(difficulty_line)
            output_buffer += "\n"
        output_buffer += "\n"

        output_buffer += "[Events]"
        output_buffer += "\n"
        for event_line in self.events_section:
            output_buffer += event_line
            output_buffer += "\n"
        output_buffer += "\n"

        output_buffer += "[TimingPoints]"
        output_buffer += "\n"
        for timing_point_line in self.timing_points_section:
            output_buffer += ",".join(timing_point_line)
            output_buffer += "\n"
        output_buffer += "\n"

        if self.colours_section:
            output_buffer += "[Colours]"
            output_buffer += "\n"
            for colours_line in self.colours_section:
                output_buffer += colours_line
                output_buffer += "\n"
            output_buffer += "\n"

        output_buffer += "[HitObjects]"
        output_buffer += "\n"
        for hit_objects_line in self.hit_objects_section:
            output_buffer += hit_objects_line
            output_buffer += "\n"
        output_buffer += "\n"

        if save_file:
            output_file = open(save_file, "w")
            output_file.write(output_buffer)
            output_file.close()
        else:
            self.file.seek(0)
            self.file.write(output_buffer)
            self.file.truncate()
            self.file.close()
        print("File saved!")


def convert_timing_points(timing_points_section):
    timing_points = []
    base_beat_length = 0
    for current_timing_point in timing_points_section:
        time, beat_length, meter, sample_set, sample_index, volume, uninherited, effects = current_timing_point

        if uninherited == "1":
            # red line
            base_beat_length = float(beat_length)
            timing_points.append([time, beat_length, meter, sample_set, sample_index, volume, "1", effects])
        elif uninherited == "0":
            # green line
            new_beat_length = round(base_beat_length * abs(float(beat_length)) / 100, 12)
            timing_points.append([time, str(new_beat_length), meter, sample_set, sample_index, volume, "1", effects])

    return timing_points


def convert_diff_settings(difficulty_section):
    new_difficulty_settings = {}
    for difficulty_line in difficulty_section.items():
        diff_setting = difficulty_line[0]

        if diff_setting == "OverallDifficulty":
            new_difficulty_settings["OverallDifficulty"] = str(int(float(difficulty_line[1])))
        elif diff_setting == "ApproachRate":
            new_difficulty_settings["OverallDifficulty"] = str(int(float(difficulty_line[1])))
        elif diff_setting == "HPDrainRate":
            new_difficulty_settings["HPDrainRate"] = str(int(float(difficulty_line[1])))
        elif diff_setting == "CircleSize":
            new_difficulty_settings["CircleSize"] = str(int(float(difficulty_line[1])))
        elif diff_setting == "SliderMultiplier":
            new_difficulty_settings["SliderMultiplier"] = str(float(difficulty_line[1]))
        elif diff_setting == "SliderTickRate":
            new_difficulty_settings["SliderTickRate"] = str(int(float(difficulty_line[1])))

    return new_difficulty_settings


def fix_max_sv(beatmap):
    timing_points = []
    slider_multiplier = float(beatmap.difficulty_section['SliderMultiplier'])
    if slider_multiplier > 2.6:
        slider_multiplier = slider_multiplier / 2
        beatmap.difficulty_section['SliderMultiplier'] = str(slider_multiplier)

        for current_timing_point in beatmap.timing_points_section:
            time, beat_length, meter, sample_set, sample_index, volume, uninherited, effects = current_timing_point

            timing_points.append([time, str(float(beat_length) / 2), meter, sample_set, sample_index, volume, uninherited, effects])

    beatmap.timing_points_section = timing_points


del sys.argv[0]


def convert(file_to_convert):
    a = Beatmap(file_to_convert)
    if a.osu_file_format_version > 5:
        a.parse()
        a.timing_points_section = convert_timing_points(a.timing_points_section)
        a.difficulty_section = convert_diff_settings(a.difficulty_section)
        fix_max_sv(a)
        a.osu_file_format_version = 5
        a.save_file()
        print("saved " + file_to_convert)
    else:
        print("skipped because already compatible " + file_to_convert)


if not sys.argv:
    for file in os.listdir(os.getcwd()):
        if file.endswith(".osu"):
            convert(os.getcwd()+"/"+file)
else:
    convert(" ".join(sys.argv))

