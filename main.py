#Author: Spase Sandoval
#python script for detecting and cleaning out trojans on windows systems for testing use only

import os
import shutil

def scan_directory(dir_path, signature_db):
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            scan_file(file_path, signature_db)

def scan_file(file_path, signature_db):
    with open(file_path, 'rb') as f:
        contents = f.read()
        file_hash = hashlib.md5(contents).hexdigest()
        if file_hash in signature_db:
            print(f"Found malware in file: {file_path}")
            remove_file(file_path)

def remove_file(file_path):
    try:
        os.remove(file_path)
        print(f"Removed malware file: {file_path}")
    except:
        print(f"Unable to remove file: {file_path}")

def remove_directory(dir_path):
    try:
        shutil.rmtree(dir_path)
        print(f"Removed malware directory: {dir_path}")
    except:
        print(f"Unable to remove directory: {dir_path}")

def remove_malware(signature_db):
    for root, dirs, files in os.walk('C:\\'):
        for file in files:
            file_path = os.path.join(root, file)
            scan_file(file_path, signature_db)
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if dir_path in ['C:\\Windows', 'C:\\Program Files', 'C:\\Program Files (x86)']:
                continue
            if any([file.endswith('.dll') for file in os.listdir(dir_path)]):
                print(f"Found malware directory: {dir_path}")
                remove_directory(dir_path)
