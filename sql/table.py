import sqlite3

conn = sqlite3.connect(".db")
cursor = conn.cursor()

query = """

"""

cursor.execute(query)
conn.commit()