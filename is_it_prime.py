def is_it_prime(x:int) -> bool:
    x = abs(x)
    if x == 1:
        return False
    for i in range(2,  x - 1):
        if x % i == 0 and x != 2:
            return False
    return True