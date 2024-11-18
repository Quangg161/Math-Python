#Cách 1:
print("cách 1:")
trang_thai="s0"

def chuyen(tin_hieu):
    global trang_thai
    if trang_thai == 's0':
        if tin_hieu == 0:
            print('0-s0')
            trang_thai = 's0'
        elif tin_hieu ==1:
            print('1-s1')
            trang_thai = 's1'

    elif trang_thai == 's1':
        if tin_hieu == 0:
            print('0-s1')
            trang_thai = 's1'
        elif tin_hieu ==1:
            print('1-s2')
            trang_thai = 's2'

    elif trang_thai =='s2':
        if tin_hieu == '0':
            print('0-s2')
            trang_thai = 's2'
        elif tin_hieu == 1:
            print('1-s0')
            trang_thai ='s0'

tap_tinhieu = [1, 0, 1, 0, 1, 1, 0 , 0, 1] # thiết lập tập dữ liệu đầu vào
for i in tap_tinhieu:
    print(chuyen(i))

#Cách 2
print("cách 2:")
trang_thai="s0"
trangthai_ke = {'s0': ['s0', 's1'],
                's1': ['s1', 's2'],
                's2': ['s2', 's0']  }

ket_qua = { 's0': [ 0, 1],
            's1': [ 0, 1],
            's2': [ 0, 1]   }

def chuyen_trangthai(tin_hieu):
    global trang_thai
    chuoi_in = str (ket_qua[trang_thai][tin_hieu])
    chuoi_in = chuoi_in + " - " + trangthai_ke[trang_thai][tin_hieu]
    print(chuoi_in)
    trang_thai = trangthai_ke[trang_thai][tin_hieu]

tap_tinhieu = [1, 0, 1, 0, 1, 1, 0 , 0, 1] 
for i in tap_tinhieu:
    print(chuyen_trangthai(i))