import sqlite3
from itemadapter import ItemAdapter


class QuotePipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.connection = sqlite3.connect('quotes.db')
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS QUOTE(
                                title TEXT,
                                author TEXT,
                                tags text)
                            """)

    def store_db(self, item):
        self.cursor.execute("""INSERT INTO QUOTE (title, author, tags) VALUES (?, ?, ?)""", (
            item['title'],
            item['author'],
            ', '.join(item['tags'])
        ))

    def process_item(self, item, spider):
        self.store_db(item)
        self.connection.commit()
        return item
