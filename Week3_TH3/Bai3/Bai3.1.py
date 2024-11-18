sodiem_DL = 9
diadiem = ['Cần Giờ', 'Củ Chi', 'Chợ Bến Thành', 'Sở Thú', 'BV thẫm mỹ răng', 'Chí Hòa',
'Dinh Độc lập', 'Bào tàng', 'Trường Văn Lang']
thoigian = [1.0, 1.0, 0.6, 0.4, 1.5, 0.3, 0.3, 0.3, 0.6]
songay_dulich=1.5

def kiemtra_chuoi(chuoi_dang_chon, thoigian, gioihan):
    tong_thoigian = 0
    for j in range(len(chuoi_dang_chon)):
        if chuoi_dang_chon[j] == '1':
            tong_thoigian += thoigian[j]
    return tong_thoigian <= gioihan, tong_thoigian

def lietke_chuoinhiphan(n):
    from itertools import product
    return [''.join(i) for i in product('01', repeat=n)]

def tim_phuongan(thoigian, gioihan):
    search = []
    cac_phuongan = lietke_chuoinhiphan(len(thoigian))
    for i in range(len(cac_phuongan)):
        dc_kg, tong_thoigian = kiemtra_chuoi(cac_phuongan[i], thoigian, gioihan)
        if dc_kg:
            print(cac_phuongan[i], dc_kg, tong_thoigian)
            search.append(cac_phuongan[i])
    return search

songay_dulich = 1.5
tim_phuongan(thoigian, songay_dulich)
