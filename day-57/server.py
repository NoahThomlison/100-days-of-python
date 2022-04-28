from urllib import response
from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/')
def blogHome():
    url = "https://api.npoint.io/bc51ef055aeee88fde25"
    blogPosts = requests.get(url).json()
    print(blogPosts)
    return render_template("index.html", posts=blogPosts)

if __name__ == "__main__":
    app.run(debug=True)


