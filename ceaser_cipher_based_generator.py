#Description:
# This program takes input from the user and encrypted or decrypts as per need of the user

import string

encrypted_word = ''
decrypted_word = ''
choice = input("Enter what you want to do ( encryption or decryption) : ")

if( choice == 'encryption' ) :
    encryption_key = int(input("Enter the key (0-9) :"))
    if encryption_key <0 or encryption_key>9 :
        print("please enter correct key (0-9")
    else:
        plain_text = input("enter the message you want to get encrypted :")
        for char in plain_text :
            if char in string.ascii_lowercase:
                index = string.ascii_lowercase.index(char)
                new_index = (index + encryption_key) % 26
                encrypted_word += string.ascii_lowercase[new_index]
            else:
                encrypted_word += char
            
        print(f"encrypted message is : {encrypted_word}")
        
elif(choice == 'decryption' ) :
    
    decryption_key = int(input("decryption_key the decyption kry to decipher the code :"))
    
    if(decryption_key < 0 or decryption_key >9):
        print("Enter the correct key , i.e 0-9")

    else:
        encrypted_msg = input("Enter the encrypted_msg to be deciphered :")
        for char in encrypted_msg:
            if char in string.ascii_lowercase:
                index = string.ascii_lowercase.index(char)
                new_index = (index - decryption_key) % 26
                decrypted_word += string.ascii_lowercase[new_index]
            else:
                decrypted_word += char
        print(f"your deciphered message is : {decrypted_word}")
    
else:
    print("Please enter correct option : encryption or decryption")
