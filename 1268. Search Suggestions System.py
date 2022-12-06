sol = []
res = []
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchword = "mouse"
products.sort()
for i in range(len(searchword)):
    searched = searchword[0:i+1]
    for item in products:
        if item[0:i+1] == searched:
          res.append(item)
    products = res 
    if len(res) >= 3:
      res = res[0:3]
    sol.append(res)
    res = []
print(sol)
     