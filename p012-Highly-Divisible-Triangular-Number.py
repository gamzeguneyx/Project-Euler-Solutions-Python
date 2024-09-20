# The answer is 76576500.

import math

def divisors(n):
  """Returns the number of divisors of a given number n."""
  count = 0
  for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
      count += 2  # For both i and n // i
  return count

def triangle_number(n):
  """Returns the nth triangle number."""
  return n * (n + 1) // 2

def first_triangle_number_with_over_500_divisors():
  """Finds the first triangle number with over 500 divisors."""
  n = 1
  while divisors(triangle_number(n)) <= 500:
    n += 1
  return triangle_number(n)

result = first_triangle_number_with_over_500_divisors()
print(result)
