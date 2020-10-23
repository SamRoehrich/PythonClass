def parseFile(f):
    file = open(f)
    line = file.readline()
    words = line.split(' ')
    sortedWords = words.sort()
    for i in range(len(words)):
        print(words[i])

parseFile('example.txt')