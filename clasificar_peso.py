def clasificar_imc(peso, altura):
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        categoria = "Bajo peso"
    else:
        if imc < 25:
            categoria = "Normal"
        else:
            categoria = "Sobrepeso"
            
    return categoria
# Caso 1: Persona con peso dentro del rango normal
resultado1 = clasificar_imc(70, 1.75)
print("Caso 1 - Resultado:", resultado1)

# Caso 2: Persona con bajo peso
resultado2 = clasificar_imc(48, 1.70)
print("Caso 2 - Resultado:", resultado2)