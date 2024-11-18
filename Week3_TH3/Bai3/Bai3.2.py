def lietke_chuoinhiphan(n):
    danh_sach = []
    for i in range (0,2**n):
        gia_tri = i
        chuoi_np = bin(gia_tri).replace('0b','')
        while(len(chuoi_np) <n):
            chuoi_np = '0' + chuoi_np
        danh_sach.append(chuoi_np)
    return danh_sach
print(bin(10))
print(bin(10).replace('0b',''))

n = 9
chuoi_np = bin(10).replace('0b','')
while(len(chuoi_np) <n):
    chuoi_np = '0' + chuoi_np
print(chuoi_np)

print('liệt kê chuỗi nhị phân có 3 giá trị:',lietke_chuoinhiphan(3))

print('liệt kê chuỗi nhị phân có 4 giá trị:',lietke_chuoinhiphan(4))




