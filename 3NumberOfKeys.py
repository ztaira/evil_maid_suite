"""
This is a short script to visualize the amount I pressed each key.
"""
import matplotlib.pyplot as plt

# ============================================================================
# Reading in Data
# ============================================================================

# a list of characters
letter_names = []
# the ascii value associated with each character
letter_values = []
# how many times I typed said character
letter_amounts = []
# read in information from a text file
with open('diagrams/3NumberOfKeys.txt') as readfile:
    for line in readfile:
        line = line.split(' : ')
        letter_names.append(line[0])
        letter_values.append(ord(line[0]))
        letter_amounts.append(float(line[1]))

# ============================================================================
# Plotting the graph
# ============================================================================

# create a bar graph
plt.bar(letter_values, letter_amounts)
# annotate the bars
for i in range(len(letter_names)):
    plt.text(letter_values[i], letter_amounts[i]+1000, letter_names[i])
# set limits on the x axis
plt.xlim((30, 125))
# label the axes
plt.xlabel('Character ASCII value')
plt.ylabel("Amount Character Has Been Pressed")
plt.title("How Many Times I've Pressed Each Character")
plt.show()
