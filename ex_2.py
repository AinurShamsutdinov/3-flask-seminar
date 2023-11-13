from flask import Flask, jsonify
from datetime import datetime, timedelta

from model_book import db, Book, Author

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.cli.command('init-tables')
def init_tables():
    db.create_all()


@app.cli.command('add-books')
def init_books():
    book = Book(name='Existential crisis of middle aged men',
                date=(datetime.utcnow() - timedelta(days=133)),
                amount=31,
                id_author=1)
    book1 = Book(name='Existential crisis of middle aged cats',
                 date=(datetime.utcnow() - timedelta(days=133)),
                 amount=43,
                 id_author=2)
    book2 = Book(name='Existential crisis of middle aged dogs',
                 date=(datetime.utcnow() - timedelta(days=133)),
                 amount=17,
                 id_author=3)
    book3 = Book(name='Existential crisis of middle aged women',
                 date=(datetime.utcnow() - timedelta(days=133)),
                 amount=25,
                 id_author=4)
    db.session.add(book)
    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)
    db.session.commit()


@app.cli.command('add-authors')
def init_author():
    author = Author(name='John', surname='Kaczynski')
    author1 = Author(name='Mary', surname='Jane')
    author2 = Author(name='Tomy', surname='Lee')
    author3 = Author(name='Joodie', surname='Foster')
    db.session.add(author)
    db.session.add(author1)
    db.session.add(author2)
    db.session.add(author3)
    db.session.commit()


@app.cli.command('get-books')
def get_books():
    books = Book.query.all()
    json_books = jsonify(
        [{'id': book.id,
          'name': book.name,
          'date': book.date,
          'amount': book.amount,
          'id_author': book.id_author} for book in books]
    )
    print(json_books.get_data())


if __name__ == '__main__':
    app.run(debug=True)
