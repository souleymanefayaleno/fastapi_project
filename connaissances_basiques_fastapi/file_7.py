"""
Dictionaries
"""

user_dictionary = {
    'username': 'codingWhithSouleymane',
    'name': 'Eric',
    'age': 32
}

print("\n")

print(user_dictionary)

print("\n")

print(user_dictionary.get("username"))
print(user_dictionary.get("age"))

print("\n")

# add value to user_dictionary
user_dictionary["married"] = "True"
print(user_dictionary)

# delete one item of user_dictionary
user_dictionary.pop("age")
print(user_dictionary)

# clear the user dictionary
user_dictionary.clear()
print(user_dictionary)

# delete the user_dictionary
del user_dictionary
