import colorama
from colorama import init, Fore, Back, Style
init(convert=True)
def email ():
    email input('Type your email')
    email_confirmation input('Repeat your email')

    while (True):
        if email == email_confirmation:
            print('Now Insert your Password')
            break
        else:
            print('Emails do not match')
            print('Type your email again')
        
def password ():
    password input("Type your password")
    password_confirmation input("Repeat your password")
    
    while (True):
        if password == password_confirmation:
            print('Logged Succesfully')
            break
        else:
            print('Passwords do not match')
            print('Try again')
            


    
    