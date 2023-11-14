from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    agreement = db.Column(db.Boolean)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'id={self.id}, name={self.name}, email={self.email}, agreement={self.agreement}, password={self.password}'
