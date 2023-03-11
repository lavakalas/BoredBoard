from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Homepage")

app.run(port=8000, host='127.0.0.1')