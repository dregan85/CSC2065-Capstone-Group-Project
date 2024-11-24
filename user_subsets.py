# 11/24/2024
# Daniel Bradford
# Front Range Community College
import json

# Load data
with open('SocialNetworkData_10K.json', 'r') as f: 
    data = json.load(f)

# Create set
S = set()

# Union, intersect, or difference user_ids with specified field values
# Example: editSet('interests', '["sports", "food", "travel"]', 'u')
def editSet(field, value, op):
    subset = set()
    for user_id, user_data in data.items():
        if(str(user_data[field]).lower() == str(value).lower()):
            subset.add(user_id)
    if(op == 'u'):
        S.update(subset)
    elif(op == 'i'):
        S.intersection_update(subset)
    elif(op == 'd'):
        S.difference_update(subset)

option = ''
print('Current set is Ø')
while option != 'q':
    print('Please select an option:\n\
    q - Quit\n\
    u - Union set\n\
    i - Intersect set\n\
    d - Difference set\n\
    c - Clear set\n')
    option = input()
    if option == 'q': continue
    if option == 'c':
        S.clear()
        print('Current set is Ø')
    else:
        print('Enter field (age, location, or interests):')
        field = input()
        print('Enter value:')
        value = input()
        editSet(field, value, option)
        print('Current set is', S)