^#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        character = None
    else:
        character = sentence[0]
        return(len(sentence), character)
