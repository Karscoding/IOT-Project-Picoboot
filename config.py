import socket
hostname = socket.gethostname()

WIFI_SSID = "JULIANSLAPTOP"
WIFI_PASSWORD = "3@093p3Q"
SERVER = socket.gethostbyname(hostname)
ENDPOINT='/temperature'
AENDPOINT='/afstand'
SENDPOINT='/input'
GETPOINT='/get'
PORT= '5000'