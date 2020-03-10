from __future__ import print_function

import tkinter as tk
from tkinter import font,ttk
from tkfontchooser import askfont

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



#%%'''   class Font_wm(tk.Toplevel):   '''
"""
class Font_wm(tk.Toplevel):
    def __init__(self, Font=None):

        tk.Toplevel.__init__(self)
        self.mainfont = font.Font
        self.title('Font ...')
        
        obj = self.mainfont.actual(self, 'family')

        # Variable
        self.var = tk.StringVar()# For Font Face
        self.var.set(self.mainfont.actual(self, 'family'))
        self.var1 = tk.IntVar()  # for Font Size
        self.var1.set(self.mainfont.actual(self, 'size'))
        self.var2 = tk.StringVar() # For Bold
        self.var2.set(self.mainfont.actual(self, 'weight'))
        self.var3 = tk.StringVar() # For Italic
        self.var3.set(self.mainfont.actual(self, 'slant'))
        self.var4 = tk.IntVar()# For Underline
        self.var4.set(self.mainfont.actual(self, 'underline'))
        self.var5 = tk.IntVar() # For Overstrike
        self.var5.set(self.mainfont.actual(self, 'overstrike'))


        # Font Sample
        self.font_1 = tkFont.Font()
        for i in ['family', 'weight', 'slant', 'overstrike', 'underline', 'size']:
            self.font_1[i] = self.mainfont.actual(i)

        # Function
        def checkface(event):
            try:
                self.var.set(str(self.listbox.get(self.listbox.curselection())))
                self.font_1.config(family = self.var.get(), size = self.var1.get(), weight = self.var2.get(), slant = self.var3.get(), underline = self.var4.get(), overstrike = self.var5.get())
            except:
               pass
        def checksize(event):
            try:
                self.var1.set(int(self.size.get(self.size.curselection())))
                self.font_1.config(family = self.var.get(), size = self.var1.get(), weight = self.var2.get(), slant = self.var3.get(), underline = self.var4.get(), overstrike = self.var5.get())
            except:
                pass            
        def applied():
            self.result = (self.var.get(), self.var1.get(), self.var2.get(), self.var3.get(), self.var4.get(), self.var5.get())
            self.mainfont['family'] = self.var.get()
            self.mainfont['size'] = self.var1.get()
            self.mainfont['weight'] = self.var2.get()
            self.mainfont['slant'] = self.var3.get()
            self.mainfont['underline'] = self.var4.get()
            self.mainfont['overstrike'] = self.var5.get()
        def out():
            self.result = (self.var.get(), self.var1.get(), self.var2.get(), self.var3.get(), self.var4.get(), self.var5.get())
            self.mainfont['family'] = self.var.get()
            self.mainfont['size'] = self.var1.get()
            self.mainfont['weight'] = self.var2.get()
            self.mainfont['slant'] = self.var3.get()
            self.mainfont['underline'] = self.var4.get()
            self.mainfont['overstrike'] = self.var5.get()
            self.destroy()
        def end():
            self.result = None
            self.destroy()
            
        # Main window Frame
        self.mainwindow = ttk.Frame(self)
        self.mainwindow.pack(padx = 10, pady = 10)
        # Main LabelFrame
        self.mainframe = ttk.Frame(self.mainwindow)
        self.mainframe.pack(side = 'top',ipady = 30, ipadx = 30,expand = 'no', fill = 'both')
        self.mainframe0 = ttk.Frame(self.mainwindow)
        self.mainframe0.pack(side = 'top', expand = 'yes', fill = 'x', padx = 10, pady = 10)
        self.mainframe1 = ttk.Frame(self.mainwindow)
        self.mainframe1.pack(side = 'top',expand = 'no', fill = 'both')
        self.mainframe2 = ttk.Frame(self.mainwindow)
        self.mainframe2.pack(side = 'top',expand = 'yes', fill = 'x', padx = 10, pady = 10)
        # Frame in [  main frame]
        self.frame = ttk.LabelFrame(self.mainframe, text = 'Select Font Face')
        self.frame.pack(side = 'left', padx = 10, pady = 10, ipadx = 20, ipady = 20, expand = 'yes', fill = 'both')
        self.frame1 = ttk.LabelFrame(self.mainframe, text = 'Select Font size')
        self.frame1.pack(side = 'left', padx = 10, pady = 10, ipadx = 20, ipady = 20, expand = 'yes', fill = 'both')
        ttk.Entry(self.frame, textvariable = self.var).pack(side = 'top', padx = 5, pady = 5, expand = 'yes', fill = 'x')
        self.listbox = tk.Listbox(self.frame, bg = 'gray70')
        self.listbox.pack(side = 'top', padx = 5, pady = 5, expand = 'yes', fill = 'both')
        for i in tkFont.families():
            self.listbox.insert(tk.END, i)

        # Frame in [ 0. mainframe]
        self.bold = ttk.Checkbutton(self.mainframe0, text = 'Bold', onvalue = 'bold', offvalue = 'normal', variable = self.var2)
        self.bold.pack(side = 'left',expand = 'yes', fill = 'x')
        self.italic = ttk.Checkbutton(self.mainframe0, text = 'Italic', onvalue = 'italic', offvalue = 'roman',variable = self.var3)
        self.italic.pack(side = 'left', expand = 'yes', fill = 'x')
        self.underline = ttk.Checkbutton(self.mainframe0, text = 'Underline',onvalue = 1, offvalue = 0, variable = self.var4)
        self.underline.pack(side = 'left', expand = 'yes', fill = 'x')
        self.overstrike = ttk.Checkbutton(self.mainframe0, text = 'Overstrike',onvalue = 1, offvalue = 0, variable = self.var5)
        self.overstrike.pack(side = 'left', expand = 'yes', fill = 'x')
        
        # Frame in [ 1. main frame]
        ttk.Entry(self.frame1, textvariable = self.var1).pack(side = 'top', padx = 5, pady = 5, expand = 'yes', fill = 'x')
        self.size = tk.Listbox(self.frame1, bg = 'gray70')
        self.size.pack(side = 'top', padx = 5, pady = 5, expand = 'yes', fill = 'both')
        for i in range(30):
            self.size.insert(tk.END, i)

        tk.Label(self.mainframe1, bg = 'white',text = '''ABCDEabcde12345''', 
                 font = self.font_1).pack(expand = 'no', padx = 10,pady = 10)

        # Frame in [ 2. mainframe]
        ttk.Button(self.mainframe2, text = '   OK   ', command = out).pack(side = 'left', expand = 'yes', fill = 'x', padx = 5, pady = 5)
        ttk.Button(self.mainframe2, text = ' Cancel ', command = end).pack(side = 'left', expand = 'yes', fill = 'x', padx = 5, pady = 5)
        ttk.Button(self.mainframe2, text = ' Apply  ', command = applied).pack(side = 'left', expand = 'yes', fill = 'x', padx = 5, pady = 5)
        
        self.listbox.bind('<<ListboxSelect>>', checkface)
        self.size.bind('<<ListboxSelect>>', checksize)
        return
"""

'''
    class CustomText(tk.Text):
'''
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
        print(command, args, "=>", result)

        # Note: returning the result of the original command
        # is critically important!
        return result



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

'''
import Tkinter as tk

class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        """A text widget that reports on internal widget commands"""
        tk.Text.__init__(self, *args, **kwargs)

        # create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, command, *args):
        cmd = (self._orig, command) + args
        result = self.tk.call(cmd)

        if command in ("insert", "delete", "replace"):
            self.event_generate("<<TextModified>>")

        return result
'''