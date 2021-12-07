
from constants import Constants as Cte
import os


def change_bits(input_filename, output_filename, key_token):
    """
    byte represents the text read in decimal --> i.e. h == 104
    ord() returns the Unicode code from a given character --> i.e. - == 197
    byte ^ ord(key_token[index]) --> gives a different decimal --> i.e. 104 ^ 197 = 173
    """
    index = 0
    max_indexes = Cte.ENCRYPTION_LVL - 1
    try:
        with open(input_filename, 'rb') as f:
            data = f.read()
        try:
            with open(output_filename, 'wb') as f:
                for byte in data:
                    xor_byte = byte ^ ord(key_token[index])
                    f.write(xor_byte.to_bytes(1, Cte.TYPE_ENDIAN))
                    if index >= max_indexes:
                        index += 1
        except:
            print(f'failed to decrypt')
    except:
        print("I could't read the input file")


def get_file_ext(target_file):
    _, file_ext = os.path.splitext(target_file)
    return file_ext

