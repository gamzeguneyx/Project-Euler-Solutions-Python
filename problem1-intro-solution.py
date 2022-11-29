def multiples(number):
    numbers_list = []
    for i in range(0, number):
        if i % 3 == 0 or i % 5 == 0:
            numbers_list.append(i)
            sum_of_numbers = sum(numbers_list)
    return sum_of_numbers
print(multiples(1000))
