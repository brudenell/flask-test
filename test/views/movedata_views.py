from flask import Blueprint, request, render_template
from flask import jsonify

from test import db
from test.models import User, Movedata

bp = Blueprint('movedata', __name__, url_prefix='/movedata')


@bp.route('/list')
def _list():
    movedata_list = Movedata.query.order_by(Movedata.id)
    return render_template('movedata/movedata_list.html', movedata_list=movedata_list)


@bp.route('/sac', methods=('POST',))
def sac():
    name = request.form['name']
    user = User.query.filter_by(name=name).first()
    movedata = Movedata.query.filter_by(user_id=user.id).first()
    movedata.latitude = float(request.form['latitude'])
    movedata.longitude = float(request.form['longitude'])
    movedata.speed = request.form['speed']
    db.session.commit()
    data = []
    md_list = Movedata.query.all()
    for md in md_list:
        data.append({'user_id':md.user_id,
                     'latitude':md.latitude,
                     'longitude':md.longitude,
                     'speed':md.speed})
    return jsonify(data)