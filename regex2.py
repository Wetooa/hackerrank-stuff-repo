import re

def check(card):
    if not re.search("^[456]\d{3}(-?\d{4}){3}$",card) or re.search(r"(\d)\1{3}", re.sub("-", "",card)): # also this egotistical shit
        return False
    return True

for i in range(int(input())):
    print("Valid" if check(input()) else "Invalid") # what the fuck learn this shit

