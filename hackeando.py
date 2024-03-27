def read_file(file_path):
  my_file = open(file_path, "r+")
  file_content = my_file.read()
  my_file.close()
  return file_content

def cifrar_texto(input_file_path, output_file_path, n):
    def cifrar_caracter(caracter):
        # Mapeo especial para saltos de línea y guiones
        if caracter == '\n':
            # Ejemplo: Convertir a un caracter especial o mover N posiciones en ASCII
            return chr((ord(caracter) + n) % 128)  # Usamos % 128 para mantenernos en el rango imprimible/modificable
        elif caracter == '-':
            # Ejemplo: Convertir a un caracter especial o mover N posiciones en ASCII
            return chr((ord(caracter) + n) % 128)
        elif caracter.isalpha():  # Chequear si es una letra
            # Determinar si es mayúscula o minúscula para mantener el caso
            base = ord('A') if caracter.isupper() else ord('a')
            # Cifrar manteniendo el caso original
            cifrado = chr((ord(caracter) - base + n) % 26 + base)
            return cifrado
        return caracter  # Retornar el caracter sin cambios si no es una letra ni un caso especial

    with open(input_file_path, 'r', encoding='utf-8') as file:
        texto = file.read()

    texto_cifrado = ''.join(cifrar_caracter(caracter) for caracter in texto)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(texto_cifrado)


# inicio alalisis
        import matplotlib.pyplot as plt
from collections import Counter
import string

# El texto del que queremos contar las frecuencias de las letras
texto = read_file('texto_cifrado.txt')

# Convertir el texto a minúsculas para contar todas las letras igualmente
texto = texto.lower()

# Filtrar el texto para quedarnos solo con las letras del abecedario
letras_filtradas = [caracter for caracter in texto if caracter in string.ascii_lowercase]

# Contar la frecuencia de cada letra usando Counter
frecuencias = Counter(letras_filtradas)

# Ordenar las frecuencias de mayor a menor
frecuencias_ordenadas = frecuencias.most_common()

# Separar las letras y sus frecuencias en dos listas
letras, frecuencias = zip(*frecuencias_ordenadas)

# Dibujar el histograma
plt.figure(figsize=(10, 8))
plt.bar(letras, frecuencias, color='skyblue')
plt.xlabel('Letras')
plt.ylabel('Frecuencia de aparición')
plt.title('Histograma de frecuencias de las letras ordenado de mayor a menor')
plt.show()
# fin analisis


# Hipotesis 1 : la letra que mas se repite en los textos del alfabeto castellano es la "E"
# por lo tanto la letra que mayor frcuencia tenga en el texto encriptado debería representar
# la letra "E"

def orden_abecedario(letra):
  return ord(letra) - ord('A') + 1

# Calcular el número de la letra "E" en el abecedario
orden_e = orden_abecedario('E')
print(f'La letra "E" es la número {orden_e} del abecedario.')

# Calcular el número de la letra "H" en el abecedario
orden_h = orden_abecedario('H')
print(f'La letra "H" es la número {orden_h} del abecedario.')

# Calcular el #shift"
my_shift = abs(orden_h - orden_e)
print(f'El shift para esta encriptacion Cesar es de {my_shift}')