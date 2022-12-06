# prices = [1,2,4]
prices = [23,13,15,20,7,3,10,6,15,1,22]
minprice= prices[0]
l = 0
r = 1
profit = 0
while l != len(prices) - 1:
    if prices[r] < prices[l]:
        l = l + 1
        r = r + 1
        minprice = min(prices[l], minprice)
    else:
        profit = max((prices[r] - minprice), profit)
        l = l + 1
        r = r + 1
print(profit)



        
    

















# prices.insert(0, 0)
# if len(prices) == 2:
#         profit = max(profit, prices[1] - prices[0])
# else:

#     for i in prices:
#             if max(prices) - i > profit:
#                 profit = max(prices) - i
#                 prices.pop(0)
#             else:
#                 prices.pop(0)
#                 continue
# print(profit)     