#!/usr/bin/env python3

import os
import socket
import threading

import json
import jigly.cache

testlist = {
	"nier": [
		"../expers/nier1.mp3",
		"../expers/nier2.mp3",
	] 
}

files = [
	"expers/nier1.mp3",
	"expers/nier2.mp3",
]

chunksize = 2048

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 34567))

closser_thread = threading.Thread(target=jigly.cache.closser, args=())
closser_thread.start()

while 1:
	(dgramm, address) = sock.recvfrom(2048)
	print("Received from {}: {}".format(address, dgramm))

	trent = json.loads(dgramm)
	print(trent)

	if trent["cmd"] == "getchunk":
		fileid = trent["id"]
		chunk = trent["chunk"]

		print("fileid", fileid)
		print("chunk", chunk)

		filepath = files[fileid]
		file = jigly.cache.get_opened_file(filepath)

		file.seek(chunksize * chunk)
		data = file.read(chunksize)

		print(data)
