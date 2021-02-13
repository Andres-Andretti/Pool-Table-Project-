
from pooltable_class import PoolTable
import json 

pool_tables = []

import datetime

class PoolTable:
    def __init__(self, table_number):
        self.table_number = table_number
        self.start_time = None 
        self.end_time = None 
        self.is_occupied = False 

    def return_table(self):
        self.end_time = datetime.datetime.now()
        self.is_occupied = False

    def check_out(self):
        # check if the table was already occupied
        # if occupied, then DO NOT check out the table 
        self.start_time = datetime.datetime.now()
        self.is_occupied = True

    def total_time_played(self):
        return self.end_time - self.start_time
    
    def view_table(self):
        return { 
            "table_number": self.table_number,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "is_occupied": self.is_occupied
        }



def occupied_or_not():
    print("*"*50)
    print(" "+"*"*18 + " list table " + "*"*18)
    print("*"*50)
    data = pool_tables
    for index in data:
        if index['is_occupied']:
            print(f"Table: {index['table_number']} is occupied")
        else:
            print(f"Table: {index['table_number']} is available")

def table_occupied():
    data = pool_tables
    table_in = int(input('Enter the occupied table number: '))
    table = next(x for x in data if x["table_number"] == table_in )
    if not table['is_occupied']:   
        pool_table.check_out()
        print(f"Table: {pool_table.table_number}, status: {pool_table.is_occupied}")
    else:
        print(f"Pool Table {table_in} is currently occupied")

def return_table():
    data = pool_tables
    table_in = int(input('Enter the occupied table number: '))
    table = next(x for x in data if x["table_number"] == table_in )
    if table['is_occupied']:   
        pool_table.return_table()
    else:
        print(f"Pool Table {table_in} is not currently available")

# Create tables
for index in range(1,13):
    pool_table = PoolTable(index)
    pool_tables.append(pool_table.view_table())


def exit_menu():
    print("Exiting the system")
    exit(0)

# 
switcher = {
        "1": occupied_or_not,
        "2": table_occupied,
        "3": return_table,
        "q": exit_menu
    }

def switch_menu(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument, "nothing")
    # Execute the function
    return func()
 
## MENU
while True:
    print("\n")
    print("*"*50)
    print(" "+"*"*17 + " Cougar Pool Hall " + "*"*17)
    print("*"*50)
    option = input("Press [1] to view all tables\nPress [2] To view occupied tables\nPress [3] to view available\nPress [q] to quit\nSelect an option: ")
    print("\n")
    switch_menu(option)