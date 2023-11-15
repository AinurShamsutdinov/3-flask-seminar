from flask import Flask, request, render_template
from flask_wtf import CSRFProtect
from passlib.hash import sha256_crypt

from form_8 import RegistrationForm
from model_8 import db, User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_8.db'
app.config['SECRET_KEY'] = b'03d53c56782b623f838b2b17508c50ce258f1de46715845c1bd008754409cff0'
csrf = CSRFProtect(app)
db.init_app(app)


@app.route('/')
def index():
    return 'Hi, it is the 8th exercise'


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('8th exercise database is initiated')


@app.cli.command('get-users')
def get_users():
    users = User.query.all()
    for user in users:
        print(f'name={user.name}, surname={user.surname}, email={user.email}, password={user.password}')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form_reg = RegistrationForm()
    if request.method == 'POST' and form_reg.validate():
        user = User(name=form_reg.name.data,
                    surname=form_reg.surname.data,
                    email=form_reg.email.data,
                    password=sha256_crypt.encrypt(form_reg.password.data))
        db.session.add(user)
        db.session.commit()
        return f'User {user.name} {user.surname} was registered successfully!'
    return render_template('register_8.html', form=form_reg)


if __name__ == '__main__':
    app.run(debug=True)
