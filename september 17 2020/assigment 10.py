#Name: Jackie Yee
#Date: 17 September 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 10

phrase = input()
phrase = (phrase.upper())
print("Enter a word", phrase)
codedWord = ""
for ch in phrase:
    offset = ord(ch) - ord('A') + 13
    wrap = offset % 26
    newChar = chr(ord('A') + wrap)
    print(wrap, chr(ord('A') + wrap))
    codedWord = codedWord + newChar

print("Your word in code is", codedWord)
