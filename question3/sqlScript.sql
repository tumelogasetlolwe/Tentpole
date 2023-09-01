import sqlite3

# Create or connect to the database
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Create an initial table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY,
        filename TEXT,
        content TEXT
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()