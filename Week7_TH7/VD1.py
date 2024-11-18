import math
import sys

class Graph():
    def __init__(cung, dinh):
        cung.x = dinh
        cung.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def inketqua(cung, L, a):
        print("đỉnh nguồn xuất phát từ: ")
        for nut in range(cung.x):  # Thụt lề đúng
            print(a, " đến đỉnh ", nut, " độ dài đường đi là: ", L[nut])

    def duongdinhonhat(cung, L, P):
        min = sys.maxsize
        min_index = -1
        for x in range(cung.x):  # Thụt lề đúng
            if L[x] < min and P[x] == False:
                min = L[x]
                min_index = x
        return min_index

    def timduongdi(cung, a):
        L = [sys.maxsize] * cung.x  # Thụt lề đúng
        L[a] = 0
        P = [False] * cung.x  # Danh sách kiểm tra đỉnh đã xét

        for cout in range(cung.x):  # Vòng lặp để tìm đường đi
            u = cung.duongdinhonhat(L, P)  # Tìm đỉnh có đường đi ngắn nhất
            P[u] = True

            for x in range(cung.x):
                if cung.graph[u][x] > 0 and P[x] == False and L[x] > L[u] + cung.graph[u][x]:
                    L[x] = L[u] + cung.graph[u][x]

        cung.inketqua(L, a)  # In kết quả

# Ví dụ sử dụng lớp Graph
g = Graph(6)

# Đoạn này thêm dữ liệu vào đồ thị, ví dụ:
g.graph = [
    [0, 2, 0, 1, 0, 0],
    [3, 0, 8, 4, 0, 0],
    [0, 2, 0, 0, 7, 4],
    [4, 2, 0, 0, 2, 0],
    [0, 0, 11, 1, 0, 5],
    [0, 0, 3, 0, 5, 0]
]

g.timduongdi(0) # Gọi hàm tìm đường đi từ đỉnh 0




