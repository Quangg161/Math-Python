def implies(a,b):
    if a:
        return b
    else:
        return True
print (implies(10,11))
print (implies(1,11))
print (implies(0,11))

x,y = 2,3
print (implies(x >= 0 and y >= 0, x*y >=0 ))

z,t = -2,3
print (implies(z >= 0 and t >= 0, z*t >=0))