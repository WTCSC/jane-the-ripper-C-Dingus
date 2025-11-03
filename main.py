import mod
import os
import sys

#Bash Colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

#Characters that can not be included in user code input
NONO = "~`!@#$%^&*()-+=:;<>,."


def any_char(str1, str2):
    """
    check if any char fround in str1 is in str2
    """
    for char in str1:
        if char in str2:
            return True
    return False

def count_lines(filepath):
    """
    count the amount of lines of a file from a filepath
    used for loading bars
    """
    with open(filepath, 'r') as f:
        return sum(1 for line in f)

#Gather input for method of hashing
while True:
    method = input("what hash method would you like to use (md5, sha1, and sha256 are builtin)\n>>")
    #make sure it can't run harmfull code
    if not any_char(method, NONO):
        break
    print("invalid method please input a function in the mod folder")
            
#Get filepath to hashlist
while True:
    hashes = input("location of the hashes file\n>>")
    if not os.path.isfile(hashes):
        print("invalid hash file location")
    else:
        break

#Get filepath to wordlist
while True:
    names = input("location of wordlist\n>>")
    if not os.path.isfile(names):
        print("invalid name file location")
    else:
        break

save = input("File to save output (leave blank to not save output)\n>>")


#Dict of found hashes as keys and what they are as values
found = {}

#Used for initialization bar
hash_count = count_lines(hashes)
loading = 0.0
last = 0

print("============================================[INITIALIZING]============================================")
print("[", end="")
with open(hashes, 'r') as hash_file:
    for hash_ in hash_file:
        if int(loading) > last:
            last += 1
            sys.stdout.write("#")
            sys.stdout.flush()    
        #set all hashes in haslist to dictionary as FAILED 
        found[f"{hash_.strip()}"] = RED + "[FAILED]" + RESET
        loading += 101/hash_count
    
print("]")

name_count = count_lines(names)
loading = 0.0
last = 0
print("==============================================[LOADING]===============================================")
print("[", end="")
with open(names, 'r') as name_file:
    for name in name_file:
        if int(loading) > last:
            last += 1
            sys.stdout.write("#")
            sys.stdout.flush()     

        #Try to run the method of hashing as a function in the mod file
        try:
            exec(f"hashed = mod.{method}(name.strip())")
        except:
            print("failed to run hash function check that you have the right name or that it is setup correct in mod.py")
        
        #Check all hashed words against the hashes in found and change value
        for title in found:
            if title == hashed:
                found[title] = GREEN + "[" + name.strip() + "]" + RESET
        loading += 101/name_count
print("]\n\n")

#print hashes
for hash_ in found:
    print(f"{hash_} == {found[hash_]}")

if save.strip() != "":
    with open(save.strip(), 'w') as save_file:
        for hash_ in found:
            save_file.write(f"{hash_} == {found[hash_]}\n")