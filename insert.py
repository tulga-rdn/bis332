import psycopg2
import os
from datetime import date

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def insert_gene(cursor, connection):
    gene_id = input("Input gene_id: ")
    if not gene_id:
        clear_screen()
        print("Gene ID should not be empty.")
        return
    if gene_id == "exit":
        clear_screen()
        return
    tax_id = input("Input tax_id: ")
    if tax_id == "exit":
        clear_screen()
        return
    synonym = input("Input synonym: ")
    if synonym == "exit":
        clear_screen()
        return
    chromosome = input("Input chromosome: ")
    if chromosome == "exit":
        clear_screen()
        return
    map_location = input("Input map_location: ")
    if map_location == "exit":
        clear_screen()
        return
    description = input("Input description: ")
    if description == "exit":
        clear_screen()
        return
    gene_type = input("Input gene_type: ")
    if gene_type == "exit":
        clear_screen()
        return
    symbol = input("Input symbol: ")
    if symbol == "exit":
        clear_screen()
        return
    
    sql = """INSERT INTO gene_test (gene_id, tax_id, synonym, chromosome, map_location, description, gene_type, insert_date, symbol)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    try:
        cursor.execute(sql, (gene_id, tax_id, synonym, chromosome, map_location, description, gene_type, date.today(), symbol))
        connection.commit()
        print(f"Inserted gene {gene_id}.")
    except psycopg2.Error as e:
        clear_screen()
        print("Query error: check your input or contact developers")
        print(e)

def insert_snp(cursor, connection):
    snp_id = input("Input snp_id: ")
    if snp_id == "exit":
        clear_screen()
        return
    if not snp_id:
        clear_screen()
        print("SNP ID should not be empty.")
        return
    gene_id = input("Input gene_id: ")
    if not gene_id:
        clear_screen()
        print("Gene ID should not be empty.")
        return
    if gene_id == "exit":
        clear_screen()
        return
    chromosome = input("Input chromosome: ")
    if chromosome == "exit":
        clear_screen()
        return
    snp_position = input("Input snp_position: ")
    if snp_position == "exit":
        clear_screen()
        return
    sameposition_gene = input("Input sameposition_gene: ")
    if sameposition_gene == "exit":
        clear_screen()
        return
    anc_allele = input("Input anc_allele: ")
    if anc_allele == "exit":
        clear_screen()
        return
    minor_allele = input("Input minor_allele: ")
    if minor_allele == "exit":
        clear_screen()
        return

    sql = """INSERT INTO snp_test (snp_id, gene_id, chromosome, snp_position, sameposition_gene, anc_allele, minor_allele)
            VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    
    try:
        cursor.execute(sql, (snp_id, gene_id, chromosome, snp_position, sameposition_gene, anc_allele, minor_allele))
        connection.commit()
        print(f"Inserted SNP {snp_id}.")
    except psycopg2.Error as e:
        clear_screen()
        print("Query error: check your input or contact developers")
        print(e)

def insert_disease(cursor, connection):
    disease_id = input("Input disease id: ")
    if not disease_id:
        clear_screen()
        print("Disease ID should not be empty.")
        return
    if disease_id == "exit":
        clear_screen()
        return
    gene_id = input("Input gene_id: ")
    if not gene_id:
        clear_screen()
        print("Gene ID should not be empty.")
        return
    if gene_id == "exit":
        clear_screen()
        return
    disease_name = input("Input disease name: ")
    if disease_name == "exit":
        clear_screen()
        return
    
    sql = """INSERT INTO new_disease_test (disease_id, gene_id, disease_name)
            VALUES (%s, %s, %s)"""
    
    try:
        cursor.execute(sql, (disease_id, gene_id, disease_name))
        connection.commit()
        print("Inserted disease.")
    except psycopg2.Error as e:
        clear_screen()
        print("Query error: check your input or contact developers")
        print(e)

def insert(connection, cursor):
    while True:
        print("Select which database to edit: ")
        print("0: Gene, 1: SNP, 2: Disease")
        print("Type 'exit' to exit to the previous menu")
        insert_mode = input("Select database: ")

        if insert_mode == "exit":
            print("Exiting insertion mode...")
            clear_screen()
            break

        try:
            if insert_mode == "0":
                insert_gene(cursor, connection)
            elif insert_mode == "1":
                insert_snp(cursor, connection)
            elif insert_mode == "2":
                insert_disease(cursor, connection)
            else:
                clear_screen()
                print("Invalid input. Please input either '0', '1', '2' or 'exit'.")

        except Exception as e:
            clear_screen()
            print("An error occurred:", e)
