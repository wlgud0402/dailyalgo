# import itertools


# def digitsProduct(product):
#     div = []
#     for i in range(2, product):
#         while True:

#         if product % i == 0:
#             div.append(i)

#     # bundle = list(itertools.permutations(div, len(div)))
#     # print(bundle)


# print(digitsProduct(12))  # 26
def digitsProduct(product):
    divisors = []
    div = 2

    while product != 1:
        if product % div == 0:
            print(div)
            product = product/div
            divisors.append(div)
        else:
            div += 1

    return divisors


print(digitsProduct(12))  # 26
