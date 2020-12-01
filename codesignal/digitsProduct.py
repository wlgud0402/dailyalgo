def digitsProduct(product):
    div = []
    for i in range(1, product+1):
        if product % i == 0:
            div.append(i)

    return div


print(digitsProduct(12))  # 26
