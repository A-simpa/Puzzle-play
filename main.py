# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from tabnanny import check


def find_anagram(word, anagram):
    # [assignment] Add your code here
    wordList = [i for i in word.replace(" ", "")]
    anagramList = [i for i in anagram.replace(" ", "")]
    wordList.sort(), anagramList.sort()
    if (wordList == anagramList):
        return True
    return False

# My check
print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))
print(find_anagram("anagram", "nag a ram"))
print(find_anagram("ref", "sef"))

