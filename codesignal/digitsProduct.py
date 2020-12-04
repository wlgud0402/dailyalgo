# def digitsProduct(product):
#     divisors = []
#     div = 2

#     while product != 1:
#         if product % div == 0:
#             print(div)
#             product = product/div
#             divisors.append(div)
#         else:
#             div += 1

#     return divisors


# print(digitsProduct(12))  # 26

def digitsProduct(product):
    if product == 0:
        return 10
    if product == 1:
        return 1

    for i in range(1, 10000):
        number = str(i)
        total = 1

        for char in number:
            total *= int(char)

        if total == product:
            return i

    # if not found return -1
    return -1


print(digitsProduct(12))
