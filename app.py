"""WTForms-Adoption Agency"""

from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///Adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.app_context().push()
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def list_pets():
    """Shows list of all pets in db"""
    pets = Pet.query.all()
    return render_template('list.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def create_pet():
    """Creates a new pet"""
    form = AddPetForm()
    if form.validate_on_submit():
        data= {k: v for k,v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect('/')
    else:
        return render_template('add.html', form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Show display/edit form about a single pet"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available=form.available.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect ('/')
    else:
        # raise
        return render_template("edit.html", form=form, pet=pet)

