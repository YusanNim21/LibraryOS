class LibraryItem:
    def __init__(self, item_id, title, subject, rental_price, copies):
        self.item_id = item_id
        self.title = title
        self.subject = subject
        self.rental_price = rental_price
        self.copies = copies

    def __str__(self):
        return f"[{self.__class__.__name__}] ID: {self.item_id} | Title: {self.title} | Copies: {self.copies} | Price: LKR{self.rental_price:.2f}"

class Book(LibraryItem):
    def __init__(self, item_id, title, subject, rental_price, copies, book_format, author):
        super().__init__(item_id, title, subject, rental_price, copies)
        self.book_format = book_format
        self.author = author

    def __str__(self):
        return f"[Book] ID: {self.item_id} | Title: {self.title} by {self.author} | Copies: {self.copies}"

class Magazine(LibraryItem):
    def __init__(self, item_id, title, subject, rental_price, copies, color):
        super().__init__(item_id, title, subject, rental_price, copies)
        self.color = color

class CD(LibraryItem):
    def __init__(self, item_id, title, subject, rental_price, copies, release_year):
        super().__init__(item_id, title, subject, rental_price, copies)
        self.release_year = release_year 

class DVD(LibraryItem):
    def __init__(self, item_id, title, subject, rental_price, copies, release_year):
        super().__init__(item_id, title, subject, rental_price, copies)
        self.release_year = release_year 