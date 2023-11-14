from flask import Flask, request, render_template, jsonify, redirect, url_for, session
from flask_wtf.csrf import CSRFProtect
from datetime import datetime, date

from form_5 import RegistrationForm, ConfirmAgreement
from model_5 import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userdatabase_5.db'
app.config['SECRET_KEY'] = b'03d53c56782b623f838b2b17508c50ce258f1de46715845c1bd008754409cff0'
csrf = CSRFProtect(app)
db.init_app(app)


@app.route('/')
def index():
    return 'Hi, it is 5th exercise!'


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('User database for 5th exercise is initiated')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form_reg = RegistrationForm()
    if request.method == 'POST':
        user = User(name=form_reg.name.data,
                    email=form_reg.email.data,
                    birth_date=datetime.strptime(form_reg.birth_date.raw_data[0], '%Y-%m-%d'),
                    password=form_reg.password.data)
        db.session.add(user)
        db.session.commit()
        session['user_id'] = user.id
        return redirect(url_for('confirm'))
    return render_template('register_5.html', form=form_reg)


@app.route('/confirm/', methods=['GET', 'POST'])
def confirm():
    form_confirm = ConfirmAgreement()
    if request.method == 'POST':
        user_id = session.get('user_id')
        user_update = User.query.filter(User.id == user_id).first()

        setattr(user_update, 'agreement', form_confirm.agreement.data)
        db.session.commit()
        return redirect(url_for('userpage'))
    return render_template('confirm.html', form=form_confirm)


@app.route('/userpage/')
def userpage():
    user_id = session.get('user_id')
    user = User.query.filter(User.id == user_id).first()
    context = {
        'name': user.name,
        'email': user.email,
        'agreement': user.agreement,
        'birth_date': user.birth_date
    }
    return render_template('userpage.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
