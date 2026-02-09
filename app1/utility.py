import string
import random
import secrets

def password_generate(uppercase=True, digits=True, special=True, length=12):
    characters= string.ascii_lowercase

    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if special:
        characters += string.punctuation
    passwordss="".join(secrets.choice(characters) for _ in range(length))
    return passwordss
def strength(passwordss):
    score=0
    if len(passwordss)>=8:
        score+=1
    if any(c.isupper() for c in passwordss):
        score += 1
    if any(c.islower() for c in passwordss):
        score += 1
    if any(c.isdigit() for c in passwordss):
        score += 1
    if any(c in string.punctuation for c in passwordss):
        score += 1
    return score