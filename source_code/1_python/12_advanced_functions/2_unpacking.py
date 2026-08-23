def greet(name, age1):
    print(f"{name} is {age1} years old")
 
values_list = ["Ahmed", 25]
# greet(*values_list)          # Ahmed is 25

values_tuple = ("Waseem", 22)
# greet(*values_tuple)

info = {"name": "Sara", "age": 22}
# greet(**info)           # Sara is 22


def log(level, *parts, **meta):
    message = " ".join(str(p) for p in parts)
    tags = ", ".join(f"{k}={v}" for k, v in meta.items())
    print(f"[{level}] {message}  ({tags})")
 
# log("INFO", "User", "logged in", user_id=42, ip="10.0.0.1")
# [INFO] User logged in  (user_id=42, ip=10.0.0.1)


x = lambda n: n * 2

print(x)