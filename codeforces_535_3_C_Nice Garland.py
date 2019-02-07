from itertools import permutations


def main():
    n = int(input())
    s = input()

    prms = list(permutations("RGB"))

    cost = 1e9
    for item in prms:
        prms_li = []
        diff = 0
        for i in range(n):
            prms_li.append(item[i % 3])
            diff += s[i] is not prms_li[i]

        if diff < cost:
            cost = diff
            ans = prms_li

    print(cost)
    print(''.join(ans))


if __name__ == "__main__":
    main()
