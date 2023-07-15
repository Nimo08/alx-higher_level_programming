#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        res = (len(sentence), sentence[0])
        return res
    else:
        res += None
