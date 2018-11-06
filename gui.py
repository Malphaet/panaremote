try:
    from tkinter import *
    from tkinter import ttk
except:
    from Tkinter import *
    import ttk

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
    if tab.vp.st_shutter=='Off':
        tab.btno.config(relief=SUNKEN)
        tab.btnf.config(relief=RAISED)
    else:
        tab.btnf.config(relief=SUNKEN)
        tab.btno.config(relief=RAISED)
    tab.strstatus.set(tab.vp.strStatus())

def shall(listtab):
    for vp in listVP:
        vp.shutterOn()

def opall(listtab):
    for vp in listVP:
        vp.shutterOff()

def swall(listtab):
    for vp in listVP:
        if vp.st_shutter=="On":
            vp.shutterOff()
        else:
            vp.shutterOn()


print("Connecting to hosts")
listVP=[request.VP('192.168.0.4'),
request.VP('192.168.0.8')]

window = Tk()

window.title("Panasonic Remote GUI")
window.geometry('350x200')

tabctrl=ttk.Notebook(window)
lball=Label(window,text="ALL")
btallsh=Button(window, text="SHUT",command=lambda: shall())
btallop=Button(window, text="OPEN",command=lambda: opall())
btallsw=Button(window, text="SWITCH",command=lambda: swall())
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

listTab=[]
for vp in listVP:
    listTab.append(tkTab(vp))
    setstat(listTab[-1])

tabctrl.pack(expand=1,fill='both')
btallsh.pack(side=LEFT)
btallop.pack(side=LEFT)
btallsw.pack(side=LEFT)
window.mainloop()
