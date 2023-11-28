from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/top1/')
def top1():
    return render_template('top1.html')


@app.route('/top2/')
def top2():
    return render_template('top2.html')


@app.route('/top3/')
def top3():
    return render_template('top3.html')


if __name__ == '__main__':
    app.run(debug=True)