from pyswip import Prolog

p = Prolog()

# Khai báo quy tắc phaichet: Một người sẽ chết nếu là con người.
p.assertz('phaichet(X) :- connguoi(X)')

# Khai báo các thực thể con người.
p.assertz('connguoi(micheal_jackson)')
p.assertz('connguoi(trinh_cong_son)')
p.assertz('connguoi(vo_tong)')

# Truy vấn tất cả các con người.
print(list(p.query('connguoi(Which)')))

# Truy vấn tất cả những ai sẽ phải chết.
print(list(p.query('phaichet(What)')))
