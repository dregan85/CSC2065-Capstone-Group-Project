# 11/24/2024
# Daniel Bradford
# Front Range Community College
import json
import math

# Load data
with open('SocialNetworkData_10K.json', 'r') as f: 
    data = json.load(f)

# Create set
S = set()

# Union, intersect, or difference user_ids with specified field values
# Example: editSet('interests', '["sports", "food", "travel"]', 'u')
def editSet(field, value, op):
    subset = set()
    # Create subset of user_ids with specified field values
    for user_id, user_data in data.items():
        if(str(user_data[field]).lower() == str(value).lower()):
            subset.add(user_id)
    # Perfrom chosen operation with S and subset
    if(op == 'u'):
        S.update(subset)
    elif(op == 'i'):
        S.intersection_update(subset)
    elif(op == 'd'):
        S.difference_update(subset)

option = ''
print('Current set is Ø')
while option != 'q':
    # Get user input
    print('Please select an option:\n\
    q - Quit\n\
    u - Union set\n\
    i - Intersect set\n\
    d - Difference set\n\
    p - Calculate possible connections\n\
    c - Clear set\n')
    option = input()
    if option == 'q': continue # Quit

    if option == 'c': # Clear set
        S.clear()
        print('Current set is Ø')
    elif option in ['u', 'i', 'd']: # Perform operation on set
        # Get field to be filtered into subset
        while True:
            print('Enter field (age, location, or interests):')
            field = input()
            if field == 'age' or field == 'location' or field == 'interests':
                break
            else:
                print('Field', field, "does not exist")
        # Get value to filter by
        print('Enter value:')
        value = input()
        # Perform operation
        editSet(field, value, option)
        # Print ∅ if len(S) == 0 or S if len(S) > 0
        print('Current set is', '∅' if not (len(S)) else S)
    elif option == 'p':
        # Use combination function to find maximum possible connections in 
        # the current set (assuming connections are always mutual)
        print('The maximum possible number of mutual connections in the current set is', math.comb(len(S), 2))
    else:
        print('Invalid option')