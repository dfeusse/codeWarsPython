'''
We give you an Array of friend's list.

Write a method called greetingForAllFriends, with this signature:

This method takes an array of friends name and return a greeting messages Array.

Message sample: for the friend "Bilal" we get "Hello, Bilal!"

Rules:

If the argument is null, the method should return null
If the argument is an empty array, the method should return null
If the argument is a valide array of strings, the method should return a hello message for every array entry
'''
import sys

def greeting_for_all_friends(friends):
    try:
        if len(friends) == 0:
            return None
        else:
            return [ 'Hello, ' + i + '!' for i in friends ]
    except:
        return None

print greeting_for_all_friends()
print greeting_for_all_friends(None)
print greeting_for_all_friends(['dan', 'alexa'])

'''
def greeting_for_all_friends(friends):
    return ["Hello, %s!"%friend for friend in friends] if friends else None

def greeting_for_all_friends(friends):
    if friends != None and friends:
        greeting = ["Hello, {}!".format(friend) for friend in friends]
        return greeting
 '''