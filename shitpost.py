import random as random

def shitPost(message):
    if message.lower() == "owo":
        responses = ["What's this?", "Nuzzles you"]
        choice = random.choice(responses)
        return(choice)
    if message.lower() == "rawr":
        responses = ["It means 'Fuck You' in dinosaur", "It means 'I Love You' in dinosaur", "XD Rawr~"]
        choice = random.choice(responses)
        return(choice)