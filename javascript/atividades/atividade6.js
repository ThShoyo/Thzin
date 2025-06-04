const readlineSync = require('readline-sync');

const dia = parseInt(readlineSync.question('Escolha umn dia entre1 - 7: '))

switch (dia){ 
    case 1: 
        console.log (`Dia ${dia} é um domingo.`)
    break
    case 2: 
        console.log (`Dia ${dia} é uma segunda.`)
    case 3: 
        console.log(`Dia ${dia} é uma terça`) 
    case 4: 
        console.log (`Dia ${dia} é uma quarta`) 
    case 5: 
        console.log(`Dia ${dia} é uma quinta`) 
    case 6: 
        console.log (`Dia ${dia} é uma sexta`) 
    case 7: 
        console.log (`Dia ${dia} é uma sábado`) 
    default:
        console.log('Dia inválido.')
    }
