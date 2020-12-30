from flask import Blueprint, render_template, flash
from project import db
from project.models import Member, User, BookItem
from project.librarians.forms import AddLibrarianForm, AddMemberForm, AddBookForm

librarians = Blueprint('librarians', __name__)

@librarians.route('/dashboard', methods=['GET','POST'])
def dashboard():
    form1 = AddLibrarianForm()
    form2 = AddMemberForm()
    form3 = AddBookForm()
    members = Member.query.all()
    books = BookItem.query.all()
    
    if form2.submit2.data and form2.validate():
        print("Good!")
        member = Member(
            name=form2.name.data,
            email=form2.email.data,
            gender=form2.gender.data
        )
        user = User(
            name=form2.name.data,
            email=form2.email.data,
            password='instics12345',
            role='member'
        )

        db.session.add(user)
        db.session.add(member)
        db.session.commit()
        flash('New member added successfully', 'alert-success')
    
    elif form3.submit3.data and form3.validate():
        book = BookItem(
            title=form3.title.data,
            subject=form3.subject.data,
            author=form3.subject.data,
            pub_date=form3.pub_date.data,
            ISBN=form3.isbn.data,
            loan_period=form3.loan_period.data,
            barcode=form3.barcode.data,
            pages=form3.pages.data,
            status="available"
        )

        db.session.add(book)
        db.session.commit()
        flash('New book added successfully', 'alert-success')
    return render_template('dashboard.html', form1=form1, form2=form2, form3=form3, members=members, books=books)