try:
    from tkinter import *
    from tkinter import ttk
except:
    from Tkinter import *
    import ttk
import sys
import request

def shon(tab):
    tab.vp.shutterOn()
    setstat(tab)

def shoff(tab):
    tab.vp.shutterOff()
    setstat(tab)

def toggle(tab):
    if tab.vp.st_shutter=="On":
        tab.vp.shutterOff()
    else:
        tab.vp.shutterOn()
    setstat(tab)

def stat(tab):
    tab.vp.getStatus()
    setstat(tab)

def setstat(tab):
    online=True
    if tab.vp.st_shutter=='Off':
        tab.btno.config(relief=SUNKEN)
        tab.btnf.config(relief=RAISED)
    elif tab.vp.st_shutter=='On':
        tab.btnf.config(relief=SUNKEN)
        tab.btno.config(relief=RAISED)
    else:
        tab.btnf.config(relief=RAISED)
        tab.btno.config(relief=RAISED)
        online=False

    tab.strstatus.set(tab.vp.strStatus())
    if not online:
        tab.lbstat.config(fg="red")
    else:
        tab.lbstat.config(fg='black')

# NOT CLEVER AT ALL
def shall(listtab):
    for vp in listVP:
        vp.shutterOn()
    for tab in listtab:
        setstat(tab)

def opall(listtab):
    for vp in listVP:
        vp.shutterOff()
    for tab in listtab:
        setstat(tab)

def swall(listtab):
    for vp in listVP:
        if vp.st_shutter=="On":
            vp.shutterOff()
        else:
            vp.shutterOn()
    for tab in listtab:
        setstat(tab)

print("Connecting to hosts")
listVP=[request.VP('192.168.0.4'),
request.VP('192.168.0.8')]
print("All hosts initialised")
window = Tk()

window.title("Panasonic Remote GUI")
window.geometry('350x200')

tabctrl=ttk.Notebook(window)
lball=Label(window,text="Send all: ")
listTab=[]
btallsh=Button(window, text="SHUT",command=lambda: shall(listTab))
btallop=Button(window, text="OPEN",command=lambda: opall(listTab))
btallsw=Button(window, text="SWITCH",command=lambda: swall(listTab))
# "ALL [SHUT] [OPEN] [SWITCH]"
class tkTab(object):
    """A tk tab"""
    def __init__(self, vp):
        super(tkTab, self).__init__()
        self.vp = vp

        self.tab=ttk.Frame(tabctrl)

        self.tab.columnconfigure(3,weight=1)
        self.tab.rowconfigure(2,weight=1)

        tabctrl.add(self.tab,text=vp.ip)

        self.lbsh = Label(self.tab, text="SHUTTER",anchor=W)
        self.lbst = Label(self.tab, text="STATUS",anchor=W)
        self.strstatus=StringVar()
        self.lbstat=Label(self.tab, textvariable=self.strstatus,anchor=W)

        self.btno = Button(self.tab, text="OFF",command=lambda: shoff(self))
        self.btnf = Button(self.tab, text="ON",command=lambda: shon(self))
        self.btstat=Button(self.tab, text="Refresh",command=lambda: stat(self))

        self.btno.grid(column=2, row=0)
        self.btnf.grid(column=1, row=0)
        self.btstat.grid(column=1,columnspan=2,row=1)
        self.lbsh.grid(column=0,row=0,sticky=W,padx=10)
        self.lbst.grid(column=0,row=1,sticky=W,padx=10)

        self.lbstat.grid(column=0,columnspan=4,sticky=SE)

        self.tab.bind("a", lambda x: shon(self))
        self.tab.bind("z", lambda x: shoff(self))
        self.tab.bind("<space>", lambda x:toggle(self))

for vp in listVP:
    listTab.append(tkTab(vp))
    setstat(listTab[-1])

tabctrl.pack(expand=1,fill='both')
lball.pack(side=LEFT,padx=10)
btallsh.pack(side=LEFT)
btallop.pack(side=LEFT)
btallsw.pack(side=LEFT)
window.mainloop()
