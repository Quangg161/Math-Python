from sympy import FiniteSet
s = FiniteSet(0,1,2,3,4,5,6,7,8,9) #các số có thể có trong biến số
a = FiniteSet(2,3,5,7) # các số nguyên tố
b = FiniteSet(1,3,5,7,9) # các số lẻ
e = a.intersect(b) 
print(len(e)/len(s))