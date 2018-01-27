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
    reprompts = [
        'Are you still there?',
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
        "I'm sorry you aren't feeling good.",
        "I'm so sorry you feel like that.",
        "I'm sorry, it's going to get better.",
        "Well that's not ideal.",
        "That's too bad.",
        "Your emotions are important during this time, and I’m happy to help you shoulder them.",
        "I promise it gets better. ",
        "I'm sorry, but I am here for you."
    ]
    print(random.choice(condolences))
    return (random.choice(condolences))

if __name__ == '__main__':

    welcome()
    re()
    condolences()
