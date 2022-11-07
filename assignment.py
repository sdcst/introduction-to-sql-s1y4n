#!python

"""
Create a program that will store the database for a veterinary
Each record needs to have the following information:
id unique integer identifier
pet name
pet species (cat, bird, dog, etc)
pet breed (persian, beagle, canary, etc)
owner name
owner phone number
owner email
owner balance (amount owing)
date of first visit

create a program that will allow the user to:
insert a new record into the database and save it automatically
retrieve a record by their id and display all of the information
retrieve a record by the email and display all of the information
retrieve a record by phone number and display all of the information

You will need to create the table yourself. Consider what data types you will
need to use.
"""
import sqlite3

file = 'pbase.db'
connection = sqlite3.connect(file)
cursor = connection.cursor()

query = """
create table if not exists petbase(
    id integer primary key autoincrement,
    petname tinytext,
    petspecies tinytext,
    petbreed tinytext,
    ownername tinytext,
    ownernum tinytext,
    owneremail tinytext,
    ownerbalance tinytext,
    date tinytext);
"""
cursor.execute(query)
title = ["pet name", "pet species","pet breed","owner name","owner phone number", "owner email", "owner balance", "date of first visit"]

def add():
    data = []
    choice = None
    while choice != "N":
        info = []
        for x in title:
            info.append(input(f"Please Enter {x}: "))
        data.append(info)
        print(data) #debug
        choice = input("Your data has been saved, would you like to enter more? [Y/N]").strip().upper()
    else:
        for i in data:
            query = f"insert into petbase(petname, petspecies, petbreed, ownername, ownernum, owneremail, ownerbalance, date) values ('{i[0]}','{i[1]}','{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}');"
        cursor.execute(query)
        connection.commit()

def display():
    choice = input("how would you like to retrieve?\n by id\n by owner email\n by owner phone number[I/E/P]")
    query2 = """""" 
    if choice == "I":
        query = """select id from petbase"""
    elif choice == "E":
        query = """select owneremail from petbase"""
    elif choice == "P":
        query = """select ownernum from petbase"""
    cursor.execute(query)
    data = cursor.fetchall()
    search = input("type your search: ")
    for i in data:
        if search in i:
            data.index(i)
    
#menu
mouse = None
while mouse != "N":
    mouse = input("enter: ")
    if mouse == "A":
        add()
    elif mouse == "D":
        display()
