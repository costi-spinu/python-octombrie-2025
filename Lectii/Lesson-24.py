# absolute path
# fileHandler = open("D:/__Curs/1-Python/cod/files/test.txt")

# relative path
# fileHandler = open("./files/test.txt")
# str1 = fileHandler.readline()
# print(str1)
# str2 = fileHandler.readline()
# print(str2)

# fileHandler = open("./files/test.txt")
# lines = fileHandler.readlines()
# print(lines)

# fileHandler = open("./files/test.txt", "w")
# n = fileHandler.write("How to Create a Text File in Python?")
# print("We wrote {} symbols. Let's check it.".format(n))
# print(len("How to Create a Text File in Python?"))


# fileHandler = open("./files/test.txt", "a")
# n = fileHandler.write("\n 3-How to Create a Text File in Python?")
# print("We wrote {} symbols. Let's check it.".format(n))
# print(len("How to Create a Text File in Python?"))


# fileHandler = open("./files/test.txt", "a")
# myStrs = {"Appended line 1\n", "Appended line 2\n"}
# fileHandler.writelines(myStrs)
# # File Handling
# fileHandler.close()


# with open("./files/test.txt", "w") as fileHandler:
#     fileHandler.write("Hello!!!")

path1 = "./files/test.txt"
path2 = "./files/result.txt"

with open(path1) as inFile, open(path2, "w") as outFile:
    # read the content from example.txt
    fileContents = inFile.read()
    # transform the content
    fileContents = fileContents.lower()
    # write the transformed content to result.txt
    outFile.write(fileContents)
