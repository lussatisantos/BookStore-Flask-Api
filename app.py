from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'The young woman',
        'author': 'Unknown'
    },

    {
        'id': 2,
        'title': 'Nodejs is awesome',
        'author': 'John Doe'
    },

    {
        'id': 3,
        'title': 'The biggest Secret',
        'author': 'David Icker'
    },
]

# check all
@app.route('/books', methods=['GET'])
def get_book():
    return jsonify(books)

# check for id
@app.route('/books/<int:id>', methods=['GET'])
def get_book_to_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)

# edit
@app.route('/books/<int:id>', methods=['PUT'])
def edit_book(id):
    book_changed = request.get_json()
    for index,book in enumerate(books):
        if book.get('id') == id:
            books[index].update(book_changed)
            return jsonify(livro[indice])

# create
@app.route('/books', methods=['POST'])
def new_books():
    new_book = request.get_json()
    livros.append(new_book)

# delete
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book():
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]
    return jsonify(books)


app.run(
    port = 5000,
    host = 'localhost',
    debug = True
)