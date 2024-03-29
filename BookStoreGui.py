

from MyInheritanceObjects import CustomText, FontChooser, isInputAnInteger, isInputAYear 
from MyInheritanceObjects import countChars, countWords, countWords_n_string, donothing
import tkinter as tk
from tkinter import *
import tkinter.messagebox as MSGBOX
import tkinter.filedialog as fd
import re
from tkfontchooser import askfont
import pyperclip as pc

txObjBackground = 'cyan'


def setColRowWeight(obj):
    colCount, rowCount = obj.grid_size()

    for i in range(rowCount):
        obj.grid_rowconfigure(i, weight=1)

    for i in range(colCount):
        obj.grid_columnconfigure(i, weight=1)





"""
The BookStoreGui has a "main" frame [BookStoreBackFrameClass]
    which contains comprised of three components: 
        BookStoreTopFrameClass,
        BookStoreMidFrameClass,
        BookStoreStatusBarClass.
These elements are arranged vertically in the order written above.
"""
#%%  BookStoreBackFrameClass(tk.Canvas):
class BookStoreBackFrameClass(tk.Canvas):
    """
    this frame is the base widget upon which all other widgets are created
    """
    def __init__(self, root):
        super().__init__()
        self.__Parent = root
        #self['height']= root.winfo_height
        #self['width'] = root.winfo_width
        self['bd'] = 2
        self['bg'] = 'navy'
        self.configure(scrollregion=(0, 0, self['height'], self['width']))
        #root['menu'] = BuildMainMenu(root)

        return


