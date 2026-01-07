# Description:
# python program to check the strength of a password provided by user.
import string

print("************************************")
print("PASSWORD STRENGTH CHECKER")
print("************************************")

def count(passwd):
    uC = lC = num = sp_ch = 0
    if passwd == "":
        print("Error! You need to enter a password!")
        exit()

    for char in passwd:
        if char in string.ascii_uppercase:
            uC += 1
        elif char in string.ascii_lowercase:
            lC += 1
        elif char in string.digits:
            num += 1
        elif char in string.punctuation:
            sp_ch += 1

    return uC, lC, num, sp_ch


def evaluate(length_passwd, uC, lC, num, sp_ch):
    if length_passwd < 8:
        print(" Weak password: too short, needs immediate attention")

    elif uC == 0 or lC == 0 or num == 0 or sp_ch == 0:
        print(" Weak password: must contain uppercase, lowercase, number, and special character")

    elif 12 <= length_passwd <= 16:
        print(" Strong password!")

    elif 8 <= length_passwd < 12:
        print(" Good password, but could be stronger")

    else:
        print(" Password length is unusual, review recommended")


#Main Program
passwd = input("Enter your password to get it evaluated: ")
length_passwd = len(passwd)

uC, lC, num, sp_ch = count(passwd)  

print(f"Password length: {length_passwd}")
evaluate(length_passwd, uC, lC, num, sp_ch)
