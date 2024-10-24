from flask import Flask, request, jsonify

app = Flask(__name__)


books = ["Harry Potter", "Fire and Ice", "Physics"]


@app.route('/flask/insert_book/', methods=['POST'])
def insert_book():
    try:
        book_data = request.json
        new_book = book_data.get('book_name')

        if new_book:
            books.append(new_book)
            return jsonify({"message": "Book inserted"}), 200
        else:
            return jsonify({"message": "Book name not provided"}), 400

    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route('/flask/books', methods=['GET'])
def get_books():
    try:
        return jsonify({"message": books}), 200

    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route('/flask/update_record', methods=['PUT'])
def update_book():
    try:
        book_data = request.json
        book_id = book_data.get('book_id')
        new_book_name = book_data.get('book_name')

        if 0 <= book_id < len(books):
            books[book_id] = new_book_name
            return jsonify({"message": books}), 200
        else:
            return jsonify({"message": "Invalid book ID"}), 400

    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route('/flask/delete', methods=['DELETE'])
def delete_book():
    try:
        book_data = request.json
        book_id = book_data.get('book_id')

        if 0 <= book_id < len(books):
            del books[book_id]
            return jsonify({"message": books}), 200
        else:
            return jsonify({"message": "Invalid book ID"}), 400

    except Exception as e:
        return jsonify({"message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
