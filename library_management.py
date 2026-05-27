# class Book
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
        self.total_copies = copies
        self.is_available = True
        
    def borrow(self):
        if self.is_available:
            print(f"{self.title} is borrowed")
            self.copies -= 1
            if self.copies == 0:
                self.is_available = False
        else:
            print(f"{self.title} is not available.")  

    def return_book(self):
        if self.copies < self.total_copies:
            print(f"Received The book: {self.title}")
            self.copies += 1
            self.is_available = True
        else:
            print(f"All copies of {self.title} are already in the Library")
    
    def info(self):
        status = "Available" if self.is_available else " All borrowed"
        print(f"Title: {self.title} | Author: {self.author} | Status: {status} | Copies: {self.copies}\n")
        
# class Library        
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        
    def search(self, title):
        for book in self.books:
            if book.title == title:
                book.info()
                break
        else:
            print(f"No book found with name: {title}")
                
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                book.borrow()
                break
        else:
            print(f"No book found with name: {title}")
                
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                break
        else:
            print(f"No book found with name: {title}")        
        
    def available_books(self):
        found = False
        for book in self.books:
            if book.is_available:
                book.info()
                found = True
        if not found:
            print("No books are currently available.")
                              
    def all_books(self):
        if not self.books:
            print("No books in the Library yet.")
        else:
            for book in self.books:
                book.info()

    def update_copies(self, title, count):
        if count == 0:
            print("Only non-zero numbers are allowed.")
            return
        for book in self.books:
            if book.title == title:
               if book.copies + count < 0:
                   print(f"Cannot remove more than available copies: {book.copies}.")
                   return
               book.copies += count
               book.total_copies += count
               book.is_available = book.copies > 0
               do = "Added" if count > 0 else "Removed"
               print(f"{do}! {book.title} now has {book.copies} copies.")
               break
        else:
           print(f"No book found with name: {title}.")        
        
 # Menu
lib = Library("Admin")
while True:
    try:
        st = int(input("\nWelcome to 'The Library'\nPress 1 for manager\nPress 2 for user\nPress 3 to Quit "))
    except ValueError:
        print("Only numbers are allowed")
        continue
    else:
        if st == 1:
# pas isonly a little safe measure to prevent user to enter manager's menu 
            pas = input("\nEnter password: ")
            if pas == "838383":                       
                while True:
                    try:
                        a = int(input("\nWelcome Manager\n Press 1 to Add book\n Press 2 to see all book\n Press 3 to update copies\n Press 4 to Quit "))
                    except ValueError:
                        print("Only numbers are allowed")
                        continue
                    else:
                        if a == 1:
                            title = input("\nEnter Title of the book: ").strip().title()
                            author = input("Enter Author of the book: ").strip().title()
                            while True:
                                try:
                                    copy = int(input("Enter Copies of the book: "))
                                except ValueError:
                                    print("Only numbers are allowed")
                                    continue
                                else:
                                    book = Book(title, author, copy)                            
                                    lib.add_book(book)
                                    break
                        elif a == 2:
                            lib.all_books()
                        elif a == 3:
                            t = input("Enter the title of book: ").strip().title()
                            if any(book.title == t for book in lib.books):
                                while True:
                                    try:
                                        more = int(input("Enter number (positive to add copies, negative to remove copies: "))
                                    except ValueError:
                                        print("Only numbers are allowed")
                                        continue
                                    else:
                                        lib.update_copies(t, more)
                                        break
                            else:
                                print(f"No book found with name: {t}")
                        elif a == 4:
                            break
                        else:
                            print("Invalid input")
                            continue
            else:
                print("Invalid password")
                continue
            
        elif st == 2:
            while True:
                try:
                    b = int(input("\nWelcome User\n Press 1 to Search book.\n Press 2 to Borrow book.\n Press 3 to Return book.\n Press 4 to see Available books.\n Press 5 to Quit. "))
                except ValueError:
                    print("Only numbers are allowed")
                    continue
                else:
                    if b == 1:
                        lib.search(input("\nEnter the book's title: ").strip().title())
                    elif b == 2:
                        lib.borrow_book(input("\nEnter the book's title: ").strip().title())
                    elif b == 3:
                        lib.return_book(input("\nEnter the book's title: ").strip().title())
                    elif b == 4:
                        lib.available_books()
                    elif b == 5:
                        break
                    else:
                        print("\nInvalid input")
                        continue
        elif st == 3:
            print("\nThanks for using.")
            break