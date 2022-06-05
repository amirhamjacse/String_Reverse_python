user_input = input("Enter a sentence: ")
word = user_input.split()
word = list(reversed(word))
print(" ".join(word))