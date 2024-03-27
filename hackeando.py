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