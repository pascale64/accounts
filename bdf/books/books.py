from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
import csv
from bdf import db
from bdf.models import  Book
from bdf.books import bp
from bdf.books.forms import AddBookForm



@bp.route('/books', methods=['GET', 'POST'])
def books():
    books = Book.query.order_by(Book.date.desc())
    forms = []
    for book in books:
        form = AddBookForm()
        form.id.default = book.id
        form.date.default = book.date
        form.description.default = book.description
        form.debit.default = book.debit
        form.credit.default = book.credit
        form.montant.default = book.montant
        form.AUX.default = book.AUX
        form.TP.default = book.TP
        form.REF.default = book.REF
        form.JN.default = book.JN
        form.PID.default = book.PID
        form.CT.default = book.CT
        forms.append(form)
    for form in forms:
        if form.validate_on_submit():
            if form.modify.data:
                book = Book.query.filter_by(id=form.id.data).one()
                book.date = form.date.data
                book.description = form.description.data
                book.debit = form.debit.data
                book.credit = form.credit.data
                book.montant = form.montant.data
                book.AUX = form.AUX.data
                book.TP = form.TP.data
                book.REF = form.REF.data
                book.JN = form.JN.data
                book.PID = form.PID.data
                book.CT = form.CT.data
                db.session.add(book)
                db.session.commit()
            elif form.delete.data:
                book = Book.query.filter_by(id=form.id.data).one()
                db.session.delete(book)
                db.session.commit()
                return redirect(url_for('books.books'))
        form.process()  # Do this after validate_on_submit or breaks CSRF token
    return render_template('books/books.html', books=books, title='books', forms=forms)


@bp.route('/books/add_book', methods=('GET', 'POST'))
def add_book():
    form = AddBookForm()
    if form.validate_on_submit():
        obj = Book(id=form.id.data, date=form.date.data, description=form.description.data, debit=form.debit.data,\
                  credit=form.credit.data, montant=form.montant.data, AUX=form.AUX.data, TP=form.TP.data,\
                  REF=form.REF.data, JN=form.JN.data, PID=form.PID.data, CT=form.CT.data)
        db.session.add(obj)
        db.session.commit()
        flash('Congratulations, you have now a registered a new Aux!')
        return redirect(url_for('books.books'))
    return render_template('books/add_book.html', form=form)

