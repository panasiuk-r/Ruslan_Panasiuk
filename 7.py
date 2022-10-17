import ipaddress

def address(ip):
    return ipaddress.ip_address(ip)

def main():
    ip=2149583361
    print(address(ip))

if __name__ == '__main__':
    main()
