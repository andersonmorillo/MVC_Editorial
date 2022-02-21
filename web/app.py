from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.book import Book


app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/book', methods=['GET'])
def book():
    return render_template('book.html')



@app.route('/books')
def books():
    data = [(i.title, i.id_person, i.name, i.last_name, i.post_date, i.id_book, i.edition, i.no_page) for i in model]
    print(data)
    return render_template('books.html', value=data)


if __name__ == '__main__':
    app.run()