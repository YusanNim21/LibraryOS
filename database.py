import sqlite3

def setup_database():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            item_id TEXT PRIMARY KEY,
            item_type TEXT NOT NULL,
            title TEXT NOT NULL,
            subject TEXT NOT NULL,
            rental_price REAL NOT NULL,
            copies INTEGER NOT NULL,
            
            -- Specific attributes (NULL if not applicable)
            book_format TEXT,  
            magazine_color TEXT,
            author TEXT,          
            release_year INTEGER  
        )
    ''')

    conn.commit()
    conn.close()
    print("Success: Upgraded database initialized!")

if __name__ == "__main__":
    setup_database()