from flask import Flask, render_template
from flask_ask import Ask, statement, question, session, context
from controller import welcome, re, condolences,ideas
from geopy.geocoders import Nominatim
import random
import requests

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

def get_alexa_location():
    URL =  "https://api.amazonalexa.com/v1/devices/{}/settings" \
           "/address".format(context.System.device.deviceId)
    TOKEN =  context.System.user.permissions.consentToken
    HEADER = {'Accept': 'application/json',
             'Authorization': 'Bearer {}'.format(TOKEN)}
    r = requests.get(URL, headers=HEADER)
    if r.status_code == 200:
        print(r.json())
        return(r.json())

"""These functions handle intent logic for the voice interface. """

@ask.intent('PositiveFeeling')
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
    return question((random.choice(congrats)) + '      ' + 'Is there anything else you need? Want to send a report? Want me to reccommend a therapist?')

@ask.intent('NegativeFeeling')
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
    session.attributes["State"] = "Suggested"
    response = evaluate_answers()
    if response == "Good job doing all those things. When you're depressed, those little things can be the most difficult.":
        suggestion_inquiry = "Let's try something else to improve your mood."
    else:
        suggestion_inquiry = "Here's an idea for an extra way to improve your mood."
        idea = ideas()

    return statement(message + "      " + suggestion_inquiry + "       " + idea + "          " + "I hope I could help. Would you like another suggestion?")

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
    return statement(message + "      " + response + "       " + suggestion_inquiry + "       " + idea + "          " + "I hope I could help.  Would you like another suggestion?")

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
            return statement(
                message + "      " + response + "       " + suggestion_inquiry + "       " + idea + "          " + "I hope I could help. Anything else I can do? I can send reports or suggest a local therapist.")
        elif session.attributes["State"] == "Suggested":
            session.attributes["State"] = "AnythingElse"
            return question("Okay, I hope that helped. Anything else I can do for you?")
        elif session.attributes["State"] == "AnythingElse":
            return question("No problem. Check in with me later. Goodbye")
        else:
            return question("I'm sorry, I didn't get that. How are you feeling? ")
    except:
        return question("I'm sorry, I didn't get that. How are you feeling?")


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
                return statement(
                    message + "      " + suggestion_inquiry + "       " + idea + "          " + "I hope I could help. Is there anything else I can do?")
        elif session.attributes["State"] == "Suggested":
            message = "Okay, here's another idea. "
            idea = ideas()
            session.attributes["State"] = "Suggested"
            return statement(
               message + "       " + idea + "          " + "Would you like another suggestion?")
        elif session.attributes["State"] == "AnythingElse":
            return question("Okay, I love to help. What can I do for you? Say help if you would like to learn about my other capabilites.")
        else:
            return question("I'm sorry, I didn't get that. How are you feeling? ")
    except:
        return question("I'm sorry, I didn't get that. How are you feeling? ")

@ask.intent('SuggestIdea')
def suggest_ideas():
    suggestion_inquiry = "Okay. Here's an idea for an extra way to improve your mood."
    idea = ideas()
    session.attributes["State"] = "Suggested"
    return statement(suggestion_inquiry + "       " + idea + "          " + "Would you like another suggestion?")

@ask.intent('HotLine')
def hot_line():
    return statement("""Please don't hurt yourself or anyone else. I may just be a robot, but I
                    was created by a person who wants to help you and thinks you are worth it.
                    Please call the National Suicide Prevention Hotline at 1-800-273-8255. They are available to  talk to you 24 hours a day, 7 days a week.
                    I've placed their number on a card in your Alexa app for reference.""") \
      .standard_card(title='National Suicide Prevention Hot Line', text='Call Now 1-800-273-8255 ', large_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Lifelinelogo.svg/1200px-Lifelinelogo.svg.png' )


@ask.intent('FindTherapist')
def find_therapist():
    keyword = "counseling OR therapist OR psychiatrist"
    alexa_location = get_alexa_location()
    geolocator = Nominatim()  # Set provider of geo-data
    address = "{}, {}".format(alexa_location["addressLine1"].encode("utf-8"),
                              alexa_location["city"].encode("utf-8"))
    location = geolocator.geocode(address)
    key = "AIzaSyA1yY-DOHIun0v_7kTwa_U5Ah6Am-kcjCM"
    print(address)
    print(location.latitude, location.longitude)
    URL = "https://maps.googleapis.com/maps/api/place/textsearch/json?location={}&query={}&key={}".format(location,keyword,key)
    #print(URL)
    r = requests.get(URL)
    if r.status_code == 200:
        first_output = r.json()
    else:
        return "Sorry, I'm having trouble doing that right now. Please try again later."
    results = first_output['results']
    idnum = (results[1]['place_id'])
    name = (results[1]['place_id'])
    # print(results[1])
    # print(idnum)
    URL2 = "https://maps.googleapis.com/maps/api/place/details/json?placeid={}&key={}".format(idnum, key)
    r2 = requests.get(URL2)
    if r2.status_code == 200:
        second_output = r2.json()
        phone = (second_output['result'])['international_phone_number']
        # print(second_output)
        # print(phone)
        return statement("""I've found a therapist near you. Their name is {}, and their number is {}. I've added their
        contact info to a card in the Alexa app. Is there anything else I can do?""").standard_card(title="I've found you a possible therapist",
                text="Name:{} \n Phone:{}",
                large_image_url="https://images.unsplash.com/photo-1489533119213-66a5cd877091?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=7c006c52fd09caf4e97536de8fcf5067&auto=format&fit=crop&w=1051&q=80").format(name,phone)
    else:
        return statement("Sorry, I'm having trouble doing that right now. Please try again later.")

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


#@ask.intent('AMAZON.HelpIntent')



if __name__ == '__main__':
    app.run(debug=True, port=5000)
