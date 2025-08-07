function gerarBotao() {
    const idadeInput = document.getElementById('idadeInput');
    const idade = parseInt(idadeInput.value);

    if (isNaN(idade) || idade < 0 || idade > 130) {
        resultadoDiv.innerHTML = "<p style='color: red;'>Por favor, insira uma idade válida entre 0 e 130.</p>";
        return;
    }

    let situacaoVoto = "";

    if (idade < 18) && idade < 65){
        situacaoVoto = "Vo.";
    }
} 