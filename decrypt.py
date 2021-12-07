
from constants import Constants as Cte
from utils import change_bits


def write_decrypt(list_input_filename, key):
    for input_filename in list_input_filename:
        if Cte.DECRYPT_TAG not in input_filename:
            decrypted_filename = input_filename.replace(Cte.ENCRYPT_TAG, Cte.DECRYPT_TAG)
            change_bits(input_filename, decrypted_filename, key)
    print('Decryption Done')


























