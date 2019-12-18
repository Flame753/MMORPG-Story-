def sum_two_numbers(a, b):
    try:
        return int(a) + int(b)
    except Exception as e:
        print(str(e))
        return "Enter Only Numbers"


int1 = input("Enter a integer: ")
int2 = input("Enter another integer: ")


print(sum_two_numbers(int1, int2))
