import re
import getpass

def password_check(passwd):
    val = True
    # Get last character of string i.e. char at index position -1
    last_char = passwd[len(passwd) - 1]
    while val:
        # This is the condition that checks the first character is a capital letter
        if passwd and not passwd[0].isalpha():
            val = False
            print('First character must always be letter')
        elif not  last_char.isdigit() and not last_char.isalpha():
            print("the last digit should always be letter")
            break
        elif len(passwd)<1 or len(passwd)>20:
            print("the password did not meet the required length")
            #^[a-zA-Z]{3}[0-9]{1,2}$
        elif not passwd.isalpha() and not passwd.isdigit():
        #elif not passwd.isdigit() or not passwd.isdigit():
            print("password can only consist of Latin letters, numbers, dot and minuses")
            break
        else:
            print("The Input string Given Matches the Password Rules")
            break
    else:
        print("the password is not Valid")

my_str = getpass.getpass("Enter a password: ")
print("The password you entered is" , my_str)
password_check(my_str)




