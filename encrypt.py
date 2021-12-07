
from constants import Constants as Cte
from utils import change_bits, get_file_ext
from threading import Thread
from queue import Queue


def encrypt(key, q):
    input_filename = q.get()
    if Cte.ENCRYPT_TAG not in input_filename:
        file_ext = get_file_ext(input_filename)
        encrypted_filename = input_filename.replace(file_ext, f'_{Cte.ENCRYPT_TAG}{file_ext}')
        change_bits(input_filename, encrypted_filename, key)
    q.task_done()
    print('Encryption Done')


def write_encrypt(list_input_filename, key):
    q = Queue()
    for file in list_input_filename:
        q.put(file)
    for i in range(30):
        thread = Thread(target=encrypt, args=(key,q,), daemon=True)
        print('thread ', i)
        thread.start()
    q.join()



























