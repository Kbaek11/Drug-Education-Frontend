from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


#Database
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, unique=True)
    team = db.Column(db.String(80), unique=False)

    def __init__(self, userId, team):
        self.userId = userId
        self.team = team


class Calendar(db.Model):
    __tablename__ = 'calendar'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.userId'))
    day1 = db.Column(db.Integer)
    day2 = db.Column(db.Integer)
    day3 = db.Column(db.Integer)
    day4 = db.Column(db.Integer)
    day5 = db.Column(db.Integer)
    day6 = db.Column(db.Integer)
    day7 = db.Column(db.Integer)
    day8 = db.Column(db.Integer)
    day9 = db.Column(db.Integer)
    day10 = db.Column(db.Integer)
    day11 = db.Column(db.Integer)
    day12 = db.Column(db.Integer)
    day13 = db.Column(db.Integer)
    day14 = db.Column(db.Integer)

    def __init__(self, userId, day1, day2, day3, day4, day5, day6, day7, day8,
                 day9, day10, day11, day12, day13, day14):
        self.userId = userId
        self.day1 = day1
        self.day2 = day2
        self.day3 = day3
        self.day4 = day4
        self.day5 = day5
        self.day6 = day6
        self.day7 = day7
        self.day8 = day8
        self.day9 = day9
        self.day10 = day10
        self.day11 = day11
        self.day12 = day12
        self.day13 = day13
        self.day14 = day14


class CalendarAnswers(db.Model):
    __tablename__ = 'calendaranswers'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.userId'))
    calendarId = db.Column(db.Integer, db.ForeignKey('calendar.id'))
    a1 = db.Column(db.Integer)
    a2 = db.Column(db.Integer)
    a3 = db.Column(db.Integer)

    def __init__(self, userId, calendarId, a1, a2, a3):
        self.userId = userId
        self.calendarId = calendarId
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3


class TrueFalse(db.Model):
    __tablename__ = 'truefalse'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.userId'))
    q1 = db.Column(db.Boolean)
    q2 = db.Column(db.Boolean)
    q3 = db.Column(db.Boolean)
    q4 = db.Column(db.Boolean)
    q5 = db.Column(db.Boolean)
    q6 = db.Column(db.Boolean)
    q7 = db.Column(db.Boolean)
    q8 = db.Column(db.Boolean)
    q9 = db.Column(db.Boolean)
    q10 = db.Column(db.Boolean)

    def __init__(self, userId, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
        self.userId = userId
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6
        self.q7 = q7
        self.q8 = q8
        self.q9 = q9
        self.q10 = q10