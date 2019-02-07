
def per_rec(n, x):
    if n == x:
        return 1
    return n * per_rec(n-1, x)
'''
    nPr = 1
    i = 0
    while i < r:
        nPr *= n-i  # nPr = n*(n-1)*(n-2) .... r

        i += 1

    print('nPr = ', nPr)
'''


def permutation_gen(a, n):  # finding permutation with using an extra list
    if a == n:
        # tpl for only unique permutations

        tpl = tuple(per_li)
        if tpl in per_set:
            return
        per_set.add(tpl)

        print(per_li)
        return

    for i in range(n):
        if taken[i] is False:
            taken[i] = True
            per_li[a] = li[i]
            permutation_gen(a+1, n)
            taken[i] = False


def gen_permutation(a, r):  # without an extra array
    if a == r:
        print(li)
        return

    for i in range(a, r+1):
        if li[i] in li[a:i]:
            continue
        li[i], li[a] = li[a], li[i]
        gen_permutation(a+1, r)
        li[i], li[a] = li[a], li[i]


def main():
    n = int(input())
    r = int(input())
    print('nPr = ', per_rec(n, n-r))

if __name__ == "__main__":
    # main()
    li = [1, 1, 2]
    n = len(li)
    per_li = [-1] * n
    taken = [False] * n
    per_set = set()
    #  permutation_gen(0, n)
    gen_permutation(0, n-1)
