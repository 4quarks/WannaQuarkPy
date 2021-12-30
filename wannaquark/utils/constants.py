
class Constants:
    VERSION = "0.0.1"
    AUTHOR = '4quarks'
    CREDIT = 'WannaQuarkPy '
    EMAIL = 'not_this_time@nothing.com'
    PACKAGE_NAME = 'wannaquark'
    URL_PROJECT = 'https://github.com/4quarks/WannaQuarkPy'
    DESCRIPTION = 'Encrypt all data on the target folder'

    LOG_FILE = "wannaquark.log"

    ENCRYPTION_LVL = 128 // 8  # == 16
    TYPE_ENDIAN = 'little'  # Most of the OS are Little Endian --> run the command --> lscpu
    ENCRYPT_TAG = 'cry'
    DECRYPT_TAG = 'decry'
    KEY_FILENAME = "key_file.key"
    TARGETS_FILENAME = 'targets.txt'


