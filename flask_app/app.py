from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


# @app.route("/about")
# def about():
#     return "<h1>About</h1>"


if __name__ == "__main__":
    app.run(debug=True)