def filter_list(flst):
    lst = []
    for n in flst:
        if type(n) is int:
            lst.append(n)
    filter_lst = lst
    print(filter_lst)

def main():
    flst= [1, 2, 'a', 'aas14', 7]
    filter_list(flst)

if __name__ == '__main__':
   main()
