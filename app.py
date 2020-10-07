from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)




@app.route('/')
def index():
    return redirect(url_for('hello_world'))

@app.route('/main')
def hello_world():
    return render_template('main_page.html')
    # return "<h1> Welcome To  World! </h1>"


if __name__ == '__main__':
    app.run(host='192.168.1.4')
