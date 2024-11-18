def difference(A, B):
    phantu_moi = 0  # Số phần tử có trong tập A mà không có trong tập B
    for x in A:
        if x not in B:
            phantu_moi += 1
    return phantu_moi

def add(A, B):
    ketqua = B.copy()  # Sao chép tập B để tránh thay đổi trực tiếp
    for x in A:
        if x not in B:
            ketqua.append(x)  # Thêm các phần tử không có trong B
    return ketqua

# Khai báo các camera phủ các khu vực
I = [1, 3, 4, 6, 7]
II = [4, 7, 8, 12]
III = [2, 5, 9, 11, 13]
IV = [1, 2, 18, 19, 21]
V = [3, 6, 10, 12, 14]
VI = [8, 14, 15, 16, 17]
VII = [18, 21, 24, 25]
VIII = [2, 10, 16, 23]
IX = [1, 6, 11]
X = [20, 22, 24, 25]
XI = [2, 4, 6, 8]
XII = [1, 6, 12, 17]

cameras = [I, II, III, IV, V, VI, VII, VIII, IX, X, XI, XII]
khuvuc = list(range(1, 26))  # 25 khu vực từ 1 đến 25

# Xử lý chính
tapphu = []  # Ban đầu tập phủ là tập rỗng
while len(tapphu) < len(khuvuc):
    max_new_cameras = 0  # Số camera mới nhiều nhất có thể thêm vào tập phủ
    for camera in cameras:
        max_new_cameras = max(difference(camera, tapphu), max_new_cameras)
    
    luachon = 0  # Duyệt lần nữa để tìm camera có số khu vực phủ nhiều nhất
    while difference(cameras[luachon], tapphu) < max_new_cameras:
        luachon += 1  # Vị trí camera sẽ được chọn
    
    if luachon < len(cameras):  # Đảm bảo vị trí cameras là tồn tại
        tapphu = add(cameras[luachon], tapphu)
        print(f"Camera: {luachon+1}, Khu vực phủ: {cameras[luachon]}, Tập phủ: {tapphu}")

# In ra kết quả cuối cùng
tapphu.sort()
print("Tập phủ cuối cùng:", tapphu)
