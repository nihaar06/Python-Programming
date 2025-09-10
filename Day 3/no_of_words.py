def count_words(s):
    words=s.split()
    return len(words)
s=input("Enter the string: ")
print("The number of words in the string is:",count_words(s))