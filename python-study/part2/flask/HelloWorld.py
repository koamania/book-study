import sqlite3

from flask import Flask, jsonify, request

app = Flask(__name__)

app.debug = True


def jsonize(result):
    result_list = []
    for book in result:
        result_list.append({
            "title": book[0],
            "author": book[1],
            "translator": book[2],
            "pub_date": book[3],
            "isdn": book[4]
        })
    return result_list


@app.route("/")
def hello():
    with get_db_con() as con:
        cur = con.cursor()

        q = "select * from hanbit_books"

        cur.execute(q)
        result = list(cur.fetchall())

    result_json = jsonize(result);
    print(result_json)
    return jsonify(result_json)


@app.route("/hello/<name>")
def hello_with_name(name):
    return "Hello, {}".format(name)


@app.route("/books/by/author")
def get_books_by_author():
    name = request.args.get("name")

    with get_db_con() as con:
        cur = con.cursor()

        q = "SELECT * FROM hanbit_books WHERE author LIKE :name ORDER BY title"

        result = list(cur.execute(q, {"name": "%" + name + "%"}))

    result_json = jsonify(jsonize(result))

    return result_json


@app.route("/books/by/month")
def get_books_by_month():
    pass


def get_db_con() -> sqlite3.connect:
    return sqlite3.connect("db.sqlite")


if __name__ == "__main__":
    app.run()