#%%  BookStoreMidFrameClass(tk.Frame):
class BookStoreMidFrameClass(tk.Canvas):
    """
    this "midFrame" has two major components: a list box on the left and a panel of buttons on the right
    """
    def __init__(self, mfrm, sBar):
        super().__init__(master=mfrm)
        self.mfrm_height=500
        self.mfrm_width=500
        #self.__Parent = mfrm
        self['height']= self.mfrm_height
        self['width'] = self.mfrm_width
        self['bd'] = 2
        self['relief'] = tk.RIDGE
        self['bg'] = '#b8d7a8'
        #self['bg'] = 'red'
        #self.configure(scrollregion=(0, 0, self.mfrm_height, self.mfrm_width))

        self.bldTextBoxFrame(sBar, mfrm)
        
        #self.bldMainMenu(mfrm)  ## this was moved into class BuildMainMenu()  ##
        self.sbar = sBar  ## for updating the statusbar
        self.lineNumbers = TextLineNumbers(self.txObj)
        self.lineNumbers.attach(self.txObj)
        self.mfrm = mfrm
        self._flag_text_changed = False
        self.bldPopupMenu()
        self.bindRightMouseBtnToPopupMenu()

    currentDirectory = ""        


    def doSelectFont(self):
        ## TODO: select from font dialog
        theFont = FontChooser()
        print(theFont)
        self.txObj['font'] = theFont
        return
       
    def doCopy(self):
        return

    def doCut(self):
        return

    def doPaste(self):
        return

    def doSelectAll(self):
        return

    def edit_undo(self):
        return
    def edit_redo(self):
        return
    def edit_modified(self):
        return

    def bldPopupMenu(self):

        self.popupMenu = tk.Menu(self.txObj)
        self.popupMenu.add_command(label="Copy", command = self.doCopy)

        self.popupMenu.add_command(label="Cut", command = self.doCut)
        self.popupMenu.add_command(label="Paste", command=self.doPaste)
        self.popupMenu.add_separator()
        self.popupMenu.add_command(label="Select All", command=self.doSelectAll)
        self.popupMenu.add_separator()
        self.popupMenu.add_command(label = "Choose Font", command = self.doSelectFont)

        return
    
    def bindRightMouseBtnToPopupMenu(self):
        self.txObj.bind("<Button-3>", self.show_menu_)
        return

    def show_menu_(event):
        self.popupMenu.tk_popup(event.x, event.y)
        return


    def enDisAbleEditing(self):
        if self.txObj['state']=='normal':
            global txObjBackground
            txObjBackground = self.txObj['bg']
            self.txObj['state']= 'disabled'
            self.txObj['bg'] = 'light gray'
        else:
            self.txObj['state'] = 'normal'
            self.txObj['bg'] = txObjBackground
        return

    
    def __quit__(self, event=None):
        print('hello from BookStoreMidFrameClass.__quit__')
        super().quit()
         
    """
        def bldTextBoxFrame(self)
        this frame contains three objects: the text box for displaying the book rows;
                                           a horizontal scrollbar;
                                           a vertical scroll bar

                                       
                c.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

                c.grid(row=0, column=0, sticky="nsew")
    """
 
    def motion(self, event):
        ###print("Mouse position: (%s %s)" % (event.x, event.y))
        self.sbar.setMousePosition("(%s:%s)" % (event.x, event.y))
        return

    
    '''
        TODO: have loadDummyData() check for line numbers and add to them
    '''
    def loadDummyData(self):
        '''  check last row in self.txObj; if it begins with 5 digit integer, query to extend  '''
        for i in range(100):
            self.txObj.insert(tk.END,  format(i, '0>5') +'\tnow is the time for all good men to come to the aid of their party\n')    
        self.lineNumbers.redraw()
        pass

    def clearData(self):
        msgbox = MSGBOX.askquestion ('Clear Text Data','Are you sure you want to delete all of this data?',icon = 'warning')
        
        if msgbox == 'yes':
            self.txObj.delete('1.0', tk.END)
        return

    def check_pos(self, event):
        #print(self.txObj.index(tk.INSERT))
        self.sbar.setPosition(self.txObj.index(tk.INSERT))

    def countCharacters(self):
        i = 0
        for ln in self.txObj:
            i += len(ln)
        self.sbar.setCharCount(i)

    def bldTextBoxFrame(self, sbar, mfrm):
        self.txBoxWidth = int(float(self['width'])/6/10)
        self.txBoxHeight= int(float(self['height'])/6/10)
        self.txBoxFrame = tk.Canvas(self,
                                      height= self.txBoxHeight,
                                      width = self.txBoxWidth, 
                                      bd=2,
                                      relief=tk.RAISED,
                                      bg='light blue')
        self.configure(scrollregion=(0,0, self.txBoxHeight, self.txBoxWidth))



        '''
            the event handler for the key press event of the text object (txObj)
            I was surprised that sbar was recognized. To wit, the statusbar object 
            was passed to this class in the manager program.
        '''

       
        #self.txObj is the actual Text object  
        ###txObjBackground = 'cyan'
        self.txObj = CustomText(self.txBoxFrame, font='Times 10', background=txObjBackground, undo=True)
        #self.txObj = tk.Text(self.txBoxFrame, font='Times 10', background=txObjBackground, undo=True)
        self.txObj['font'] = ("Helvetica", "12")
        self.txObj['wrap'] = None
        self.txObj.bindtags(('Text','post-class-bindings', '.', 'all'))

        self.txObj.bind_class("post-class-bindings", "<KeyPress>", self.check_pos)
        self.txObj.bind_class("post-class-bindings", "<Button-1>", self.check_pos)
        self.txBoxFrame.create_window((0, 0), anchor='nw', window=self.txObj)
        
        self.txObj.grid(row=0, column=0, sticky='news', columnspan=4)
        
        ##self.txObj.bind('<Motion>', self.motion)

        
        bindtags = list(self.txObj.bindtags())
        bindtags.insert(2, "mousePosition")
        self.txObj.bindtags(tuple(bindtags))
        self.txObj.bind_class("mousePosition", "<Motion>", self.motion)

        #       vsb = Scrollbar(t, orient="v", command=c.yview)
        #       hsb = Scrollbar(t, orient="h", command=c.xview)
        '''
            ???the following changes had no APPARENT effect???
        '''
        ##vsb=tk.Scrollbar(self.txBoxFrame, orient=tk.HORIZONTAL, command=self.txObj.yview(), width=16)
        vsb=tk.Scrollbar(self.txBoxFrame, orient=tk.HORIZONTAL, command=self.yview(), width=16)
        ##hsb=tk.Scrollbar(self.txBoxFrame, orient=tk.VERTICAL, command=self.txObj.xview(), width=16)
        hsb=tk.Scrollbar(self.txBoxFrame, orient=tk.VERTICAL, command=self.txObj.xview(), width=16)
   
    
        ##vsb.grid(row=1, column=0, sticky='news')
        hsb.grid(row=0, column=6, sticky='news')
        
        # make sure everything is displayed before configuring the scrollregion
        self.update_idletasks()

        '''
        self.txObj.configure(scrollregion=self.bbox('all'), 
                 yscrollcommand=hsb.set, 
                 xscrollcommand=vsb.set)
        '''

        self.txBoxFrame.grid(row=2, column=0, sticky='nws')
        self.bldButtonFrame(self.txBoxFrame).grid(row=0, column=10, sticky='news')
        self.txBoxFrame.bind("<Configure>", self.onFrameConfigure)
        '''
            moved this following command from above and it made no difference
        '''
        ##self.txObj.configure(scrollregion=self.bbox('all'), 
        self.txObj['yscrollcommand'] = hsb.set
        self.txObj['xscrollcommand'] = vsb.set
        ##self.txObj.configure(yscrollcommand=hsb.set, 
        ##                     xscrollcommand=vsb.set)

        '''
        self.txBoxFrame.grid_propagate('False')  ## this prevents the button frame from being attached to 
        Tried putting it above self.bldButtonFrame (above) and the effect was the same    
        '''
        
    def onFrameConfigure(self, event):
        self.txObj.configure(scrollregion = self.bbox('all'))
        return

    #def countlines(self, event):
    #    (line, c) = map(int, self.txObj.index("end-1c").split("."))
    #    print('countlines: ', line, c)
    #    self.sbar.setLineCount(str(line))
    #    self.sbar.setCharCount(str(c))
    #    return

    '''
             def updateCount(self)
    '''
    def doUpdateCount(self): # without "event"
        s = self.txObj.count('1.0', "end", "displaylines")
        print("displaylines: ", s)
        s1 = self.txObj.count("1.0", "end", "lines")
        tpl=int(float(self.txObj.index('end-1c').split('\n\r')[0]))
        print(format("lines: {}".format( tpl)))

        #self.txObj.get('1.0', "end") returns all the characters in the Text.txObj
        s = self.txObj.get('1.0', "end")
        charcnt = countChars(s)
        print(format("Characters: {}".format(charcnt)))
        self.sbar.setCharCount(charcnt)

        # to get work count take the s string above and split it on \r\n
        wordcount = countWords_n_string(s)

        self.sbar.wordCntVar.set(wordcount)
        self.sbar.setWordCount(wordcount)

        self.sbar.lineCntVar.set(tpl)
        self.sbar.setLineCount(tpl)

        return

    def doQuit(self, event=None):
        print('hello from doQuit')
        self.__quit__()

        
    def bldButtonFrame(self, ownerFrame):
        btnFrameHeight=int(self['height'])-4
        btnFrameWidth=int(self['width'])-4
        
        btnFrame = tk.LabelFrame(ownerFrame, height=btnFrameHeight, width=btnFrameWidth, relief=tk.RAISED)

        btnHeight = int(float(ownerFrame['height'])/6/10)
        btnWidth = 15
        viewButton = tk.Button(btnFrame, height=btnHeight, width=btnWidth, relief=tk.RIDGE, text='View All', justify=tk.CENTER)
        srchButton = tk.Button(btnFrame, height=btnHeight, width=btnWidth, relief=tk.RIDGE, text='Search')
        add_Button = tk.Button(btnFrame, height=btnHeight, width=btnWidth, relief=tk.RIDGE, text='Add')
        upd_Button = tk.Button(btnFrame, height=btnHeight, width=btnWidth, relief=tk.RIDGE, text='Update')
        deleButton = tk.Button(btnFrame, height=btnHeight, width=btnWidth, relief=tk.RIDGE, text='Delete')

        updCntBtn = tk.Button(btnFrame, height=btnHeight, width=btnWidth, relief=tk.RIDGE,
                              text='Update Count', command=self.doUpdateCount)
      
        closButton = tk.Button(btnFrame, height=btnHeight, width=btnWidth, relief=tk.RIDGE,
                               text='Close', command=self.doQuit)
        ##closButton.bind("<Button-1>", self.doQuit)


         

        viewButton.grid(row=0, column=0)
        srchButton.grid(row=1, column=0)
        add_Button.grid(row=2, column=0)
        upd_Button.grid(row=3, column=0)
        deleButton.grid(row=4, column=0)
        closButton.grid(row=6, column=0)
        updCntBtn.grid(row=5, column=0)
        #updCntBtn.bind_class("post-class-bindings", "<ButtonPress>", self.updateCount)
        #updCntBtn.invoke()

        return(btnFrame)


