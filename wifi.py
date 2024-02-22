import network
from config import wifi_config
def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(wifi_config['name'], wifi_config['password'])
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())