A = set ([x for x in range (-50,50) if x**2 + x-6==0]) #(x**2 + x-6==0) đây là ptr bậc 2 có nghiệm là (2,-3)
B = set ([2,-3])

if (A == B):
    print ("True")
else:
    print ("False")

#có thể thay thế bằng khoảng khác vì chỉ cần tìm 1 khoảng khác có giá trị là (2,-3). VD: (-5,5)
