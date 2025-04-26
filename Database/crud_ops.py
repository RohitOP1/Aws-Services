import psycopg2

conn = psycopg2.connect(
    host="database-1.c5wu48gaox8x.ap-south-1.rds.amazonaws.com",
    database="testdb",  
    user="postgres",
    password="adityakumar",
    port=5432
)

cursor = conn.cursor()

# 1. CREATE Table
def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS games (
            game_id SERIAL PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            genre VARCHAR(50),
            release_year INTEGER
        );
    """)
    conn.commit()
    print("Table 'games' created.")

# 2. INSERT Data
def insert_game(title, genre, release_year):
    cursor.execute("""
        INSERT INTO games (title, genre, release_year)
        VALUES (%s, %s, %s);
    """, (title, genre, release_year))
    conn.commit()
    print(f"Game '{title}' inserted.")

# 3. READ Data
def read_games():
    cursor.execute("SELECT * FROM games;")
    games = cursor.fetchall()
    print("🎮 All Games:")
    for game in games:
        print(game)

# 4. UPDATE Data
def update_game(game_id, new_title):
    cursor.execute("""
        UPDATE games
        SET title = %s
        WHERE game_id = %s;
    """, (new_title, game_id))
    conn.commit()
    print(f"Game ID {game_id} updated to '{new_title}'.")

# 5. DELETE Data
def delete_game(game_id):
    cursor.execute("DELETE FROM games WHERE game_id = %s;", (game_id,))
    conn.commit()
    print(f"Game ID {game_id} deleted.")

# Run operations
try:
    create_table()
    insert_game("God of War", "Action", 2018)
    insert_game("The Witcher 3", "RPG", 2015)
    insert_game("FIFA 21", "Sports", 2020)

    read_games()

    update_game(2, "The Witcher 3: Wild Hunt")

    read_games()

    delete_game(3)

    read_games()

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    cursor.close()
    conn.close()
    print("Connection closed.")
