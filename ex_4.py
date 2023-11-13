from flask import Flask, request, render_template, jsonify
from flask_wtf.csrf import CSRFProtect
from forms import RegistrationForm
from model_user import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userdatabase.db'
app.config['SECRET_KEY'] = b'03d53c56782b623f838b2b17508c50ce258f1de46715845c1bd008754409cff0'
csrf = CSRFProtect(app)
db.init_app(app)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('DB for User created')


@app.route('/')
def index():
    return 'Hi, the 4 app works!'


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form_reg = RegistrationForm()
    if request.method == 'POST' and form_reg.validate():
        user_exist = User.query.filter(User.name == form_reg.name.data or User.email == form_reg.email.data).all()
        if len(user_exist) == 0:
            # processing data form and save
            user = User(name=form_reg.name.data, email=form_reg.email.data, password=form_reg.password.data)
            db.session.add(user)
            db.session.commit()
            context = {
                'title': 'User page',
                'name': form_reg.name.data
            }
            return render_template('userpage.html', **context)
        else:
            return jsonify({'error': f'User with name \"{form_reg.name.data}\" exists'}), 409
    return render_template('register.html', form=form_reg)


@app.route('/user/<string:username>')
def get_user_page(username):
    user = User.query.filter(User.name == username).all()
    if len(user) > 0:
        context = {
            'name': user[0].name,
            'email': user[0].email
        }
        return render_template('userpage.html', **context)
    else:
        return f'User with name {username} does not exist'


@app.cli.command('get-users')
def get_users():
    users = User.query.all()
    for user in users:
        print(user)


if __name__ == '__main__':
    app.run(debug=True)