'''
    class TextLineNumbers(tk.Canvas) what does this do?
    https://stackoverflow.com/questions/16369470/tkinter-adding-line-number-to-text-widget
'''
class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: 
                break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2,y,anchor="nw", text=linenum)
            i = self.textwidget.index("%s+1line" % i)


#%%  BookStoreTopFrameClass(tk.Frame)
class  BookStoreTopFrameClass(tk.Frame):
    def __init__(self, mfrm):
        super().__init__(mfrm)  ## provide the master
        self['height']=26
        self['width']= mfrm.winfo_width()
        self['bd']=4
        #self['relief']=RAISED
        self['bg']='#cccccc'
        self.grid_rowconfigure(0, weight = 3)

        self.grid_rowconfigure(1, weight=3)
        #self['text']='BookStoreTopFrameClass'  this was for LabelFrame
        self.bldCapsNEntries()
        

    def  bldCapsNEntries(self):
        lblHtValue= 1
        lblWdValue=20
        lblBgValue=self['bg']
        lblBdrWd = 3
        lblBrdRelief = 'ridge'
        lblFont = 'Times 10 bold'

        editframe = tk.Frame(self)
        self.ttlLbl = tk.Label(editframe, width=lblWdValue, justify=tk.RIGHT,
                               height=lblHtValue,
                               text='Title', font=lblFont,
                               bg=lblBgValue,
                               borderwidth=lblBdrWd,
                               relief=lblBrdRelief)
        self.yearLbl = tk.Label(editframe, width=lblWdValue,
                                height=lblHtValue, text='Year', font=lblFont,
                                bg=lblBgValue,
                                borderwidth=lblBdrWd,
                                relief=lblBrdRelief)

        self.authLbl = tk.Label(editframe, width=lblWdValue,
                                height=lblHtValue,text='Author', font=lblFont,
                                bg=lblBgValue,
                                borderwidth = lblBdrWd,
                                relief = lblBrdRelief)

        self.ISBNLbl = tk.Label(editframe, width=lblWdValue,
                                height=lblHtValue,text='ISBN', font=lblFont,
                                bg=lblBgValue,
                                borderwidth = lblBdrWd,
                                relief = lblBrdRelief)


        self.ttlLbl.grid(row=0, column=0)
        self.ttlLbl.grid_rowconfigure(0, weight = 1)

        self.authLbl.grid(row=1, column=0)
        self.authLbl.grid_rowconfigure(0, weight=1)

        self.yearLbl.grid(row=2, column=0)
        self.yearLbl.grid_rowconfigure(0, weight = 1)

        self.ISBNLbl.grid(row=3, column=0)
        self.ISBNLbl.grid_rowconfigure(0, weight = 1)

        entryHtValue = 1
        entryWdValue = 45
        entryBgValue = '#ead1dc'
        self.ttlEntry = tk.Entry(editframe, width=entryWdValue, justify=tk.LEFT, text='Title',
                               font='Times 10', bg=entryBgValue)

        self.authEntry = tk.Entry(editframe, width=entryWdValue, justify=tk.LEFT, text='Author',
                                font='Times 10',
                                bg=entryBgValue)

        #################################################################################
        # two ways to validate: 
        #   1st: with tk.StringVar(), trace anonymous function and declare textvariable
        #   in declaration of tk.Entry.
        #################################################################################
        #yearentrySV = tk.StringVar()
        #yearentrySV.trace('w', lambda nm, idx, mode, var=yearentrySV: isInput_a_year(var))
        #################################################################################
        #   2nd: register'ed function and declaration in tk.Entry declaration of
        #       validate = 'key', validatecommand = ()
        #       '%S' - passes key entered to validatecommand.
        #################################################################################
        check4year = self.register(isInputAYear)
        self.yearEntry = tk.Entry(editframe, width=entryWdValue, justify=tk.LEFT, text='Year',
                                font='Times  10',
                                bg=entryBgValue,
                                #textvariable = yearentrySV);
                                validate = 'key',
                                validatecommand = (check4year, '%P', '%s'))
        #################################################################################
        # valid percent substitutions (from the Tk entry man page)
        # note: you only have to register the ones you need; this
        # example registers them all for illustrative purposes
        #
        # %d = Type of action (1=insert, 0=delete, -1 for others)
        # %i = index of char string to be inserted/deleted, or -1
        # %P = value of the entry if the edit is allowed
        # %s = value of entry prior to editing
        # %S = the text string being inserted or deleted, if any
        # %v = the type of validation that is currently set
        # %V = the type of validation that triggered the callback
        #      (key, focusin, focusout, forced)
        # %W = the tk name of the widget
        #################################################################################
        # OnValidate: user entered "asdf"
        # #d='1'
        # #i='3'
        # #P='asdf'
        # #s='asd'
        # #S='f'
        # #v='key'
        # #V='key'
        # #W='.!example.!entry'
        #################################################################################
        

        self.ISBNEntry = tk.Entry(editframe, width=entryWdValue,justify=tk.LEFT, text='ISBN',
                                font='Times 10',
                                bg=entryBgValue)

        sv = tk.StringVar()
        ent = Entry(editframe, textvariable=sv)


        self.ttlEntry.grid(row=0, column=1)
        self.authEntry.grid(row=1, column=1)

        self.yearEntry.grid(row=2, column=1)
        self.ISBNEntry.grid(row=3, column=1)

        setColRowWeight(self)
        self.grid_rowconfigure(0, weight = 2 )
        editframe.grid(row = 0, column =0)
        self.ttlEntry.focus_set()

        return self



