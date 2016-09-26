# evil_maid_suite
Hack-A-Week 10: Data on the time I keylogged myself

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

![alt text][outputimage1]
[outputimage1]: https://github.com/ztaira14/evil_maid_suite/blob/master/diagrams/1KeystrokesOverTime.png "Keystrokes Over Time""

### Ratio Of Keys (Script 2)

![alt text][outputimage2]
[outputimage2]: https://github.com/ztaira14/evil_maid_suite/blob/master/diagrams/2RatioOfKeys.png "Ratio Of Keys""

### Number Of Keys Pressed (Script 3)

![alt text][outputimage3]
[outputimage3]: https://github.com/ztaira14/evil_maid_suite/blob/master/diagrams/3NumberOfKeys.png "Number Of Keys""

### Ratio Of Keys, Bar Form (Script 4)

![alt text][outputimage4]
[outputimage4]: https://github.com/ztaira14/evil_maid_suite/blob/master/diagrams/4RatioOfKeysBarForm.png "Ratio Of Keys, Bar Form""
