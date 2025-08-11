import sqlite3

conn = sqlite3.connect("flights.db")  
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        flight_number TEXT,
        from_location TEXT,
        to_location TEXT,
        date TEXT,
        seat TEXT
    )
''')

conn.commit()
conn.close()

print("Database and table created successfully.")
