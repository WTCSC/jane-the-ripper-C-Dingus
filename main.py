#read hashes file
#read names file
#hash names file
#match hashed names and hashes

#<hash method file>



def test_hash(str):
    return str + "w"




method = input("what hash method would you like to use (only MD5 is builtin)\n>>")
hashes = input("location of the hashes file\n>>")
names = input("location of names file\n>>")

found = {}

if method == "MD5":
    with open(names, 'r') as name_file:
        for name in name_file:
            hashed = name.strip() + "pl"
            #hash name
            with open(hashes, 'r') as hash_file:
                for hash_ in hash_file:
                    print(hash_.strip())
                    print(hashed)
                    if hash_.strip() == hashed:
                        found[f"{hash_}"] = name
else:
    print("oh i see")

print(found)