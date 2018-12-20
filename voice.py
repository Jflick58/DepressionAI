#### Credit to Cookiecutter Flask Ask for built-in intent functions

from flask import Flask
from flask_ask import Ask, statement, question, session
from controller import welcome, re, condolences,ideas, get_alexa_location
import geocoder
import traceback
import random
import requests
import logging

logging.getLogger('flask_ask').setLevel(logging.DEBUG)

app = Flask(__name__)
ask = Ask(app, '/')

""" These functions handle what are essentially the beginning and end of the main use case of the skill."""
@ask.launch
def start_session():
    """ This function is what initializes the application. It calls the welcome() method from controller.py
    to generate a different welcome message each time """
    welcome_text = welcome()
    welcome_re_text = re()

    return question(welcome_text).reprompt(welcome_re_text)


def evaluate_answers():
    """This function evaluates the user's answers to the questions the skill poses if "NegativeFeeling" is called.
    It evaluates the functions in order of usual routine. """
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

# @ask.intent('StartReport')
# def start_reporting():
#     try:
#         if session.attributes['State'] == 'Startedreport':
#             return question("""Okay, please tell me the email address you would like the report sent to""")
#         elif session.attributes["State"] == "Question 0 Answered":
#             return question("""Okay, please tell me the email address you would like the report sent to""")
#         elif session.attributes["State"] == "Question 1 Answered":
#             return question("""Okay, please tell me the email address you would like the report sent to""")
#         else:
#             return question("""Okay, I can send a report for you. If you haven't told me how you feel,
#                     tell me after this, otherwise tell me the email address you would like the report sent to""")
#     except:
#         return question("""Okay, I can send a report for you. If you haven't told me how you feel,
#                             tell me after this, otherwise tell me the email address you would like the report sent to""")

# @ask.intent('Email')
# def get_name(email_address):
#     session.attributes["Email"] = email_address
#     return question("Okay, and what is your name?")
#
# @ask.intent('Name')
# def finish_report(person_name):
#     message = "Okay, I've sent a report to {} about your day. Is there anything else I can do?"
#     return question(message)

@ask.intent('PositiveFeeling')
def user_feels_good():
    """This function is triggered if the PositiveFeeling intent is detected. """
    congrats = [
        'That is so good to hear!',
        'I am happy you feel good today',
        'I am glad to hear that.',
        'Oh happy day!',
        'Awesome.',
        'Good to hear!',
        'Wonderful!',
        'Great!',
        'I am so happy about that!',
        'That is so great!'
    ]

    session.attributes["feeling"] = "Good"
    session.attributes["State"] = "Question 0 Answered"
    return question((random.choice(congrats)) + '      ' + 'Is there anything else you need? Want me to recommend a therapist?')

@ask.intent('NegativeFeeling')
def user_feels_bad():
    """This function is triggered if the NegativeFeeling intent is detected. This also kicks off the question to guage
    whether the user has perfomed daily activities."""
    condolence = condolences()
    session.attributes["feeling"] = "Down"
    session.attributes["State"] = "Question 1 Answered"
    return question(condolence + "       " + "Have you gotten out of bed today?")

""" The following functions are called depending on the user's answers."""
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
    session.attributes["State"] = "Suggested"
    response = evaluate_answers()
    if response == "Good job doing all those things. When you're depressed, those little things can be the most difficult.":
        suggestion_inquiry = "Let's try something else to improve your mood."
    else:
        suggestion_inquiry = "Here's an idea for an extra way to improve your mood."
        idea = ideas()

    return question(message + "      " + suggestion_inquiry + "       " + idea + "          " + "I hope I could help. Would you like another suggestion?")

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
    session.attributes["State"] = "Suggested"
    response = evaluate_answers()
    suggestion_inquiry = "Let's also try something else to improve your mood."
    idea = ideas()
    return question(message + "      " + response + "       " + suggestion_inquiry + "       " + idea + "          " + "I hope I could help.  Would you like another suggestion?")

""" The following functions handle the built-in Amazon intents based on the session state. """
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
            session.attributes["State"] = "Suggested"
            response = evaluate_answers()
            suggestion_inquiry = "Let's also try something else to improve your mood."
            idea = ideas()
            return question(
                message + "      " + response + "       " + suggestion_inquiry + "       " + idea + "          " + "I hope I could help. Anything else I can do?")
        elif session.attributes["State"] == "Suggested":
            session.attributes["State"] = "AnythingElse"
            return question("Okay, I hope that helped. Anything else I can do for you?")
        elif session.attributes["State"] == "AnythingElse":
            return statement("No problem. Check in with me later. Goodbye")
        else:
            return question("I'm sorry, I didn't get that. How are you feeling? ")
    except:
        return question("I'm sorry, I didn't get that. How are you feeling?")

