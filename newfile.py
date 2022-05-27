# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

str1 = "stake"
str2 = "takes"

def find_anagram(str1, str2):
    # [assignment] Add your code here

     #sorted strings are checked
     if (sorted(str1)==sorted(str2)):
             return True
     else:
             return False
             
print (find_anagram("stake", "takes"))

