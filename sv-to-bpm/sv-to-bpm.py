#!/usr/bin/env python3

import sys

if not len(sys.argv) == 2:
    print("Pass in the location to a file containing your timing points as your only argument")
    exit()

input_file = open(sys.argv[1], "r")

timing_points = input_file.readlines()

base_bpm = 0

for current_timing_point in timing_points:
    t11, t12, t13, t14, t15, t16, t17, t18 = current_timing_point.split(",")

    if t17 == "1":
        base_bpm = float(t12)
        print(f"{t11},{t12},{t13},{t14},{t15},{t16},{t17},{t18}")
    elif t17 == "0":
        nt = str(round(base_bpm * (abs(float(t12))/100), 3))
        print(f"{t11},{nt},{t13},{t14},{t15},{t16},1,{t18}")

print("# This is done")
