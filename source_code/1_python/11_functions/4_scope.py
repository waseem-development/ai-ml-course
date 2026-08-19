x = 10   # global

def show_x():
    print(x)   # can read the global x just fine
 
def change_x():
    x = 5      # this creates a NEW local x — the global x is untouched
    print(f"Local x: {x}")
 
change_x()
print(f"Global x: {x}")   # still 10