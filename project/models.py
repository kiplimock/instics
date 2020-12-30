from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
from project import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# abstract class person for all person classes
class Person(db.Model):
    __abstract__ = True
    
    name = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    image = db.Column(db.String(16), default='profile.png')

    def __init__(self, name, email):
        self.name = name
        self.email = email

# this model builds authentication table
class User(Person, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    pw_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(16), nullable=False)

    def __init__(self, name, email, password, role):
        super().__init__(name, email)
        self.pw_hash = generate_password_hash(password)
        self.role = role
    
    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

# stores details of admin users
class Console(Person):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    pw_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(16), nullable=False, default='admin')

    def __init__(self, name, email, password):
        super().__init__(name, email)
        self.pw_hash = generate_password_hash(password)
    

class Member(Person):
    __tablename__ = 'members'

    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(16), nullable=False)
    joined = db.Column(db.DateTime, nullable=False, default=date.today())
    books = db.relationship('BorrowedBook', backref='member', lazy=True)

    def __init__ (self, name, email, gender):
        super().__init__(name, email)
        self.gender = gender

class Librarian(Person):
    __tablename__ = 'librarians'

    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(16), nullable=False)
    joined = db.Column(db.DateTime, nullable=False, default=date.today())

    def __init__ (self, name, email, gender):
        super().__init__(name, email)
        self.gender = gender

# abstract class book for all book models to inherit from
class Book(db.Model):
    __abstract__ = True

    title = db.Column(db.String(64), nullable=False)
    subject = db.Column(db.String(128), nullable=False)
    image = db.Column(db.String(16), default='cover.png')

    def __init__(self, title, subject):
        self.title = title
        self.subject = subject
    
# stores individual books available in the library
class BookItem(Book):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(64), nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False)
    ISBN = db.Column(db.String(32), nullable=False)
    loan_period = db.Column(db.String(16), nullable=False)
    barcode = db.Column(db.String(64), nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(16), nullable=False)

    def __init__(self, title, subject, author, pub_date, ISBN, loan_period, barcode, pages, status):
        super().__init__(title, subject)
        self.author = author
        self.pub_date = pub_date
        self.ISBN = ISBN
        self.loan_period = loan_period
        self.barcode = barcode
        self.pages = pages
        self.status = status

# every borrowed books is entered in this table
class BorrowedBook(Book):
    __tablename__ = 'borrowedbooks'

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'), nullable=False)
    borrowed_on = db.Column(db.DateTime, nullable=False)
    returned_on = db.Column(db.DateTime, nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    fines = db.relationship('Fine', backref='borrowedbook', lazy=True)

    def __init__(self, title, subject, member_id, borrowed_on, returned_on, deadline):
        super().__init__(title, subject)
        self.member_id = member_id
        self.borrowed_on = borrowed_on
        self.returned_on = returned_on
        self.deadline = deadline

class Reserved(Book):
    __tablename__ = 'reservedbooks'

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'), nullable=False)

    def __init__(self, title, subject, member_id):
        super().__init__(title, subject)
        self.member_id = member_id

class Fine(db.Model):
    __tablename__ = 'fines'

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('borrowedbooks.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)

    def __init__(self, member_id, book_id, amount):
        self.member_id = member_id
        self.book_id = book_id
        self.amount = amount
