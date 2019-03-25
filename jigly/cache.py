import time
import threading

class OpenedFile:
	def __init__(self, path):
		self.path = path
		self.lastread = time.time()
		self.file = open(self.path, "rb")

opened_files = {}
lock = threading.Lock()

def closser():
	while 1:
		lock.acquire()
		t = time.time()

		todel = []

		for k, v in opened_files.items():
			if t - v.lastread > 60:
				v.file.close()
				todel.append(k)

		for d in todel:
			del opened_files[d]
			print("cleanfile: {}".format(k))


		lock.release()
		time.sleep(5)

def get_opened_file(path):
	lock.acquire()
	if path not in opened_files:
		opened_files[path] = OpenedFile(path)

	opened_files[path].lastread = time.time()
	file = opened_files[path].file
	lock.release()
	return file