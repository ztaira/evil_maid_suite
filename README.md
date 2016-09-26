# evil_maid_suite
Hack-A-Week 10: Data visualization on the time I keylogged myself

Note: All keylogging was done ONLY on my personal laptop. I would never mess
with a machine that's not my own.

### Usage:
- You can run any of the python files with `python [filename]`. However,
I've included the graphs below so you can view the data more easily.

### Features:
- Clear labeling with multiple colors and descriptive naming conventions
- Text files in diagrams/ are aptly named to easily associate them with the
script that uses them
- Keylogger not included (I did fork it on GitHub, though)

### What it does:
- Uses matplotlib and pyplot to plot useful graphs using data from the time I
keylogged myself

### What it doesn't do:
- N/A

### Included Files:
```
- README.md.................................This readme file
- 0LogParser.py.............................Python script to get the log file,
process its text, and write data about it.
- 1KeystrokesOverTime.py....................Python script to plot keystrokes over
time using matplotlib
- 2RatioOfKeys.py...........................Python script to plot the expected
occurrence of each key versus the actual occurrence
- 3NumberOfKeys.py..........................Python script to plot the number
of times I pressed each key.
- 4RatioOfKeysBarForm.py.....................Python script to plot the expected
occurrence of keys and the actual occurrence in bar form

- diagrams/.................................Relevant diagrams, images, and data
- diagrams/1KeystrokesOverTime.txt..........Data set for total keystrokes over time.
Obtained by sizing the log file from keylogging myself after processing
- diagrams/1KeystrokesOverTime.png..........Image of graph output for script 1
- diagrams/2NormalLetterFrequency.txt.......Data set for normal letter
frequency. Obtained via Wikipedia.
- diagrams/2RatioOfKeys.txt.................Data set for my letter frequency.
Obtained by counting the instances of each character in the log file after
processing.
- diagrams/2RatioOfKeys.png.................Image of graph output for script 2
- diagrams/3NumberOfKeys.txt................Data set for individual key usage.
- diagrams/3NumberOfKeys.png................Image of graph output for script 3
- diagrams/4RatioOfKeysBarForm.png..........Image of graph output for script 4
```
### Example Output:

### Keystrokes Over Time (Script 1)

Interesting Tidbit: The flat line from June to August is where I got a work
laptop. My keys are untracked during this time - there's no way I would mess
with a machine that's not my own.

Interesting Tidbit 2: The flat line in the middle of August is where I went on
vacation with my family.

![alt text][outputimage1]
[outputimage1]: https://github.com/ztaira14/evil_maid_suite/blob/master/diagrams/1KeystrokesOverTime.png "Keystrokes Over Time""

### Ratio Of Keys (Script 2)

Interesting Tidbit 3: Since I use vim, the 'j' and 'k' keys are pressed far
more than normal, as I use those to navigate through text files.

![alt text][outputimage2]
[outputimage2]: https://github.com/ztaira14/evil_maid_suite/blob/master/diagrams/2RatioOfKeys.png "Ratio Of Keys""

### Number Of Keys Pressed (Script 3)

Interesting Tidbit 4: "<" represents the "delete". I've pressed this more than
any other single key.

Interesting Tidbit 5: "D" represents the "down" key.  I use this key to scroll
downwards when I'm reading articles on the internet or reading through text
files on my laptop, so it makes sense that this would be the second most
most common key.

Interesting Tidbit 6: " " represents the space bar. This comes in third. No
surprises here.

Interesting Tidbit 7: "S" represents the Shift Key, which I've pressed fourth-
most often.

Interesting Tidbit 8: "V" represents the command key. This comes in fifth.

Note: Which character represents which key can be found in the 0LogParser.py
file.

![alt text][outputimage3]
[outputimage3]: https://github.com/ztaira14/evil_maid_suite/blob/master/diagrams/3NumberOfKeys.png "Number Of Keys""

### Ratio Of Keys, Bar Form (Script 4)

Interesting Tidbit 9: It's interesting to see graphically how far my use of
the 'j' and 'k' keys has skewed the data set.

![alt text][outputimage4]
[outputimage4]: https://github.com/ztaira14/evil_maid_suite/blob/master/diagrams/4RatioOfKeysBarForm.png "Ratio Of Keys, Bar Form""
