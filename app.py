from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app._static_folder = 'templates/static'

@app.route("/")
def home():
    return render_template("index.html", name="Michal")

if __name__ == "__main__":
    app.run(debug=False)
