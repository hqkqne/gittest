def addTwoNumbers(l1, l2):
    l1 = int(''.join(map(str,l1[::-1])))
    l2 = int(''.join(map(str, l2[::-1])))
    return list(map(int, str(l1+l2)))[::-1]
    # return list(str(l1+l2))[::-1]
l1 = [2,2,3]
l2 = [1,2,3]
print(addTwoNumbers(l1,l2))
# digits = list(map(int, str(number)))
