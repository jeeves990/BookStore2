
from BookStoreGui import *



'''
print('hello')
print(type(tk))
print('goodbye')
'''
win = tk.Tk()

appName = "Book Store Inventory: "

def setTitle(appendage=""):
    win.title(appName +str(appendage))

setTitle()
#win.wm_title("Book Store Inventory")

win['bd']=2
#win['relief'] = RIDGE
win.wm_attributes("-topmost", 1)
winHeight = 550
winWidth = 750
'''
    win.resizable(0,0) makes the window fixed in geometry: width and height
'''
#win.resizable(0,0)
bookStoreTopFrame = BookStoreTopFrameClass(win)
bookStoreTopFrame.grid(row=0, column=0, sticky='nwe', columnspan=4)

'''
    the following two values: win.winfo_screenwidth() and 
                              win.winfo_screenheight()
        are the value in pixels of the monitor screen
'''
x = win.winfo_screenwidth() /2 - (winWidth /2)
y = win.winfo_screenheight() /2 - (winHeight / 2)
'''
    the following values: bookStoreTopFrame.winfo_reqwidth() and
                          bookStoreTopFrame.winfo_reqheight()   
        are the value in pixels of the obj's presentation on the monitor
'''
w = bookStoreTopFrame.winfo_reqwidth()
h = bookStoreTopFrame.winfo_reqheight()
#setColRowWeight(win) this seems to make the weights non-sticky


statusBar=BookStoreStatusBarClass(win)
statusBar.grid(row=8, column=0, sticky='ew')

print('win_size: ' +str(win.size()))
mainFrame=BookStoreMainFrameClass(win, statusBar)
mainFrame.grid(row=1, column=0,sticky='new')
mainFrame.loadDummyData()

mainFrame.lineNumbers.redraw()

setColRowWeight(mainFrame)

print('win.winfo_geometry: ' +str(win.winfo_geometry))

#win.size() returns a tuple: column count, row count
print('win_size: ' +str(win.size()))
'''
    win.winfo_width() and win.winfo_height() return the width and height of the dialog in pixels
'''
print('win.winfo_width() :' +str(win.winfo_width()))
print('win.winfo_height() :' +str(win.winfo_height()))



'''
    win.geometry('%dx%d+%d+%d' % (winWidth, winHeight, x, y))  ## this makes the window remain the same regardless of the widgets added.

    win.geometry('+%d+%d' % (x, y))  ## this is nice. It permits tkinter to adjust the size of the main window to accomodate the widgets present
'''
win.geometry('+%d+%d' % (x, y))  ## this is nice. It permits tkinter to adjust the size of the main window


    
'''
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = Message(win, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.bind('<Motion>',motion)
msg.grid(row=0, column=0)
'''
win.mainloop()


