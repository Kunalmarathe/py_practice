class BookStore:

  NoOfBooks = 0

  def __init__(self, name, author):
    self.Name = name
    self.Author = author
    BookStore.NoOfBooks += 1

  def Display(self):
    print(self.Name, " by " ,self.Author, "No of books", BookStore.NoOfBooks)

bookName = input("Enter the name of book: ")
authorName = input("Enter the author name: ")

obj1 = BookStore(bookName,authorName)
obj1.Display()

bookName = input("Enter the name of book: ")
authorName = input("Enter the author name: ")

obj2 = BookStore(bookName,authorName)
obj2.Display()