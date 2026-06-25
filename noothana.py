d1 = input("data: ").split(",")
L = list(d1)
print("list:",L)
ind = int(input("index: "))
if - len(L) <= ind < len(L):
    print("element: ",L[ind])
else:
    print("invalid")