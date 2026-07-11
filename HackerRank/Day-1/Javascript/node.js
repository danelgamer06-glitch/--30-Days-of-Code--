// Reads complete line from STDIN
function readLine() {
    return input_stdin_array[input_currentline++];
}

function main() {
    var i = 4
    var d = 4.0
    var s = "Bien entrado a 30 días de código! "
 
    // 1. Declarar y leer las variables de entrada
    var entero = parseInt(readLine("Ingresa un número entero: "));
    var decimal = parseFloat(readLine("Ingresa un número decimal: "));
    var cadena_texto = readLine("Ingresa una cadena de texto: ");

    // 2. Imprimir la suma de ambos enteros
    console.log(i + entero);

    // 3. Imprimir la suma de los dobles con un decimal
    console.log((d + decimal).toFixed(1));

    // 4. Concatenar e imprimir las variables de tipo String
    console.log(s + cadena_texto);
}
