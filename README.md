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
occurence of each key versus the actual occurence
- 3NumberOfKeys.py..........................Python script to plot the number
of times I pressed each key.

- diagrams/.................................Relevant diagrams, images, and data
- diagrams/KeystrokesOverTime.txt...........Data set for total keystrokes over time.
    Obtained by sizing the log file from keylogging myself after processing
- diagrams/NormalLetterFrequency.txt........Data set for normal letter frequency.
    Obtained via Wikipedia.
- diagrams/NumberOfKeys.txt.................Data set for individual key usage.
    Obtained by counting the instances of each character in the log file after
    processing.
- diagrams/KeystrokesOverTime.png...........Graph of keystrokes over time
```
### Example Output:
