#Write a python program that counts and returns the number of words in a given text

saySomething = input("what do you have to say: ")
# wordList = saySomething.split()
# wordCount = len(wordList)
# print(wordList)
# print("Number of words spokenclear :" + str(wordCount))

def countWordsInPhrase(saySomething : str):
    return(len(saySomething.split()))

print(countWordsInPhrase(saySomething))