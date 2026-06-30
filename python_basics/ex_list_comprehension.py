# Syntax : new_list = [new_item for item in list]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers_power_2 = [n * n for n in numbers]
print(numbers_power_2)

odd_numbers = [n for n in numbers if n % 2 != 0]
print(odd_numbers)

even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)