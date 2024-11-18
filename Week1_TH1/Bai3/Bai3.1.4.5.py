from sympy import FiniteSet
s = FiniteSet()
print(s)

phantu=[2,4,6,8,10] #lưu trữ trong 1 ds các phần tử
tap = FiniteSet(*phantu) #gọi ds đó thay vì nhập 
print(tap)

phantu1=[6,7,8,9,6,7] #kiểu tập hợp sẽ loại bỏ những phần tử trùng
taphop= FiniteSet(*phantu1) #kh quan tâm đến thứ tự
print(taphop)

for thanhphan in taphop:
    print (thanhphan)