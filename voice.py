from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from controller import welcome, re, condolences
import random

app = Flask(__name__)
ask = Ask(app, '/')
answers = []

@ask.launch
def start_session():
    welcome_text = welcome()
    welcome_re_text = re()

    return question(welcome_text).reprompt(welcome_re_text)

def evaluate_answers():
    if session.attributes["Bed"] == "No":
        return "Okay, well let's start by getting out of bed. You can do it!"
    elif session.attributes["Eaten"] == "No":
        return "That's okay, but you should try to eat. You got this!"
    elif session.attributes["Showered"] == "No":
        return "Hmmm. Maybe you should take a nice, hot shower. It will help you feel better."
    elif session.attributes["Dressed"] == "No":
        return "Alright. Well let's try getting dressed. You can do it!"
    elif session.attributes["Outside"] == "No":
        return "Well let's try going outside. It might elate you. "
    else:
        return "Good job doing all those things. When you're depressed, those little things can be the most difficult"


"""These functions handle intent logic for the voice interface. """

@ask.intent('Positivefeeling')
def user_feels_good():
    congrats = [
        'That is so good to hear!',
        'I am happy you feel good today',
        'I am glad to hear that.',
        'Oh happy day!',
        'Awesome.',
        'Good to hear!',
        'Wonderful!',
        'Great!',
        'I am so happy about that!'
    ]

    return statement((random.choice(congrats)) + ' ' + 'Check in with me tomorrow so I can see how you are doing!')

@ask.intent('Negativefeeling')
def user_feels_bad():
    condolence = condolences()

    return question(condolence + "Have you gotten out of bed today?")

@ask.intent('BedYes')
def out_of_bed():

    message = random.choice([
                'Awesome.',
                'Good to hear!',
                'Wonderful!',
                'Great!',
    ])
    session.attributes["Bed"] = "Yes"
    return question (message + " " + "Have you eaten today?")

@ask.intent('BedNo')
def not_out_of_bed():

    message = random.choice([
        "That's too bad.",
        "That's okay, we all have days like that.",
        "I'm sorry. ",
        "That's too bad",
        "It's okay."
    ])

    session.attributes["Bed"] = "No"
    return question(message + " " + "Have you eaten today?")

@ask.intent('AteYes')
def eaten():
    message = random.choice([
        'Awesome.',
        'Good to hear!',
        'Wonderful!',
        'Great!',
    ])
    session.attributes["Eaten"] = "Yes"
    return question(message + " " + "Have you showered today?")

@ask.intent('AteNo')
def not_eaten():
    message = random.choice([
        "That's too bad.",
        "That's okay, we all have days like that.",
        "I'm sorry. ",
        "That's not good.",
        "It's okay."
    ])

    session.attributes["Eaten"] = "No"
    return question(message + " " + "Have you showered today?")

@ask.intent('ShowerYes')
def showered():
    message = random.choice([
        'Awesome.',
        'Good to hear!',
        'Wonderful!',
        'Great!',
    ])

    session.attributes["Showered"] = "Yes"
    return question(message + " " + "Have you gotten dressed?")

@ask.intent('ShowerNo')
def not_showered():
    message = random.choice([
        "That's too bad.",
        "That's okay, we all have days like that.",
        "I'm sorry. ",
        "That's not good.",
        "It's okay."
    ])

    session.attributes["Showered"] = "No"
    return question(message + " " + "Have you gotten dressed?")

@ask.intent('DressedYes')
def dressed():
    message = random.choice([
        'Awesome.',
        'Good to hear!',
        'Wonderful!',
        'Great!',
    ])

    session.attributes["Outside"] = "Yes"
    return question(message + " " + "Have you gone outside at all today?")


@ask.intent('DressedNo')
def not_dressed():
    message = random.choice([
        "That's too bad.",
        "That's okay, we all have days like that.",
        "I'm sorry. ",
        "That's not good.",
        "It's okay."
    ])

    session.attributes["Showered"] = "No"
    return question(message + " " + "Have you gone outside at all today?")

@ask.intent('OutsideYes')
def outside():
    message = random.choice([
        'Awesome.',
        'Good to hear!',
        'Wonderful!',
        'Great!',
    ])

    session.attributes["Outside"] = "Yes"
    response = evaluate_answers()
    if response == "Good job doing all those things. When you're depressed, those little things can be the most difficult":
        suggestion_inquiry = "Let's try something else to improve your move"
    else:
        suggestion_inquiry = "Would you like an additional idea for activites to improve your mood?"
    return question(message)

@ask.intent('OutsideNo')
def not_outiside:
    message = random.choice([
        "That's too bad.",
        "That's okay, we all have days like that.",
        "I'm sorry. ",
        "That's not good.",
        "It's okay."
    ])

    session.attributes["Outside"] = "No"
    return question(message)










@ask.intent('AMAZON.StopIntent')
def handle_stop():
    """
    (STATEMENT) Handles the 'stop' built-in intention.
    """
    farewell_text = render_template('stop_bye')
    return statement(farewell_text)


@ask.intent('AMAZON.CancelIntent')
def handle_cancel():
    """
    (STATEMENT) Handles the 'cancel' built-in intention.
    """
    farewell_text = render_template('cancel_bye')
    return statement(farewell_text)


@ask.intent('AMAZON.HelpIntent')
def handle_help():
    """
    (QUESTION) Handles the 'help' built-in intention.

    You can provide context-specific help here by rendering templates conditional on the help referrer.
    """

    help_text = render_template('help_text')
    return question(help_text)

if __name__ == '__main__':
    app.run(debug=True)