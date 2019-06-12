a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 7]
def common_member(a, b):
    x = set(a)
    y = set(b)
    if (x & y):
        print(x & y)
    else:
        print("No common elements")
common_member(a, b)

