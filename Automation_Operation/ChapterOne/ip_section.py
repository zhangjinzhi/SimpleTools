# coding:utf-8
from IPy import IP
print IP('10.0.0.0/8').version()
print IP('::1').version()


from IPy import IP
def main():
    ip = IP('182.168.8.0/26')
    print ip.len()
    for x in ip:
        print x


if __name__=='__main__':
    main()