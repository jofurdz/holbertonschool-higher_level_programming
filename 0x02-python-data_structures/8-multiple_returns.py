#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        tupple = (len(sentence), sentence[0])
    else:
        tupple = (len(sentence), None)
    return tupple
