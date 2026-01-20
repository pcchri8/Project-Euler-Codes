def get_reversed_number(number):

    temp = [int(d) for d in str(number)]
    reversed_number = int(''.join(map(str, list(reversed(temp)))))

    return reversed_number


def palindromic_production_check(number, iterations = 50):

    if number <= 0:
        return 0
    else:
        reversed_number = get_reversed_number(number)
        new_number = number + reversed_number
        i = 1

        while new_number != get_reversed_number(new_number) and i <= iterations:
            new_number = new_number + get_reversed_number(new_number)
            i = i + 1

        if new_number != get_reversed_number(new_number):
            return 0
        else:
            return new_number


def is_lychrel_number(number):

    if palindromic_production_check(number):
        print(f"{number} is not a Lychrel number")
        return number
    else:
        print(f"{number} is a Lychrel number")
        return 0


lim = 10000
s = 0

for j in range(1, lim + 1):
    output = is_lychrel_number(j)
    if output == 0:
        s = s + 1

print(s)