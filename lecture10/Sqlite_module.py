import sqlite3

conn = splite3.connect('mydatabase.db')
cur = conn.cursor()

cur.execute('''
    CRETE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            city TEXT NOT NULL
            )
            ''')

cur.execute("INSERT INT0 users (name, age, city) VALUES ('Alice', 25,'New York')")
cur.execute("INSERT INT0 users (name, age, city) VALUES ('Bob', 30,'Los Angeles')")
cur.execute("INSERT INT0 users (name, age, city) VALUES ('Charlie', 35,'Chicago')")

conn.commit()

cur.execute("SELECT - FROM users WHERE age > 28")
rows = cur.fetchall()

print("Users older than 28:")
for row in rows:
    print(f"ID: {row[0]}, name: {row[1]}, age: {row[2]} , city: {row[3]}")
          
conn.clone()
