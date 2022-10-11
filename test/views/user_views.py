from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect

from test import db
from test.models import User

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/list')
def _list():
    user_list = User.query.order_by(User.id)
    return render_template('user/user_list.html', user_list=user_list)


@bp.route('/create', methods=('POST',))
def create():
    name = request.form['name']
    connection = 0
    user = User(name=name, connection=connection)
    # 확인 필요
    db.session.add(user)
    db.session.commit()
    return "create"