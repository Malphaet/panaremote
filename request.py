import urllib2,sys
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
    try:
        p,url=cmd
        handler = urllib2.HTTPBasicAuthHandler(p)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)
        page = urllib2.urlopen(url).read()
        return page
    except Exception as e:
        print(e)
        return None


shutter_on=makeURL("shutter_on")
shutter_off=makeURL("shutter_off")
if __name__ == '__main__':
    try:
        cmd=sys.argv[1]
        print(cmd)
        if cmd=="on":
            openURL(shutter_on)
        elif cmd=="off":
            openURL(shutter_off)
    except:
        openURL(shutter_off)
