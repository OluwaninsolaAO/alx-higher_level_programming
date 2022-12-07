#!/usr/bin/python3i
def best_score(a_dictionary):
    """Returns the key to the highest value pair of a int in a dictionary"""
    if not a_dictionary:
        return "None"

    best_score_key = ""
    best_score = -99999999999999999999999999999
    for i in list(a_dictionary):
        if a_dictionary[i] > best_score:
            best_score = a_dictionary[i]
            best_score_key = i
    if best_score_key == "":
        best_score_key = "None"
    return best_score_key
