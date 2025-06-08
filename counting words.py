text = input ("enter your text :")
words = text.split()
dic = {}
for word in words :
    if word in dic :
        dic[word] += 1
    else :
        dic[word] = 1
most = None
max_word = 0
for word in dic :
    if dic[word] > max_word:
        max_word = dic[word]
        most = word
print ("the most word freq: ",most)
print ("number of times :", max_word, "times")