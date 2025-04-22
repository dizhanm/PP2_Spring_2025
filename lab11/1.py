import psycopg2
import csv
#SELECT * FROM phonebook;


def connect():
    return psycopg2.connect(
        host="localhost", 
        dbname="postgres", 
        user="postgres",
        password="dizhan2006" 
    )

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            phone VARCHAR(20)
        )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Gotovo")


def insert_manual():
    conn = connect()
    cur = conn.cursor()
    name = input("Input your name: ")
    phone = input("Input your phone number: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("All informations added.")


def insert_from_csv():
    conn = connect()
    cur = conn.cursor()
    file_path = input("Input your CSV file name (example, contacts.csv): ")
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                name, phone = row
                cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Informations added from CSV file")

def update_data():
    conn = connect()
    cur = conn.cursor()
    name = input("What kind of name do you want to change?")
    new_phone = input("New phone number: ")
    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))
    conn.commit()
    cur.close()
    conn.close()
    print("Phone number updated")


def query_data():
    conn = connect()
    cur = conn.cursor()
    name_filter = input("Input the name: ")
    cur.execute("SELECT * FROM phonebook WHERE name = %s", (name_filter,))
    rows = cur.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone number: {row[2]}")
    if not rows:
        print("Nothing found")
    cur.close()
    conn.close()


def delete_data():
    conn = connect()
    cur = conn.cursor()
    name = input("What kind of name do you want to delete?")
    cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    conn.commit()
    cur.close()
    conn.close()
    print("Information deleted")

def search_by_pattern(pattern):
    conn = connect()
    cur = conn.cursor()
    query = """
        SELECT * FROM phonebook
        WHERE name LIKE %s OR phone LIKE %s
    """
    pattern = '%' + pattern + '%'
    cur.execute(query, (pattern, pattern))
    rows = cur.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone number: {row[2]}")
    if not rows:
        print("No matching records found.")
    cur.close()
    conn.close()


def insert_multiple_users(users):
    conn = connect()
    cur = conn.cursor()

    users_str = [f"{name},{phone}" for name, phone in users]

 
    cur.execute("CALL insert_multiple_users(%s)", (users_str,))
    conn.commit()
    cur.close()
    conn.close()
    print("Users inserted or invalid data reported.")


def query_with_pagination(limit, offset):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook LIMIT %s OFFSET %s", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone number: {row[2]}")
    if not rows:
        print("No data found.")
    cur.close()
    conn.close()



def insert_or_update_user(name, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("User inserted or updated.")


def delete_data_by_user_or_phone(value):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL delete_data_by_user_or_phone(%s)", (value,))
    conn.commit()
    cur.close()
    conn.close()
    print("Data deleted.")



def menu():
    create_table()  
    while True:
        print("\n PHONEBOOK:")
        print("1. Adding information by myself")
        print("2. Adding informations from CSV file.")
        print("3. Updating informations.")
        print("4. Search the information")
        print("5. Delete information")
        print("6. Search by pattern")
        print("7. Insert multiple users from list")
        print("8. Query with pagination")
        print("9. Insert or Update user by name and phone")
        print("10. Delete data by user or phone")
        print("0. Exit")

        choice = input("Choose the option: ")
        if choice == "1":
            insert_manual()
        elif choice == "2":
            insert_from_csv()
        elif choice == "3":
            update_data()
        elif choice == "4":
            query_data()
        elif choice == "5":
            delete_data()
        elif choice == "6":
            pattern = input("Enter the pattern to search: ")
            search_by_pattern(pattern)
        elif choice == "7":
            users = [["Qwerty", "+1234567890"], ["Jan", "+0987654321"]]  # Example users
            insert_multiple_users(users)
        elif choice == "8":
            limit = int(input("Enter limit: "))
            offset = int(input("Enter offset: "))
            query_with_pagination(limit, offset)
        elif choice == "9":
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            insert_or_update_user(name, phone)
        elif choice == "10":
            value = input("Enter the name or phone number to delete: ")
            delete_data_by_user_or_phone(value)
        elif choice == "0":
            print("The code stopped. Thank you!")
            break
        else:
            print("ERROR. Please, try again.")



if __name__ == "__main__":
    menu()
