import random

<<<<<<< HEAD
def welcome():
=======
def random_welcome():
>>>>>>> 291d75f02a639ec57a842c8a987e844f6ea5af41
    greetings = [
        'Hi,',
        'Hello,'
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

<<<<<<< HEAD
def re():
    reprompts = [
        'Are you still there?',
        'Did you leave?',
        'Did you still want me to check in on you?',
        'Hello?'
        'Are you there?'
    ]

    print((random.choice(reprompts)) + " " + (help_message()))
    return ((random.choice(reprompts)) + " " + (help_message()))

def help_message():
    return "Say 'help' if you need assistance."


if __name__ == '__main__':

    welcome()
    re()
=======

if __name__ == '__main__':

    random_welcome()
>>>>>>> 291d75f02a639ec57a842c8a987e844f6ea5af41
