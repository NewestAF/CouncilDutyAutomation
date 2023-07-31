import numpy as np
import pandas as pd
from flask import Blueprint, render_template
from pretty_html_table import build_table
import sqlite3 as sql

from app import models

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    data = models.PatrolStudent.query.all()
    data.sort(key=lambda x: x.day)

    lunch1 = ['점심']
    smoking1 = ['흡연']

    for i in data:
        if i.type == "점심":
            lunch1.append(i.name)
        else:
            smoking1.append(i.name)

    patrol_array = np.array([lunch1, smoking1])
    data_frame = pd.DataFrame(data=patrol_array, columns=['종류', '월요일', '화요일', '수요일', '목요일', '금요일'], index=['점심', '흡연'])

    return render_template('index.html', df=data_frame)
