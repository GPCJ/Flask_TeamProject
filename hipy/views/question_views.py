from flask import Blueprint, render_template, request, url_for, g
from werkzeug.utils import redirect
from datetime import datetime
from .. import db
from hipy.models import Photo
from hipy.models import Question

from hipy.views.auth_views import login_required

from hipy.forms import QuestionForm, AnswerForm

bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int, default=1)  # 페이지
    photos = Photo.query.order_by(Photo.id.desc())
    return render_template('question/question_list.html', photos=photos)


@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    if question_id == 1:
        return render_template('question/question_detail1.html')
    if question_id == 2:
        return render_template('question/question_detail2.html')
    if question_id == 3:
        return render_template('question/question_detail3.html')
    if question_id == 4:
        return render_template('question/question_detail4.html')
    if question_id == 5:
        return render_template('question/question_detail5.html')
    if question_id == 6:
        return render_template('question/question_detail6.html')


@bp.route('/create/<int:id>/', methods=('GET','POST'))
@login_required
def create(id):
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now(), user=g.user)
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('question/question_form.html', form=form, id = id)

@bp.route('/favorites/')
def favorites():
    favorites = Question.query.order_by(Question.create_date.desc())
    return render_template('question/favorite_list.html', favorites=favorites)
