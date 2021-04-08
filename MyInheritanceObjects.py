from __future__ import print_function

import tkinter as tk
from tkinter import font,ttk
from tkinter.ttk import Style, Button, Label
import pandas as pd
import datetime as dt


try:
    from tkinter import tkfontchooser
except ImportError:
    print(ImportError.name)

def isInputInteger(s):
    return isinstance(s, int)

def isInput_a_year(s):
    if (isInputInteger(s)):
        yr = int(s)
        if len(s) > 4:
            return 'false'
        elif len(s) < 4:
            return 'true'
        else:
            thisyr = int(dt.datetime.now().strftime('%Y'))
            if yr in range(1825, thisyr):
                return 'true'
            else:
                return 'false'

class FontChooser(tk.Text):

    def __init__(self, *args, **kwargs):
        print(str(*args))
        self._text = tk.Text
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
            tk.messagebox(title = 'Chosen Font', text = font_str.replace('\ ', ' '))
            ##label.configure(font=font_str, text='Chosen font: ' + font_str.replace('\ ', ' '))




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


