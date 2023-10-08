import psycopg2
from datetime import date
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def modify_gene(cursor, connection):
    cursor.execute("SELECT * FROM gene_test LIMIT 0")
    print("Column names:")
    print(", ".join([desc[0] for desc in cursor.description]))
    gene_id = input("Enter the ID of the gene to modify: ")
    
    if gene_id == "exit":
        return

    col = input("Choose which column to update: ")
    
    if col == "exit":
        return

    mod_val = input("Enter new value: ")
    
    if col in ["gene_id", "tax_id"]:
        sql = f"UPDATE gene_test SET {col} = %s WHERE gene_id = %s"
    else:
        print("Column not in dataset")
        return
    
    try:
        cursor.execute(sql, (mod_val, gene_id))
        connection.commit()
        cursor.execute("UPDATE gene_test SET mod_date = %s WHERE gene_id = %s", (date.today(), gene_id))
        connection.commit()
        print(f"Updated gene {gene_id}.")
    except psycopg2.Error as e:
        print("Query error: check your input or contact developers")
        print(e)

def modify_snp(cursor, connection):
    cursor.execute("SELECT * FROM snp_test LIMIT 0")
    print("Column names:")
    print(", ".join([desc[0] for desc in cursor.description]))
    snp_id = input("Enter the ID of the SNP to modify: ")
    
    if snp_id == "exit":
        return

    col = input("Choose which column to update: ")
    
    if col == "exit":
        return

    mod_val = input("Enter new value: ")
    
    if col in ["snp_id", "gene_id", "snp_position"]:
        sql = f"UPDATE snp_test SET {col} = %s WHERE snp_id = %s"
    else:
        print("Column not in dataset")
        return
    
    try:
        cursor.execute(sql, (mod_val, snp_id))
        connection.commit()
        print(f"Updated SNP {snp_id}.")
    except psycopg2.Error as e:
        print("Query error: check your input or contact developers")
        print(e)

def modify_disease(cursor, connection):
    cursor.execute("SELECT * FROM new_disease_test LIMIT 0")
    print("Column names:")
    print(", ".join([desc[0] for desc in cursor.description]))
    disease_id = input("Enter the ID of the disease to modify: ")
    
    if disease_id == "exit":
        return

    col = input("Choose which column to update: ")
    
    if col == "exit":
        return

    mod_val = input("Enter new value: ")
    
    if col == disease_id:
        sql = f"UPDATE new_disease_test SET {col} = %s WHERE disease_id = %s"
    else:
        print("Column not in dataset")
        return
    
    try:
        cursor.execute(sql, (mod_val, disease_id))
        connection.commit()
        print(f"Updated disease {disease_id}.")
    except psycopg2.Error as e:
        print("Query error: check your input or contact developers")
        print(e)

def modify(connection, cursor):
    while True:
        print("Select which database to modify: ")
        print("0: Gene, 1: SNP, 2: Disease")
        print("Type 'exit' to exit to the previous menu")
        mod_mode = input("Select database: ")
        clear_screen()
        if mod_mode == "exit":
            print("Exiting modification mode...")
            clear_screen()
            break
        
        try:
            if mod_mode == "0":
                modify_gene(cursor, connection)
            elif mod_mode == "1":
                modify_snp(cursor, connection)
            elif mod_mode == "2":
                modify_disease(cursor, connection)
            else:
                clear_screen()
                print("Invalid input. Please input either '0', '1', '2' or 'exit'.")
        except Exception as e:
            clear_screen()
            print("An error occurred:", e)
