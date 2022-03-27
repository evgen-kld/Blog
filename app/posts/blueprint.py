from flask import Blueprint, render_template
from flask import render_template

posts = Blueprint('posts', __name__, template_folder='templates')

@posts.route('/')
def index():
    return render_template('posts/index.html')