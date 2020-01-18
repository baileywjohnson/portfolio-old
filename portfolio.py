from flask import Flask, render_template
from datetime import date
year_ = date.today().year
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', title='Home', year=str(year_))


@app.route("/projects")
def projects():
    return render_template('projects.html', title='Projects', year=str(year_))


@app.route("/other")
def other():
    return render_template('other.html', title='Other', year=str(year_))


@app.route("/twitterminer")
def twitterminer():
    return "Coming Soon"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
