from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect
from flask import jsonify

from test import db
from test.models import User, Movedata

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/list')
def _list():
    user_list = User.query.order_by(User.id)
    return render_template('user/user_list.html', user_list=user_list)


@bp.route('/create', methods=('POST',))
def create():
    name = request.form['name']
    connection = 0
    exist_user = User.query.filter_by(name=name).first()
    if not exist_user:
        user = User(name=name, connection=connection)
        # 확인 필요
        db.session.add(user)
        db.session.commit()
        return jsonify(id=user.id, success=True)
    else:
        return jsonify(id=-1, success=False)


@bp.route('/connection', methods=('POST',))
def connection():
    name = request.form['name']
    connection = request.form['connection']
    user = User.query.filter_by(name=name).first()
    user.connection = connection
    db.session.commit()
    if connection == 1:
        movedata = Movedata(user=user, latitude=0, longitude=0, speed=0)
        db.session.add(movedata)
        db.session.commit()
    elif connection == 0:
        movedata = Movedata.query.filter_by(user_id=user.id).first()
        db.session.delete(movedata)
        db.session.commit()
    return jsonify(id=user.id, success=True)