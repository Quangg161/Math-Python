from sympy import FiniteSet
v = FiniteSet(1,2,5)
p = v**2 # kq in ra có dạng v*v = {(x,y)}
print(p)

for phantu in p:
    print (phantu) # in chi tiết từng kq có được sau phép tính