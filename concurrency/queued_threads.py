import time
import random
import queue

from threading import Thread

counter = 0
job_queue  = queue.Queue() # things to be printed out
counter_queue  = queue.Queue() # amounts by which to increase counter

def inc_manager():
    global counter
    while True:
        increment = counter_queue.get() # this waits until an item is available and then locks the queue
        old_counter = counter
        counter = old_counter + increment
        job_queue.put((f'New counter value is {counter}', '--------'))
        counter_queue.task_done()
Thread(target=inc_manager, daemon=True).start()

def print_manager():
    while True:
        for line in job_queue.get():
            print(line)
        job_queue.task_done()

Thread(target=print_manager, daemon=True).start()

def inc_counter():
    counter_queue.put(1)

worker_thhreads = [Thread(target=inc_counter) for thread in range(10)]

for thread in worker_thhreads:
    thread.start()

for thread in worker_thhreads:
    thread.join()

counter_queue.join()
job_queue.join()