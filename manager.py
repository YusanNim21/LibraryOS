import sqlite3
from models import Book, Magazine, CD, DVD

class LibraryManager:
    def __init__(self):
        self.db_name = 'library.db'

    def _get_connection(self):
        return sqlite3.connect(self.db_name)

    def add_item(self, item):
        # VALIDATION: No negative numbers allowed!
        if item.rental_price < 0 or item.copies < 0:
            print("Error: Price and copies cannot be negative!")
            return

        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT item_id FROM inventory WHERE item_id = ?", (item.item_id,))
        if cursor.fetchone():
            print(f"Error: Item with ID {item.item_id} already exists!")
            conn.close()
            return

        # Safely extract all specific attributes
        book_format = getattr(item, 'book_format', None)
        magazine_color = getattr(item, 'color', None)
        author = getattr(item, 'author', None)              
        release_year = getattr(item, 'release_year', None)  
        
        item_type = item.__class__.__name__

        cursor.execute('''
            INSERT INTO inventory (item_id, item_type, title, subject, rental_price, copies, book_format, magazine_color, author, release_year)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (item.item_id, item_type, item.title, item.subject, item.rental_price, item.copies, book_format, magazine_color, author, release_year))
        
        conn.commit()
        conn.close()
        print(f"Success: Saved '{item.title}' to the database.")

    def update_item(self, original_id, updated_item):
        conn = self._get_connection()
        cursor = conn.cursor()
        
        # Extract attributes safely
        book_format = getattr(updated_item, 'book_format', None)
        magazine_color = getattr(updated_item, 'color', None)
        author = getattr(updated_item, 'author', None)
        release_year = getattr(updated_item, 'release_year', None)
        item_type = updated_item.__class__.__name__

        # Execute the UPDATE query
        cursor.execute('''
            UPDATE inventory 
            SET item_type = ?, title = ?, subject = ?, rental_price = ?, copies = ?, 
                book_format = ?, magazine_color = ?, author = ?, release_year = ?
            WHERE item_id = ?
        ''', (item_type, updated_item.title, updated_item.subject, updated_item.rental_price, 
              updated_item.copies, book_format, magazine_color, author, release_year, original_id))
        
        conn.commit()
        conn.close()
        print(f"Success: Updated item {original_id}.")

    def remove_item(self, item_id):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM inventory WHERE item_id = ?", (item_id,))
        
        if cursor.rowcount > 0:
            print(f"Success: Removed item {item_id}.")
        else:
            print(f"Error: Item {item_id} not found.")
            
        conn.commit()
        conn.close()

    def _row_to_object(self, row):
        item_id, item_type, title, subject, rental_price, copies, book_format, magazine_color, author, release_year = row
        
        if item_type == 'Book':
            return Book(item_id, title, subject, rental_price, copies, book_format, author)
        elif item_type == 'Magazine':
            return Magazine(item_id, title, subject, rental_price, copies, magazine_color)
        elif item_type == 'CD':
            return CD(item_id, title, subject, rental_price, copies, release_year)
        elif item_type == 'DVD':
            return DVD(item_id, title, subject, rental_price, copies, release_year)

    def show_available(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        print("\n--- Available Items ---")
        cursor.execute("SELECT * FROM inventory WHERE copies > 0")
        rows = cursor.fetchall()
        
        if not rows:
            print("No items currently available.")
        else:
            for row in rows:
                print(self._row_to_object(row))
        conn.close()

    def search_by_subject(self, subject):
        conn = self._get_connection()
        cursor = conn.cursor()
        print(f"\n--- Search Results for Subject: '{subject}' ---")
        cursor.execute("SELECT * FROM inventory WHERE subject = ? COLLATE NOCASE", (subject,))
        rows = cursor.fetchall()
        
        if not rows:
            print("No items found.")
        else:
            for row in rows:
                print(self._row_to_object(row))
        conn.close()