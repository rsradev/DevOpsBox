import time 
from threading import Thread
import multiprocessing


def do_work():
    print("Start work")
    i = 0
    for _ in range(200_000_000):
        i += 1
    print("Finished work")


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    for _ in range(5):
        p = multiprocessing.Process(target=do_work, args=())
        p.start()
