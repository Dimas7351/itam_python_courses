def product(a, b):
    if a < 0:
        a *= -1
    elif b < 0:
        b *= -1
    result = a * b
    print("Product of", a, "and", b, "equals", result)
    return result

def pre_product(a,b):
    if ((a<0 or b<0) and (not(a<0 and b<0))) or (a<0 and b<0):
        product_result = -product(a, b)
    else:
        product_result = product(a, b)
    return product_result
print(pre_product(-1,-7))

