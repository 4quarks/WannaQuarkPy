import random
from wannaquark.utils.constants import Constants as Cte
import logging


def generate_key():
    key, char_pool = '', ''
    for i in range(0x00, 0xFF):  # == range(254)
        #  Get a string representing of a character which points to a Unicode code integer
        char_pool += (chr(i))
    for i in range(Cte.ENCRYPTION_LVL):
        # The key will have 16 random Unicode characters
        key += random.choice(char_pool)
    key_ascii = str(key.encode('ascii', 'ignore'))
    return key_ascii


def write_file_key(write_key=False):
    key = generate_key()
    if write_key:
        # Write the key
        with open(Cte.KEY_FILENAME, 'w') as f:
            f.write(key)
    logging.info(f"The key generated is {key}")
    return key




"""
hostname = os.getenv('HOSTNAME')
time = datetime.now()
print(f'[{time}] - {hostname}:{key}'.encode('utf-8'))

ip_address = '1XXXXXX'
port = '5677'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ip_address, port))
    s.send(f'[{time}] - {hostname}:{key}'.encode('utf-8'))
"""

if __name__ == "__main__":
    generate_key()




