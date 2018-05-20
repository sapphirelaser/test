import numpy as np
import ast
import matplotlib.pyplot as plt

def convert_time(time):
    hours, minutes = time.split(":")
    hours, minutes = int(hours), int(minutes)
    setting = "AM"
    if hours > 12:
        setting = "PM"
        hours -= 12
    return ("%02d:%02d" + setting) % (hours, minutes)
fp = open('punch_card_data')

time_of_day = np.zeros(24)
for line in fp.readlines():
    punch_card = ast.literal_eval(line)
    
for punch in punch_card:
    time_slot = punch[1]
    time_of_day[time_slot] += punch[2]

max_bin_indicies = [i for i, freq in enumerate(time_of_day) if freq == max(time_of_day)]
min_bin_indicies = [i for i, freq in enumerate(time_of_day) if freq == min(time_of_day)]
for bin in max_bin_indicies:
    start_hour = str(bin) + ':00'
    end_hour = str(bin) + ':59'
    print "The hour of day with highest commits are between %s and %s" %(convert_time(start_hour),convert_time(end_hour))
for bin in min_bin_indicies:
    start_hour = str(bin) + ':00'
    end_hour = str(bin) + ':59'
    print "The hour of day with lowest commits are between %s and %s" %(convert_time(start_hour),convert_time(end_hour))

