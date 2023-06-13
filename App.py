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


if __name__ == '__main__':
    app.run(debug=True)