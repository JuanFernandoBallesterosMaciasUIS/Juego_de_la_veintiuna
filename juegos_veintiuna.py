# Juego de la veintiuna
import random
print("---------------------------------------------------")
print("---------------JUEGO-DE-LA-VEINTIUNA---------------")
print("---------------------------------------------------")

#input
j1 = input("Ingresa el nombre del primer jugador: ")
j2 = input("Ingresa el nombre del primer jugador: ")
print("")

#process

carta1_j1 = random.randint(1,12)
carta2_j1 = random.randint(1,12)
carta1_j2 = random.randint(1,12)
carta2_j2 = random.randint(1,12)

total1 = carta1_j1 + carta2_j1
total2 = carta1_j2 + carta2_j2


print(j1,":La primera carta fue ",carta1_j1, "y la segunda fue",carta2_j1, ",el total es",total1 )
print("")
print(j2,":La primera carta fue ",carta1_j2, "y la segunda fue",carta2_j2, ",el total es",total2 )
print("")