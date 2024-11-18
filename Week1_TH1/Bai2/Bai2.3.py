#đoạn mã dùng để kiểm tra trạng thái nguyên tố của các số trong dãy
def isPrime(N):
    for i in [x+1 for x in range (N)]:
        if N % i==0 and (i!=1 and i!=N):
            return False
    return True
S_prime = [isPrime(k) for k in range (1,40)] # nếu N có số ước ngoài 1 và N (tức kh phải số nguyên tố) thì trả về False nếu không trả về True
print (S_prime)

index = int(input("Nhập vị trí muốn kiểm tra: ")) - 1  # Trừ 1 để điều chỉnh index cho đúng
if 0 <= index < len(S_prime): # đảm bảo vị trí kiểm tra nằm trong khoảng 0 đến 38 vì ds bắt đầu từ số 0
    print(f"Kết quả tại vị trí {index + 1}: {S_prime[index]}") # tạo ra 1 chuỗi thông báo cho biết giá trị tại vị trí trong ds isPrime (N)
else:
    print("Vị trí không hợp lệ.")