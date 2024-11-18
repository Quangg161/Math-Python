a = {2,4,6}
print(a)

print({n for n in range(100) if n%2==1}) # tạo tập hợp các số lẻ nhỏ hơn 100

tap_rong=set() #tạo một tập rỗng và in ra tập rỗng
print(tap_rong) 

setA = {n for n in range(100) if n%2==1} 
setB = {n for n in range(100) if n%2==1} # tạo 2 tập hợp lẻ 
print ("setA | setB :",setA | setB) # In tất cả ptu trong 2 tập hợp

print ("setA & setB :",setA & setB) # In tất cả ptu giống nhau trong tập hợp

print (setA - setB) # 2 tập hợp đều có số ptu bằng nhau nên trừ nhau bằng 0 (rỗng)

print (setA < setB) #Ktra xem tập A có phải là tập con chặt(proper subset) của B nhưng do giống nhau (False)

print (setA <= setB) #Ktra xem tập A có phải là tập con của B nhưng giống nhau (True)

print (10 in setA) #trong tập A không có số chẵn (10) kq (False)

print (11 in setA) #Ktra trong tập A có số lẻ (11) (True)

print (setA.add(0)) #Thêm số 0 vào tập A 
# nhưng câu lệnh trả về là (None) vì (add) không trả về giá trị

print (setA > setB) #sau khi thêm 0 vào tập A thì ktra xem A có phải là tập cha chặt (proper supetset) của B
# Vì tập A chứa nhiều ptu hơn tập B nên (True)