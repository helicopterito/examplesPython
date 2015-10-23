while True:
	print('Quien eres?')
	name = input()
	if(name != 'Nestor'):
		continue
	print('Hola Nestor ¿Cual es la contraseña?(Es un pez)')
	password = input()
	if(password == 'pez espada'):
		break
print('Acceso concedido')
