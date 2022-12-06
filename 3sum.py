# code woeks but i think its time complexity is above n**2 !
#coming up with the logic only took few minutes but as im still learning the details of python implementing it took half an hour
# all the edge cases took a few hours and it was prett frustrating but i completed it nevertheless

s = [-1,0,1,0]
sol = []
for i in s:
    if i >= 0:
        border = i
        break
s.sort()
l = 0
while s[l] < 0 and s[l] < s.index(border):
    r = len(s) - 1
    while s[r] >= 0 and r >= 0 and l != r:
        target = -(s[l]) - s[r]
        # print(l, target, r)
        if target < s[l] or target > s[r]:
            pass
        else:
            if target >= 0 and l != s.index(target):
                for i in s[s.index(border):r]:
                    if i == target:
                        res = [s[l], s[r], target]
                        sol.append(res)
                        res = []
            else:
                for i in s[l + 1:s.index(border)]:
                    if i == target:
                        res = [s[l], s[r], target]
                        sol.append(res)
                        res = []
        r -= 1
    l += 1
if s.count(0) >= 3:
    zeros = [0,0,0]
    sol.append(zeros)
finalres = []
for i in sol:
    if i in finalres:
        pass
    else:
        finalres.append(i)
print(finalres)

            
            
                
                

            


        
