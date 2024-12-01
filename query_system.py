# 11/27/2024
# Daniel Bradford
# Front Range Community College
import json
# Load data
with open('SocialNetworkData_10K.json', 'r') as f: 
    data = json.load(f)

S = set()
# List of capital cities in the US
capitals = ('Montgomery', 'Juneau', 'Phoenix', 'Little Rock', 'Sacramento', 'Denver', 'Hartford', 'Dover', 'Honolulu', 'Tallahassee', 'Atlanta', 'Boise', 'Springfield', 'Indianapolis', 'Des Moines', 'Topeka', 'Frankfort', 'Baton Rouge', 'Augusta', 'Annapolis', 'Boston', 'Lansing', 'St. Paul', 'Jackson', 'Jefferson City', 'Helena', 'Lincoln', 'Carson City', 'Concord', 'Trenton', 'Santa Fe', 'Raleigh', 'Bismarck', 'Albany', 'Columbus', 'Oklahoma City', 'Salem', 'Harrisburg', 'Providence', 'Columbia', 'Pierre', 'Nashville', 'Austin', 'Salt Lake City', 'Montpelier', 'Richmond', 'Olympia', 'Charleston', 'Madison', 'Cheyenne')

# Takes in one character symbol and one user's data
# then evaluates the data for given symbol
def evalSymbol(symbol, data):
    result = False
    match str(symbol).lower():
        # User is 21 or older
        case 'a':
            result = data['age'] >= 21
        # User has one interest
        case 'i':
            result = len(data['interests']) == 1
        # User lives in a capital city
        case 'c':
            for city in capitals:
                if data['location'] == city:
                    result = True
                    break
        case '_':
            return result
    return result if str(symbol).islower() else not result

# Takes in a boolean statement in disjunctive normal form
# and evaluates it for each user in the dataset, then 
# assigns the set of positive matches to set S
# Returns False if invalid symbol is found, True otherwise
def evalStatement(statement):
    subset = set()
    # For each user
    for user_id, user_data in data.items():
        orEval = False # Assume all OR evals are false. If one OR is true, the entire statement is true
        for component in statement.split('+'): # Logical OR eval loop
            andEval = True # Assume all AND evals are true. If one AND is false, the entire component is false
            for s in component: # Logical AND eval loop
                if str(s).lower() in ['a', 'i', 'c']:
                    if not evalSymbol(s, user_data):
                        andEval = False
                        break
                else:
                    print(f'Invalid symbol \'{s}\'')
                    return False # Invalid symbol found
            if andEval:
                orEval = True
                break
        # We can add user to subset if the boolean statement is true
        if orEval: subset.add(user_id)

    # After the entire operation is completed with no errors, subset can be assigned to global set S
    S.clear()
    S.update(subset)
    return True

# Prints the current set and its element count
def printS():
    print('Current set is', '∅' if not (len(S)) else S)
    print('Set cardinality is', len(S))


option = ''
while option != 'q':
    # Get user input
    print('\n\
Please select an option:\n\
    q - Quit\n\
    h - Help\n\
    b - Enter boolean statement query\n')
    option = input()

    if option == 'q': continue # Quit
    if option == 'h': # Help
        print('\n\
Boolean statements are made up of the following predefined symbols:\n\
    a - User is 21 years or older\n\
    i - User has one interest\n\
    c - User lives in a capital city (US)\n\
-Boolean statements are entered in disjunctive normal form\n\
-Two symbols entered next to each other represent a logical AND\n\
-A \'+\' between symbols represents a logical OR\n\
-A symbol entered in uppercase form represents a logical NOT\n\n\
Example: \'iC+a\' would return users who either have one interest\n\
and do not live in a capital city, or users who are 21 years or older')
    elif(option == 'b'):
        print('Enter boolean statement:')
        statement = input()
        if evalStatement(statement): printS() # Display results