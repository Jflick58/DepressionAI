from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from controller import welcome, re, condolences,ideas
import random

app = Flask(__name__)
ask = Ask(app, '/')

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

@ask.intent('Positive')
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

    session.attributes["feeling"] = "Good"
    session.attributes["State"] = "Question 0 Answered"
    return question((random.choice(congrats)) + '      ' + 'Is there anything else you need?')

@ask.intent('Negative')
def user_feels_bad():
    condolence = condolences()
    session.attributes["feeling"] = "Down"
    session.attributes["State"] = "Question 1 Answered"
    return question(condolence + "       " + "Have you gotten out of bed today?")

@ask.intent('BedYes')
def out_of_bed():

    message = random.choice([
                'Awesome.',
                'Good to hear!',
                'Wonderful!',
                'Great!',
    ])
    session.attributes["Bed"] = "Yes"
    session.attributes["State"] = "Question 2 Answered"
    return question (message + "         " + "Have you eaten today?")

@ask.intent('BedNo')
def not_out_of_bed():

    message = random.choice([
        "That's too bad.",
        "That's okay, we all have days like that.",
        "I'm sorry. ",
        "That's too bad",
        "It's okay."
    ])

    session.attributes["State"] = "Question 2 Answered"
    session.attributes["Bed"] = "No"
    return question(message + "            " + "Have you eaten today?")


@ask.intent('AteYes')
def eaten():
    message = random.choice([
        'Awesome.',
        'Good to hear!',
        'Wonderful!',
        'Great!',
    ])
    session.attributes["Eaten"] = "Yes"
    session.attributes["State"] = "Question 3 Answered"
    return question(message + "           " + "Have you showered today?")

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
    session.attributes["State"] = "Question 3 Answered"
    return question(message + "            " + "Have you showered today?")

@ask.intent('ShowerYes')
def showered():
    message = random.choice([
        'Awesome.',
        'Good to hear!',
        'Wonderful!',
        'Great!',
    ])

    session.attributes["Showered"] = "Yes"
    session.attributes["State"] = "Question 4 Answered"
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
    session.attributes["State"] = "Question 4 Answered"
    return question(message + "            " + "Have you gotten dressed?")

@ask.intent('DressedYes')
def dressed():
    message = random.choice([
        'Awesome.',
        'Good to hear!',
        'Wonderful!',
        'Great!',
    ])

    session.attributes["Dressed"] = "Yes"
    session.attributes["State"] = "Question 5 Answered"
    return question(message + "            " + "Have you gone outside at all today?")


@ask.intent('DressedNo')
def not_dressed():
    message = random.choice([
        "That's too bad.",
        "That's okay, we all have days like that.",
        "I'm sorry. ",
        "That's not good.",
        "It's okay."
    ])

    session.attributes["Dressed"] = "No"
    session.attributes["State"] = "Question 5 Answered"
    return question(message + "         " + "Have you gone outside at all today?")

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
    if response == "Good job doing all those things. When you're depressed, those little things can be the most difficult.":
        suggestion_inquiry = "Let's try something else to improve your mood."
    else:
        suggestion_inquiry = "Here's an idea for an extra way to improve your mood."
        idea = ideas()

    return statement(message + "      " + suggestion_inquiry + "       " + idea + "          " + "I hope I could help.  Check in with me again later!")

@ask.intent('OutsideNo')
def not_outside():
    message = random.choice([
        "That's too bad.",
        "That's okay, we all have days like that.",
        "I'm sorry. ",
        "That's not good.",
        "It's okay."
    ])

    session.attributes["Outside"] = "No"
    response = evaluate_answers()
    suggestion_inquiry = "Let's also try something else to improve your mood."
    idea = ideas()
    return statement(message + "      " + response + "       " + suggestion_inquiry + "       " + idea + "          " + "I hope I could help.  Check in with me again later!")

