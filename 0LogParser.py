"""
Module to get and parse the data from the keylogger I ran on myself.
Also outputs useful things to files.
"""

import time

class letterProcessor():
    def __init__(self):
        self.mytext = ''
        self.getlog()

    def parse_logs(self, option=0):
        """Gets the log, removes the tags, converts it to qwerty, and prints
        it to a file. Also, optionally, adds to the size file."""
        self.getlog()
        print('got log')
        self.removetags()
        print('removed tags')
        self.qwertyconvert()
        print('converted to qwerty')
        self.printtext()
        print('printed to text file')
        if option == 1:
            self.printsize()
            print('printed to size file')

    def printtext(self):
        """Writes whatever's in self.mytext to a text file."""
        file = open('log.txt', 'w')
        file.write(self.mytext)
        file.close()

    def printsize(self):
        """Appends the current size of self.mytext to a text file, along with
        a timestamp."""
        file = open('size.txt', 'a')
        file.write(str(int(time.time())) +' : ' + str(len(self.mytext)) + '\n')
        file.close()

    def printkeys(self):
        """Prints the amount of times I've pressed each key to keys.txt"""
        file = open('log.txt', 'r')
        keys = {}
        filetext = file.read()
        print(len(filetext))
        file.close()
        file = open('keys.txt', 'w')
        for letter in filetext:
            keys[letter] = 0
        for letter in filetext:
            keys[letter] = keys[letter]+1
        sortedlist = []
        for letter in keys:
            sortedlist.append(str(letter)+' : '+str(keys[letter]))
        sortedlist.sort()
        for entry in sortedlist:
            print(entry)
            file.write(entry+'\n')
        file.close()

    def removetags(self):
        """Removes the tags from self.mytext. This takes too long because it
        checks all of self.mytext instead of just what's been recently added.
        Next time, I'll just modify the part of self.mytext that's changed."""
        mystring = '[cmd]'
        while self.mytext.find(mystring) != -1:
            place = self.mytext.index(mystring)
            self.mytext = self.mytext[0:place]+'V'+self.mytext[place+len(mystring):]
        mystring = '[del]'
        while self.mytext.find(mystring) != -1:
            place = self.mytext.index(mystring)
            self.mytext = self.mytext[0:place]+'<'+self.mytext[place+len(mystring):]
        mystring = '[up]'
        while self.mytext.find(mystring) != -1:
            place = self.mytext.index(mystring)
            self.mytext = self.mytext[0:place]+'U'+self.mytext[place+len(mystring):]
        mystring = '[down]'
        while self.mytext.find(mystring) != -1:
            place = self.mytext.index(mystring)
            self.mytext = self.mytext[0:place]+'D'+self.mytext[place+len(mystring):]
        mystring = '[left]'
        while self.mytext.find(mystring) != -1:
            place = self.mytext.index(mystring)
            self.mytext = self.mytext[0:place]+'L'+self.mytext[place+len(mystring):]
        mystring = '[right]'
        while self.mytext.find(mystring) != -1:
            place = self.mytext.index(mystring)
            self.mytext = self.mytext[0:place]+'R'+self.mytext[place+len(mystring):]
        mystring = '[return]'
        while self.mytext.find(mystring) != -1:
            place = self.mytext.index(mystring)
            self.mytext = self.mytext[0:place]+'E'+self.mytext[place+len(mystring):]
        mystring = '[unknown]'
        while self.mytext.find(mystring) != -1:
            place = self.mytext.index(mystring)
            self.mytext = self.mytext[0:place]+'?'+self.mytext[place+len(mystring):]
        mystring = '[shift]'
        while self.mytext.find(mystring) != -1:
            place = self.mytext.index(mystring)
            self.mytext = self.mytext[0:place]+'S'+self.mytext[place+len(mystring):]
        mystring = '[ctrl]'
        while self.mytext.find(mystring) != -1:
            place = self.mytext.index(mystring)
            self.mytext = self.mytext[0:place]+'X'+self.mytext[place+len(mystring):]
        mystring = '[fn]'
        while self.mytext.find(mystring) != -1:
            place = self.mytext.index(mystring)
            self.mytext = self.mytext[0:place]+'F'+self.mytext[place+len(mystring):]
        mystring = '[f5]'
        while self.mytext.find(mystring) != -1:
            place = self.mytext.index(mystring)
            self.mytext = self.mytext[0:place]+'%'+self.mytext[place+len(mystring):]
        mystring = '[tab]'
        while self.mytext.find(mystring) != -1:
            place = self.mytext.index(mystring)
            self.mytext = self.mytext[0:place]+'Q'+self.mytext[place+len(mystring):]

    def qwertyconvert(self):
        """Converts each letter in self.mytext to qwerty"""
        realtext = ''
        for letter in self.mytext:
            realtext = realtext + self.getqwerty(letter)
        self.mytext = realtext

    def getqwerty(self, letter):
        """Converts a single letter to qwerty."""
        if str(letter) == 'q':
            return "'"
        elif str(letter) == 'w':
            return ','
        elif str(letter) == 'e':
            return '.'
        elif str(letter) == 'r':
            return 'p'
        elif str(letter) == 't':
            return 'y'
        elif str(letter) == 'y':
            return 'f'
        elif str(letter) == 'u':
            return 'g'
        elif str(letter) == 'i':
            return 'c'
        elif str(letter) == 'o':
            return 'r'
        elif str(letter) == 'p':
            return 'l'
        elif str(letter) == '[':
            return '/'
        elif str(letter) == ']':
            return '='
        elif str(letter) == "\\":
            return '\\'
        elif str(letter) == 'a':
            return 'a'
        elif str(letter) == 's':
            return 'o'
        elif str(letter) == 'd':
            return 'e'
        elif str(letter) == 'f':
            return 'u'
        elif str(letter) == 'g':
            return 'i'
        elif str(letter) == 'h':
            return 'd'
        elif str(letter) == 'j':
            return 'h'
        elif str(letter) == 'k':
            return 't'
        elif str(letter) == 'l':
            return 'n'
        elif str(letter) == ';':
            return 's'
        elif str(letter) == "'":
            return '-'
        elif str(letter) == 'z':
            return ';'
        elif str(letter) == 'x':
            return 'q'
        elif str(letter) == 'c':
            return 'j'
        elif str(letter) == 'v':
            return 'k'
        elif str(letter) == 'b':
            return 'x'
        elif str(letter) == 'n':
            return 'b'
        elif str(letter) == 'm':
            return 'm'
        elif str(letter) == ',':
            return 'w'
        elif str(letter) == '.':
            return 'v'
        elif str(letter) == '/':
            return 'z'
        elif str(letter) == '-':
            return '['
        elif str(letter) == '=':
            return ']'
        elif str(letter) == ' ':
            return ' '
        elif str(letter) == '1':
            return letter
        elif str(letter) == '2':
            return letter
        elif str(letter) == '3':
            return letter
        elif str(letter) == '4':
            return letter
        elif str(letter) == '5':
            return letter
        elif str(letter) == '6':
            return letter
        elif str(letter) == '7':
            return letter
        elif str(letter) == '8':
            return letter
        elif str(letter) == '9':
            return letter
        elif str(letter) == '0':
            return letter
        elif str(letter) == 'V':
            return letter
        elif str(letter) == '<':
            return letter
        elif str(letter) == 'U':
            return letter
        elif str(letter) == 'D':
            return letter
        elif str(letter) == 'L':
            return letter
        elif str(letter) == 'R':
            return letter
        elif str(letter) == 'E':
            return letter
        elif str(letter) == '?':
            return letter
        elif str(letter) == 'S':
            return letter
        elif str(letter) == 'X':
            return letter
        elif str(letter) == 'F':
            return letter
        elif str(letter) == '%':
            return letter
        elif str(letter) == 'Q':
            return letter
        else:
            return '('+letter+')'

    def getlog(self):
        """Gets the log and puts it in self.mytext"""
        file = open('/var/log/keystroke.log', 'r')
        self.mytext = file.read()
        file.close()

if __name__ == '__main__':
    z = letterProcessor()
    print('parse_logs: logging!')
    # z.parse_logs(option=1)
    # z.printkeys()
    print('logged... parse_logs')
