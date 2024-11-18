import networkx as nx
import matplotlib.pyplot as plt

# Tạo đồ thị
g = nx.Graph()

# Thêm các đỉnh
g.add_nodes_from(['TP.HCM', 'Dong Nai', 'Ba Ria Vung Tau', 'Lam Dong', 'Can Tho', 'Long An'])

# Thêm các cạnh
g.add_edges_from([('TP.HCM', 'Dong Nai'), 
                  ('TP.HCM', 'Ba Ria Vung Tau'), 
                  ('TP.HCM', 'Long An'),
                  ('Dong Nai', 'Lam Dong'), 
                  ('Dong Nai', 'Ba Ria Vung Tau')])

# In thông tin về đồ thị
print(f"Số lượng tỉnh/thành trong đồ thị: {g.number_of_nodes()}")
print(f"Số lượng cạnh trong đồ thị: {g.number_of_edges()}")
print(f"Danh sách các đỉnh: {list(g.nodes())}")
print(f"Danh sách các cạnh: {list(g.edges())}")
print(f"Số kết nối của mỗi đỉnh: {dict(g.degree())}")

# Kiểm tra đường đi ngắn nhất từ Lâm Đồng đến Long An
try:
    print(f"Đường đi ngắn nhất từ Lâm Đồng đến Long An: {nx.shortest_path(g, 'Lam Dong', 'Long An')}")
except nx.NetworkXNoPath:
    print("Không có đường đi từ Lâm Đồng đến Long An")

# Vẽ biểu đồ đồ thị
pos = nx.spring_layout(g)
plt.figure(figsize=(10, 8))
nx.draw(g, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=12, font_color="black", font_weight="bold", edge_color="gray")
