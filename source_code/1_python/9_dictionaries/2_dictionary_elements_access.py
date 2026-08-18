my_contact_dictionary = {
    "ehsan":  124,
    "musa": 4124,
    "ahmed": 893,
    "name": "Waseem",
    # "email": "someone@example.com"
}
# print(f"my_contact_dictionary['ahmed']: {my_contact_dictionary['ahmed']}")
# print(f"my_contact_dictionary.get('ahmed'): {my_contact_dictionary.get('ahmed')}\n\n\n\n")

# print(f"my_contact_dictionary['musa']: {my_contact_dictionary['musa']}")
# print(f"my_contact_dictionary.get('musa'): {my_contact_dictionary.get('musa')}\n\n\n")

# print(f"my_contact_dictionary['email']: {my_contact_dictionary['email']}")
print(f"my_contact_dictionary.get('email'): {my_contact_dictionary.get('email', 'No Email found')}")