# put your python code here
words = input().split()
word_lower = [w.lower() for w in words]
word_count = {}
for word in word_lower:
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1
for key, value in word_count.items():
    print(key, value)