print("Блок А, задание 6")

def F(n, x=2):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % x == 0:
        return False
    if x * x > n:
        return True
    return F(n, x + 1)

n = int(input())

if F(n):
    print("YES")
else:
    print("NO")