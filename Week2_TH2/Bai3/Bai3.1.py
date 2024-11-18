from datetime import datetime # lấy ngày giờ hiện hành
from datetime import timedelta # thư viện tính toán thời gian
def millis (start_time): # tham số lưu trữ thời gian trước đó
    dt = datetime.now() - start_time # lấy hiệu 2 thời gian: thời gian hiện hành và trước đó
    ms = (dt.days*24*60*60 + dt.seconds)*1000 + dt.microseconds / 100.0 # chuyển đổi khoảng thời gian chêch lệch thành miligiay
    return ms # trả về giá trị mili giây

def milisec_passed(start_time):
    thoigian_troiqua = millis(start_time) # thời gian trôi qua
    s = "Thoi gian da troi qua: " + str(int(thoigian_troiqua)) + "mili giay."
    return s

def tong(n):
    bat_dau = datetime.now() # ghi nhận thời điểm bắt đầu
    ketqua = 0
    for i in range (n+1):
        ketqua = ketqua + i
    thoi_gian = str (milisec_passed(bat_dau)) # tính toán thời gian trôi qua
    print(thoi_gian)
    return ketqua
print(tong(100000000)) # tính toán từ tổng 1 đến 1 trăm triệu

def tong1(n):
    bat_dau = datetime.now() #ghi nhận thời điểm bắt đầu
    ket_qua = n*(n+1)/2
    thoi_gian = str(milisec_passed(bat_dau))
    print(thoi_gian)
    return(ket_qua)
print (tong1(100000000))
