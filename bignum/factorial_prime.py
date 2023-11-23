import sys

sys.set_int_max_str_digits(25000000)

def main():
    fact = 1
    # n = 422429
    # n = 110059
    # for i in range(1, n+1):
    #     fact = fact * i
    
    # print(fact + 1)
    n = 82589933
    print(1 << n - 1)

main()