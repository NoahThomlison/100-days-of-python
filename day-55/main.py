from flask import Flask
import random
app = Flask(__name__)
value = random.randint(0, 10)
@app.route("/")
def hello():
    return "<p>Guess a number between 1 and 10 in your URL</p>"

@app.route("/<int:guess>")
def checkGuess(guess):
  global value
  print(value)
  print(guess)
  if (guess > value):
    return (
      f"<h1>Your guess of {guess} was too high</h1>"
      '<iframe src="https://giphy.com/embed/BzyTuYCmvSORqs1ABM" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/hallmarkecards-cute-hallmark-shoebox-BzyTuYCmvSORqs1ABM">via GIPHY</a></p>'
      )
  elif(guess < value):
    return (
      f"<h1>Your guess of {guess} was too Low</h1>"
      '<iframe src="https://giphy.com/embed/3oEduQAsYcJKQH2XsI" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/cat-lasers-cucumber-3oEduQAsYcJKQH2XsI">via GIPHY</a></p>'
      )
  else:
    return(
    f'<h1>Your guess of {guess} was correct!</h1>'
    '<iframe src="https://giphy.com/embed/13CoXDiaCcCoyk" width="480" height="398" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/wiggle-shaq-13CoXDiaCcCoyk">via GIPHY</a></p>'
    )

if __name__ == "__main__":
    app.run(debug=True)