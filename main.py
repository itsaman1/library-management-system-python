from crud import add_book, get_book,add_member, get_member, issue_book, return_book, get_transaction_by_member

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

def addNewMember():
  name = input("Enter member name: ")
  email = input("Enter member email: ")
  add_member(name, email)
  print(">New member added")

def printMember():
  members = get_member()
  for member in members:
    print(f"{member.id}: {member.name} (Email: {member.email})")

def issueABook():
  book_id = int(input("Enter book id: "))
  member_id = int(input("Enter member id: " ))
  issue_book(book_id, member_id)

def returnABook():
   transaction_id = int(input("Enter a transaction Id: "))
   return_book(transaction_id)

def getTransactionForMember():
  member_id = int(input("Enter a member id: "))
  transaction = get_transaction_by_member(member_id)
  for transaction in transaction:
    return_state = "Returns" if transaction.return_date else "Not Returned"
    print(f"Transaction ID: {transaction.id}, Book Id : {transaction.book_id} Issue Date:{transaction.issue_date}, Return Date:{transaction.return_date}, Status: {return_state}")

def main():
  while True:
    print("************************************")
    print("1. Add Book")
    print("2. View Book")
    print("3. Add Member")
    print("4. View Member")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. View Transaction by Member")
    print("8. Exit")
    print("************************************")

    choice = input("Enter your choice: ")

    if choice == "1":
      addNewBook()
    elif choice == "2":
      printBooks()
    elif choice == "3":
      addNewMember()
    elif choice == "4":
      printMember()
    elif choice == "5":
      issueABook()
    elif choice == "6":
      returnABook()
    elif choice == "7":
      getTransactionForMember()
    else:
      break
  
    

if __name__ == "__main__":
  main()