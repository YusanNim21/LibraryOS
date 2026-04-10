from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from models import Book, Magazine, CD, DVD
from manager import LibraryManager

app = Flask(__name__)
lib_manager = LibraryManager() 

def get_db_connection():
    #  Helper function to get a database connection that returns dictionary-like rows.
    conn = sqlite3.connect('library.db')
    conn.row_factory = sqlite3.Row 
    return conn

@app.route('/')
def index():
    # Check if the user typed something in the search bar
    search_query = request.args.get('q')
    
    conn = get_db_connection()
    
    if search_query:
        # Use SQL 'LIKE' to find partial matches in the subject
        items = conn.execute('SELECT * FROM inventory WHERE subject LIKE ? COLLATE NOCASE', ('%' + search_query + '%',)).fetchall()
    else:
        items = conn.execute('SELECT * FROM inventory').fetchall()
        
    conn.close()
    
    return render_template('index.html', items=items)

@app.route('/add', methods=('GET', 'POST'))
def add_item():
    if request.method == 'POST':
        item_type = request.form['item_type']
        item_id = request.form['item_id']
        title = request.form['title']
        subject = request.form['subject']
        rental_price = float(request.form['rental_price'])
        copies = int(request.form['copies'])

        # Create the correct object
        if item_type == 'Book':
            format_type = request.form.get('book_format', '')
            author = request.form.get('author', '')
            new_item = Book(item_id, title, subject, rental_price, copies, format_type, author)
        elif item_type == 'Magazine':
            color = request.form.get('color', '')
            new_item = Magazine(item_id, title, subject, rental_price, copies, color)
        elif item_type == 'CD':
            year = request.form.get('release_year', 0)
            new_item = CD(item_id, title, subject, rental_price, copies, int(year) if year else None)
        elif item_type == 'DVD':
            year = request.form.get('release_year', 0)
            new_item = DVD(item_id, title, subject, rental_price, copies, int(year) if year else None)

        lib_manager.add_item(new_item)
        return redirect(url_for('index'))

    return render_template('add_item.html')

@app.route('/edit/<item_id>', methods=('GET', 'POST'))
def edit_item(item_id):
    conn = get_db_connection()
    item = conn.execute('SELECT * FROM inventory WHERE item_id = ?', (item_id,)).fetchone()
    
    if request.method == 'POST':
        item_type = request.form['item_type']
        title = request.form['title']
        subject = request.form['subject']
        rental_price = float(request.form['rental_price'])
        copies = int(request.form['copies'])

        if item_type == 'Book':
            format_type = request.form.get('book_format', '')
            author = request.form.get('author', '')
            updated_item = Book(item_id, title, subject, rental_price, copies, format_type, author)
        elif item_type == 'Magazine':
            color = request.form.get('color', '')
            updated_item = Magazine(item_id, title, subject, rental_price, copies, color)
        elif item_type == 'CD':
            year = request.form.get('release_year', 0)
            updated_item = CD(item_id, title, subject, rental_price, copies, int(year) if year else None)
        elif item_type == 'DVD':
            year = request.form.get('release_year', 0)
            updated_item = DVD(item_id, title, subject, rental_price, copies, int(year) if year else None)

        lib_manager.update_item(item_id, updated_item)
        conn.close()
        return redirect(url_for('index'))

    conn.close()
    return render_template('edit_item.html', item=item)

@app.route('/delete/<item_id>', methods=('POST',))
def delete_item(item_id):
    lib_manager.remove_item(item_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)