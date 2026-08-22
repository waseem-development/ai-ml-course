def is_valid_email(email):
    return "@" in email and email.endswith(".com")


def register_user(name, email):
    if not is_valid_email(email): # if not True
        return "Invalid email"
    return f"Registered {name}"
 
print(register_user("Ahmed", "ahmed@mail"))