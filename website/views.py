from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note, Planet
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/', methods=['GET', 'POST'])
@login_required
def upload_file():
       uploaded_file = request.files['file']
       if uploaded_file.filename != '':
               uploaded_file.save(uploaded_file.filename)
       return redirect(url_for('SolarSystems'))

@views.route('/planet', methods=['POST', 'GET'])
@login_required
def planet():
       if request.method == "POST":
               query = Planet.query.all()
               return render_template("planet.html", query ,user=current_user)
       else:
               flash("Nothing found, please try again!")
               return render_template("planet.html")