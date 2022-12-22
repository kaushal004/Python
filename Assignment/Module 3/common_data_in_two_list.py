def common_in_two_list(l1, l2):
    status = False
    for a in l1:
        for b in l2:
            if a == b:
                status = True
            else:
                status = False
                return status

    return status   

x = [1, 4, 5, 9]
y = [2, 9, 7, 6]
print(common_in_two_list(x, y))