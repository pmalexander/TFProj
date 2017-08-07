'''Use as reference only, completed project in ThinkfulProjectsv2 repository'''

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

def dr_question(dr_type):
# Offers customer the intensity of the drink 
    cust_response = {}
    for dr_type in questions:
        print(questions[dr_type])
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

def dr_composition(dr_ingredients):
# Arranges ingredients in drink based on previously selected drink intensity in a random manner
    cust_affirmative = ['y', 'Y', 'yes', 'Yes', 'YES']    
    dr_complete = []
    for dr_ingredients in ingredients:
        if dr_ingredients == cust_affirmative:
            print(random.choice(ingredients))
    return dr_complete
    
if __name__ == '__main__':
    dr_awaiting = input( "Itchin' fer a drink?" ) #Identifies cust_affirmative as undefined variable
    dr_pending = [ 'y' , 'Y', 'yes', 'Yes', 'YES' ] #Identifies dr_type and dr_message, which I later removed, as undefined variable
    while dr_awaiting in dr_pending: #Identifies dr_ingredient as undefined variable
        dr_question(dr_type)
        dr_composition(dr_ingredients)
