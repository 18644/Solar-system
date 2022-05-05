from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from website.models import solarSystem, planet


views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
    solarSystem = request.form.get('solarSystem')
    
    return render_template('home.html')



