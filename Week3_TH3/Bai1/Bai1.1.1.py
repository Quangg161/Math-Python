#VD1
print("Ví dụ 1")
N = 4
for i1 in range(0,N):
    for i2 in range(0,N):
        for i3 in range (0,N):
                print(i1,i2,i3)

#VD2
print("Ví dụ 2")
for i1 in range(0,N):
    for i2 in range(0,N):
        for i3 in range (0,N):
             if i1 !=i2 and i2 !=i3 and i1 !=i3:
                  print(i1,i2,i3)

#VD3
print("Ví dụ 3")
for i1 in range(0,N):
    for i2 in range(i1+1,N):
        for i3 in range (i2+1,N):
             print(i1,i2,i3)

#VD4
print("Ví dụ 4")
for i1 in range(0,N):
    for i2 in range(i1,N):
        for i3 in range (i2,N):
             print(i1,i2,i3)

#VD5
print("Ví dụ 5")
K = 3 
ketqua = []
for i1 in range (0,K):
     for i2 in range (i1,K):
          for i3 in range (i2,K):
               ketqua = ketqua + [(i1,i2,i3)]
print (ketqua)
print (ketqua[3])