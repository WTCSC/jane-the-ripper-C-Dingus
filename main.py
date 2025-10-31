#import hashlib
import mod
import os
import sys

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

NONO = "~`!@#$%^&*()-+=:;<>,."


#def test_hash(str):
 #   return str + "pl"

def any_char(str1, str2):
    for char in str1:
        if char in str2:
            return True
    return False

def count_lines(filepath):
    with open(filepath, 'r') as f:
        return sum(1 for line in f)

while True:
    method = input("what hash method would you like to use (only MD5 is builtin)\n>>")
    if not any_char(method, NONO):
        break
    print("invalid method please input a function in the mod folder")
            

while True:
    hashes = input("location of the hashes file\n>>")
    if not os.path.isfile(hashes):
        print("invalid hash file location")
    else:
        break

while True:
    names = input("location of names file\n>>")
    if not os.path.isfile(names):
        print("invalid name file location")
    else:
        break

found = {}

hash_count = count_lines(hashes)
loading = 0.0
last = 0
print("=================================[HASHING]=======================================")
print("[", end="")
with open(hashes, 'r') as hash_file:
    for hash_ in hash_file:
        if int(loading) > last:
            last += 1
            sys.stdout.write("#")
            sys.stdout.flush()     
        title = f"{hash_.strip()}"
        with open(names, 'r') as name_file:
            for name in name_file:
                try:
                    exec(f"hashed = mod.{method}(name.strip())")
                except:
                    print("failed to run hash function check that you have the right name or that it is setup correct in mod.py")
                if hash_.strip() == hashed:
                    found[title] = GREEN + "[" + name.strip() + "]" + RESET
            if title not in found:
                found[title] = RED + "[FAILED]" + RESET
        loading += 21/hash_count
    

print("]")
for hash_ in found:
    print(f"{hash_} == {found[hash_]}")