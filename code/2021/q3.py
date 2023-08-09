import _thread
from time import sleep

items = [2, 4, 5, 2.5, 1, 7]

def sleep_sort(i):
    sleep(i)
    print(i)

for i in items:
    arg_tuple = (i,)
    _thread.start_new_thread(sleep_sort, arg_tuple)
