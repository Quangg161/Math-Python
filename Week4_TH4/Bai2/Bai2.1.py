#chọn ngẫu nhiên trong tập có sẵn
import random
print('Chọn ngẫu nhiên:',random.choice(['Táo', 'Lê', 'Ổi', 'Chuối'])) 

#Phát sinh số thực ngẫu nhiên trong khoảng [0,1]
print("Số thực ngẫu nhiên [0,1]:",random.random())

#Số thực ngẫu nhiên trong [a,b)
print('Số thực ngẫu nhiên trong [a,b):',random. uniform(4.9, 10.0))

#Số ngẫu nhiên trong khoảng 0 đến 5
print("số ngẫu nhiên trong khoảng 0 đến 5:",random.randrange(6))

#số ngẫu nhiên trong khoảng 50 đến 500:
print('số ngẫu nhiên trong khoảng 50 đến 500:',random.randrange(50, 500))\

#số nguyên chẵn ngẫu nhiên trong khoảng 20 đến 100:
print('số nguyên chẵn ngẫu nhiên trong khoảng 20 đến 100:',random.randrange(20, 100, 2))

#Phát sinh ngẫu nhiên 10 giá trị trong khoảng 0 đến 99: 
print('Phát sinh ngẫu nhiên 10 giá trị trong khoảng 0 đến 99:', random.sample(range(100), 10))

#Phát sinh ngẫu nhiên 15 giá trị trong khoảng 10 đến 99:
print('Phát sinh ngẫu nhiên 15 giá trị trong khoảng 10 đến 99:', random.sample(range(10, 100), 15))

#Phát sinh ngẫu nhiên 5 giá trị trong danh sách [‘a’, ‘b’, ‘c’, ‘d’, ‘e’, ‘f’, ‘g’, ‘h’, ‘i’, ‘j’]:
chars = ['a','b','c','d','e','f','g','h','i','j']
rand5_char = random.sample(chars, 5)
print('Phát sinh ngẫu nhiên 5 giá trị trong danh sách:',(rand5_char))

