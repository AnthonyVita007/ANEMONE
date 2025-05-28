import network
import ubinascii
import machine

# Rete WiFi simulata su Wokwi
ssid = 'Wokwi-GUEST'
password = ''

# Connessione WiFi
print("Connessione alla rete WiFi in corso...", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(ssid, password)

while not sta_if.isconnected():
    pass  # attende fino alla connessione

print(" Connesso!")
print(sta_if.ifconfig())
