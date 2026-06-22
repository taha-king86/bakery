import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_path='bakery.db'):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_number TEXT NOT NULL,
            bread_count INTEGER NOT NULL,
            face_image_path TEXT NOT NULL,
            created_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS delivered_customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_number TEXT NOT NULL,
            delivered_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS all_customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_number TEXT NOT NULL,
            bread_count INTEGER NOT NULL,
            face_image_path TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        '''
        self.conn.executescript(query)
        self.conn.commit()

    def add_customer(self, ticket_number, bread_count, face_image_path):
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = 'INSERT INTO customers (ticket_number, bread_count, face_image_path, created_at) VALUES (?, ?, ?, ?);'
        self.conn.execute(query, (ticket_number, bread_count, face_image_path, created_at))
        query2 = 'INSERT INTO all_customers (ticket_number, bread_count, face_image_path, created_at) VALUES (?, ?, ?, ?);'
        self.conn.execute(query2, (ticket_number, bread_count, face_image_path, created_at))
        self.conn.commit()

    def get_all_customers(self):
        cursor = self.conn.execute('SELECT * FROM customers ORDER BY id DESC')
        return cursor.fetchall()

    def delete_customer(self, customer_id):
        cursor = self.conn.execute('SELECT ticket_number FROM customers WHERE id = ?', (customer_id,))
        row = cursor.fetchone()
        if row:
            ticket_number = row[0]
            delivered_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.conn.execute('INSERT INTO delivered_customers (ticket_number, delivered_at) VALUES (?, ?)', (ticket_number, delivered_at))
        query = 'DELETE FROM customers WHERE id = ?'
        self.conn.execute(query, (customer_id,))
        self.conn.commit()

    def get_today_customers(self):
        today = datetime.now().strftime('%Y-%m-%d')
        query = "SELECT * FROM customers WHERE created_at LIKE ? ORDER BY CAST(ticket_number AS INTEGER) ASC"
        cursor = self.conn.execute(query, (today + '%',))
        return cursor.fetchall()

    def get_last_delivered_ticket(self):
        today = datetime.now().strftime('%Y-%m-%d')
        query = "SELECT ticket_number FROM delivered_customers WHERE delivered_at LIKE ? ORDER BY delivered_at DESC LIMIT 1"
        cursor = self.conn.execute(query, (today + '%',))
        row = cursor.fetchone()
        return row[0] if row else None

    def get_today_bread_count(self):
        today = datetime.now().strftime('%Y-%m-%d')
        query = "SELECT SUM(bread_count) FROM customers WHERE created_at LIKE ?"
        cursor = self.conn.execute(query, (today + '%',))
        row = cursor.fetchone()
        return row[0] if row and row[0] is not None else 0

    def get_today_total_bread_count(self):
        today = datetime.now().strftime('%Y-%m-%d')
        query = "SELECT SUM(bread_count) FROM all_customers WHERE created_at LIKE ?"
        cursor = self.conn.execute(query, (today + '%',))
        row = cursor.fetchone()
        return row[0] if row and row[0] is not None else 0

    def get_today_total_customers(self):
        today = datetime.now().strftime('%Y-%m-%d')
        query = "SELECT COUNT(*) FROM all_customers WHERE created_at LIKE ?"
        cursor = self.conn.execute(query, (today + '%',))
        row = cursor.fetchone()
        return row[0] if row and row[0] is not None else 0

    def reset_all_data(self):
        self.conn.execute('DELETE FROM customers')
        self.conn.execute('DELETE FROM delivered_customers')
        self.conn.execute('DELETE FROM all_customers')
        self.conn.commit()

    def close(self):
        self.conn.close()
