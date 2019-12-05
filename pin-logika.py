def isRetarded(n, m):
    if m == 1:
        return True
    if m == 2:
        x = n % 10
        n1 = n // 10
        x1 = n1 % 10
        if x <= x1:
            return True
        else:
            return False
    if m == 3:
        x = n % 10
        n1 = n // 10
        x1 = n1 % 10
        n2 = n1 // 10
        x2 = n2 % 10
        if x <= x1 <= x2:
            return True
        else:
            return False
    if m == 4:
        x = n % 10
        n1 = n // 10
        x1 = n1 % 10
        n2 = n1 // 10
        x2 = n2 % 10
        n3 = n2 // 10
        x3 = n3 % 10
        if x <= x1 <= x2 <= x3:
            return True
        else:
            return False
    if m == 5:
        x = n % 10
        n1 = n // 10
        x1 = n1 % 10
        n2 = n1 // 10
        x2 = n2 % 10
        n3 = n2 // 10
        x3 = n3 % 10
        n4 = n3 // 10
        x4 = n4 % 10
        if x <= x1 <= x2 <= x3 <= x4:
            return True
        else:
            return False
    if m == 6:
        x = n % 10
        n1 = n // 10
        x1 = n1 % 10
        n2 = n1 // 10
        x2 = n2 % 10
        n3 = n2 // 10
        x3 = n3 % 10
        n4 = n3 // 10
        x4 = n4 % 10
        n5 = n4 // 10
        x5 = n5 % 10
        if x <= x1 <= x2 <= x3 <= x4 <= x5:
            return True
        else:
            return False
    if m == 7:
        x = n % 10
        n1 = n // 10
        x1 = n1 % 10
        n2 = n1 // 10
        x2 = n2 % 10
        n3 = n2 // 10
        x3 = n3 % 10
        n4 = n3 // 10
        x4 = n4 % 10
        n5 = n4 // 10
        x5 = n5 % 10
        n6 = n5 // 10
        x6 = n6 % 10
        if x <= x1 <= x2 <= x3 <= x4 <= x5 <= x6:
            return True
        else:
            return False
    if m == 8:
        x = n % 10
        n1 = n // 10
        x1 = n1 % 10
        n2 = n1 // 10
        x2 = n2 % 10
        n3 = n2 // 10
        x3 = n3 % 10
        n4 = n3 // 10
        x4 = n4 % 10
        n5 = n4 // 10
        x5 = n5 % 10
        n6 = n5 // 10
        x6 = n6 % 10
        n7 = n6 // 10
        x7 = n7 % 10
        if x <= x1 <= x2 <= x3 <= x4 <= x5 <= x6 <= x7:
            return True
        else:
            return False
    if m == 9:
        x = n % 10
        n1 = n // 10
        x1 = n1 % 10
        n2 = n1 // 10
        x2 = n2 % 10
        n3 = n2 // 10
        x3 = n3 % 10
        n4 = n3 // 10
        x4 = n4 % 10
        n5 = n4 // 10
        x5 = n5 % 10
        n6 = n5 // 10
        x6 = n6 % 10
        n7 = n6 // 10
        x7 = n7 % 10
        n8 = n7 // 10
        x8 = n8 % 10
        if x <= x1 <= x2 <= x3 <= x4 <= x5 <= x6 <= x7 <= x8:
            return True
        else:
            return False
    if m == 10:
        x = n % 10
        n1 = n // 10
        x1 = n1 % 10
        n2 = n1 // 10
        x2 = n2 % 10
        n3 = n2 // 10
        x3 = n3 % 10
        n4 = n3 // 10
        x4 = n4 % 10
        n5 = n4 // 10
        x5 = n5 % 10
        n6 = n5 // 10
        x6 = n6 % 10
        n7 = n6 // 10
        x7 = n7 % 10
        n8 = n7 // 10
        x8 = n8 % 10
        n9 = n8 // 10
        x9 = n9 % 10
        if x <= x1 <= x2 <= x3 <= x4 <= x5 <= x6 <= x7 <= x8 <= x9:
            return True
        else:
            return False


if isRetarded(944321, 5):
    print("yes")
else:
    print("no")
