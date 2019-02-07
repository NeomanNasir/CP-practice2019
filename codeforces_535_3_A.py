
def main():
    n = int(input())
    for i in range(n):
        input_list = [int(i) for i in input().split()]

        a, b, c, d = input_list
        if a != c:
            print(a, c)
        else:
            print(a, d)

if __name__ == "__main__":
    main()
