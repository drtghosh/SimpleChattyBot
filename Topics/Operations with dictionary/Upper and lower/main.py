# the list with words from string
# please, do not modify it
some_iterable = input().split()

# use dictionary comprehension to create a new dictionary
word_dict = {s.upper(): s.lower() for s in some_iterable}
print(word_dict)