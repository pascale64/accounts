from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_paginate import Pagination, get_page_args
from bdf import db
from bdf.models import Auxilliere
from bdf.aux import bp
from bdf.aux.forms import AddAuxilliereForm



@bp.route('/aux', methods=['GET', 'POST'])
def aux():
    auxs = Auxilliere.query.order_by(Auxilliere.id.desc())
    forms = []
    def get_forms(offset=0, per_page=10):
        return forms[offset: offset + per_page]
    for aux in auxs:
        form = AddAuxilliereForm()
        form.id.default = aux.id
        form.name.default = aux.name
        forms.append(form)
    for form in forms:
        if form.validate_on_submit():
            if form.modify.data:
                aux = Auxilliere.query.filter_by(id=form.id.data).one()
                aux.name = form.name.data
                db.session.add(aux)
                db.session.commit()
            elif form.delete.data:
                aux = Auxilliere.query.filter_by(id=form.id.data).one()
                db.session.delete(aux)
                db.session.commit()
            return redirect(url_for('aux.aux'))
        page, per_page, offset = get_page_args(page_parameter='page',
                                               per_page_parameter='per_page')
        total = len(forms)
        pagination_forms = get_forms(offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total)
        form.process()  # Do this after validate_on_submit or breaks CSRF token
    return render_template('aux/aux.html', auxs=auxs, title=Auxilliere,
                          page=page, forms=pagination_forms, per_page=per_page, pagination=pagination)


@bp.route('/add_aux', methods=('GET', 'POST'))
def add_aux():
    form = AddAuxilliereForm()
    if form.validate_on_submit():
        aux = Auxilliere(id=form.id.data, name=form.name.data)
        db.session.add(aux)
        db.session.commit()
        flash('Congratulations, you have now a registered a new Aux!')
        return redirect(url_for('aux.aux'))
    return render_template('aux/add_aux.html', form=form)


    
    
