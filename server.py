from flask import Flask, request, redirect, url_for, render_template
import sqlite3

app = Flask(__name__)

def init_db():
    with sqlite3.connect("database.db") as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS submissions
                        (id INTEGER PRIMARY KEY, nickname TEXT, content TEXT)''')

@app.route('/')
def home():
    return "Server is running."

@app.route('/submit', methods=['POST'])
def submit():
    nickname = request.form['nickname']
    content = request.form['user-input']

    with sqlite3.connect("database.db") as conn:
        conn.execute("INSERT INTO submissions (nickname, content) VALUES (?, ?)", (nickname, content))

    return redirect(url_for('home'))


# Hello :)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

