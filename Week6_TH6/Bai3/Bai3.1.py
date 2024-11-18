class InitializationError(Exception):
    pass

class StateMachine:
    def __init__(self): #hàm khỏi tạo 3 thuộc tính
        self.tap_xuly = {} # từ điển chứa trạng thái và các hàm xử lý
        self.trangthaiBatdau = None # chưa được thiết lập
        self.trangthaiKetThuc = [] # danh sách trạng thái kết thúc, khi đến đây sẽ dừng lại

    def them_Trangthai(self, trangthai, xuly, trangthai_ketthuc=0):
        trangthai = trangthai.upper()
        self.tap_xuly[trangthai] = xuly
        if trangthai_ketthuc:
            self.trangthaiKetThuc.append(trangthai)

    def thietlap_TrangthaiBatdau(self, trangthai):
        self.trangthaiBatdau = trangthai.upper()

    def thucthi(self, dauvao):
        try:
            xuly = self.tap_xuly[self.trangthaiBatdau]
        except KeyError:
            raise InitializationError("Phải gọi .thietlap_TrangthaiBatdau() trước khi gọi .thucthi()")
        if not self.trangthaiKetThuc:
            raise InitializationError("Ít nhất 1 trạng thái phải là trạng thái kết thúc")
        while True:
            (TrangThaiMoi, dauvao) = xuly(dauvao)
            if TrangThaiMoi.upper() in self.trangthaiKetThuc:
                print("Đến đích! ", TrangThaiMoi)
                break
            else:
                xuly = self.tap_xuly[TrangThaiMoi.upper()]

# Khởi tạo các danh sách từ vựng:
tinhtu_tichcuc = ["vi_dai", "sieu", "vui", "de", "giai_tri"] # danh sách tính từ tích cực
tinhtu_tieucuc = ["chan", "kho", "xau", "kem"] # tính từ tiêu cực

def trangthai_baudau(txt):
    splitted_txt = txt.split(None, 1)
    tu, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
    if tu == "Python":
        trangthaimoi = "Python_state"
    else:
        trangthaimoi = "error_state"
    return (trangthaimoi, txt)

def trangthai_python(txt):
    splitted_txt = txt.split(None, 1)
    tu, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
    if tu == "is": # nếu từ là ‘is’ thì
        trangthaimoi = "is_state" # trạng thái mới là is_state
    else:
        trangthaimoi = "error_state" # ngược lại trạng thái mới là lỗi (error_state)
    return (trangthaimoi, txt) 

def trangthai_is_chuyentrangthai(txt):
    splitted_txt = txt.split(None, 1)
    tu, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
    if tu == "not":
        trangthaimoi = "not_state"
    elif tu in tinhtu_tichcuc:
        trangthaimoi = "pos_state"
    elif tu in tinhtu_tieucuc:
        trangthaimoi = "neg_state"
    else:
        trangthaimoi = "error_state"
    return (trangthaimoi, txt)

def trangthai_isnot_chuyentrangthai(txt):
    splitted_txt = txt.split(None, 1)
    tu, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
    if tu in tinhtu_tichcuc:
        trangthaimoi = "pos_state"
    elif tu in tinhtu_tieucuc:
        trangthaimoi = "neg_state"
    else:
        trangthaimoi = "error_state"
    return (trangthaimoi, txt)

def neg_state(txt):
    print ("Chao!")
    return ("neg_state","")

if __name__ == "__main__":
    m = StateMachine()
    # add_state 
    m.them_Trangthai("Start", trangthai_baudau)
    m.them_Trangthai("Python_state", trangthai_python)
    m.them_Trangthai("is_state", trangthai_is_chuyentrangthai)
    m.them_Trangthai("not_state", trangthai_isnot_chuyentrangthai)
    m.them_Trangthai("neg_state", None, trangthai_ketthuc = 1)
    m.them_Trangthai("pos_state", None, trangthai_ketthuc = 1)
    m.them_Trangthai("error_state", None, trangthai_ketthuc = 1)
    # set_start
    m.thietlap_TrangthaiBatdau("Start")
    # run 
    m.thucthi("Python is vi_dai")
    m.thucthi("Python is kho")
    m.thucthi("Python is xau")
    m.thucthi("Python is xao")