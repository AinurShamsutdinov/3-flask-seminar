from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    group = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    grades = db.relationship('Grade', backref='grades', lazy=False)

    def __repr__(self):
        return f'id={self.id}, name={self.name}, surname={self.surname}, group={self.group}, email={self.email}'


class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_student = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    subject_name = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'id={self.id}, subject_name={self.subject_name}, grade={self.grade}'
