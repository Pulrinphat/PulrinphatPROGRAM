fruites_with_duplicates = ['apple', 'banana', 'apple', 'cherry', 'apple',"kiwi"]
while "apple" in fruites_with_duplicates:
    fruites_with_duplicates.remove("apple")
    print(f"fruites after remove :{fruites_with_duplicates}")