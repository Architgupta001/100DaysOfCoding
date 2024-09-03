word = "My Love Mangoes"
word2 = 'IMAAMI'

# take input from user as a string and reverse it.
print(word[::-1])

# check if string contains only digits.
print(word.isdigit())

# check if string is palindrome.
reversed_word = word2[::-1]
if(reversed_word == word2):
    print('Is Palindrome.')
else:
    print('Not a Palindrome.')
    
# Number of vowels in a string
noOfVowels = 0
for i in word:
    if i in ['a','e','i','o','u','A','E','I','O','U']:
        noOfVowels +=1
print(noOfVowels)

# check if every word in string starts with capital letter
print(word.istitle())
print(word2.istitle())