import random
import requests
import logging
import os
from flask_ask import context

logging.getLogger('flask_ask').setLevel(logging.DEBUG)

def get_alexa_location():
    """This functions gets the location of the User's Alexa device, if they have granted location permissions. """
    URL = "https://api.amazonalexa.com/v1/devices/{}/settings" \
          "/address".format(context.System.device.deviceId)
    TOKEN = context.System.user.permissions.consentToken
    HEADER = {'Accept': 'application/json',
              'Authorization': 'Bearer {}'.format(TOKEN)}
    r = requests.get(URL, headers=HEADER, verify=False)
    try:
    #if r.status_code == 200:
        alexa_location = r.json()
        logging.info(r.json())
        address = "{} {}".format(alexa_location["addressLine1"],
                             alexa_location["city"])
    except:
        logging.error('COULD NOT LOCATION FROM API')
        logging.debug(r.json())
        address = NULL
    return address

def welcome():
    """This function generates welcome messages that voice.py functions use to welcome the user."""
    greetings = [
        'Hi,',
        'Hello,',
        'Good day,',
        'Hola,',
        'Howdy,',
    ]

    inquires = [
        "How's it going?",
        "How are you doing?",
        "How are you feeling today?",
        "How are you feeling?",
        "How are you?",
        "How are you doing today?",
        "How is your day going?",
        "How have you been?",
        "How have you been feeling?",
        "How have you been today?",
        "How have you been feeling today?"
    ]

    welcome = ((random.choice(greetings)) + " " + (random.choice(inquires)))

    print(welcome)

    return (welcome)

def re():
    """This generates the re-prompt phrases that the skill uses if a user has not responded. """
    reprompts = [
        'Are you still there?',
        'Did you leave?',
        'Did you still want me to check in on you?',
        'Hello?',
        'Are you there?'
    ]

    help_message = "Say 'help' if you need assistance"
    print((random.choice(reprompts)) + " " + (help_message))
    return ((random.choice(reprompts)) + " " + (help_message))

def condolences():
    """This function  generates the condolences used by the voice.py functions when a user responds with something negative"""
    condolences = [
        "I'm sorry to hear that.",
        "I'm sorry you aren't feeling good.",
        "I'm so sorry you feel like that.",
        "I'm sorry, it's going to get better.",
        "Well that's not ideal.",
        "That's too bad",
        "Your emotions are important during this time, and I’m happy to help you shoulder them.",
        "I promise it gets better. ",
        "I'm sorry, but I am here for you."
    ]
    print(random.choice(condolences))
    return (random.choice(condolences))

def ideas():

    """This is the function that generates the idea for mood improvement that is offered by various voice.py functions"""

    ideas = [
        "Go for a walk.",
        "Complete one chore.",
        "Play your favorite video game.",
        "Play with your pet.",
        "Watch a movie.",
        "Look at pictures from your last vacation.",
        "Put on a fancy outfit.",
        "Go thrifting.",
        "Work on your hobby.",
        "Go to the gym.",
        "Exercise.",
        "Do 10 push-ups.",
        "Cook a delicious meal.",
        "Go window shopping.",
        "Do some Yoga.",
        "Repair something around your house.",
        "Go for a bike ride.",
        "Doodle.",
        "Paint a picture.",
        "Call a friend and hang out.",
        "Go to your favorite coffee shop.",
        "Go for a scenic drive.",
        "Get a new haircut.",
        "Listen to your favorite music.",
        "Go fishing.",
        "Gaze at the stars.",
        "Meditate.",
        "Vist a museum.",
        "Watch a video of baby pugs.",
        "Do a puzzle.",
        "Re-arrange the furniture in a room in your house.",
        "Clean your house.",
        "Do laundry.",
        "Make a to-do list for this week.",
        "Prep your lunch for tomorrow.",
        "Look in a mirror and tell yourself that you are awesome.",
    ]

    return (random.choice(ideas))





