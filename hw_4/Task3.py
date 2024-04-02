import threading
from threading import Thread
import time
from multiprocessing import Pool, Queue, Pipe, Process
import codecs
from datetime import datetime


def process_A(messages_queue, a_conn_b):
    while True:
        message = messages_queue.get()
        message = message.lower()
        a_conn_b.send(message)
        time.sleep(5)
        if message == "end":
            break

def process_B(main_queue, b_conn_a):
    while True:
        message = b_conn_a.recv()
        encoded_message = codecs.encode(message, 'rot_13')
        time = datetime.now()
        time = time.strftime("%d/%m/%Y, %H:%M:%S")
        print(f"{time}: {encoded_message}")
        main_queue.put(encoded_message)
        if message == "end":
            break


if __name__ == '__main__':
    queue_to_A = Queue()
    queue_from_B = Queue()
    a_conn_b, b_conn_a = Pipe()

    A = Process(target=process_A, args=(queue_to_A, a_conn_b))
    B = Process(target=process_B, args=(queue_from_B, b_conn_a))
    A.start()
    B.start()
    
    while True:
        time = datetime.now()
        time = time.strftime("%d/%m/%Y, %H:%M:%S")
        input_str = input(f"{time}: Enter a message : (to stop, enter end)")
        queue_to_A.put(input_str)
        if input_str == "end":
            break

