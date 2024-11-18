from sympy import FiniteSet
s = FiniteSet(0,1,2,3,4,5,6,7,8,9) #các số có thể có trong biến số
a = FiniteSet(2,3,5,7) # các số nguyên tố
b = FiniteSet(1,3,5,7,9) # các số lẻ
e = a.intersect(b) # phép giao chứa các phần tử chung giữa a và b
print (len(e)) # tập e có 3 ptu
print (len(s)) #tập s có 10 ptu 
print(len(e)/len(s)) # tỉ lệ phép tính 3/10 = 0.3

# đây là xác xuất để chọn ra 1 số nguyên tố lẻ từ 0 đến 9 (33%)