process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();    
});

// Reads complete line from STDIN
function readLine() {
    return input_stdin_array[input_currentline++];
}

function main() {
    var i = 4
    var d = 4.0
    var s = "HackerRank "
 
    // 1. Declarar y leer las variables de entrada
    var i2 = parseInt(readLine());
    var d2 = parseFloat(readLine());
    var s2 = readLine();

    // 2. Imprimir la suma de ambos enteros
    console.log(i + i2);

    // 3. Imprimir la suma de los dobles con un decimal
    console.log((d + d2).toFixed(1));

    // 4. Concatenar e imprimir las variables de tipo String
    console.log(s + s2);
}