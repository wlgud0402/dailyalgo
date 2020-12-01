import itertools


def digitsProduct(product):
    div = []
    for i in range(2, product):
        while True:

        if product % i == 0:
            div.append(i)

    # bundle = list(itertools.permutations(div, len(div)))
    # print(bundle)


print(digitsProduct(12))  # 26
