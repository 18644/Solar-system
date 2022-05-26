from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import SolarSystem, Planet
from . import db

views = Blueprint('views', __name__)

@views.route('/SolarSystems', methods=['GET', 'POST']) 
@login_required
def SolarSystems():
        if request.method == "GET":
                query = SolarSystem.query.all()
                return render_template("home.html", query ,user = current_user)

@views.route('/planet', methods=['POST', 'GET']) 
@login_required
def planet():
        if request.method == "GET":
                query = Planet.query.all()
                return render_template("planet.html", query ,user=current_user)