import hashlib

#list of passwords
myPasswords = ("Hello World", "HelloWorld","administrator")

#loop to use a password and run through the hash function and print the hex value
for i in myPasswords:
    hash_object = hashlib.sha256(i.encode())
    hex_dig = hash_object.hexdigest()
    print("password = ",i, "hexHash = ",hex_dig)


# Open lab10_test_data.csv file
lab_Data = open("lab10_test_data.csv", "r+")

# Read lab10_test_data.csv file and calculate hash value
data = lab_Data.read()
has_object = hashlib.sha256(data.encode())
hex_dig = has_object.hexdigest()
print("Using CSV file modified SHA256= ", hex_dig)

# Close opend file
lab_Data.close()

