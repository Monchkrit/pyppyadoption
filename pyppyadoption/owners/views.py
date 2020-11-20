from flask import Blueprint,render_template,redirect,url_for
from pyppyadoption import db
from pyppyadoption.models import Owner, Pyppy
from pyppyadoption.owners.forms import AddForm

owners_blueprint = Blueprint('owners',__name__,template_folder='templates/owners/')

@owners_blueprint.route('/add',methods=['GET','POST'])
def add():
  pyppies = Pyppy.query.all()
  form = AddForm()

  if form.validate_on_submit():
    name = form.name.data
    new_owner = Owner(name)
    new_owner.street = form.street.data
    new_owner.city = form.city.data
    new_owner.state = form.state.data
    new_owner.zipcode = form.zipcode.data
    new_owner.pypid = form.pypid.data
    db.session.add(new_owner)
    db.session.commit()

    return redirect(url_for('pyppies.list'))
  return render_template('add.html',pyppies=pyppies,form=form)
