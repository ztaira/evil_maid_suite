"""
This is a short script to plot the ratio of letters I type against the
expected ratios of letters in the English language in bar form.
"""
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

# ============================================================================
# Reading in Data
# ============================================================================

# reusing the code from part 2, because the values I want to get are the same
letter_coordinates = {}
with open('diagrams/2NormalLetterFrequency.txt') as readfile:
    for line in readfile:
        line = line.split()
        letter_coordinates[line[0]] = [float(line[2])]
with open('diagrams/2RatioOfKeys.txt') as readfile:
    for line in readfile:
        line = line.split()
        if line[0] in letter_coordinates.keys():
            letter_coordinates[line[0]].append(float(line[2]))

# normalize all the values to a percentage of 1
normal_letter_count_total = 0
my_letter_count_total = 0
for key in letter_coordinates:
    normal_letter_count_total += letter_coordinates[key][0]
    my_letter_count_total += letter_coordinates[key][1]
for key in sorted(letter_coordinates.keys()):
    letter_coordinates[key][0] /= normal_letter_count_total
    letter_coordinates[key][1] /= my_letter_count_total

# create separate lists to represent expected ratios and actual ratios
expected_percentage = [letter_coordinates[key][0] for key in sorted(letter_coordinates.keys())]
actual_percentage = [letter_coordinates[key][1] for key in sorted(letter_coordinates.keys())]
print("Total percentages:", sum(expected_percentage), sum(actual_percentage))

# ============================================================================
# Plotting the graph
# ============================================================================

# create 2 bar plots and plot them
fig, ax = plt.subplots()
width = 0.3
plot1_indices = [x for x in range(97, 123)]
plot1 = ax.bar(plot1_indices, expected_percentage, width, color='r')
plot2_indices = [x + width for x in range(97, 123)]
plot2 = ax.bar(plot2_indices, actual_percentage, width, color='b')

# label
plt.title("My Typing Pattern vs Normal English Letter Distribution (Bar)")
plt.xlabel('Character ASCII value')
plt.ylabel('Percentage of Total Characters Typed')
letters = [key for key in sorted(letter_coordinates.keys())]
for i in range(26):
    if expected_percentage[i] < actual_percentage[i]:
        height = actual_percentage[i] + 0.002
    else:
        height = expected_percentage[i] + 0.002
    plt.text(ord(letters[i]), height, letters[i])
# legend
red_patch = mpatches.Patch(color='red', label='Expected Percentage')
blue_patch = mpatches.Patch(color='blue', label='Actual Percentage')
plt.legend(handles=[red_patch, blue_patch])
plt.show()
