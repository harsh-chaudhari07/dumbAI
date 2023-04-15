import json
import random

neurodata = "mdata.txt"

def match(a, b):
    # returns the %age of words of b in a
    #It uses 9:1 for words match and consecutive order
    a_list = list(a)
    b_list = list(b)
    useless = [',', '.', '!', '?', '*', '(', ')', '"', '\'', '-']
    for foo in a:
        if foo in useless:
            a_list.remove(foo)
            a = ''.join(a_list)
    for foo in b:
        if foo in useless:
            b_list.remove(foo)
            b = ''.join(b_list)

    matches = []
    a_words = a.split()
    b_words = b.split()
    for word in a_words:
        if word in b_words:
            matches.append(1)
        else:
            matches.append(0)

    count = 0
    max_count = 0

    # checks the no. of consecutive 1s
    for num in matches:
        # if the number is 1, increment the counter
        if num == 1:
            count += 1
        # else, reset the counter and update the maximum if needed
        else:
            max_count = max(max_count, count)
            count = 0

    # update the maximum one last time in case the list ends with 1
    max_count = max(max_count, count)

    try:
        return (sum(matches)*90 + max_count*10) / len(a_words)
    except ZeroDivisionError:
        return 0

def lbm(keys, x):
    # list best match
    # returns best match of x from keys or False if no matches
    maval = []
    bm = []    # Best matches

    for key in keys:
        maval.append(match(key, x))

    for i in range(len(maval)):
        if maval[i] == max(maval):
            bm.append(keys[i])

    if max(maval) != 0:
        return random.choice(bm)
    else:
        return False

neurons = json.load(open(neurodata, "r"))

#main program interface
while True:
    all_keys = list(neurons.keys())
    query = input('\n---')

    if lbm(all_keys, query):
        print('--->' + neurons[lbm(all_keys, query)])
    else:
        print("Sorry, I don't have answer for this🥲 Please provide me answer in feedback")

    # feedback
    feedback = input("Are you satisfied with answer?(y or n) ")
    if feedback == 'n':
        neurons.update({query: input("Please write a satisfactory answer then: ")})
        # !!! Check this is should insert new items from start
    json.dump(neurons, open(neurodata, "w"))
