class Library:
  def __init__(self):
    self.noBooks = 0
    self.books = []

  def addBook(self, book):
    self.books.append(book)
    self.noBooks = len(self.books)

  def showInfo(self):
    print(f"The library has {self.noBooks} books.The books are:")
    for book in self.books:
       print(book)
    

l1 = Library()
l1.addBook("Harry Potter")
l1.addBook("To Kill a Mockingbird")
l1.addBook("The Great Gatsby")
l1.addBook("Pride and Prejudice")
l1.addBook("The Catcher in the Rye")
l1.addBook("1984")
l1.addBook("The Hobbit")
l1.addBook("The Lord of the Rings")
l1.addBook("The Chronicles of Narnia")
l1.addBook("The Da Vinci Code")
l1.showInfo()


