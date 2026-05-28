from random import *
import os

u_pwd = input("Enter your password: ")
pwd = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
       '1','2','3','4','5','6']
1
123

pw = ""
while pw != u_pwd:
    pw = ""
    for letter in range(len(u_pwd)):
        guess_pwd = pwd[randint(0, len(pwd) - 1)]
        pw = pw + str(guess_pwd)
        print(pw)
        print("Cracking Password...Please Wait")
        os.system("clear")  # use "cls" on Windows

print("Your Password Is:", pw)