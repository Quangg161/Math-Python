#Phép giao
print('phép giao')
A = [0,1,2,3,4,5,6,7]
B = [2,4,6,8,10]

def intersection(A,B):
    ketqua = []
    for x in A:
        if x in B:
            ketqua = ketqua +[x]
print(intersection (A,B))

#phép tìm tập hiệu
print ('phép tìm tập hiệu')
def difference(A,B):
    ketqua =[]
    for x in A:
        if x not in B:
            ketqua = ketqua +[x]
    return ketqua
print(difference(A,B))

#Kiểm tra tập con
print('Kiểm tra tập con')
def isSubSet(A,B):
    ketqua = True
    for x in A:
        if x not in B:
            ketqua = False
    return ketqua
print(isSubSet(A,B))

B = [1,3,5,7]
print(isSubSet(A,B))
print(isSubSet(B,A))

#Sự bằng nhau của 2 tập hợp
print('Sự bằng nhau của 2 tập hợp')
def equalSets(A,B):
    return isSubSet(A,B) and isSubSet(B,A)
print(equalSets([1,3,5,7],[7,3,5,1]))