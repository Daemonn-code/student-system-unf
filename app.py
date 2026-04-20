from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# function to connect to database
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/students", methods=["GET", "POST"])
def students():
    conn = get_db_connection()

    if request.method == "POST":
        name = request.form["name"]
        conn.execute("INSERT INTO students (name) VALUES (?)", (name,))
        conn.commit()

    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()

    return render_template("students.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)