import random

def welcome():
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
        "How are you feeling?",
        "How are you feeling today?",
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
    reprompts = [
        'Did you leave?',
        'Did you still want me to check in on you?',
        'Hello?',
        'Are you there?'
    ]

    print((random.choice(reprompts)) + " " + (help_message()))
    return ((random.choice(reprompts)) + " " + (help_message()))

def help_message():
    return "Say 'help' if you need assistance."

def condolences():
    condolences = [
        "I'm sorry to hear that.",
        "I'm sorry you aren't feeling well.",
        "I'm so sorry you feel like that.",
        "I'm sorry, it's going to get better.",
        "Your emotions are important during this time, and I’m happy to help you shoulder them.",
        "I promise it gets better.",
        "I'm sorry, but I am here for you."
    ]
    print(random.choice(condolences))
    return (random.choice(condolences))

def ideas():

    ideas = [
        "Go for a walk?",
        "Complete one chore?",
        "Play your favorite video game?",
        "Play your favorite game?",
        "Play with your pet?",
        "Watch a movie?",
        "Look at pictures from your last vacation?",
        "Put on a fancy outfit?",
        "Go thrifting?",
        "Work on your hobby?",
        "Go to the gym?",
        "Exercise?",
        "Do 10 push-ups?",
        "Wear a funky hat?",
        "Cook a delicious meal?",
        "Go window shopping?",
        "Do some Yoga?",
        "Put on 'Staying Alive' by the Bee Gees and dance!",
        "Repair something around your house?",
        "Watch a funny Youtube video?",
        "Go for a bike ride?",
        "Doodle!",
        "Paint a picture?",
        "Call a friend and hang out?",
        "Go to your favorite coffee shop?",
        "Go for a scenic drive?",
        "Get a new haircut?",
        "Read Reddit?",
        "Listen to your favorite music?",
        "Go fishing?",
        "Gaze at the starts?",
        "Meditate?",
        "Visit a museum?",
        "Watch a video of baby pugs?",
        "Do a puzzle?",
        "Re-arrange the furniture in a room in your house?",
        "Clean your house?",
        "Do laundry?",
        "Eat chocolate cake!",
        "Make a to-do list for this week?",
        "Prep your lunch for tomorrow?",
        "Look in a mirror and tell yourself that you are awesome!",
    ]

    return (random.choice(ideas))
if __name__ == '__main__':

    welcome()
    re()
    condolences()
