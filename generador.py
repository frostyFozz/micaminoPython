def GeneraNum(limite):
    num = 1

    while num < limite:
        yield num*2
        num+=1
devuleveme = GeneraNum(20)
# esto es un generador de numeros, que depende de cada solicitud
print(next(devuleveme))

print("ejemplo que simula codigo escrito")

print(next(devuleveme))

print("ejemplo que simula codigo escrito")

print(next(devuleveme))

print("ejemplo que simula codigo escrito")

print(next(devuleveme))



def platosDominicanos(*Platos):
    for comida in Platos:
        yield from comida
# esto equivale a hacer un ciclo for anidado para ver el sub de platos dominicanos

listaPlatos = platosDominicanos("arroz", "moro", "locrio", "fritos")

print(next(listaPlatos))

print(next(listaPlatos))