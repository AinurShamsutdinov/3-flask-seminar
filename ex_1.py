from flask import Flask, jsonify
from model_student import db, Student, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'


@app.cli.command('init-db')
def init_db():
    # show error with wrong wsgi.py
    db.create_all()
    print('OK')


@app.cli.command('add-students')
def add_user():
    student1 = Student(name='John', surname='Smith', age=20, sex=1, group='Fancy', id_faculty=1)
    student2 = Student(name='Jane', surname='Dow', age=21, sex=2, group='Shmancy', id_faculty=2)
    student3 = Student(name='John', surname='Dow', age=18, sex=1, group='Not fancy', id_faculty=3)
    student4 = Student(name='Jake', surname='Jillenhall', age=19, sex=1, group='Not shmancy', id_faculty=4)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.commit()
    print('Students in DB!')


@app.cli.command('add-faculties')
def add_user():
    faculty1 = Faculty(faculty_name='philosophy')
    faculty2 = Faculty(faculty_name='philology')
    faculty3 = Faculty(faculty_name='physics')
    db.session.add(faculty1)
    db.session.add(faculty2)
    db.session.add(faculty3)
    db.session.commit()
    print('Faculty in DB!')


@app.cli.command('get-faculty')
def get_faculties():
    faculties = Faculty.query.all()
    for faculty in faculties:
        print(faculty)


@app.cli.command('get-students')
def get_students():
    students = Student.query.all()
    for student in students:
        print(student)


if __name__ == '__main__':
    app.run(debug=True)
