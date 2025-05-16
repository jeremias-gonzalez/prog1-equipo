from random import choice
# for i in range(0,101):
#      if i % 20 == 0:
#         print()
#      elif i % 3 == 0  :
#           print("fizz")
#      elif i % 5 == 0:
#           print("buzz")
#      elif i % 3 == 0 and i % 5 == 0 :
#           print("fizzbuzz")
#      else:  
#           print(i)

computerChoise = choice(["piedra", "papel", "tijera"])
userChoise = input("Elige piedra, papel o tijera: ")
if userChoise == computerChoise:
    print("Empate")
elif userChoise == "piedra" and computerChoise == "tijera":
    print("Ganaste")
elif userChoise == "papel" and computerChoise == "piedra":
    print("Ganaste")
elif userChoise == "tijera" and computerChoise == "papel":
    print("Ganaste")
elif userChoise == "piedra" and computerChoise == "papel":
    print("Perdiste")
elif userChoise == "papel" and computerChoise == "tijera":
    print("Perdiste")
elif userChoise == "tijera" and computerChoise == "piedra":
    print("Perdiste")
elif userChoise == "piedra" or userChoise == "papel" or userChoise == "tijera":
    print("Perdiste")       
else:
    print("Opcion no valida")
print("La computadora eligio: ", computerChoise)