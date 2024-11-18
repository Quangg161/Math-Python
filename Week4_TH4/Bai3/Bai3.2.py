from __future__ import division
import numpy as np
import random,pdb
import operator
def roulette_selection(weights):
    sorted_indexed_weights = sorted(enumerate(weights), key = operator.itemgetter(1)); #enumerate(weights): Trả về danh sách các cặp giá trị dạng (chỉ số, giá trị) từ danh sách
    #sorted(..., key=operator.itemgetter(1)): Sắp xếp danh sách theo trọng số, với operator.itemgetter(1) lấy phần tử thứ hai (trọng số) để làm khóa sắp xếp.
    indices, sorted_weights = zip(*sorted_indexed_weights);  #zip(*sorted_indexed_weights): Tách danh sách đã sắp xếp thành hai phần: chỉ số và trọng số.

    tot_sum = sum(sorted_weights)#Tính tổng các trọng số, dùng để chuẩn hóa thành xác suất.
    prob = [x/tot_sum for x in sorted_weights]
    cum_prob = np.cumsum(prob) #Tính xác suất tích lũy (cumulative probability) của các trọng số.
    random_num = random.random()

    for index_value, cum_prob_value in zip(indices,cum_prob):
        if random_num < cum_prob_value:
            return index_value

xanhdo =[87, 3, 20]
for i in range(20):
    print (roulette_selection(xanhdo)) 

xanhdo =[27, 3, 30]
for i in range(20):
    print (roulette_selection(xanhdo)) 
