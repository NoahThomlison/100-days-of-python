from flask import Flask
import random
from flask import render_template

app = Flask(__name__)
value = random.randint(0, 10)
@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)