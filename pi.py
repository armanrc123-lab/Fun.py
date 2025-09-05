from decimal import Decimal, getcontext

def compute_pi_to_digits(digits):

    getcontext().prec = digits + 5

    C = 426880 * Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = Decimal(L)

    k = 1
    while True:
        M = M * (K**3 - 16*K) // (k**3)
        L += 545140134
        X *= -262537412640768000
        term = Decimal(M * L) / X

        if abs(term) < Decimal(10) ** -(digits + 1):
            break

        S += term
        K += 12
        k += 1

    pi = C / S
    return str(+pi)[:digits + 2] 



print(compute_pi_to_digits(100000))




