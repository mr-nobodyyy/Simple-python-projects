# Description:
# This prigram tried to generate strong random password for the user conataining Uppercase,Lowercae Lettes , numbers as well as special characters .


import random
import string

print("******************************************************************")
print("************        RANDOM PASSWORD GENERATOR      ***************")
print("******************************************************************")


def gen_passwd(passwd) :
    count=0
    for _ in range(2) :
        passwd += random.choice(string.ascii_uppercase)
        passwd += random.choice(string.digits)
        passwd += random.choice(string.punctuation)
        count += 3

    while count < length_pass:
        passwd += random.choice(string.ascii_lowercase)
        count += 1
    return passwd
#ma;in
length_pass = int(input("Enter the desired password length (8-16): "))

if length_pass < 8 or length_pass > 16:
    print("Try again! Length must be between 8 and 16.")
    exit()

passwd=''

passwd=gen_passwd(passwd)

# Shuffle -> predictable
passwd = ''.join(random.sample(passwd, len(passwd)))

print(f"Your random password is: {passwd}")

