import sqlite3

class Database:
    def __init__(self, db_name="vk_bot.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            vk_id INTEGER UNIQUE,
            age INTEGER,
            city TEXT,
            sex INTEGER,
            status INTEGER
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def add_user(self, user):
        query = """
        INSERT INTO Users (vk_id, age, city, sex, status) VALUES (?, ?, ?, ?, ?)
        """
        self.cursor.execute(query, (user['vk_id'], user['age'], user['city'], user['sex'], user['status']))
        self.conn.commit()

    def get_user(self, vk_id):
        query = """
        SELECT * FROM Users WHERE vk_id = ?
        """
        self.cursor.execute(query, (vk_id,))
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()
