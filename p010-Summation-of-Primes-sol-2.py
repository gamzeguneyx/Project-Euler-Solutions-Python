# This question also can be solved easily by importing eulerlib library and using prime number function:

import eulerlib
def compute():
	ans = sum(eulerlib.list_primes(2000000))
	return str(ans)

if __name__ == "__main__":
	print(compute())
