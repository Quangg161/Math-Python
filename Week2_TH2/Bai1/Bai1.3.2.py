# VD2
def thue(phan_tram):return lambda x:x*phan_tram
HCM = thue(0.012) #Khai báo thuế ở Hồ Chí Minh
HN = thue(0.01) #khai báo thuế ở Hà Nội

print(HCM(1000000)) #gọi hàm tính thuế 1 triệu ở HCM
print(HN(100000000)) # gọi hàm tính thuế 1 tỉ ở HN

#VD3
day_so = range(2, 50)  # tạo dãy số từ 2 đến 49
result = list(filter(lambda x: x % 3 == 0, day_so)) # filter lọc các số chia hết cho 3
#list() chuyển kq của filter sang danh sách để in
print(result)

#VD4
day_so4 = range(1, 11)  # Tạo dãy số từ 1 đến 10
kq4 = list(map(lambda x: x * x, day_so4))  # Bình phương từng phần tử
print(kq4)

#VD5
from functools import reduce
day_so5 = range(1,11)
kq5 = reduce(lambda x, y : x+y, day_so5) #reduce áp dụng hàm lambda cho từng cặp giá trị trong ds_5
#biểu thức lambda cộng 2 giá trị x và y
print(kq5)
                 
#VD6
ds = [20,25,50,103,13,19]
f = lambda a,b : a if (a>b) else b
print(reduce(f,ds))

#VD7
imatrix = lambda n :[[1 if j==i else 0 for j in range(n)] for i in range (n)]
print (imatrix(3))

#VD8
#in ra ma trận hệ số n=3 thì ma trận 3x3 có đg chéo là căn 2
import math
g = lambda n:[[1 if (j + 1 == i or j == i + 1) else math.sqrt(2) for j in range (n)] for i in range(n)]
print (g(3))

#VD9
g = lambda n:[[1 if (j + 1 == i or j == i + 1) else 0 if (i==n/2) else math.sqrt(2) for j in range (n)] for i in range(n)]
print (g(3))
