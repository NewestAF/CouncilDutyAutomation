from app import db


class PatrolStudent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(), nullable=False)
    day = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Text(), nullable=False)


class Patrol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Text(), nullable=False)
    weekday = db.Column(db.Integer, nullable=False)
    student1 = db.Column(db.Text(), nullable=False)
    student2 = db.Column(db.Text(), nullable=False)
