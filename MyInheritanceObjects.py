from __future__ import print_function

import tkinter as tk
from tkinter import font,ttk
from tkinter.ttk import Style, Button, Label
import pandas as pd
import datetime as dt


try:
    from tkfontchooser import askfont
except ImportError:
    print(ImportError.name)

yrRangeStart = 1825

def isInputAnInteger(s):
    try:
        int(s)
        return True
    except:
        return False
    

def testVal(inStr,acttyp):
    if acttyp == '1': #insert
        if not inStr.isdigit():
            return False
    return True


def isPartialYear(yearRange, ifAllowed):
    try:  # if the ifAllowed parameter cannot be converted to an integer, return false
        int(ifAllowed)
    except:
        return False
    # assume: yearRange is a list
    # ifAllowed is the input string as of now. Assume it represents an integer
    # reorder yearRange, if necessary.
    if (yearRange[0] > yearRange[1]):
        kpYr = yearRange[0]
        yearRange[0] = yearRange[1]
        yearRange[1] = kpYr

    ln = len(ifAllowed)
    if (ln > 4):
        return False
    a = str(yearRange[0])
    a = a[:ln]
    b = str(yearRange[1])
    b = b[:ln]

    if ((ifAllowed >= a) and (ifAllowed <= b)):
        return True
    else:
        return False


def isInputAYear(ifAllowed, priorS):
    #localS = char_.get()
    #localStr = str_.get()
    if (isInputAnInteger(ifAllowed)):
        # the input is an integer

        thisyr = int(dt.datetime.now().strftime('%Y'))
        yr = int(ifAllowed)
        yearRange = [yrRangeStart, thisyr]  # a list

        if len(ifAllowed) > 4:     # input is too short to be a year
            return False
        #elif len(ifAllowed) < 4:   # input may be a year, just too short
        else:
            return isPartialYear(yearRange, ifAllowed)

    else:   ## if the input is not an integer, return False
        return False


def countWords_n_string(str):

    # Here we are removing the spaces from start and end,
    # and breaking every word whenever we encounter a space
    # and storing them in a list. The len of the list is the
    # total count of words.
    return (len(str.strip().split(" ")))


def countWords(longS):
    lst = (longS.strip().splitlines(longS))
    i = 0
    for ln in lst:
        newlst = re.split(r'[-,\s]\s*',ln)
        i += len(newlst)


def countChars(s):
    i = 0
    for ln in s:
        i += 1
    return i


def select_all(event=None):
    content_text.tag_add('sel', '1.0', 'end')
    return "break"

#%% class FontChooser
class FontChooser(str):
    def __init__(self, txtobj):
        self._text = txtobj
        self.callback()
        return

    def callback(self):
        # open the font chooser and get the font selected by the user
        font = askfont(self._text)
        # font is "" if the user has cancelled
    
        if font:
            # spaces in the family name need to be escaped
            font['family'] = font['family'].replace(' ', '\ ')
            font_str = "%(family)s %(size)i %(weight)s %(slant)s" % font
            if font['underline']:
                font_str += ' underline'
            if font['overstrike']:
                font_str += ' overstrike'
            ##tk.messagebox(title = 'Chosen Font', text = font_str.replace('\ ', ' '))
            ##label.configure(font=font_str, text='Chosen font: ' + font_str.replace('\ ', ' '))
            return font_str

        return font


#%%
'''    class CustomText(tk.Text):    '''
class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        """A text widget that report on internal widget commands"""
        tk.Text.__init__(self, *args, **kwargs)

        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self.proxy)

    def proxy(self, command, *args):
        # this lets' tkinter handle the command as usual
        cmd = (self._orig, command) + args
        result = self.tk.call(cmd)

        #order = self.area.bindtags()
        #self.area.bindtags((order[1], order[0], order[2], order[3]))

        if command in ("insert", "delete", "replace"):
            self.event_generate("<<TextModified>>")


        # here we just echo the command and result
        #print(command, args, "=>", result)

        # Note: returning the result of the original command
        # is critically important!
        return result


#%%
"""
    a CustomText box with an event which fires when the text is modified.
    https://stackoverflow.com/questions/40617515/python-tkinter-text-modified-callback
    I was unable to make this work
"""
class anotherCustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        """A text widget that reports on internal widget commands"""
        super().__init__()
        ##super().__init__(self, *args, **kwargs)

        # create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

        

    def _proxy(self, command, *args):
        cmd = (self._orig, command) + args
        result = self.tk.call(cmd)

        return result

class WordCount(int):
    def __init__(self, *args, **kwargs):
        return

def donothing():
    return
