import network
import wup

print ('Module toosl.py loaded')

def wphone():
    wlan = network.WLAN(network.STA_IF)
    if wlan.isconnected():
        wlan.disconnect()
    wlan.active(True)
    wlan.connect('ilia','thepassword')
    print(wlan.ifconfig())

def whome():
    wlan = network.WLAN(network.STA_IF)
    if wlan.isconnected():
        wlan.disconnect()
    wlan.active(True)
    wlan.connect(wup.homessid, wup.homepass)
    print(wlan.ifconfig())

def wconf():
    wlan = network.WLAN(network.STA_IF)
    print(wlan.ifconfig())
