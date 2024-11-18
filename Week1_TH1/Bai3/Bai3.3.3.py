from sympy import FiniteSet
K = FiniteSet(35,18,27,29,24)
for k in K: #duyệt qua từng ptu trong K
    T = k/10.0 #chia từng ptu k cho 10.0
               # VD: 35/10.0 = 3.5
    print (T,k) #in ra kết quả chia và giá trị của ptu k trong K

