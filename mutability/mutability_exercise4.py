"""
Exercise 4
Use the Library class below for this coding exercise.
class Library:
Create the following methods for the Library class:
add_books - takes a list of book titles (strings) and adds each title to the list of available books
borrow_book - takes a book title (string) and moves it from the available list to the list of books 
on loan
return_book - takes a book title (string) and moves it from the list of books on loan to the list of 
available books
Expected Output
Assume you have an instance of the Library class called my_library. Add some books to object,
and then print the list of available books.
"""


class Library:
    """List of available books and list of books on loan"""

    def __init__(self):
        self.available = []
        self.on_loan = []

    def add_books(self, books):
        """Add each book to the list of available books"""
        for book in books:
            self.available.append(book)

    def borrow_book(self, book):
        """Remove book from available list and add to on loan list"""
        self.available.remove(book)
        self.on_loan.append(book)

    def return_book(self, book):
        """Remove book from on loan list and add to availabe list"""
        self.on_loan.remove(book)
        self.available.append(book)


my_library = Library()
my_library.add_books(
    [
        "Four Seasons",
        "Say Nothing",
        "Milkman",
        "Harry Potter and the Order of the Phoenix",
    ]
)
print(my_library.available)

my_library.borrow_book("Harry Potter and the Order of the Phoenix")
my_library.borrow_book("Say Nothing")
print(my_library.available)
print(my_library.on_loan)

my_library.return_book("Say Nothing")
print(my_library.available)
print(my_library.on_loan)
