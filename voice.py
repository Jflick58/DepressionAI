from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
<<<<<<< HEAD
from controller import welcome, re
=======
from controller
>>>>>>> 291d75f02a639ec57a842c8a987e844f6ea5af41

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def start_session():
<<<<<<< HEAD
    welcome_text = random_welcome()
    welcome_re_text = re()

    return question(welcome_text).reprompt(welcome_re_text)

"""These functions handle intent logic for the voice interface. """

=======
    welcome_text = render_template('')
    welcome_re_text = render_template('welcome_re')

    return question(welcome_text).reprompt(welcome_re_text)

>>>>>>> 291d75f02a639ec57a842c8a987e844f6ea5af41
if __name__ == '__main__':
    app.run(debug=True)
