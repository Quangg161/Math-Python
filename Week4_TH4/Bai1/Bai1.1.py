#tích tổng tích tụ
import itertools
for i in itertools.accumulate([1,2,3,4,5,6,7,8,9,10]): 
    print ("Tích tổng tích tụ: ",i)

#Hàm lặp
for i in itertools.repeat('Red', 3):
    print('Hàm lặp',i)

# Tích descartes
#PP1
for i in ((i,j) for i in [1,2] for j in [6,7,8,9]):
    print("Tích descartes: ",i)

#PP2 
for  i in itertools.product([1,2],[6,7,8,9]):
    print(i)


for i in itertools.product('AB', 'C', 'DEF'): 
    print(i)

for i in itertools.product('24', 'IT', repeat = 2):
    print (i)

#Hoán vị
from itertools import permutations
for i in permutations("ABC"):
    print('Hoán vị:',i)

#Chỉnh hợp chập k từ n
for i in permutations('ABC',2):
    print('Chỉnh hợp chập k từ n: ',i)

#Tổ hợp
for i in itertools.combinations("ABCDE",3):
    print('Tổ hợp: ',i)

import itertools
nhaccu='Đàn Trống Sáo Bo'.split()
chonmua_2mon = list(itertools.combinations(nhaccu,2))
print(chonmua_2mon)

#Tổ hợp có lặp
for i in itertools.combinations_with_replacement('ABCDE', 3):
    print ("Tổ hợp có lặp",i)

#Xoay vòng giá trị cần lấy
for i in itertools.repeat('Red', 3):
    print ('xoay vòng giá trị cần lấy: ',i)

