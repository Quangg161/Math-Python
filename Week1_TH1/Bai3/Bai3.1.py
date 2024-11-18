from sympy import FiniteSet
s=FiniteSet(3,5,7) # (FiniteSet)tạo ra 1 tập hợp hữu hạn chứa các phần tử chỉ định
print (s)

from fractions import Fraction
s=FiniteSet(1,1.5,Fraction(1.5)) #Fraction(1.5) là cách biểu diễn phân số.(1.5) tương đương với (3, 2) (3/2)
print(s)

s=FiniteSet(1,1.5,Fraction(8,2)) #Fraction(8, 2) là phân số biểu diễn cho giá trị 4.
print(s)

print(len(s)) # trả về số lượng phần tử trong tập hợp s

print(8 in s) # "in" trả về giá trị True hoặc False nếu 8 hoặc 1 nằm trong tập hợp s ở trên
print(1 in s) 
