// Solicite 3 nots e calcule a médai. 

// npm isntall readline-sync

const readline = require('readline-sync')

const listaDeNotas = []

for (let i = 1; i <= 3; i++) {
    nota = readline.questionFloat(`Digite a ${i}ª nota: `)
    listaDeNotas.push(nota)
}

console.log('\nSoma das notas: ')
soma = listaDeNotas.reduce((soma, total) => soma +total, 0)
console.log(soma)

console.log('\nQuantidade de notas: ')
quantidadeNotas = listaDeNotas.length
console.log(quantidadeNotas)

console.log('\nMédia: ')
media = soma / quantidadeNotas
console.log(media)

console.log('\nExibindo todas as notas: ')
listaDeNotas.forEach((nota, index) => console.log(`${++index}ª nota: ${nota} `))