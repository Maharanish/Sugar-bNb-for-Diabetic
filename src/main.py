import sqlite3
from controller import get_food, add_food
from branchNbound import knapsack_01_branch_and_bound, FoodItem

def main():
    conn = sqlite3.connect('src/database/food.db')
    
    try:
        # Meminta jumlah pilihan makanan dari pengguna
        while True:
            num_choices = int(input("Berapa banyak pilihan makanan yang ingin Anda makan hari ini? "))
            if num_choices >= 3:
                break
            print("Pilihan makanan minimal 3 buah. Silakan masukkan lagi.")
        food_choices = []

        for _ in range(num_choices):
            food_name = input("Masukkan nama makanan: ")
            quantity = float(input(f"Masukkan jumlah yang ingin Anda makan : "))
            food = get_food(conn, food_name)
            if not food:
                add_new = input(f"Makanan {food_name} belum ada di database. Apakah Anda ingin menambahkan data makanan ini? (yes/no) ").strip().lower()
                if add_new == 'yes':
                    carbo = float(input("Masukkan kadar karbohidrat: "))
                    sugar = float(input("Masukkan kadar gula: "))
                    enjoyment = float(input("Masukkan tingkat kenikmatan: "))
                    protein = float(input("Masukkan kadar protein: "))
                    quantity = float(input("Masukkan ukuran untuk kadar tersebut : "))
                    add_food(conn, food_name, carbo, sugar, enjoyment, protein, quantity)
                    food = get_food(conn, food_name)
                else:
                    print("Silakan masukkan makanan yang sudah ada di database.")
                    continue
            
            adjusted_food = (
                food[0],
                food[1],
                food[2],
                food[3],
                food[4],
                quantity
            )
            food_choices.append(adjusted_food)
       
        max_sugcar = float(input("Masukkan kapasitas gula + karbohidrat harian Anda: "))

        items = [FoodItem(name, sugar + carbo, protein + enjoyment) for name, carbo, sugar, enjoyment, protein, _ in food_choices]
        
            
        best_value, best_items = knapsack_01_branch_and_bound(items, max_sugcar)
        
        print("Total Nilai Keuntungan (Protein + Tingkat Kepuasan) Optimal:", best_value)
        print("Makanan yang terpilih:")
        for item in best_items:
            print(f"{item.name}")
        

    finally:
        conn.close()

if __name__ == "__main__":
    main()
