def process_data(input_string):
    # Separamos el texto de entrada por saltos de linea
    lines = input_string.strip().split('\n')
    if len(lines) < 2:
        return
        
    t = int(lines[0].strip())
    
    # Procesamos cada palabra
    for i in range(1, t + 1):
        if i < len(lines):
            s = lines[i].strip()
            
            even_chars = s[::2]   # Letras en posiciones pares (0, 2, 4...)
            odd_chars = s[1::2]   # Letras en posiciones impares (1, 3, 5...)
            
            print(even_chars + " " + odd_chars)


# --- EJECUCIÓN DIRECTA EN VS CODE ---
if __name__ == '__main__':
    # Modifica este texto entre comillas triples para probar diferentes palabras
    datos_de_prueba = """2
Hacker
Rank"""
    
    print("--- RESULTADO EN CONSOLA ---")
    process_data(datos_de_prueba)