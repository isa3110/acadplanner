from flask import Blueprint, render_template
import utils

main_bp = Blueprint('main', __name__, template_folder='templates', static_folder='static')

@main_bp.route('/')
def home():
    print("---------------------")
    return render_template('home.html')