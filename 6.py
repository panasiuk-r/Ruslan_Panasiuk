from itertools import permutations

def nextBigger(num):
    lst = []
    bigger = False
    num1 = num
    while num1 != 0:
        i = num1 % 10
        lst.append(i)
        num1 //= 10
    lst.sort()
    per = permutations(lst)
    for arr in list(per):
        n=0
        for y in range(len(arr)):
            n = n*10 + arr[y]
        if n > num:
            bigger = True
            break
    if bigger == True:
        return n
    else:
        return -1
def main():
    print("Enter digit: ")
    i = int(input())
    print(nextBigger(i))

if __name__ == '__main__':
    main()
