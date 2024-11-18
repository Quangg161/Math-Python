import random
S = random.sample(range(1, 100), 10) # lấy mẫu 10 số tự nhiên trong [1, 99]
print ('Lấy mẫu 10 số tự nhiên từ 1 đến 99:',S)

tS = []
for i in range (len(S)):
    tS.append(0)
    for j in range(i, len(S)):
        if S[i] < S[j]:
            tS[i] = tS[i]+1
print(tS)