from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.Integer, nullable=False)
    # The four codes specified in ISO / IEC 5218 are:
    # 0 = Not known;
    # 1 = Male;
    # 2 = Female;
    # 9 = Not applicable.
    group = db.Column(db.String, nullable=False)
    id_faculty = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)

    def __repr__(self):
        return f'{self.id}, {self.name}, {self.surname}, {self.age}, {self.sex}, {self.group}, {self.id_faculty}'


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    faculty_name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'Faculty({self.id}, {self.faculty_name})'
