def sum_two_numbers(a, b):
    return a + b


# print(sum_two_numbers(45, 55))


def flag_check(arg):
    if arg in ['y', 'Y', 'yes', 'Yes']:
        return False
    else:
        return True


def add():
    flag = True
    while flag:
        user_input1 = input("Enter a number: ")
        user_input2 = input("Enter another number: ")
        print(user_input1 + user_input2)
        out = input("Want to Stop (yes/no)")
        flag = flag_check(out)


def mult_table():
    mult2 = ''
    for i in range(1, 11):
        for j in range(1, 11):
            mult = i * j
            mult2 += f" {str(mult)}"
        print(mult2)
        mult2 = ''


# mult_table()

def ever_third():
    var = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta']
    for index, value in enumerate(var):
        if index % 3 == 0:
            print(value)


# ever_third()
