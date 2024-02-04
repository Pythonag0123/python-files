class LibraryBook:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available
    def borrow(self):
        if self.available:
            self.available = False
            print(f"You have borrowed {self.title} by {self.author}")
        else:
            print(f"Sorry, {self.title} by {self.author} is not available")
    def return_book(self):
        self.available = True
        print(f"You have returned {self.title} by {self.author}")
book1 = LibraryBook("A Good Girl's Guide to Murder", "Holly Jackson", True)
book1.borrow()
book1.return_book()

