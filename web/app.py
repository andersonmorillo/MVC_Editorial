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


@app.route('/book_detail', methods=['POST'])
def book_detail():
    title = request.form['title']
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    post_date = request.form['post_date']
    id_book = request.form['id_book']
    edition = request.form['edition']
    no_page = request.form['no_page']

    p = Book(title=title,  id_person=id_person, name=first_name, last_name=last_name, post_date= post_date, id_book=id_book, edition=edition, no_page=no_page)
    model.append(p)
    return render_template('book_detail.html', value=p)



@app.route('/books')
def books():
    data = [(i.title, i.id_person, i.name, i.last_name, i.post_date, i.id_book, i.edition, i.no_page) for i in model]
    print(data)
    return render_template('books.html', value=data)


if __name__ == '__main__':
    app.run()