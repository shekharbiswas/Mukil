def unique_item(l1):
    return list(set(l1))


def sort_list(l1):
    return l1.sort_list()

def fib(n):
    a, b = 0, 1
	
    while (a < n):
        print(a, end=' ')
        a = b
        b = a + b
    print()