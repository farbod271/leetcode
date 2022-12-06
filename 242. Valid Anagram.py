from collections import Counter
scounter = {}
t = "anagrams"
s = "nagaram"
scounter = Counter(s)
for letter in t:
    if letter in scounter:
        scounter[letter] = scounter[letter] - 1
    else:
        print(False)
        break
# for x in scounter.values():
#     if x == 0:
if all(x == 0 for x in scounter.values()):
        print(True)
else:
        print(False)
# print(scounter)



    
