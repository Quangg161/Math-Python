from sympy import FiniteSet
s = FiniteSet(1,2,3) # ở đây có 3 ptử nên n = 3
ps = s.powerset() # tính tập hợp con theo ct 2^n 

print(len(ps)) # trả về số lượng ptử trong ps

print(ps) # Hàm in ra tất cả tập hợp con trong ps

t = FiniteSet(3,2,1)
#tập hợp con thực sự phải có ít nhất 1 phần tử không có trong siêu tập hợp
print(s.is_proper_subset(t)) #KT xem s có phải là tập con thực sự của t (False)

#Ktra xem t có phải là siêu tập hợp thực sự của s
print(t.is_proper_superset(s)) #vì t kh có thêm ptử nào so với s (False)

T= FiniteSet(3,2,1,4)
#Ktra s có phải là tập con thực sự của T
print(s.is_proper_subset(T)) # Vì T có thêm (4) mà s kh có nên (True)

#Ktra T có phải siêu tập hợp thực sự của s
print(T.is_proper_superset(s)) #Vì T chứa tất cả các ptử s và có thêm (4) (True)
