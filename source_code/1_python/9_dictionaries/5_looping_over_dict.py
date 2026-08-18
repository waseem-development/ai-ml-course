contact = {
    "name": "Ahmed",
    "age": 25,
    "city": "Karachi"
}
 
# for key, value in contact.items():
#     print(key, "->", value)
 

# for key in contact.keys():
#     print(key)

# for val in contact.values():
#     print(val)


text = "the cat sat on the mat the cat ran ran ran ran ran I ran very fast you can't catch me"
words = text.split()

counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
 
print(counts)   # {'the': 3, 'cat': 2, 'sat': 1, ...}