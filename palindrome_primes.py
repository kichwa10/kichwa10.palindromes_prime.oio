def is_prime(n):

    if n >= 2:
        for x in range (2, n):
            if not (n % x):
                return False
        return True
    else:
        return False
out = []

n = 10000
while len(str(n))==5:
    n = n + 1
    if is_prime(n)==True:
        if str(n)[0] == str(n)[4] and str(n)[1] == str(n)[3]:
            out.append(n)
print(out)

