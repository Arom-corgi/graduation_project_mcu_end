def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('动手康1', 'dsk20221116')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())