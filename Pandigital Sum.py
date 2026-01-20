from collections import Counter

two_digits_min = 12
two_digits_max = 78
three_digits_min = 123
three_digits_max = 798
pan_product = []

for i in range(two_digits_min, two_digits_max + 1):
    for j in range(three_digits_min, three_digits_max + 1):

        two_digits = list(map(int, str(i)))
        three_digits = list(map(int, str(j)))

        if any(count > 1 for count in Counter(two_digits).values()) or any(count > 1 for count in Counter(three_digits).values()) or 0 in two_digits or 0 in three_digits:
            pass
        else:
            check = any(n in three_digits for n in two_digits)

            if check:
                pass
            else:
                product = i * j
                four_digits = list(map(int, str(product)))

                if len(four_digits) > 4 or any(count > 1 for count in Counter(four_digits).values()) or 0 in four_digits:
                    pass
                else:
                    check2 = any(n in four_digits for n in two_digits)
                    check3 = any(n in four_digits for n in three_digits)

                    if check2 or check3:
                        pass
                    else:
                        if product in pan_product:
                            print(f"{i} * {j} = {product} is a pan-digital triplet")
                        else:
                            pan_product.append(product)
                            print(f"{i} * {j} = {product} is a pan-digital triplet")

one_digit_min = 1
one_digit_max = 9
four_digits_min = 1234
four_digits_max = 9876

for i in range(one_digit_min, one_digit_max + 1):
    for j in range(four_digits_min, four_digits_max + 1):
        one_digit = list(map(int, str(i)))
        four_digits = list(map(int, str(j)))

        if any(count > 1 for count in Counter(four_digits).values()) or 0 in four_digits:
            pass
        else:
            check = any(n in four_digits for n in one_digit)

            if check:
                pass
            else:
                product = i * j
                four_digits_new = list(map(int, str(product)))

                if len(four_digits_new) > 4 or any(count > 1 for count in Counter(four_digits_new).values()) or 0 in four_digits_new:
                    pass
                else:
                    check2 = any(n in four_digits_new for n in one_digit)
                    check3 = any(n in four_digits_new for n in four_digits)

                    if check2 or check3:
                        pass
                    else:
                        if product in pan_product:
                            print(f"{i} * {j} = {product} is a pan-digital triplet")
                        else:
                            pan_product.append(product)
                            print(f"{i} * {j} = {product} is a pan-digital triplet")

print(pan_product)
print(f"The sum of the non-repeating products of the pan-digital triplets is {sum(pan_product)}")