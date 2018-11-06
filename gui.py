try:
    from tkinter import *
except:
    from Tkinter import *
import request

def shon(event):
    request.openURL(request.shutter_on)

def shoff(event):
    request.openURL(request.shutter_off)

def stat():
    lbstat.text='Shutter: {} / OSD: {} / INPUT: {}'.format(*request.openSTATUS(request.status))

window = Tk()

window.title("Panasonic Remote GUI")
window.geometry('350x200')

lbsh = Label(window, text="SHUTTER")
lbst = Label(window, text="STATUS")
lbstat=Label(window, text="")

btno = Button(window, text="OFF",command=lambda: shoff(None))
btnf = Button(window, text="ON",command=lambda: shon(None))
btstat=Button(window, text="Refresh",command=stat)

btno.grid(column=2, row=0)
btnf.grid(column=1, row=0)
btstat.grid(column=1,row=1)
lbsh.grid(column=0, row=0)
lbst.grid(column=0,row=1)
lbstat.grid(column=0,row=2)

window.bind("a", shon)
window.bind("z", shoff)

window.mainloop()
