from models import Book, Member, Transaction
from database import session
from datetime import date

def add_book(title, author, isbn, count):
  book = Book(title=title, author=author, isbn=isbn, count=count)
  session.add(book)
  session.commit()

def get_book():
  return session.query(Book).all()

def add_member(name, email):
  member = Member(name=name, email=email)
  session.add(member)
  session.commit()

def get_member():
  return session.query(Member).all()

def issue_book(book_id, member_id):
  book = session.query(Book).filter_by(id=book_id).first()
  if book and int(book.count) > 0:
    # Corrected: Call the method with parentheses to get the date
    transaction = Transaction(book_id=book_id, member_id=member_id, issue_date=date.today())
    book.count = int(book.count) - 1
    session.add(transaction)
    session.commit()
    print("> Book Issued")
  else:
    print("> Book not available for issue")


def return_book(transaction_id):
  transaction = session.query(Transaction).filter_by(id=transaction_id).first()
  if transaction and not transaction.return_date:
    transaction.return_date = date.today()
    book = session.query(Book).filter_by(id=transaction.book_id).first()
    book.count = int(book.count) + 1
    session.commit()
    print(">Book return to library")
  else:
    print(">Book is already returned or not issued")