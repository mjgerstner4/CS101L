punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
wordCount = dict()

while True:
    fname = input("Enter the name of the file to open: ")
    try:
        with open(fname, 'r') as f:
            lines = f.readlines()
        break
    except:
        print("Could not open file ", fname)
        print("Please Try again\n")

for line in lines:
    for x in line:
        if x in punctuation:
            line = line.replace(x, "")
    words = line.lower().split()
    for word in words:
        if len(word) > 3:
            if word not in wordCount.keys():
                wordCount[word] = 1
            else:
                wordCount[word] += 1

word_count = [(word, count) for word, count in sorted(wordCount.items(), key=lambda item: item[1], reverse=True)[:10]]

print("Most frequently used words")
print("#\t" + "Word".rjust(10) + "\t\tFreq.".rjust(2))
print("=====================================")

for i, (key, value) in enumerate(word_count):
    print(str(i) + '\t' + key.rjust(10) + '\t\t' + str(value).rjust(4))
print()

once = sum(count == 1 for count in wordCount.values())
print("There are {} words that occur only once".format(once))
print("There are {} unique words in the document".format(len(wordCount)))