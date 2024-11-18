def fibo_mem(n, so_da_tinh = {0:0,1:1}): # khởi tạo từ điển với 2 giá trị cơ bản của dãy fibonacci
    if n not in so_da_tinh:
        #nếu giá trị Fibonacci thứ n chưa được tính, tính nó và lưu vào số đã tính
        so_da_tinh[n] = fibo_mem (n-1, so_da_tinh) + fibo_mem (n-2, so_da_tinh)
    # trả về giá trị fibonacci thứ n từ số đã tính
    return so_da_tinh[n]

print(fibo_mem(3)) # tính giá trị số fibonacci thứ 3 là 2

print(fibo_mem(4))

print(fibo_mem(5))

print(fibo_mem(200))

print(fibo_mem(500))