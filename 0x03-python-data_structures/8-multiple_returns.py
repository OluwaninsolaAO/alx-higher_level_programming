#!/usr/bin/python3
def multiple_returns(sentence):
    """No add descrptn since: well sentence"""
    if not sentence:
        return (len(sentence), None)
    else:
        return (len(sentence), sentence[0])
