from __future__ import print_function
import urllib2,sys
import re
try:
    import Tkinter as tk
except:
    import tkinter as tk

reinp=re.compile('INPUT&nbsp;(?P<np>\w+)')
debug=True

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
        if isinstance(e,urllib2.URLError):
            print(" [Error] Can't reach address: {}".format(url),file=sys.stderr)
            pass
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

def dprint(st):
    if debug:
        print(st,file=sys.stderr)

ip="192.168.0.8"
shutter_on=makeURL(ip,"shutter_on")
shutter_off=makeURL(ip,"shutter_off")
status=makeSTATUS(ip)

class VP(object):
    """Class to acess a VP."""
    def __init__(self, ip):
        super(VP, self).__init__()
        self.ip = ip
        print("Initialing {}".format(ip),file=sys.stderr)
        self.st_shutter=None
        self.st_osd=None
        self.st_input=None
        self.shutter_on=makeURL(ip,"shutter_on")
        self.shutter_off=makeURL(ip,"shutter_off")
        self.status=makeSTATUS(ip)
        self.getStatus()
        if self.st_shutter==None:
            print(" [{}] Unreachable".format(ip),file=sys.stderr)
        else:
            print(" [{}] Connected".format(ip),file=sys.stderr)

    def shutterOn(self):
        s=openURL(self.shutter_on)
        if s!=None:
            self.st_shutter='On'

    def shutterOff(self):
        s=openURL(self.shutter_off)
        if s!=None:
            self.st_shutter='Off'

    def getStatus(self):
        stat=openSTATUS(self.status)
        if stat==None:
            stat=None,None,None
        self.st_shutter,self.st_osd,self.st_input=stat
        return self

    def __str__(self):
        return self.ip

    def strStatus(self):
        if self.st_osd!=None:
            return 'OSD: {} - INPUT: {}'.format(self.st_osd,self.st_input)
        else:
            return 'Host: {} OFFLINE'.format(self.ip)

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
