
from constants import Constants as Cte
from targets import write_file_targets, get_targets
from key_generator import write_key
from encrypt import write_encrypt
from decrypt import write_decrypt


if __name__ == "__main__":
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

