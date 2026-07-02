# Library Book

# Create a Book class.

# Attributes:

# title
# author
# ISBN
# total_copies
# available_copies

# Methods:
# Borrow a book.
# Return a book.
# Check availability.
# Display book detail

class Book():
    def __init__(self,title,author,ISBN,total_copies,available_copies):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.total_copies = total_copies
        self.available_copies = available_copies

    def borrow(self):
        if(self.available_copies<=0):
            print(f'There are no available copies')
        

