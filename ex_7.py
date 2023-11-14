from flask import Flask, request, render_template, redirect, url_for, session
from flask_wtf import CSRFProtect

from model_7 import db, User
from form_7 import RegistrationForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_7.db'
app.config['SECRET_KEY'] = b'03d53c56782b623f838b2b17508c50ce258f1de46715845c1bd008754409cff0'
csrf = CSRFProtect(app)
db.init_app(app)


@app.route('/')
def index():
    return 'Hi, 7th exercise is on the way!'


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('7th exercise database is initiated')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form_reg = RegistrationForm()
    if request.method == 'POST' and form_reg.validate():
        user = User(name=form_reg.name.data,
                    surname=form_reg.surname.data,
                    email=form_reg.email.data,
                    password=form_reg.password.data)
        db.session.add(user)
        db.session.commit()
        session['user_id'] = user.id
        return redirect(url_for('userpage'))
    return render_template('register_7.html', form=form_reg)


@app.route('/userpage/')
def userpage():
    user_id = session.get('user_id')
    user = User.query.filter(User.id == user_id).first()
    context = {
        'name': user.name,
        'surname': user.surname,
        'email': user.email
    }
    return render_template('userpage_7.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
