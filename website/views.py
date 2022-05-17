from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from sqlalchemy import func
from .models import SolarSystem, Planet
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['POST']) 
@login_required
def home():
        Search = request.form.get('SolarSystem')
        return render_template("home.html", user=current_user)

@views.route('/planet', methods=['POST', 'GET']) 
@login_required
def planet():
        if request.method == "POST":
                Planet = request.form.get('Planet')
                
                
        return render_template("home.html", Planet, user=current_user)



