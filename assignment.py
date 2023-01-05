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
def add():
    data = []
    choice = None
    while choice != "X":
        info = []
        for x in title:
            info.append(input(f"Please Enter {x}: "))
        data.append(info)
        for i in data:
            print("------")
            for key, value in dict(zip(title, i)).items():
                print(key,":",value)
        choice = input("Would you like to enter more?\ntype anything to continue, [X] to exit: ").strip().upper()
    else:
        for i in data:
            query = f"insert into petbase(petname, petspecies, petbreed, ownername, ownernum, owneremail, ownerbalance, date) values ('{i[0]}','{i[1]}','{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}', '{i[7]}');"
            cursor.execute(query)
            connection.commit()

def search():
    
    query = "select * from petbase"
    cursor.execute(query)
    all = cursor.fetchall()
    
    if len(all) == 0:
        print("no data to display")
    else:
        choice = None
        result = []
        while choice not in ["I","E","P","X"]:
            choice = input("how would you like to retrieve?\n by id [I]\n by owner email [E]\n by owner phone number [P]\n enter [X] to exit\nwhat would you like to do? [I/E/P]").strip().upper()
        if choice == "I":
            query = "select id from petbase"
        elif choice == "E":
            query = "select owneremail from petbase"
        elif choice == "P":
            query = "select ownernum from petbase"
        elif choice == "X":
            exit()
        cursor.execute(query)
        data = cursor.fetchall()
        search = input("type your search: ")
        try:
            for i in data:
                if search in str(i):
                    result.append(all[data.index(i)])
            if len(result) != 0:
                for i in result:
                    print("----------")
                    for x in range(8):
                        print(f"{title[x]}: {i[x+1]}")
                    print("----------")
            else:
                print("----------")
                print("no match found")
                print("----------")
        except Exception as e:
            print(f"An error occurred {e}")
            

import sqlite3

#basic
title = ["pet name", "pet species","pet breed","owner name","owner phone number", "owner email", "owner balance", "date of first visit"]
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

#menu
loop = True
while loop:
    mouse = None
    print("----------")
    print("Veterinary Database")
    print("----------")
    print("Add new record [A]\nSearch existing record [S]\nExit [X]")
    print("----------")
    while mouse not in ["A","S","X"]:
        mouse = input("what would you like to do? ").strip().upper()
        if mouse == "A":
            add()
        elif mouse == "S": 
            search()
        elif mouse == "X": 
            break
