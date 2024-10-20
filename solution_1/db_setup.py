# db_setup.py

import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create table for storing rules
cursor.execute('''
CREATE TABLE IF NOT EXISTS rules (
    rule_id INTEGER PRIMARY KEY AUTOINCREMENT,
    rule_string TEXT NOT NULL
)
''')

# Commit and close the connection
conn.commit()
conn.close()

print("Database setup completed.")
