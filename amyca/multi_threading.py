from threading import Thread
import time


def func1():
	while True:
		print ('Function 1')

def func2():
	while True:
		print ('Function 2')


if __name__ == '__main__':
	while True:
		Thread(target = func1).start()
		time.sleep(1)
		Thread(target = func2).start()
		time.sleep(1)

