import urllib2
try:
    import Tkinter as tk
except:
    import tkinter as tk

def makeURL(cmd):
    url = 'http://192.168.0.8/cgi-bin/proj_ctl.cgi?key={}&lang=e&osd=on'.format(cmd)
    username = 'admin1'
    password = 'panasonic'
    p = urllib2.HTTPPasswordMgrWithDefaultRealm()

    p.add_password(None, url, username, password)
    return p,url

def openURL(cmd):
    p,url=cmd
    handler = urllib2.HTTPBasicAuthHandler(p)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)

    page = urllib2.urlopen(url).read()

shutter_on=makeURL("shutter_off")
shutter_off=makeURL("shutter_on")

top = tk.Tk()
w = Label ( top).pack()
top.mainloop()
