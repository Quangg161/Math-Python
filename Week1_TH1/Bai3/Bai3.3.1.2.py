from sympy import FiniteSet
s = FiniteSet(1,2,10)
t = FiniteSet(1,3,10)
giao = s.intersect(t) #Ktra ptu giao nhau của s và t
print(giao) 

u = FiniteSet(10,20,50)
hop=s.union(t).union(u) # Hợp của 3 tập hợp s,t,u
print(hop) #tập hợp tất cả các ptu co it nhat trong 1 tap hop

giao1 = s.intersect(t).intersect(u) # giao của 3 tập hợp s,t,u
print(giao1)

v = FiniteSet(1,2,5)
rong = u.intersect(v) #tìm giao của u và v
print(rong) #do kh có ptu chung nên kq là rỗng

rong1 = v.intersect(u) #tìm giao của v và u
print(rong1) #do kh có ptu chung nên kq là rỗng
