N = 3
ketqua =[]
for i1 in range (0,N):
    for i2 in range (i1,N):
        for i3 in range (i2,N):
            ketqua = ketqua + [(i1+i2+i3)]
print ((0,2,2) in ketqua)
print ((0,2,1) in ketqua)