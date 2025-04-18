import sqlite3

def get_user_info(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = '%s'" % user_id
    cursor.execute(query)
    return cursor.fetchall()

user_input = input("Podaj ID użytkownika: ")
print(get_user_info(user_input))
