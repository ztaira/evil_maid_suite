"""
This is a short script to plot my keystrokes over time using matplotlib.
"""

import time
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

# ============================================================================
# Reading in Data
# ============================================================================

# load in data to a couple of lists
# times = a time, stored in seconds since the epoch
# keystrokes = cumulative keystrokes from the start of the experiment until
# the epoch time stored in the equivalent entry in the times list
# 
# for example, keystrokes[x] is the total amount of keystrokes from the start of
# the experiment until time times[x]
times = []
keystrokes = []
with open('diagrams/1KeystrokesOverTime.txt', 'r') as readfile:
    for line in readfile:
        line = line.split()
        times.append(line[0])
        keystrokes.append(line[2])
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(line[0])))

# ============================================================================
# Plotting the graph
# ============================================================================

# plot keystrokes over time using matplotlib and pyplot
plt.plot(times, keystrokes, 'k')
# April 1, 2016
plt.axvline(x=1459468800, color='r')
# May 1, 2016
plt.axvline(x=1462060800, color='y')
# June 1, 2016
plt.axvline(x=1464739200, color='g')
# July 1, 2016
plt.axvline(x=1467331200, color='b')
# August 1, 2016
plt.axvline(x=1470009600, color='c')
# September 1, 2016
plt.axvline(x=1472688000, color='m')
# make title and labels:
plt.xlabel('Epoch Time')
plt.ylabel('Number of Keystrokes')
plt.title('Keystrokes over time')
# legend
red_patch = mpatches.Patch(color='red', label='April')
yellow_patch = mpatches.Patch(color='yellow', label='May')
green_patch = mpatches.Patch(color='green', label='June')
blue_patch = mpatches.Patch(color='blue', label='July')
cyan_patch = mpatches.Patch(color='cyan', label='August')
magenta_patch = mpatches.Patch(color='magenta', label='September')
plt.legend(handles=[red_patch, yellow_patch, green_patch, blue_patch,
                    cyan_patch, magenta_patch], loc=4)
plt.show()
