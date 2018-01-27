from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from controller import welcome, re

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def start_session():
    welcome_text = random_welcome()
    welcome_re_text = re()

    return question(welcome_text).reprompt(welcome_re_text)

"""These functions handle intent logic for the voice interface. """

if __name__ == '__main__':
    app.run(debug=True)
