import sqlite3
import os

def init_db(conn):
    with conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS food (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            carbo FLOAT,
            sugar FLOAT,
            enjoyment FLOAT CHECK(enjoyment <= 5),
            protein FLOAT,
            quantity FLOAT
        )''')

def seed_data(conn):
    food_seeder = [
        {
            "name": "Bubur Ayam",
            "carbo": 47.7,
            "sugar": 0.3,
            "protein": 34.5,
            "enjoyment": 4.5,
            "quantity": 300
        },
        {
            "name": "Indomie Goreng Rasa Rendang",
            "carbo": 186,
            "sugar": 27,
            "protein": 27,
            "enjoyment": 5,
            "quantity": 273
        },
        {
            "name": "Sate Ayam",
            "carbo": 3,
            "sugar": 0.9,
            "protein": 8.7,
            "enjoyment": 4,
            "quantity": 3
        },
        {
            "name": "Sup Ayam",
            "carbo": 30.3,
            "sugar": 0.9,
            "protein": 12.3,
            "enjoyment": 3.5,
            "quantity": 711
        },
        {
            "name": "Caesar Salad",
            "carbo": 30,
            "sugar": 6,
            "protein": 15,
            "enjoyment": 4,
            "quantity": 3
        },
        {
            "name": "Dada Ayam Fillet",
            "carbo": 3,
            "sugar": 3,
            "protein": 99,
            "enjoyment": 4.5,
            "quantity": 3
        },
        
        {
            "name": "Nasi Goreng",
            "carbo": 60,
            "sugar": 3,
            "protein": 15,
            "enjoyment": 4.7,
            "quantity": 300
        },
        {
            "name": "Mie Ayam",
            "carbo": 90,
            "sugar": 6,
            "protein": 21,
            "enjoyment": 4.8,
            "quantity": 450
        },
        {
            "name": "Gado-Gado",
            "carbo": 36,
            "sugar": 9,
            "protein": 18,
            "enjoyment": 4.6,
            "quantity": 600
        },
        {
            "name": "Rendang",
            "carbo": 24,
            "sugar": 1.5,
            "protein": 30,
            "enjoyment": 5,
            "quantity": 300
        }
    ]

    with conn:
        for food in food_seeder:
            conn.execute('''
            INSERT OR IGNORE INTO food (name, carbo, sugar, enjoyment, protein, quantity)
            VALUES (:name, :carbo, :sugar, :enjoyment, :protein, :quantity)
            ''', food)

def main():
    db_path = "src/database/food.db"
    if not os.path.exists(db_path):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        conn = sqlite3.connect(db_path)
        init_db(conn)
        seed_data(conn)
        conn.close()
    else:
        print("Database already exists.")

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Print all food data
    c.execute("SELECT * FROM food")
    rows = c.fetchall()
    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    main()
