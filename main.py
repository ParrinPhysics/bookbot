file_contents = []
words = 0

def getText():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)

def wordCount():
    count = 0
    with open("books/frankenstein.txt") as f:
        bookstring = f.read()
    words = bookstring.split()
    for i in words:
        count += 1
    print(count)

def characterCount():
    charDict = {}
    count = 0
    file_contents = getText()
    file_contents = file_contents.lower()
    for i in file_contents:
        if i in charDict:
            charDict[i] += 1
        else:
            charDict[i] = 1
    print(charDict)




def printReport():
    print("--- Begin report of books/frankenstein.txt")
    print(f"{wordCount} words found in the document")
    


main()
wordCount()
characterCount()
printReport()