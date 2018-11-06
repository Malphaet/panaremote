import urllib2,sys
import re
try:
    import Tkinter as tk
except:
    import tkinter as tk

reinp=re.compile('INPUT&nbsp;(?P<np>\w+)')

def makeURL(ip,cmd):
    url = 'http://{}/cgi-bin/proj_ctl.cgi?key={}&lang=e&osd=off'.format(ip,cmd)
    username = 'admin1'
    password = 'panasonic'
    p = urllib2.HTTPPasswordMgrWithDefaultRealm()

    p.add_password(None, url, username, password)
    return p,url

def makeSTATUS(ip):
    url='http://{}/cgi-bin/get_osd.cgi?lang=e'.format(ip)
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
        page = urllib2.urlopen(url,timeout=2).read()
        return page
    except Exception as e:
        print(e)
        return None

def openSTATUS(cmd):
    text=openURL(cmd)
    sh,osd,inp="Off","Off",""
    if text==None:
        return None
    if text.find("SHUTTER ON")>=0:
        sh="On"
    if text.find("ON SCREEN ON")>=0:
        osf="On"
    inp=reinp.search(text).groups()[0]
    return sh,osd,inp

ip="192.168.0.8"
shutter_on=makeURL(ip,"shutter_on")
shutter_off=makeURL(ip,"shutter_off")
status=makeSTATUS(ip)

if __name__ == '__main__':
    try:
        cmd=sys.argv[1]
        if cmd=="on":
            openURL(shutter_on)
        elif cmd=="off":
            openURL(shutter_off)
        elif cmd=="status":
            print('Shutter: {}\nOSD: {}\nINPUT: {}'.format(*openSTATUS(status)))
    except:
        openURL(shutter_off)
