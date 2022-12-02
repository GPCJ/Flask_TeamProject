from flask import Blueprint, render_template, url_for

from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_hipy():
    return 'Hello, hipy!'


@bp.route('/')
def index():
    return redirect(url_for('question._list'))