@ask.intent('AMAZON.YesIntent')
def handle_yes():
    try:
        if session.attributes["State"] == "Question 0 Answered":
            return question("Okay. What can I do for you?")

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
                message = random.choice([
                    'Awesome.',
                    'Good to hear!',
                    'Wonderful!',
                    'Great!',
                ])

                session.attributes["Outside"] = "Yes"
                session.attributes["State"] = "Suggested"
                response = evaluate_answers()
                if response == "Good job doing all those things. When you're depressed, those little things can be the most difficult.":
                    suggestion_inquiry = "Let's try something else to improve your mood."
                else:
                    suggestion_inquiry = "Here's an idea for an extra way to improve your mood."
                    idea = ideas()
                session.attributes["State"] = "AnythingElse"
                return question(
                    message + "      " + suggestion_inquiry + "       " + idea + "          " + "I hope I could help. Is there anything else I can do?")
        elif session.attributes["State"] == "Suggested":
            message = "Okay, here's another idea. "
            idea = ideas()
            session.attributes["State"] = "Suggested"
            return question(
               message + "       " + idea + "          " + "Would you like another suggestion?")
        elif session.attributes["State"] == "AnythingElse":
            return question("Okay, I love to help. What can I do for you? Say help if you would like to learn about my other capabilities.")
        else:
            return question("I'm sorry, I didn't get that. How are you feeling? ")
    except:
        return question("I'm sorry, I didn't get that. How are you feeling? ")

""" The following functions handle the additional use cases of recommending a therapist, detecting and preventing suicide, and
giving ideas on how to improve the user's mood."""

@ask.intent('SuggestIdea')
def suggest_ideas():
    suggestion_inquiry = "Okay. Here's an idea for an extra way to improve your mood."
    idea = ideas()
    session.attributes["State"] = "Suggested"
    return question(suggestion_inquiry + "       " + idea + "          " + "Would you like another suggestion?")

@ask.intent('HotLine')
def hot_line():
    return statement("""Please don't hurt yourself or anyone else. I may just be a robot, but I
    was created by a person who wants to help you and thinks you are worth it. Please call the National Suicide
    Prevention Hotline at 1-800-273-8255. They are available to  talk to you 24 hours a day, 7 days a week.
    I've placed their number on a card in your Alexa app for reference.""") \
      .standard_card(title='National Suicide Prevention Hot Line', text='Call Now 1-800-273-8255 ', large_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Lifelinelogo.svg/1200px-Lifelinelogo.svg.png' )

@ask.intent('FindTherapist')
def find_therapist():
    """This function uses the Google Places API to recommend a therapist based on the user's location. """
    keyword = "counseling OR therapist OR psychiatrist"
    try:
        address = get_alexa_location()
        logging.info(address)
        pass
    except:
        logging.error("COULD NOT GET ALEXA LOCATION")
        logging.debug(traceback.format_exc())
        return statement("""Hmm. It appears that I can't find your location. Please allow access to your
                         location in the Alexa app and try again """).consent_card("read::alexa:device:all:address")
    g = geocoder.google(address)
    latlng = g.latlng
    location = "{},{}".format(latlng[0], latlng[1])
    print(location)
    key = "AIzaSyA1yY-DOHIun0v_7kTwa_U5Ah6Am-kcjCM"
    URL2 = "https://maps.googleapis.com/maps/api/place/textsearch/json?location={}&query={}&key={}".format(location,keyword,key)
    print(URL2)
    r2 = requests.get(URL2, verify=False)
    if r2.status_code == 200:
        first_output = r2.json()
    else:
        return "Sorry, I'm having trouble doing that right now. Please try again later."
    results = first_output['results']
    idnum = (results[1]['place_id'])
    name = (results[1]['name'])
    # print(results[1])
    # print(idnum)
    URL3 = "https://maps.googleapis.com/maps/api/place/details/json?placeid={}&key={}".format(idnum, key)
    r3 = requests.get(URL3, verify=False)
    if r3.status_code == 200:
        second_output = r3.json()
        phone = (second_output['result'])['international_phone_number']
        # print(second_output)
        # print(phone)
        session.attributes["State"] = "Null"
        message = """I've found a therapist near you.
        Their name is: {}, and their number is: {}. I've added their contact info to a card in the Alexa app.
         Is there anything else I can do?""".format(name,phone)
        card = "Name:{} \n Phone:{}".format(name,phone)
        return question(message).standard_card(title="I've found you a possible therapist",
                text=card,
                large_image_url="https://images.unsplash.com/photo-1489533119213-66a5cd877091?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=7c006c52fd09caf4e97536de8fcf5067&auto=format&fit=crop&w=1051&q=80")
    else:
        return statement("Sorry, I'm having trouble doing that right now. Please try again later.")


@ask.intent('AMAZON.StopIntent')
def handle_stop():
    """
    This handles the 'stop' built-in intention.
    """
    farewell_text = "Have a good day. I hope to hear from you soon."
    return statement(farewell_text)


@ask.intent('AMAZON.CancelIntent')
def handle_cancel():
    """
    This handles the 'cancel' built-in intention.
    """
    farewell_text = "Goodbye"
    return statement(farewell_text)


@ask.intent('AMAZON.HelpIntent')
def handle_help():
    """
    This handles the 'help' built-in intention.

    """

    help_text = """There's a few things I can do to help. I can recommend a therapist or offer a suggestion for
                a way to improve your mood. I also possess the capability to detect suicidal intentions,
                but I really hope that you won't need me to do that. """
    return question(help_text)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
