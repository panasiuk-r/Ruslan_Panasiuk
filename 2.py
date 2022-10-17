def first_non_repeating_letter(string):
    uniq = True
    for x in range(len(string)):
        char = string[x]
        for y in range(x+1, len(string)):
            c = string[y]
            if char == c:
                uniq = False
        if uniq:
            print(f"the first uniq letter is: '{char}'")
            break
        else:
            uniq = True

def main():
    print('Enter string:')
    string: str = input()
    first_non_repeating_letter(string)

if __name__ == '__main__':
    main()
