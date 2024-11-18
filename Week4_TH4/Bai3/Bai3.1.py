import matplotlib.pyplot as plt
import numpy.random as rnd
from matplotlib.patches import Ellipse

NUM = 250
ells = [Ellipse(xy=rnd.rand(2)*10, width=rnd.rand(), #xy=rnd.rand(2)*10: Tọa độ trung tâm của ellipse là một cặp giá trị ngẫu nhiên trong khoảng từ 0 đến 10.
                height=rnd.rand(), angle=rnd.rand()*360) #width=rnd.rand(): Chiều rộng của ellipse là một giá trị ngẫu nhiên từ 0 đến 1.
                                                         #height=rnd.rand(): Chiều cao của ellipse cũng là một giá trị ngẫu nhiên từ 0 đến 1.
                                                         #angle=rnd.rand()*360: Góc xoay của ellipse là một giá trị ngẫu nhiên từ 0 đến 360 độ.
        for i in range(NUM)]    

fig = plt.figure(0) #plt.figure(0): Tạo một cửa sổ (figure) để chứa biểu đồ.
ax = fig.add_subplot(111, aspect='equal')
for e in ells:
    ax.add_artist(e)
    e.set_clip_box(ax.bbox) #e.set_clip_box(ax.bbox): Giới hạn việc vẽ ellipse trong vùng biểu đồ (bounding box).
    e.set_facecolor(rnd.rand(3))    #e.set_facecolor(rnd.rand(3)): Đặt màu sắc ngẫu nhiên cho từng ellipse. 
                                    #rnd.rand(3) trả về một mảng 3 phần tử (R, G, B), tạo ra một màu sắc ngẫu nhiên cho mỗi ellipse.

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
plt.show()
