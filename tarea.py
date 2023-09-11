import matplotlib.pyplot as plt

# Paso 1: Mensaje de bienvenida
print("Laboratorio de Suma Acumulativa")

# Paso 2: Ingresar la cantidad de números a sumar
while True:
    try:
        num_numeros = int(input("Ingrese la cantidad de números a sumar: "))
        if num_numeros > 0:
            break
        else:
            print("Por favor, ingrese un número entero positivo.")
    except ValueError:
        print("Por favor, ingrese un número entero positivo.")

# Paso 3: Ingresar los números uno por uno y calcular la suma acumulativa
numeros = []
suma_acumulativa = []
total_acumulado = 0

for i in range(1, num_numeros + 1):
    while True:
        try:
            numero = float(input(f"Ingrese el número {i}: "))
            total_acumulado += numero
            suma_acumulativa.append(total_acumulado)
            numeros.append(numero)
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Paso 4: Mostrar la suma acumulativa
print("Suma acumulativa:")
for i, suma in enumerate(suma_acumulativa, 1):
    print(f"Número {i}: {suma}")

# Paso 5: Crear un gráfico de barras
plt.bar(range(1, len(suma_acumulativa) + 1), suma_acumulativa)
plt.xlabel('Número de Entrada')
plt.ylabel('Suma Acumulativa')
plt.title('Suma Acumulativa de la Serie de Números')

# Datos para el gráfico
x = range(1, num_numeros + 1)  # Valores en el eje X (números de entrada)
y = suma_acumulativa           # Valores en el eje Y (suma acumulativa)

# Crear un gráfico de barras con ejes X e Y especificados
plt.bar(x, y)

# Configurar etiquetas para los ejes X e Y y un título
plt.xlabel('Número de Entrada')
plt.ylabel('Suma Acumulativa')
plt.title('Suma Acumulativa de la Serie de Números')

# Mostrar el gráfico en pantalla
plt.show()