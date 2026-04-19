from flask import Flask, render_template

app = Flask(__name__)

print("app.py __name__ =", __name__)

@app.route("/students")
def students():
    return render_template("students.html")

@app.route("/")
def home():
    return render_template("index.html")

def run_server():
    print("Starting Flask server...")
    app.run(debug=True)

if __name__ == "__main__":
    print("app.py is running directly")
    run_server()