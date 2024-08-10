word = str(input("Give me a word, and i'll tell you if it's a palindrome (Reads the same forwards and backwards). "))
reverse = word[::-1]
if word == reverse:
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a Palindrome.")