
# s = "XI"
s = list(s)
dic = {"I" : 1, "V" : 5, "X" : 10, "L": 50,"C" : 100,"D" : 500,"M" : 1000}
dicc = {"IV" : 4, "IX" : 9, "XL" : 40,"XC" : 90,"CD": 400, "CM" : 900}
output = 0
l = 0
while s:
    try:
        if str(s[l] + s[l + 1]) in dicc:
            output += dicc[str(s[l] + s[l + 1])]
            s.pop(l)
            s.pop(l)
        else:
            output += dic[s[l]] 
            s.pop(l)
    except(IndexError):
        output += dic[s[l]]
        s.pop(l)
print(output)