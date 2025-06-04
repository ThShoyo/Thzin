const vetor = [4, -2, 7, -5, 3];
let negativos = 0;
let somaPositivos = 0;

for (let num of vetor) {
    if (num < 0) {
        negativos++;
    } else if (num > 0) {
        somaPositivos += num;
    }
}

console.log("Quantidade de números negativos:", negativos);
console.log("Soma dos números positivos:", somaPositivos);