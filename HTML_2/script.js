function gerarTabuada(){
    // Pegar o valor do input do HTML.
    const numeroInput = documnent.getElementById('numeroInput')
    let numero = parseInt(numeroInput.value)

    // Mostra o resultado onde a tabela deve ser exibida. 
    const resultadoDiv = docunment.getElementById('resultadoTabudada')
    resultadoDiv.innerHTML = ''
    
    // Adiciona um título para tabuada.
    resultadoDiv.innerHTML += `<h2>Tabuada do número ${numero}</h2>`

    // Laço de repetição para gerar a tabuada.
    for (let i = 1; i <= 10; i++) {
        let resultado = numero * i 
        // Adiciona cada linha da tabuada como um parágrafo.
        resultadoDiv.innerHTML += `<p>${numero} x ${i} = ${resultado}</p>`
    }
}

// A função gerarTabuada será executada quando clicar no botão. 
const gerarBotao = document.getElementById('gerarBotao')
gerarBotao.addEventListener('click', gerarTabuada)




