#  subeen 1'st interview problem
def pow_super(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a

    mid = n // 2
    if n % 2 == 0:
        b = pow_super(a, mid)
        return b*b
    else:
        return a*pow_super(a, n-1)


if __name__ == "__main__":
    x = int(input("x: \n"))
    y = int(input("y: \n"))

    print("a^n = ", pow_super(x, y))

