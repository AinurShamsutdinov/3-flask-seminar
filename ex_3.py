from flask import Flask
from model_students_grades import db, Student, Grade

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studentbase.db'
db.init_app(app)


@app.cli.command('init-db')
def init_tables():
    db.create_all()
    print('Created all tables')


@app.cli.command('add-students')
def add_students():
    index_student = 5
    for i in range(1, index_student):
        student = Student(name=f'John{i}', surname=f'Smith{i}', group=f'Group {i}', email=f'john{i}@email.com')
        db.session.add(student)
    db.session.commit()


@app.cli.command('add-grades')
def add_grades():
    index_grade = 5
    for i in range(1, index_grade):
        grade = Grade(id_student=i, subject_name=f'subject {i}', grade=i)
        db.session.add(grade)
    db.session.commit()


@app.cli.command('get-students')
def get_students():
    students = Student.query.all()
    for student in students:
        print(student)
        print(student.grades)


if __name__ == '__main__':
    app.run(debug=True)
