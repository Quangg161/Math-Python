import networkx as nx
import matplotlib.pyplot as plt

# Khởi tạo đồ thị và thêm đỉnh, cạnh
g = nx.Graph()
g.add_node('TP.HCM')
g.add_node('Dong Nai')
g.add_node('Ba Ria Vung Tau')
g.add_node('Lam Dong')
g.add_node('Can Tho')
g.add_node('Long An')
g.add_edge('TP.HCM', 'Dong Nai')
g.add_edge('TP.HCM', 'Ba Ria Vung Tau')
g.add_edge('TP.HCM', 'Long An')
g.add_edge('Dong Nai', 'Lam Dong')
g.add_edge('Dong Nai', 'Ba Ria Vung Tau')

# Các thông tin về đồ thị
print('Số lượng tỉnh thành trong đồ thị:', g.number_of_nodes())
print('Số lượng cạnh kết nối(giữa các tỉnh thành) trong đồ thị:', g.number_of_edges())
print('Danh sách các đỉnh hiện có trong đồ thị:', g.nodes())
print('Danh sách các cạnh hiện có trong đồ thị:', g.edges())
print('Số cạnh kết nối với TPHCM:', g.degree('TP.HCM'))
print('Mỗi đỉnh có bao nhiêu kết nối:', g.degree())
print('Các đỉnh có kết nối trực tiếp với TP.HCM:', list(g.neighbors('TP.HCM')))
print('Cạnh (kết nối) giữa Lam Dong và Long An:', g.has_edge('Lam Dong', 'Long An'))

try:
    print('Đường đi ngắn nhất từ Lam Dong đến Long An:', nx.shortest_path(g, 'Lam Dong', 'Long An'))
except nx.NetworkXNoPath:
    print('Không có đường đi giữa Lam Dong và Long An')

# Bổ sung thêm đỉnh và cạnh
g.add_node('Tien Giang')
g.add_edge('Tien Giang', 'Long An')
g.add_edge('Tien Giang', 'Can Tho')

print('Đường đi ngắn nhất từ Lam Dong đến Can Tho:', nx.shortest_path(g, 'Lam Dong', 'Can Tho'))
print('Số cạnh của đường đi ngắn nhất từ Lam Dong đến BR-VT:', nx.shortest_path_length(g, 'Lam Dong', 'Ba Ria Vung Tau'))
print('Số cạnh của đường đi ngắn nhất từ Dong Nai đến BR-VT:', nx.shortest_path_length(g, 'Dong Nai', 'Ba Ria Vung Tau'))
print('Số cạnh của đường đi ngắn nhất từ Lam Dong đến Long An:', nx.shortest_path_length(g, 'Lam Dong', 'Long An'))

# Trực quan hóa đồ thị
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(g)  # Tự động sắp xếp vị trí các đỉnh
nx.draw(g, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_color="black", font_weight="bold", edge_color="gray")
plt.title("Đồ thị kết nối giữa các tỉnh thành")
plt.show()
