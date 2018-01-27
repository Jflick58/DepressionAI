import random

def random_welcome():
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


if __name__ == '__main__':

    random_welcome()
