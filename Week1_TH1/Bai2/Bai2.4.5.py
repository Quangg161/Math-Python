#với giá trị của x là (2,-3) và y lần lượt là (1,10,100)


Apro = set([(2*x*y) for x  in range (-50,50)if x**2+x-6==0 for y in [1,10,100]]) # nhân lần lượt x cho lần lượt y theo phép tính (2*x*y)
print (Apro)
#Đoạn mã (Apro) tạo ra một tập hợp các giá trị số nguyên dựa trên phép tính 2 * x * y.

AB= set([(x,2*y) for x  in range (-50,50)if x**2+x-6==0 for y in [1,10,100]]) 
print (AB) 
#Đoạn mã(AB) tạo ra một tập hợp các cặp số (tuple) với dạng (x, 2 * y).
