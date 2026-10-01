word = input("enter word: ")
keyword = input("enter word")
if keyword in word:
    print("keyword found`")
    print(f' the position of the keyword is {word.index(keyword)}')
else:
    print("keyword not found")
