#Este es un juego de adivinar un número.
import random
numeroSecreto = random.randint(1,20)
print('Estoy pensando en numero entre 1 y 20.')

#Pide al jugador que adivine 6 veces.
for vecesAdivinadas in range(1,7):
	print('Adivina una vez.')
	adivina = int(input())

	if adivina < numeroSecreto:
		print('Tu adivinanza es muy baja.')
	elif adivina > numeroSecreto:
		print('Tu adivinanza es muy alta.')
	else:
		break; #Esta condición es la adivinanza correcta.

if adivina == numeroSecreto:
	print('Buen trabajo, adivinaste mi numero en ' + str(vecesAdivinadas) + ' intentos.')
else:
	print('No. El numero que estab pensando era ' + str(numeroSecreto))

