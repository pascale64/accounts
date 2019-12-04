from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_paginate import Pagination, get_page_args
import csv
from bdf import db
from bdf.models import  Book
from bdf.books import bp
from bdf.books.forms import AddBookForm



@bp.route('/books', methods=['GET', 'POST'])
def books():
    books = Book.query.order_by(Book.date.desc())
    forms = []
    def get_forms(offset=0, per_page=20):
        return forms[offset: offset + per_page]
    for book in books:
        form = AddBookForm()
        form.id.default = book.id
        form.date.default = book.date
        form.description.default = book.description
        form.debit.default = book.debit
        form.credit.default = book.credit
        form.montant.default = book.montant
        form.AUX.default = book.AUX
        form.type.default = book.type
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
                book.type = form.type.data
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
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(forms)
    pagination_forms = get_forms(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total)
    return render_template('books/books.html', books=books, title='books',
                          page=page, forms=pagination_forms, per_page=per_page, pagination=pagination)




@bp.route('/books/add_book', methods=('GET', 'POST'))
def add_book():
    form = AddBookForm()
    if form.validate_on_submit():
        obj = Book(id=form.id.data, date=form.date.data, description=form.description.data, debit=form.$
                  credit=form.credit.data, montant=form.montant.data, AUX=form.AUX.data, type=form.type$
                  REF=form.REF.data, JN=form.JN.data, PID=form.PID.data, CT=form.CT.data)
        db.session.add(obj)
        db.session.commit()
        flash('Congratulations, you have now a registered a new Aux!')
        return redirect(url_for('books.books'))
    return render_template('books/add_book.html', form=form)

