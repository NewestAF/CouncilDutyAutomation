import random

import pandas as pd
import numpy as np
import sqlite3 as sql
from flask import Blueprint, render_template

from app import db
from app import models

bp = Blueprint('patrol', __name__, url_prefix='/patrol')

# if __name__ == '__main__':

@bp.route('/')
def index():
    lunch1 = pd.read_sql('select weekday, student1, student2 from patrol where type="점심1"', sql.connect("app/student.db"))
    lunch2 = pd.read_sql('select weekday, student1, student2 from patrol where type="점심2"', sql.connect("app/student.db"))
    smoking1 = pd.read_sql('select weekday, student1, student2 from patrol where type="흡연1"',
                           sql.connect("app/student.db"))
    smoking2 = pd.read_sql('select weekday, student1, student2 from patrol where type="흡연2"',
                           sql.connect("app/student.db"))

    return render_template('patrol.html',
                           lunch1=lunch1,
                           lunch2=lunch2,
                           smoking1=smoking1,
                           smoking2=smoking2)

@bp.route('/reset')
def patrol_reset():
    file = open("C:\\Users\\NewestAF\\Documents\\dev\\CouncilDutyAutomation\\app\\studentList.txt", "rt",
                encoding='UTF8')
    student_list1 = file.read().strip().split("\n")
    student_list2 = student_list1.copy()

    result = ""

    result += str(student_list1)
    result += "\n"

    pt = models.Patrol.query.all()
    for i in pt:
        db.session.delete(i)

    for i in range(0, 4):
        type = ''
        match i:
            case 0:
                type = '점심1'
            case 1:
                type = '점심2'
            case 2:
                type = '흡연1'
            case 3:
                type = '흡연2'
        for j in range(0, 5):
            if len(student_list1) == 0:
                student_list1 = student_list2.copy()
            student1 = random.choice(student_list1)
            student_list1.remove(student1)
            student2 = random.choice(student_list1)
            student_list1.remove(student2)
            patrol = models.Patrol(type=type, weekday=j, student1=student1, student2=student2)
            db.session.add(patrol)
            result += str(type) + " " + str(j) + " " + str(student1) + " " + str(student2)
            result += "\n"

    db.session.commit()
    return result
