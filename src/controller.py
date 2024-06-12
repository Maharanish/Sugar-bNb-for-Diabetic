import sqlite3

def get_food(conn, name):
    with conn:
        return conn.execute("SELECT name, carbo, sugar, enjoyment, protein, quantity FROM food WHERE name = ?", (name,)).fetchone()

def add_food(conn, name, sugar, enjoyment, protein, price):
    with conn:
        conn.execute("INSERT INTO food (name, carbo, sugar, enjoyment, protein, quantity) VALUES (?, ?, ?, ?, ?)",
                     (name, carbo, sugar, enjoyment, protein, quantity))
