try:
    from tkinter import *
    from tkinter import ttk
except:
    from Tkinter import *
    import ttk

import request

def shon(event):
    Pana.shutterOn()
    setstat()

def shoff(event):
    Pana.shutterOff()
    setstat()

def stat():
    Pana.getStatus()
    setstat()

def setstat():
    if Pana.st_shutter=='Off':
        btno.config(relief=SUNKEN)
        btnf.config(relief=RAISED)
    else:
        btnf.config(relief=SUNKEN)
        btno.config(relief=RAISED)
    strstatus.set(Pana.strStatus())

Pana=request.VP('192.168.0.8')

window = Tk()

window.title("Panasonic Remote GUI")
window.geometry('350x200')

tabctrl=ttk.Notebook(window)
tab1=ttk.Frame(tabctrl)
tabctrl.add(tab1,text=Pana.ip)
tabctrl.pack(expand=1,fill='both')

lbsh = Label(tab1, text="SHUTTER")
lbst = Label(tab1, text="STATUS")
strstatus=StringVar()
lbstat=Label(tab1, textvariable=strstatus,anchor=W)

btno = Button(tab1, text="OFF",command=lambda: shoff(None))
btnf = Button(tab1, text="ON",command=lambda: shon(None))
btstat=Button(tab1, text="Refresh",command=stat)


btno.grid(column=2, row=0)
btnf.grid(column=1, row=0)
btstat.grid(column=1,row=1)
lbsh.grid(column=0, row=0)
lbst.grid(column=0,row=1)

lbstat.grid(column=3,columnspan=3,pady=80,sticky=E)

window.bind("a", shon)
window.bind("z", shoff)

setstat()
window.mainloop()
