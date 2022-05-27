# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

import os


def read_file_content(filename):
    # [assignment] Add your code here 
    with open(os.path.join(os.sys.path[0], filename), "r") as f :
        return f.read()

print(read_file_content("./story.txt"))


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    wordsCounter = {}
    textContent = text.split()
    for txt in textContent:
        if txt in wordsCounter.keys():
            wordsCounter[txt] += 1
        else:
            wordsCounter[txt] = 1
    # return {"as": 10, "would": 20}
    return wordsCounter


print(count_words())