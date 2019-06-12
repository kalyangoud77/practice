def common_member(a, b):
    if (list(a) & list(b)):
        print(a & b)
    else:
        print("No common elements")


a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
common_member(a, b)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
common_member(a, b)