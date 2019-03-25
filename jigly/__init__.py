import os
import socket

testlist = {
	"nier": [
		"nier.mp3",
		"nier2.mp3",
	] 
}


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while 1:
	sock.recvfrom()