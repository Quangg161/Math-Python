import numpy as np

# Định nghĩa ma trận độ cao (ví dụ)
do_cao = np.array([
    [10, 12, 15, 17],
    [11, 9, 13, 16],
    [13, 10, 8, 14],
    [15, 12, 11, 10]
])

# Các hướng lân cận trong ma trận độ cao, tương ứng với (y, x)
huong = {
    "N": (-1, 0),
    "NE": (-1, 1),
    "E": (0, 1),
    "SE": (1, 1),
    "S": (1, 0),
    "SW": (1, -1),
    "W": (0, -1),
    "NW": (-1, -1)
}

# Hàm áp dụng thuật toán D8
def d8_algorithm(do_cao):
    rows, cols = do_cao.shape
    huong_thoat_nuoc = np.full((rows, cols), "", dtype=object)

    for i in range(rows):
        for j in range(cols):
            gia_tri_hien_tai = do_cao[i, j]
            min_do_cao = gia_tri_hien_tai
            huong_thoat = None

            # Kiểm tra từng hướng
            for key, (di, dj) in huong.items():
                ni, nj = i + di, j + dj

                # Kiểm tra giới hạn ma trận
                if 0 <= ni < rows and 0 <= nj < cols:
                    if do_cao[ni, nj] < min_do_cao:
                        min_do_cao = do_cao[ni, nj]
                        huong_thoat = key

            # Gán hướng thoát nước cho ô hiện tại
            huong_thoat_nuoc[i, j] = huong_thoat if huong_thoat else "None"

    return huong_thoat_nuoc

# Áp dụng thuật toán D8 lên ma trận độ cao
ket_qua = d8_algorithm(do_cao)

# In ra ma trận hướng thoát nước
print("Ma trận hướng thoát nước:")
print(ket_qua)