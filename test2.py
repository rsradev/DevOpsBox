import time 
from threading import Thread
import multiprocessing


def do_work():
    print("Start work")
    i = 0
    for _ in range(200_000_000):
        i += 1
    print("Finished work")

for _ in range(5):
    t = Thread(target=do_work, args=())
    t.start()
