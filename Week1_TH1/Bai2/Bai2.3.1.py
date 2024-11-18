# Lấy các số nguyên tố có trong dãy
def isPrime(N):
    for i in [x+1 for x in range (N)]:
        if N % i==0 and (i!=1 and i!=N):
            return False
    return True
S_prime = set([x for x in range (40) if (isPrime(x)==True and x>0)]) #(isPrime(x)==True) dùng để giữ lại cái số ng tố 
print (S_prime)