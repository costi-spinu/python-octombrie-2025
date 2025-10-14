# category = ["Drama", "Comedy", "Fantasy"]
# print(category)
# print(type(category))

# courses = list(("Math", "Algorithms", "Databases"))
# print(courses)
# print(type(courses))


# studentScores = []
# students = list()
# print(studentScores) #[]
# print(students) #[]


# myCourses = ["Algorithms", 2345, 7009, "Networks", "Databases"]
# print(myCourses) #['Algorithms', 2345, 7009, 'Networks', 'Databases']


# nestedList = [1, 2.5, [45, "Example"]]
# print(nestedList) #[1, 2.5, [45, 'Example']]


# mySymbols = list("spinucostelus")
# print(mySymbols)  # ['a', 'b', 'c', 'd', 'e', 'f']


# list1 = [i * i for i in range(6 + 1)]
# print(list1)  # [0, 1, 4, 9, 16, 25]


# list1 = [i +1 for i in range(6)]
# print(list1)  # [0, 1, 4, 9, 16, 25]


# list3 = [i * 5 for i in "abcdtf"]
# print(list3)  # ['aaaaa', 'bbbbb', 'ccccc', 'ddddd', 'ttttt', 'fffff']


# list4 = [i*i for i in range(1,11) if i%2==0]
# print(list4) #[4, 16, 36, 64, 100]


# customers = ["Bob", "Anna", "Joe", "Bob", "Nick"]
# list5 = [i for i in customers if i != "Bob" and i != "Joe"]
# print(list5)  # ['Anna', 'Nick']


# list6 = [x*y for x in range(1, 4) for y in range(1, 4)]
# print(list6) #[1, 2, 3, 2, 4, 6, 3, 6, 9]

# list7 = [[x * y for x in range(1, 4)] for y in range(1, 4)]
# print(list7)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


# myList = ["user", 12, 200.34, False, True]
# print(myList[2:4])
# print(myList[1:-1])


# myCourses = ["Algorithms", 2345, 7009, "Networks", "Databases"]
# # print(myCourses[1:3]) #[2345, 7009]
# # print(myCourses[-4:-2]) #[2345, 7009]
# # print(myCourses[1:-1]) #[2345, 7009, 'Networks']
# # print(myCourses[:-1]) #['Algorithms', 2345, 7009, 'Networks']
# # print(myCourses[3:]) #['Networks', 'Databases']
# print(myCourses[::2])  # ['Algorithms', 7009, 'Databases']
# print(myCourses[1::2])
# print(myCourses[2:4:2])
# # print(myCourses[::-1]) #['Databases', 'Networks', 7009, 2345, 'Algorithms']
# # print(myCourses[-4::-1]) #[2345, 'Algorithms']

# [1-de unde incepe: 2-pana unde e : 3 - pasul]

# category = ["Drama", "Comedy", "Fantasy"]
# print(category)  # ['Drama', 'Comedy', 'Fantasy']
# category[-1] = "Action"
# print(category)  # ['Drama', 'Comedy', 'Action']


# myCourses = ["Algorithms", 2345, 7009, "Networks", "Databases"]
# print(max(myCourses))


# userLogs = ["admin","student","teacher","hr","user"]
# print(len(userLogs)) #5
# print(sorted(userLogs)) #['admin', 'hr', 'student', 'teacher', 'user']
# prices = [100, 250.45, 1200, 20.78]
# print(sum(prices)) #1571.23
# print(max(prices)) #1200
# print(min(prices)) #20.78
# print(sorted(prices)) #[20.78, 100, 250.45, 1200]

# category1 = ["Drama", "Comedy", "Action"]
# category2 = ["Action", "Fantasy"]
# print(category1 + category2)  # ['Drama', 'Comedy', 'Action', 'Fantasy']
# print(category1 * 2)  # ['Drama', 'Comedy', 'Drama', 'Comedy']
