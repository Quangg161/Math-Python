a= True
b= False
if (1/0 > 0) and (a==b): # lỗi xuất hiện trước khi chương trình có thể kiểm tra điều kiện tiếp theo
    print ("a=b")
else:
    print ("a khác b")