#%%  BookStoreStatusBarClass(tk.Frame):
class BookStoreStatusBarClass(tk.Frame):
    def __init__(self, mfrm):
        super().__init__(master=mfrm)
        #self['height'] = 53
        self['width'] = mfrm.winfo_width()
        self['bd'] = 2
        self['relief'] = tk.SUNKEN
        self['bg'] = 'black'
        #self['relwidth'] = 1
        #, relheight = 1
        print('width of statusbar: ' +str(self['width']))
        self.buildLabels()


    def buildLabels(self):
        
        lblHtValue= 1
        lblWdValue=6

        self.wordCntVar = tk.StringVar()
        self.wordCntCap = tk.Label(self, width=lblWdValue, height=lblHtValue, background= 'light blue',
                                    relief=tk.RAISED, text='Words: ')
        self.wordCntLbl = tk.Label(self, width=lblWdValue, height=lblHtValue, background= 'cyan',
                                    relief = tk.SUNKEN, textvariable=self.wordCntVar)

        self.charCntVar = tk.StringVar()
        self.charCntCap = tk.Label(self, width=lblWdValue, height= lblHtValue, background= 'light blue',
                                    relief = tk.RAISED, text='Chars: ')
        self.charCntLbl = tk.Label(self, width=lblWdValue, height= lblHtValue, background= 'cyan',
                                    relief=tk.SUNKEN, textvariable=self.charCntVar)
        
        self.lineCntVar = tk.StringVar()
        self.lineCntCap = tk.Label(self, width=lblWdValue, height= lblHtValue, background= 'light blue',
                                    relief=tk.RAISED, text='Lines: ')
        self.lineCntLbl = tk.Label(self, width=lblWdValue, height= lblHtValue, background= 'cyan',
                                    relief=tk.SUNKEN, textvariable=self.lineCntVar)

        self.positionVar = tk.StringVar()
        self.positionCap = tk.Label(self, width=lblWdValue+3, height= lblHtValue, background= 'light blue',
                                    relief=tk.RAISED, text='Position: ')
        self.positionLbl = tk.Label(self, width=lblWdValue+3, height= lblHtValue, background= 'cyan',
                                    relief=tk.SUNKEN, textvariable=self.positionVar)
      

        self.mousePosVar = tk.StringVar()
        self.mousePosCap = tk.Label(self,  width=lblWdValue +6, height= lblHtValue, background= 'light blue',
                                    relief=tk.RAISED, text='Mouse Position: ')
        self.mousePosLbl =  tk.Label(self, width=lblWdValue+6, height= lblHtValue, background= 'cyan',
                                        relief=tk.SUNKEN, textvariable=self.mousePosVar)
        self.config_n_grid()
        return self


    def config_n_grid(self):
        self.wordCntLbl.config(justify=tk.RIGHT)
        self.charCntLbl.config(justify=tk.RIGHT)
        self.lineCntLbl.config(justify=tk.RIGHT)
        self.wordCntCap.config(justify=tk.RIGHT)
        self.charCntCap.config(justify=tk.RIGHT)
        self.lineCntCap.config(justify=tk.RIGHT)
        self.positionCap.config(justify=tk.RIGHT)

        
        self.wordCntCap.grid(row=0, column=0)
        self.wordCntLbl.grid(row=1, column=0)
       
        self.charCntCap.grid(row=0, column=1)
        self.charCntLbl.grid(row=1, column=1)
       
        self.lineCntCap.grid(row=0, column=2)
        self.lineCntLbl.grid(row=1, column=2)
        
        self.positionCap.grid(row=0, column=3)
        self.positionLbl.grid(row=1, column=3)

        self.mousePosCap.grid(row=0, column=4)
        self.mousePosLbl.grid(row=1, column=4)
        

        '''
        print('BookStoreStatusBarClass.width: ' +str(self['width']))
        print('self.wdCntLbl.width = ' +str(self.wdCntLbl['width']))
        print('self.charCnt.width = ' +str(self.charCnt['width']))
        print('self.wdCntLbl.height = ' +str(self.wdCntLbl['height']))
        print('self.charCnt.height = ' +str(self.charCnt['height']))
        '''
        self.setLineCount(0)


    def setMousePosition(self, position):
        self.mousePosVar.set(str(position))

    def setCharCount(self, cnt):
        self.charCntVar.set(str(cnt))

    def setLineCount(self, cnt):
        a = self.lineCntVar.get()
        self.lineCntVar.set(str(cnt))

    def setWordCount(self, cnt):
        self.wordCntVar.set(str(cnt))

    def setPosition(self, pos):
        self.positionVar.set(str(pos))
        

    def getPosition(self):
        s = self.positionLbl['text']
        if not s:
            return 'no value'
        
        return self.positionLbl['text'] 


