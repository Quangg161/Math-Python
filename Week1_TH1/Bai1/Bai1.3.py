a = True
b = False
1/0 # lỗi xảy ra ngay từ đoạn này nên sẽ không thực hiện câu lệnh if tiếp thep

if (a==b) and (1/0>0): 
    print ("a=b")
else:
    print("a khac b")
