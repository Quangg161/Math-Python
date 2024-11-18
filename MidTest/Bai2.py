import sys
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, dinh):
        self.x = dinh
        self.graph = [[0 for _ in range(dinh)] for _ in range(dinh)]

    def inketqua(self, L, path, a):
        print("Đỉnh nguồn xuất phát từ:", a)
        for nut in range(self.x):
            if L[nut] == sys.maxsize:
                print(f"Không có đường đi từ {a} đến {nut}")
            else:
                print(f"Đến đỉnh {nut}: Đường đi ngắn nhất là {' -> '.join(map(str, path[nut]))} với độ dài {L[nut]}")

    def duongdinhonhat(self, L, P):
        min = sys.maxsize
        min_index = -1
        for x in range(self.x):
            if L[x] < min and not P[x]:
                min = L[x]
                min_index = x
        return min_index

    def timduongdi(self, a):
        L = [sys.maxsize] * self.x
        L[a] = 0
        P = [False] * self.x
        path = [[] for _ in range(self.x)]  # Lưu đường đi ngắn nhất
        path[a] = [a]

        for _ in range(self.x):
            u = self.duongdinhonhat(L, P)
            if u == -1:  # Nếu không còn đỉnh nào có thể duyệt, thoát khỏi vòng lặp
                break
            P[u] = True

            for x in range(self.x):
                if self.graph[u][x] > 0 and not P[x] and L[x] > L[u] + self.graph[u][x]:
                    L[x] = L[u] + self.graph[u][x]
                    path[x] = path[u] + [x]

        self.inketqua(L, path, a)
        return L, path  # Trả về độ dài đường đi và đường đi để dùng trong vẽ đồ thị

    def vedothi(self, distances, paths, source):
        G = nx.Graph()
        for i in range(self.x):
            for j in range(self.x):
                if self.graph[i][j] != 0:
                    G.add_edge(i, j, weight=self.graph[i][j])

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')
        
        # Vẽ đồ thị với các cạnh có trọng số
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        # Vẽ đường đi ngắn nhất từ đỉnh nguồn đến các đỉnh khác
        for i in range(len(distances)):
            if i != source and distances[i] != sys.maxsize:
                path_edges = [(paths[i][j], paths[i][j + 1]) for j in range(len(paths[i]) - 1)]
                nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

        plt.show()


# Bài toán 01
print("Bài toán 01:")
g1 = Graph(6)
g1.graph = [
    [0, 4, 0, 1, 0, 0],
    [4, 0, 8, 0, 0, 0],
    [0, 8, 0, 9, 1, 4],
    [1, 0, 9, 0, 5, 0],
    [0, 0, 1, 5, 0, 7],
    [0, 0, 4, 0, 7, 0]
]
distances1, paths1 = g1.timduongdi(0)  # Tìm đường đi ngắn nhất từ đỉnh 0

