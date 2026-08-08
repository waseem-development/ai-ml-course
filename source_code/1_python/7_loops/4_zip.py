names = ["Waseem", "Ahmed", "Youssef", "Abdul Razzaq", "Malak", "Rehab", "Mahnoor", "Fatima", "Yara"]
scores = [99, 100, 101, 102, 103, 104, 105, 106]

for st, score in zip(names, scores):
    print(st, "Scored", score, "in exam")