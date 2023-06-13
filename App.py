from flask import Flask, render_template



app = Flask(__name__, template_folder='Templates')

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/overview")
def overview():
    return render_template("overview.html")


@app.route('/service')
def service():
    return render_template("service.html")

@app.route('/<user>')
def welcome(user):
    return f'Hello {user}!, Welcome to the PaNalyzer'


if __name__ == '__main__':
    app.run(debug=True)