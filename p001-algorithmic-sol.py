def multiples_of_3_or_5():
    total_sum = 0
    for i in range(1000):
        if(i%3 == 0 or i%5 == 0):
            total_sum = total_sum + i
    return total_sum
  
print(multiples_of_3_or_5())
