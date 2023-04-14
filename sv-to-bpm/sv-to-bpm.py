#!/usr/bin/env python3

input_file = open("input.txt", "r+")

output_file = open("output.txt", "w")

timing_points = input_file.readlines()

base_bpm = 0

for current_timing_point in timing_points:
    t11, t12, t13, t14, t15, t16, t17, t18 = current_timing_point.split(",")

    if t17 == "1":
        base_bpm = float(t12)
        output_file.write(f"{t11},{t12},{t13},{t14},{t15},{t16},{t17},{t18}")
    elif t17 == "0":
        nt = str(round(base_bpm * (abs(float(t12))/100), 3))
        output_file.write(f"{t11},{nt},{t13},{t14},{t15},{t16},1,{t18}")

output_file.close()

print("This is done. look for output.txt file")
