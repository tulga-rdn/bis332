import psycopg2
import os
from datetime import date
from insert import insert
from delete import delete
from modify import modify
from search import search

IP_ADDRESS = "biostar.kaist.ac.kr" 
PORT = "5432"
DB_NAME = "u20236054"
ID = "u20236054"
Passwd = "bipro20236054"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

try:
    connection = psycopg2.connect(dbname=DB_NAME, user=ID, password=Passwd, host=IP_ADDRESS, port = PORT)
    cursor = connection.cursor() 
except psycopg2.Error as e: print(e)
except RuntimeError as e: print(e)

def edit_mode():
    while True:
        #print("Please select which database you want to edit")
        clear_screen()
        print("Please select which edit you want to carry out: ")
        print("0: Insertion, 1: Modification, 2: Deletion")
        print("Type 'exit' to exit to previous menu")
        edit_mode = input("Select editing mode: ")
        if edit_mode == "exit":
            print("Exiting edit mode")
            clear_screen()
            break
        while True:
            if edit_mode == "0":
                clear_screen()
                print("You are now in insertion mode.")
                insert(connection, cursor)
                break
            elif edit_mode == "1":
                clear_screen()
                print("You are now in modification mode.")
                modify(connection, cursor)
                break
            elif edit_mode == "2":
                clear_screen()
                print("You are now in deletion mode.")
                delete(connection, cursor)
                break
            else:
                print("Invalid input. Please input either '0', '1', '2' or 'exit'.")
                break


while True: 
    c()
    print("######################################################")
    print("BioJoin Project Phase 2")
    print("By Tulga-Erdene Sodjargal (Соджаргалын Тулга-Эрдэнэ)")
    print("and Daniel Alejandro Rosa Aparicio")
    print("######################################################")
    print("\n")
    print("Please select the mode: ")
    print("0: search, 1: edit")
    print("Type 'exit' to exit the program")
    mode = input("select mode: ")
    if mode == "exit":
        print("Exiting the program. Have a nice day! :)")
        break
    while True:
        if mode == "0":
            clear_screen()
            print("You are now in search mode.")
            search(connection, cursor)
            break
        elif mode == "1":
            clear_screen()
            print("You are now in editing mode.")
            edit_mode()
            break
        else:
            print("Invalid input. Please input either '0', '1' or 'exit'.")
            break