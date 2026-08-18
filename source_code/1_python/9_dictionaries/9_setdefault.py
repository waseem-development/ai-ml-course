counts = {}
counts.setdefault("apple", 0)
print(counts) 
counts["apple"] += 1
print(counts)   # {'apple': 1}
 
# calling it again on an existing key leaves it untouched
counts.setdefault("banana", 123)
print(counts)   # still {'apple': 1}s