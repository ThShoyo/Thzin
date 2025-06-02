const readlineSync = require('readline-sync');

function verificar(a){
    if (a <0){
        console.log(`O número ${a} é negativo.`)
    }
        else{
        console.log(`O número ${a} é positivo.`)
    }
}

let shoyo = verificar(parseINt(readlineSync.question('Digite um numero')))