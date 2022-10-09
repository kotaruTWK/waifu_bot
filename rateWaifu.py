import random as random

def rateWaifu(waifu):
    random.seed(waifu)
    print(waifu)
    rate = random.randrange(0,100)
    return(str(waifu)+" is a "+ str(rate)+"/100")
