file = input("Enter the file name: ")

line = open(file).readline()
words = line.split(" ")
res = {}

for i in range(len(words)):
   if res.__contains__(words[i]):
       res[words[i]] += 1
   else:
       res[words[i]] = 1

for x, y in res.items():
    print(x, y)
        