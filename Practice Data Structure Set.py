Book_Set={122,"CSS","Hussan",67.9}
print(Book_Set)
print(type(Book_Set))
print(len(Book_Set))

for x in Book_Set:
    print(x)

Book_Set.add("Awais")
print(Book_Set)

Book_Set.discard(122)
print(Book_Set)
