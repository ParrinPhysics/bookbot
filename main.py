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
    #print(count)
    return count

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
    #print(charDict)
    return charDict

def sort_on():
    charDictList = characterCount()
    letters = []
    for char, count in charDictList.items():
        if char.isalpha():
            letters.append({"char": char, "count": count})
        letters.sort(reverse=True, key=lambda element: element['count'])
    return letters


def printReport():
    count = wordCount()
    charcter = sort_on()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document\n")

    
    for i in charcter:
        char = i['char']
        number = i['count']
        print(f"The '{char}' character was found '{number}' times")
    print(" --- End report ---")


#main()
#wordCount()
#characterCount()
#sort_on()
printReport()
