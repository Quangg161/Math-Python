from pyswip import Prolog

tgtph = Prolog()  # Khai báo quan hệ giữa tác giả tác phẩm là một đối tượng Prolog
tgtph.assertz('tacgiatacpham(nguyendu,truyenkieu)')  # Nhập dữ liệu nguyendu, truyenkieu
tgtph.assertz('tacgiatacpham(nguyendu,thanhhienthitap)')
tgtph.assertz('tacgiatacpham(nguyendu,namtrungtapngam)')
tgtph.assertz('tacgiatacpham(nguyendu,bachanhluctap)')
result = list(tgtph.query('tacgiatacpham(nguyendu, X)'))
print(result)

for tg in tgtph.query('tacgiatacpham(X, Y)'):
    print(tg["X"], ' viet ra tac pham: ', tg["Y"]) 