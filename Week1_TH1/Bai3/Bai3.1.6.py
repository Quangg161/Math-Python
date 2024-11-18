from sympy import FiniteSet
ds1 = [2,4,6] # mặc dù có các phần tử giống nhau
ds2 = [6,2,4] # nhưng thứ tự khác nhau
print(ds1==ds2) # nên kết quả trả về False

s = FiniteSet(*ds1) # Khác với ds tập hợp không quan tâm đến thứ tự  
t = FiniteSet(*ds2) 
print (s==t) #do cả 2 s và t đều chứa các pt giống nhau nên kết quả trả về True
