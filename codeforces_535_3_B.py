def main():
    n = int(input())
    input_list = [int(i) for i in input().split()]

    input_list = sorted(input_list, reverse=True)
    # print(input_list)
    x = None
    for item in input_list:
        if input_list[0] % item != 0 or item == x:
            break
        x = item

    print(input_list[0], item)

if __name__ == "__main__":
    main()