def pairs_count(lst, target):
    num = 0
    for x in range(len(lst)):
        for y in range(x + 1, len(lst)):
            if lst[x] + lst[y] == target:
                print(f"{lst[x]} {lst[y]}")
                num += 1
    return num

def main():
    lst = [1, 3, 6, 2, 2, 0, 4, 5]
    target = 5
    print(pairs_count(lst, target))

if __name__ == '__main__':
    main()
