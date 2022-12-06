columnNumber = 86768668
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
dictionary = dict(zip(number, letters))
output = []

while columnNumber>26:
    b = columnNumber % 26
    if b == 0:
        b=26
    output.append(dictionary[b])
    columnNumber = (columnNumber - b)/26
output.append(dictionary[columnNumber])
output = ''.join(output[::-1])
print(output)