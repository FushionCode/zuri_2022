# Check if a word is a Palindrome
# Example:
# find_palindrome("hello") --> False
# find_palindrome("racecar") --> True

def find_palindrome(word):
    # [assignment] Add your code here
    wordReverse = ""
    if(len(word) == 0 or len(word) == 1):
        return True
    else:
        i = len(word) - 1
        while i >= 0:
            wordReverse = wordReverse + word[i]
            i = i-1
        
    if(word == wordReverse):
        return True
    else: 
        return False

    

print("The palindrome check result is: ")
print(find_palindrome(""))



#This method was not in the downloaded file in my assignment,
# so i added it since this was supposed to be the original assignment
def find_anagram(str1,  str2):
    # [assignment] Add your code here

    if(sorted(str1) == sorted(str2)):
        return True
    else:
        return False


s1 = "center"
s2 = "recent"

print(find_anagram(s1, s2))