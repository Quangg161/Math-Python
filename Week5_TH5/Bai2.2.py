import pandas as pd
import numpy as np

# Đọc dữ liệu từ file Excel và chuyển nó thành ma trận
df = pd.read_excel("D:\\Study\\Nam 4\\HK241\\TRR\\TH\\Submit\\Week5_TH5\\monhoc.xlsx")

# Bỏ qua các cột hoặc hàng không liên quan (ví dụ như tên môn học)
matrix = df.iloc[1:, 1:].values  # Bỏ dòng đầu và cột đầu nếu chúng chứa tiêu đề và thông tin không phải số

# Loại bỏ giá trị NaN (nếu có) và chuyển về kiểu số nguyên
matrix = np.nan_to_num(matrix).astype(int)

print("Ma trận: ")
print(matrix)

#Phản xạ
def is_reflexive(matrix):
    # Ma trận vuông
    if matrix.shape[0] != matrix.shape[1]:
        return False
    # Kiểm tra đường chéo chính
    return np.all(np.diag(matrix) == 1)

print("Phản xạ:", is_reflexive(matrix))

#Đối xứng
def is_symmetric(matrix):
    return np.array_equal(matrix, matrix.T)

print("Đối xứng:", is_symmetric(matrix))

#Phản đối xứng
def is_antisymmetric(matrix):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i != j and matrix[i, j] == 1 and matrix[j, i] == 1:
                return False
    return True

print("Phản đối xứng:", is_antisymmetric(matrix))

# Tính bắt cầu
def is_transitive(matrix):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] == 1:
                for k in range(matrix.shape[1]):
                    if matrix[j, k] == 1 and matrix[i, k] == 0:
                        return False
    return True

print("Bắc cầu:", is_transitive(matrix))

# Quan hệ tương đương
def is_equivalence(matrix):
    return is_reflexive(matrix) and is_symmetric(matrix) and is_transitive(matrix)

print("Quan hệ tương đương:", is_equivalence(matrix))

# Quan hệ thứ tự 
def is_partial_order(matrix):
    return is_reflexive(matrix) and is_antisymmetric(matrix) and is_transitive(matrix)

print("Quan hệ thứ tự:", is_partial_order(matrix))
