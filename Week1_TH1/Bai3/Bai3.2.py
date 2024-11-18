from sympy import FiniteSet
s = FiniteSet(1)
t = FiniteSet(1,2)

#Kiểm tra tập con (subset)
print(s.is_subset(t)) #Kiểm tra xem s là tập con của t (True)

print(t.is_subset(s)) #Kiểm tra xem t là tập con của s (False)

print(t.is_subset(t)) #Kiểm tra xem t là tập con của t (True)

#Kiểm tra tập cha (superset)
print(s.is_superset(t)) #Kiểm tra xem s là tập cha của t (False)

print(t.is_superset(s)) #Kiểm tra xem t là tập cha của s (True)

