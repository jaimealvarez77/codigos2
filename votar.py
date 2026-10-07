def verificar_puede_votar(edad,nacionalidad):
    if edad >=18 and nacionalidad == "española":
        puede_votar = True
    else:
        puede_votar = False 

        return puede_votar
print(verificar_puede_votar(15,"kazajo"))
print(verificar_puede_votar(18,"española"))
    
    