def collatz(number):
	if number % 2 == 0:
		return number // 2
	elif number % 2 == 1:
		return 3 * number + 1

print('Introduce un numero: ')
numero = int(input())
print(collatz(numero))
