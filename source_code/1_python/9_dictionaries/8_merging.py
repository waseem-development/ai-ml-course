defaults = {
    "theme": "light", 
    "font_size": 12
}

# updated_font = {
#     "font_size": 20
# }

# defaults.update(updated_font)
# print(defaults)

merged = defaults | {"theme": "dark"}
print(merged)