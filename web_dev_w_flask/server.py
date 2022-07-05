#This project serves as a very simple intro to flask, it used flask to create a very simple guess-number game
#The user (client) guess by editing the url into the appropriate format

from flask import Flask
import random

app = Flask(__name__)
num = random.randrange(0,9)
print(num)
@app.route("/")
def home_page():
    return "<h1>Guess a number between 0 and 9</h1>" \
            "<img src='https://media.giphy.com/media/BzyTuYCmvSORqs1ABM/giphy.gif'>"

@app.route("/guess/<int:number>")
# @check_decorator
def check(number):
    if num > number:
        return "<h1>TOO LOW</h1>" \
               "<img src='https://media.giphy.com/media/11dR2hEgtN5KoM/giphy.gif'>"
    if num < number:
        return "<h1>TOO HIGH</h1>" \
               "<img src='https://media.giphy.com/media/ES4Vcv8zWfIt2/giphy.gif'>"
    if num == number:
        return "<h1>YOU GOT IT</h1>" \
               "<img src='https://media.giphy.com/media/WYEWpk4lRPDq0/giphy.gif'>"

if __name__ == "__main__":
    #run app in debug mode to auto-reload
    app.run(debug=True)





