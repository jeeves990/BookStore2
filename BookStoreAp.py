
from BookStoreGui import *


'''
print('hello')
print(type(tk))
print('goodbye')
'''
root = tk.Tk()

appName = "Book Store Inventory: "

def setTitle(appendage=""):
    root.title(appName +str(appendage))

setTitle()

root['bd']=2
#root.wm_attributes("-topmost", 1)
winHeight = 550
winWidth = 750
'''
    win.resizable(0,0) makes the window fixed in geometry: width and height
'''

mainfrm = BookStoreBackFrameClass(root) 
#mainfrm.resizable(0,0)
mainfrm['height'] = winHeight
mainfrm['width'] = winWidth



bookStoreTopFrame = BookStoreTopFrameClass(mainfrm)
bookStoreTopFrame['height'] = 20
bookStoreTopFrame.grid(row=0, column=0, sticky='nwe', columnspan=4)

'''  
    the following two values: mainfrm.winfo_screenwidth() and 
                              mainfrm.winfo_screenheight()
        are the value in pixels of the monitor screen
'''
x = mainfrm.winfo_screenwidth() /2 - (winWidth /2)
y = mainfrm.winfo_screenheight() /2 - (winHeight / 2)
'''
    the following values: bookStoreTopFrame.winfo_reqwidth() and
                          bookStoreTopFrame.winfo_reqheight()   
        are the value in pixels of the obj's presentation on the monitor
'''
w = bookStoreTopFrame.winfo_reqwidth()
h = bookStoreTopFrame.winfo_reqheight()
#setColRowWeight(mainfrm) this seems to make the weights non-sticky


statusBar=BookStoreStatusBarClass(mainfrm)
statusBar.grid(row=8, column=0, sticky='ew')

print('win_size: ' +str(mainfrm.size()))
midFrame=BookStoreMidFrameClass(mainfrm, statusBar)
midFrame.grid(row=1, column=0,sticky='new')
midFrame.loadDummyData()

midFrame.lineNumbers.redraw()

root['menu'] = BuildMainMenu(root, midFrame)

mainfrm.grid(row=0, column=0)
setColRowWeight(midFrame)

print('mainfrm.winfo_geometry: ' +str(mainfrm.winfo_geometry))

#mainfrm.size() returns a tuple: column count, row count
print('win_size: ' +str(mainfrm.size()))
'''
    mainfrm.winfo_width() and mainfrm.winfo_height() return the width and height of the dialog in pixels
'''
print('mainfrm.winfo_width() :' +str(mainfrm.winfo_width()))
print('mainfrm.winfo_height() :' +str(mainfrm.winfo_height()))

'''
    mainfrm.geometry('%dx%d+%d+%d' % (winWidth, winHeight, x, y))  
        ## this makes the window remain the same regardless of the widgets added.

    mainfrm.geometry('+%d+%d' % (x, y))  
        ## this is nice. It permits tkinter to adjust the size of the main window 
        to accomodate the widgets present
'''
root.geometry('+%d+%d' % (x, y))  ## this is nice. It permits tkinter to adjust the size of the main window


    
root.mainloop()


'''
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = Message(win, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.bind('<Motion>',motion)
msg.grid(row=0, column=0)
'''
