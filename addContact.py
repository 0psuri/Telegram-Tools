# -*- coding: utf-8 -*-

from pyrogram import Client, InputPhoneContact
from random import randint

def Add_Contact(number):
    temp = InputPhoneContact(str(number), 'Deanon', str(number))
    app.add_contacts(temp)

def fromFile():
    file_name = input("File: ")
    numbers = open(file_name).read().split('\n')

    for num in numbers:
        Add_Contact(num)

def rndGenerator():
    r0 = int(input("From (ex. 150000000000): "))
    r1 = int(input("To (ex. 150099999999): "))

    while True:
        Add_Contact(randint(r0,r1))

def inRange():
    a = int(input("From (ex. 150000000000): "))
    b = int(input("To (ex. 150099999999): "))

    while a != b:
        Add_Contact(a)
        a += 1

if __name__ == '__main__':
    app = Client("my_account")
    app.start()

    select = input("Adding from:\n1 - file\n2 - random generation\n3 - 'brutoforce' numbers\nSelect: ")

    if select == "1":
        fromFile()
    elif select == "2":
        rndGenerator()
    elif select == "3":
        inRange()
    else:
        print("Invalid input!")
    
    app.stop()
