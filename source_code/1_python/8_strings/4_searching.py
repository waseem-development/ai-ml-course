sentence = "the quick brown fox"
 
# print(sentence.find("brown"))    # 10
# print(sentence.find("zebra"))    # -1 : I could not find it OR it does not exist
# print(sentence.index("brown")) # 10
# print(sentence.index("zebra"))
# ValueError: substring not found

# filename = "report_final.csv"
 
# print(filename.endswith(".csv"))     # True
# print(filename.startswith("report")) # True
# print(filename.endswith(".xlsx"))    # False


sentence = "the quick brown fox jumps over the lazy dog"
 
print(sentence.count("the"))        # 2
print("fox" in sentence)             # True
print("cat" not in sentence)         # True