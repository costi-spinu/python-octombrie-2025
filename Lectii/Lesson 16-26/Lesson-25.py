###################################replace words in text


# def replaceTextInFile(fileName, originText, newText):
#     with open(fileName) as fileHandler:
#         data = fileHandler.read()
#         data = data.replace(originText, newText)

#     with open(fileName, "w") as fileHandler:
#         fileHandler.write(data)


# def readFromFile(fileName):
#     with open(fileName) as fileHandler:
#         data = fileHandler.read()
#         print(data)


# myFile = "./colegi/TEXT/text.txt"

# print("Original file content:")
# readFromFile(myFile)

# replaceTextInFile(myFile, "asd", "Costi")

# print("New file content:")
# readFromFile(myFile)


################ counting the number of words in the content of a text
# ############## file that are not numbers


# def readFromFile(fileName):
#     with open(fileName) as fileHandler:
#         data = fileHandler.read()
#         print(data)


# def wordCounter(fileName):
#     nWords = 0
#     with open(fileName) as fileHandler:
#         data = fileHandler.read()
#         words = data.split()
#         for word in words:
#             if not word.isnumeric():
#                 nWords += 1
#     return nWords


# myFile = "./colegi/TEXT/text.txt"

# print("File content:")
# readFromFile(myFile)

# print("Number of words: {}".format(wordCounter(myFile)))


################################print the words of the file content in reverse order


def removePunctuation(myStr, marks):
    resultStr = ""
    for symbol in myStr:
        if symbol not in marks:
            resultStr += symbol
    return resultStr


def reverseFileWords(fileName):
    with open(fileName) as fileHandler:
        data = fileHandler.read()
        data = removePunctuation(data, punctuationSymbols)
        words = data.split()
        reversedWords = reversed(words)

        for word in reversedWords:
            print(word)


#################deleting a given string from a file
punctuationSymbols = """!()-;?@#$%:'"\,./*_"""
myFile = "./colegi/TEXT/text.txt"

reverseFileWords(myFile)


def removeLine(fileIn, fileOut, lineNumber):
    with open(fileIn) as fr:
        lines = fr.readlines()

        counter = 1  # position pointer

        with open(fileOut, "w") as fw:
            for line in lines:
                if counter != lineNumber:
                    fw.write(line)
                counter += 1


myFile = "./colegi/TEXT/text.txt"
resultFile = "./colegi/TEXT/result.txt"

removeLine(myFile, resultFile, 2)
