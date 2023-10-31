print('start')

# def addNums(a, b):
#     return a + b

# addNums = lambda a, b: a + b

# sum = addNums(2, 4)
# print(sum)

# myList = [2, 3, 6, 4, 8, 9, 5, 2, 4]
# print(myList)
# print(sorted(myList))
# print(sorted(myList, reverse=True))

myFriends = ['Sonu', 'Monika', 'Pooja', "Anu"]
print(myFriends)
print(sorted(myFriends))
print(sorted(myFriends, key=lambda elem: elem))
print(filter(lambda elem: elem == 'Anu', myFriends))

print('end')

