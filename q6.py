def check_first_last_same(numbers):
    return numbers[0] == numbers[-1]

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

result_x = check_first_last_same(numbers_x)
result_y = check_first_last_same(numbers_y)

if result_x:
    print("For numbers_x, first and last numbers are the same")
else:
    print("For numbers_x,  first and last numbers are different.")

if result_y:
    print("For numbers_y, first and last numbers are the same")
else:
    print("For numbers_y, first and last numbers are different")
