
from wannaquark.utils.constants import Constants as Cte
from wannaquark.utils.tools import change_bits
import logging


def write_decrypt(list_input_filename, key):
    successful_decryptions = []
    for input_filename in list_input_filename:
        decrypted_filename = input_filename.replace(Cte.ENCRYPT_TAG, Cte.DECRYPT_TAG)
        successful = change_bits(input_filename, decrypted_filename, key)
        successful_decryptions.append(successful)
        logging.info(f'File {input_filename} decrypted {successful}')


























