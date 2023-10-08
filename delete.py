import psycopg2
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def delete(connection, cursor):
    while True:
        print("Select which database to delete from: ")
        print("0: Gene, 1: SNP, 2: Disease")
        print("Type 'exit' to exit to the previous menu")
        mod_mode = input("Select database: ")

        if mod_mode == "exit":
            print("Exiting deletion mode...")
            clear_screen()
            break

        while True:
            try:
                if mod_mode == "0":
                    gene_id = input("ID of the gene to delete: ")
                    if gene_id == "exit":
                        clear_screen()
                        break
                    
                    sql = "DELETE FROM gene_test WHERE gene_id = %s"
                    cursor.execute(sql, (gene_id,))
                    connection.commit()
                    print(f"Deleting gene {gene_id}")

                elif mod_mode == "1":
                    snp_id = input("ID of the SNP to delete: ")
                    if snp_id == "exit":
                        clear_screen()
                        break
                    
                    sql = "DELETE FROM snp_test WHERE snp_id = %s"
                    cursor.execute(sql, (snp_id,))
                    connection.commit()
                    print(f"Deleting SNP {snp_id}")

                elif mod_mode == "2":
                    disease_id = input("ID of the disease to delete: ")
                    if disease_id == "exit":
                        clear_screen()
                        break
                    
                    sql = "DELETE FROM new_disease_test WHERE disease_id = %s"
                    cursor.execute(sql, (disease_id,))
                    connection.commit()
                    print(f"Deleting disease {disease_id}")

                else:
                    clear_screen()
                    print("Invalid input. Please input either '0', '1', '2' or 'exit'.")
                    break

            except psycopg2.Error as e:
                clear_screen()
                print("Query error: check your input or contact developers")
                print(e)