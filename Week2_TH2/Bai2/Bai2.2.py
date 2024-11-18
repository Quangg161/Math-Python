def alpha(a): # hàm y = x+10
    return a+10

def beta(b): # hàm y = 3x
    return b*3

def ham_hop(g,f): # hàm compose y = 3*(x+10)
    return (lambda x:g(f(x)))

h = ham_hop(alpha, beta)
print(h(1))

g = ham_hop(beta, alpha) # hàm compose y = (3*x)+10
print(g(1))