import random

def create_phone():
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]
    suffix = random.randint(9999999,100000000)
    return "1{}{}{}".format(second, third, suffix)
# phone = create_phone()
# print(phone)