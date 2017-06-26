### TPPirateBar.py Ver 1.0 (defunct) ###

questions = { 
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    'strong': ['glug of rum', 'slug of whisky', 'splash of gin'],
    'salty': ['olive on a stick', 'salt-dusted rim', 'rasher of bacon'],
    'bitter': ['shake of bitters', 'splash of tonic', 'twist of lemon peel'],
    'sweet': ['sugar cube', 'spoonful of honey', 'spash of cola'],
    'fruity': ['slice of orange', 'dash of cassis', 'cherry on top'],
}

greeting = "Welcome to the Salty Seadog!"
print(greeting)

def drinkstr():
    print(questions['strong'.format()])        
    answer = input()
    if answer == input('y' or 'yes'): 
        print("Knew you had a strong stomach!")
    else:
        print("Sure, what else ya want?")
        
def drinksal():
    print(questions['salty'.format()]) 
    answer = input()
    if answer == input('y' or 'yes'):
        print("Mug of seawater coming up!")
    else:
        print("Sure, what else ya want?")
        
def drinkbit():
    print(questions['bitter'.format()]) 
    answer = input()
    if answer == input('y' or 'yes'):
        print("Somethin' sour ta sip!")
    else:
        print("Sure, what else ya want?")
        
def drinkswt():
    print(questions['sweet'.format()]) 
    answer = input()
    if answer == input('y' or 'yes'):
        print("Here's something sweet and not-so-neat!")
    else:
        print("Sure, what else ya want?")
        
def drinkfrt():
    print(questions['fruity'.format()]) 
    answer = input()
    if answer == input('y' or 'yes'):
        print("You sure? Alright then...")
    else:
print("Sure, what else ya want?")

### TPPirateBar.py Ver 2.0 (in need of review) ###

import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

print("Welcome to the Salty Seadog!")
print("We're runnin' a bit short on spirits since the storm sunk our last shipment, we still got what ya want in stock if yer'n interested...")

def dr_question(dr_type, dr_message):
""" Offers customer the intensity of the drink """
    cust_response = {}
    for dr_type in questions:
	answer = input()
	answer = answer.lower()
	answer = answer.upper()
	if answer == "y" or answer == "yes":
	    cust_response[dr_type] == True
	    print("Oy! Order up for a {} !".format(dr_type))
    else:
	    cust_response[dr_type] == False
	    print("Hey! They didn't want a {} !".format(dr_type))
    return cust_response

def dr_composition(dr_ingredient):
""" Arranges ingredients in drink based on previously selected drink intensity in a random manner """
    cust_affirmative = ['y', 'yes']
    cust_affirmative = cust_affirmative.lower[] #Error encountered in Cloud 9, counted as invalid syntax
    cust_affirmative = cust_affirmative.upper[]
    cust_response = []
    for dr_ingredient in ingredients:
        if dr_ingredient == cust_affirmative:
            print(random.choice(ingredients))
    return cust_response
    
if __name__ == '__main__':
    while input( "Itchin' for a drink?" ) in [cust_affirmative]:    
        dr_question(dr_type, dr_message)
        dr_composition(dr_ingredient)
