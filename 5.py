def friends_list(s):
    lst1 = []
    s = s.upper()
    lst = s.split(';')
    for str in lst:
        v = str.split(':')
        lst1.append(f"({v[1]}, {v[0]})")
    lst1.sort()
    return lst1

def main():
    lst = []
    lst1 = []
    s = "Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
    print(friends_list(s))

if __name__ == '__main__':
    main()
