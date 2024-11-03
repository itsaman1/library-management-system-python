from crud import add_book, get_book

def addNewBook():
  title = input("Enter the book title: ")
  author = input("Enter book author: ")
  isbn = input("Enter book ISBN: ")
  count = int(input("Enter number of copies: "))
  add_book(title, author, isbn, count)

def printBooks():
  books = get_book()
  for book in books:
      # available = ""
      # if book.count > 0:
      #   available = "Available"
      # else:
      #   available = "Not Available"
    available = "Available" if int(book.count) > 0 else "Not Available"
    print(f"{book.id}: '{book.title}' by {book.author} (ISBN: {book.isbn}) - {available} ({book.count} copies)")


def main():
  print("************************************")
  print("1.Add Book")
  print("2.View Book")
  print("************************************")

  choice = input("Enter your choice: ")

  if choice == "1":
    addNewBook()
  elif choice == "2":
    printBooks()
    

if __name__ == "__main__":
  main()