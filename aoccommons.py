def isPrime(n: int) -> bool:
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True

def divisors(n: int) -> list[int]:
	divs = []
	for i in range(1, n + 1):
		if n % i == 0:
			divs.append(i)
	return divs

def transpose(l: list[list]) -> list[list]:
	return [[*a] for a in zip(*l)]

i9e9 = int(9e9)
f9e9 = float(9e9)
s9e9 = str(i9e9)