class BuildMainMenu(tk.Menu):
    def __init__(self, root, midFr):
        super().__init__()
        self._midfr = midFr
        self['tearoff'] = 0
        self.root = root
        self.constructMenu()
        return

    def constructMenu(self):
        #menubar = tk.Menu(mfrm)
        #menu = tk.Menu(menubar, tearoff=0)
        filemenu = tk.Menu(self, tearoff=0)
        filemenu.add_command(label="New", command = self.newFileName)
        filemenu.add_command(label="Open", command = self.openFileName)
        filemenu.add_command(label="Save", command = donothing)
        filemenu.add_command(label="Choose Directory", command = self.chooseDirectory)
        filemenu.add_command(label="Save as...", command = donothing)
        filemenu.add_command(label="Close", command = donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command = self.exitApp)

        self.add_cascade(label="File", menu=filemenu)

        '''
            edit_modified(arg=None) [#]
            The edit_modified method.
        '''
        editmenu = tk.Menu(self, tearoff=0)
        editmenu.add_command(label="Undo", command = self._midfr.edit_undo)
        editmenu.add_command(label="Redo", command = self._midfr.edit_redo)
        editmenu.add_command(label="Modified", command = self._midfr.edit_modified)

        editmenu.add_separator()

        editmenu.add_command(label="Cut", command = donothing)
        editmenu.add_command(label="Copy", command = donothing)
        editmenu.add_command(label="Paste", command = donothing)
        editmenu.add_command(label="Delete", command = donothing)
        editmenu.add_command(label="Select All", command = donothing)

        editmenu.add_separator()
        editmenu.add_command(label='Toggle edit', command = self._midfr.enDisAbleEditing)
        self.add_cascade(label="Edit", menu=editmenu)

        viewmenu = tk.Menu(self)
        viewmenu.add_separator()
        viewmenu.add_command(label = 'Change Font', command = self._midfr.doSelectFont)
        
        self.add_cascade(label = 'View', menu = viewmenu)


        datamenu = tk.Menu(self, tearoff=0)
        datamenu.add_separator()
        datamenu.add_command(label="Load dummy data", command = self._midfr.loadDummyData)
        datamenu.add_separator()
        datamenu.add_command(label="Clear data", command = self._midfr.clearData)
        self.add_cascade(label="Data", menu=datamenu)
        
        helpmenu = tk.Menu(self, tearoff=0)
        helpmenu.add_command(label="Help Index", command = donothing)
        helpmenu.add_command(label="About...", command = self.postAbout)
        self.add_cascade(label="Help", menu=helpmenu)

        return self

        
    def postAbout(self):
        MSGBOX.showinfo("About", " About Book Store Application")

    def openFileName(self):
        name = fd.askopenfilename(
            ##filetypes=(
            ##("Template files", "*.tplate"),
            ##                           ("HTML files", "*.html;*.htm"),
            ##                           ("All files", "*.*") )
        )
        if name:
            try:
                print("""here it comes: self.settings["template"].set(name)""")
                print(mfrm['title'])
                mfrm.title(appName + name)
            except:                     # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % name)
        return


    def chooseDirectory(self):
        name=fd.askdirectory()
        print(name)
        currentDirectory = name

    def newFileName(self):
        ##name= fd.askopenfilename(typename{'*.*'}) 
        '''
            if self.txObj.text has "stuff", ask to save or not.
        '''
        return

    def exitApp(self):
        MsgBox = MSGBOX.askquestion ('Exit Book Store App','Are you sure you want to exit?',icon = 'warning')
        if MsgBox == 'yes':
            self.mfrm.destroy()
        else:
            MSGBOX.showinfo('Return','You will now return to the application screen')
    
 