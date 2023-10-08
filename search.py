import psycopg2
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def search_gene_by_symbol(cursor, symbol):
    sql = "SELECT DISTINCT * FROM gene_test WHERE symbol = %s"
    return execute_and_display_query(cursor, sql, (symbol,))

def search_gene_by_id(cursor, gene_id):
    sql = "SELECT DISTINCT * FROM gene_test WHERE gene_id = %s"
    return execute_and_display_query(cursor, sql, (gene_id,))

def search_snp_by_gene_id(cursor, gene_id):
    sql = "SELECT DISTINCT * FROM snp_test WHERE gene_id = %s"
    return execute_and_display_query(cursor, sql, (gene_id,))

def search_snp_by_snp_id(cursor, snp_id):
    sql = "SELECT DISTINCT * FROM snp_test WHERE snp_id = %s"
    return execute_and_display_query(cursor, sql, (snp_id,))

def search_disease_by_name(cursor, disease_name):
    sql = "SELECT DISTINCT * FROM new_disease_test WHERE disease_name = %s"
    return execute_and_display_query(cursor, sql, (disease_name,))

def search_disease_by_gene_symbol(cursor, symbol):
    sql = """
        SELECT DISTINCT ndt.*
        FROM new_disease_test ndt
        JOIN gene_test gt ON ndt.gene_id = gt.gene_id
        WHERE gt.symbol = %s OR gt.synonym LIKE %s OR gt.synonym LIKE %s OR gt.synonym LIKE %s
    """
    pattern = f"%|{symbol}|%", f"%|{symbol}", f"{symbol}|%"
    return execute_and_display_query(cursor, sql, (symbol, *pattern))

def execute_and_display_query(cursor, sql, params):
    print("-----")
    try:
        cursor.execute(sql, params)
        rs = cursor.fetchall()
        cursor.execute(f"SELECT DISTINCT * FROM {cursor.description[0][0]} LIMIT 0")
        cols = [desc[0] for desc in cursor.description]
        if len(rs) == 0:
            print("Query returned no value: check your input or contact developers")
        else:
            for r in rs:
                for i, line in enumerate(r):
                    print(f"{cols[i]}: {str(line)}")
                print("-----")
    except psycopg2.Error as e:
        print("Query error: check your input or contact developers")
        print(e)

def search(connection, cursor):
    while True:
        print("Select which database to choose from: ")
        print("0: Gene, 1: SNP, 2: Disease")
        print("Type 'exit' to exit to the previous menu")
        search_mode = input("Select database: ")
        if search_mode == "exit":
            print("Exiting search mode...")
            clear_screen()
            break
        clear_screen()
        while True:
            if search_mode == "0":
                gene_mode = input("How do you want to select the gene? (0: by gene symbol, 1: by gene ID): ")
                if gene_mode == '0':
                    while True:
                        inp = input("Input gene symbol: ")
                        if inp == "exit":
                            clear_screen()
                            break
                        search_gene_by_symbol(cursor, inp)
                elif gene_mode == '1':
                    while True:
                        inp = input("Input gene ID: ")
                        if inp == "exit":
                            clear_screen()
                            break
                        search_gene_by_id(cursor, inp)
                elif gene_mode == "exit":
                    clear_screen()
                    break
                else:
                    print("Invalid input. Please input either '0', '1', or 'exit'.")
            elif search_mode == "1":
                snp_mode = input("How do you want to select the SNP? (0: by gene ID, 1: by SNP ID): ")
                if snp_mode == '0':
                    while True:
                        inp = input("Input gene ID: ")
                        if inp == "exit":
                            clear_screen()
                            break
                        search_snp_by_gene_id(cursor, inp)
                elif snp_mode == '1':
                    while True:
                        inp = input("Input SNP ID: ")
                        if inp == "exit":
                            clear_screen()
                            break
                        search_snp_by_snp_id(cursor, inp)
                elif snp_mode == "exit":
                    clear_screen()
                    break
                else:
                    print("Invalid input. Please input either '0', '1', or 'exit'.")
            elif search_mode == "2":
                disease_mode = input("How do you want to select the disease? (0: by disease name, 1: by gene symbol): ")
                if disease_mode == '0':
                    while True:
                        inp = input("Input disease name: ")
                        if inp == "exit":
                            clear_screen()
                            break
                        search_disease_by_name(cursor, inp)
                elif disease_mode == '1':
                    while True:
                        inp = input("Input gene symbol: ")
                        if inp == "exit":
                            clear_screen()
                            break
                        search_disease_by_gene_symbol(cursor, inp)
                elif disease_mode == "exit":
                    clear_screen()
                    break
                else:
                    print("Invalid input. Please input either '0', '1', or 'exit'.")
            else:
                print("Invalid input. Please input either '0', '1', '2' or 'exit'.")
                break
