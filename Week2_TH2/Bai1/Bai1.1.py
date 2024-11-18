def luythua(x,n):
    kq = 1
    for i in range (n):
        kq = kq*x
        return kq
print(luythua(2,1)) # lũy thừa của 2^1 = 2

print(luythua(2,0)) # lũy thừa của x^n là 2^0 = 0