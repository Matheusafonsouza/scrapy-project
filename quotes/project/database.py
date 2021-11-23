import sqlite3

connection = sqlite3.connect('quotes.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE QUOTE(
                    title TEXT
                    author TEXT
                    TAG text)
""")

connection.commit()
connection.close()