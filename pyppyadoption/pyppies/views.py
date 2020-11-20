from flask import Blueprint,render_template,redirect,url_for
from pyppyadoption import db
from pyppyadoption.models import Pyppy
from pyppyadoption.pyppies.forms import AddForm,DelForm

pyppies_blueprint = Blueprint('pyppies',__name__,template_folder='templates/pyppies/')

@pyppies_blueprint.route('/add',methods=['GET','POST'])
def add():
  form = AddForm()

  if form.validate_on_submit():
    name = form.name.data
    new_pyp = Pyppy(name)
    db.session.add(new_pyp)
    db.session.commit()

    return redirect(url_for('pyppies.list'))
  return render_template('pyppy_add.html',form=form)

@pyppies_blueprint.route('/list')
def list():
  pyppies = Pyppy.query.all()
  return render_template('list.html',pyppies=pyppies)

@pyppies_blueprint.route('/delete',methods=["GET","POST"])
def delete():
  form = DelForm()
  pyppies = Pyppy.query.all()

  if form.validate_on_submit():
    id = form.id.data
    pyp = Pyppy.query.get(id)
    db.session.delete(pyp)
    db.session.commit()

    return redirect(url_for('pyppies.list'))
  return render_template('delete.html',pyppies=pyppies,form=form)