@ask.intent('AMAZON.NoIntent')
def handle_no():
    try:
        if session.attributes["State"] == "Question 0 Answered":
            return statement("Okay. Check in with me again later!")
        elif session.attributes["State"] == "Question 1 Answered":
            message = random.choice([
                "That's too bad.",
                "That's okay, we all have days like that.",
                "I'm sorry. ",
                "That's too bad",
                "It's okay."
            ])

            session.attributes["State"] = "Question 2 Answered"
            session.attributes["Bed"] = "No"
            return question(message + "            " + "Have you eaten today?")
        elif session.attributes["State"] == "Question 2 Answered":
            message = random.choice([
                "That's too bad.",
                "That's okay, we all have days like that.",
                "I'm sorry. ",
                "That's not good.",
                "It's okay."
            ])

            session.attributes["Eaten"] = "No"
            session.attributes["State"] = "Question 3 Answered"
            return question(message + "            " + "Have you showered today?")
        elif session.attributes["State"] == "Question 3 Answered":
            message = random.choice([
                "That's too bad.",
                "That's okay, we all have days like that.",
                "I'm sorry. ",
                "That's not good.",
                "It's okay."
            ])

            session.attributes["Showered"] = "No"
            session.attributes["State"] = "Question 4 Answered"
            return question(message + "            " + "Have you gotten dressed?")
        elif session.attributes["State"] == "Question 4 Answered":
            message = random.choice([
                "That's too bad.",
                "That's okay, we all have days like that.",
                "I'm sorry. ",
                "That's not good.",
                "It's okay."
            ])

            session.attributes["Dressed"] = "No"
            session.attributes["State"] = "Question 5 Answered"
            return question(message + "         " + "Have you gone outside at all today?")
        elif session.attributes["State"] == "Question 5 Answered":
            message = random.choice([
                "That's too bad.",
                "That's okay, we all have days like that.",
                "I'm sorry. ",
                "That's not good.",
                "It's okay."
            ])

            session.attributes["Outside"] = "No"
            response = evaluate_answers()
            suggestion_inquiry = "Let's also try something else to improve your mood."
            idea = ideas()
            return statement(
                message + "      " + response + "       " + suggestion_inquiry + "       " + idea + "          " + "I hope I could help.  Check in with me again later!")
        else:
            return question("I'm sorry, I didn't get that. How are you feeling? ")
    except:
        return question("I'm sorry, I didn't get that. How are you feeling? ")


@ask.intent('AMAZON.YesIntent')
def handle_yes():
    try:
        if session.attributes["State"] == "Question 0 Answered":
            return statement("Okay. What can I do for you?")

        elif session.attributes["State"] == "Question 1 Answered":
            message = random.choice([
                'Awesome.',
                'Good to hear!',
                'Wonderful!',
                'Great!',
            ])
            session.attributes["Bed"] = "Yes"
            session.attributes["State"] = "Question 2 Answered"
            return question(message + "         " + "Have you eaten today?")

        elif session.attributes["State"] == "Question 2 Answered":
            message = random.choice([
                'Awesome.',
                'Good to hear!',
                'Wonderful!',
                'Great!',
            ])
            session.attributes["Eaten"] = "Yes"
            session.attributes["State"] = "Question 3 Answered"
            return question(message + "           " + "Have you showered today?")

        elif session.attributes["State"] == "Question 3 Answered":
            message = random.choice([
                'Awesome.',
                'Good to hear!',
                'Wonderful!',
                'Great!',
            ])

            session.attributes["Showered"] = "Yes"
            session.attributes["State"] = "Question 4 Answered"
            return question(message + " " + "Have you gotten dressed?")

        elif session.attributes["State"] == "Question 4 Answered":
            message = random.choice([
                'Awesome.',
                'Good to hear!',
                'Wonderful!',
                'Great!',
            ])

            session.attributes["Dressed"] = "Yes"
            session.attributes["State"] = "Question 5 Answered"
            return question(message + "            " + "Have you gone outside at all today?")

        elif session.attributes["State"] == "Question 5 Answered":
            def outside():
                message = random.choice([
                    'Awesome.',
                    'Good to hear!',
                    'Wonderful!',
                    'Great!',
                ])

                session.attributes["Outside"] = "Yes"
                response = evaluate_answers()
                if response == "Good job doing all those things. When you're depressed, those little things can be the most difficult.":
                    suggestion_inquiry = "Let's try something else to improve your mood."
                else:
                    suggestion_inquiry = "Here's an idea for an extra way to improve your mood."
                    idea = ideas()

                return statement(
                    message + "      " + suggestion_inquiry + "       " + idea + "          " + "I hope I could help.  Check in with me again later!")
        else:
            return question("I'm sorry, I didn't get that. How are you feeling? ")
    except:
        return question("I'm sorry, I didn't get that. How are you feeling? ")

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
    app.run(debug=True, port=5000)
