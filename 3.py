def digital_root(num, sum):
    if num != 0:
        sum += num % 10
        num //= 10
        return root_sum(num, sum)
    else:
        return sum

def main():
   print("Enter digital number: ")
   i = int(input())
   print(digital_root(i, 0))

if __name__ == '__main__':
    main()
