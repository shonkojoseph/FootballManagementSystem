import sqlite3

def connect_db():
    return sqlite3.connect('football_manager.db')

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS teams (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        team_id INTEGER,
        FOREIGN KEY (team_id) REFERENCES teams (id) ON DELETE CASCADE
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Database tables created.")
