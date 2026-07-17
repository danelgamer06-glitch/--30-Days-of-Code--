const fs = require('fs');

function processData(input) {

    console.log("Datos recibidos en processData:\n", input);
    
    // Ejemplo de cómo procesar las líneas:
    // const lineas = input.trim().split('\n');
    // console.log("Primera línea:", lineas[0]);
}

// Detecta si estás ejecutando el archivo localmente o en la plataforma
if (process.env.USERNAME || process.env.USER || process.env.HOME) {
    // Si estás en local (VS Code), lee el archivo 'input.txt' de forma síncrona
    try {
        const inputLocal = fs.readFileSync('input.txt', 'utf-8');
        processData(inputLocal);
    } catch (err) {
        console.error("Falta el archivo 'input.txt'. Por favor, créalo en la misma carpeta que tu script.");
    }
} else {
    // Si estás en la plataforma, lee la entrada estándar   
    process.stdin.resume();
    process.stdin.setEncoding("ascii");
    let _input = "";
    process.stdin.on("data", function (input) {
        _input += input;
    });

    process.stdin.on("end", function () {
       processData(_input);
    });
}