word1 = input("word1: ")
word2 = input("word2: ")
i = j = 0
merged = ""
while i < len(word1) or j < len(word2):
    if i < len(word1):
        merged = merged + word1[i]#adb
        i += 1
    if j < len(word2):
        merged = merged + word2[j]#ad
        j += 1

print (merged)
        

