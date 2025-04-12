import sqlite3

def main():
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
    ''')
    
    cursor.execute('SELECT COUNT(*) FROM users')
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute('INSERT INTO users (name) VALUES (?)', ("John Doe",))
        connection.commit()
    
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    print("Користувачі:")
    for row in rows:
        print(row)
    
    connection.close()

if __name__ == "__main__":
    main()