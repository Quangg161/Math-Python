from sympy import FiniteSet
s = FiniteSet(2,4,6)
t = FiniteSet(3,5,7)
kq = s.union(t) #hợp 2 tập hợp 
print(kq) # chứa tất cả các phần tử thuộc ít nhất 1 trong 2 tập hợp

u = FiniteSet(10,20,50)
v = FiniteSet(1,2,5)
print (u + v) #Chứa tất cả phần tử thuộc ít nhất 1 trong 2 tập hợp

