Book_List=[445,"Think and Grow Rich","Husnain",50.5]
print(Book_List)
print(type(Book_List))
print(len(Book_List))

for x in Book_List:
    print(x)
print(Book_List[2])

print(type(Book_List[2]))
print(Book_List[3])
print(type(Book_List[3]))

Book_List.append("ABC")
print(Book_List)

Book_List.insert(1,2020)
print(Book_List)

Book_List.remove(50.5)
print(Book_List)

Book_List.pop(4)
print(Book_List)


