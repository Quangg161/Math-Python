James = [True, True, True, True, False, False, False, True]
Jonathan =[True, True, True, True, False, False, False, True]
ngay_trong_tuan = ["Thu 2", "Thu 3", "Thu 4", "Thu 5", "Thu 6", "Thu 7", "Chu nhat","Thu 2"]
#code
for i in range (0,7):
    if ((James[i] == True and James[i+1] == False)
        or((James[i] == False and James[i+1] == True))):
            if ((Jonathan[i] == True and Jonathan[i+1] == False)
                or((Jonathan[i] == False and Jonathan[i+1] == True))):
                    print(ngay_trong_tuan[i])

#code rút gọn
for i in range(0, 7):
    if ((James[i] != James[i + 1]) and (Jonathan[i] != Jonathan[i + 1])):
        print(ngay_trong_tuan[i])
