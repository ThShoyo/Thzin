// Criando um vetor.
const listaDeNumeros = [1, 2, 3,4]

console.log('Listando todos os numeros da lista: ')
console.log(listaDeNumeros)

console.log('\nMultiplicando valores por 2: ')
const dobrados = listaDeNumeros.map(n => n * 2)
console.log(dobrados)

console.log('\nFiltrando elementos pares: ')
const pares = listaDeNumeros.filter(n => n % 2 === 0)
console.log(pares)

console.log('\nSomando todos os numeros da lista: ')
const soma  = listaDeNumeros.reduce((soma, total) => soma + total, 0)
console.log(soma)
