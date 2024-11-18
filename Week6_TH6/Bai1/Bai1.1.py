#Liệt kê các trường hợp giá trị cả hàm bool trong bảng
def bool_xy(x, y):
    kq = 0
    if (x==1) and (y==1):
        kq = 0
    if (x==1) and (y==0):
        kq = 1
    if (x==0) and (y==1):
        kq = 0
    if (x==0) and (y==0):
        kq = 0
    return kq 

for x in [1,0]:
    for y in [1,0]:
        print (bool_xy(x,y)) 

#cải tiến hàm theo phân tích
def bool_xy1(x,y):
    kq = 0
    if (x == 1) and (y==0):
        kq = 1
    return kq

for x in [1,0]:
    for y in [1,0]:
        print (bool_xy(x,y))
