from flask import Blueprint, request, render_template
from flask import jsonify

from test import db
from test.models import User, Movedata

bp = Blueprint('movedata', __name__, url_prefix='/movedata')


@bp.route('/list')
def _list():
    movedata_list = Movedata.query.order_by(Movedata.id)
    return render_template('movedata/movedata_list.html', movedata_list=movedata_list)