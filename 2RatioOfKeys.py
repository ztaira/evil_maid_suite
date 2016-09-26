"""
This is a short script to plot the ratio of letters I type against the
expected ratios of letters in the English language.
"""
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

# ============================================================================
# Reading in Data
# ============================================================================

# load in data to a dictionary
# dictionary contains all the letters in the alphabet (unicode values 0x61
# to 0x7a) and is stored as follows:

# {
# 'a': [x_coordinate, y_coordinate],
# 'b': [x_coordinate, y_coordinate],
# 'c': [x_coordinate, y_coordinate],
# 'd': [x_coordinate, y_coordinate],
# etc
# }
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

# create separate lists of x and y coordinates, because that's what pyplot
# wants
x_coords = [letter_coordinates[key][0] for key in sorted(letter_coordinates.keys())]
y_coords = [letter_coordinates[key][1] for key in sorted(letter_coordinates.keys())]
print("Total percentages:", sum(x_coords), sum(y_coords))

# ============================================================================
# Plotting the graph
# ============================================================================

# create a scatter plot
plt.scatter(x_coords, y_coords)
# annotate the points
for letter in sorted(letter_coordinates.keys()):
    plt.annotate(letter, xy=letter_coordinates[letter])
# plot the line x = y
plt.plot([0, 0.10], [0, 0.10], '-')
# label the axes
plt.xlabel('Percentage Found in Normal Engish')
plt.ylabel("Percentage of the Letters I've typed")
plt.title("My Typing Pattern vs Normal English Letter Distribution")
# legend
blue_patch = mpatches.Patch(color='blue', label='Expected value = Actual Value')
plt.legend(handles=[blue_patch])

plt.show()
