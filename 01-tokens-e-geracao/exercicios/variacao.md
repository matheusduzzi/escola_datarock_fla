# Exercício: explicar uma variação sem prometer verdade

Objetivo: ver a diferença entre token, distribuição de próxima saída e temperatura. O que mostra que você entendeu: explicação com exemplos de variação, apoiada numa conta que dá para repetir.

A gerente da Vento Norte me pede para checar outra mensagem de pedido. Eu uso o mesmo contexto e os candidatos da aula. A distribuição original agora é `[0.5, 0.25, 0.25]`, na ordem ` pronto`, ` atrasado`, ` cancelado`. A ficha do pedido diz que o pedido está cancelado. Você compara as escolhas com essa ficha.

1. Compare T=1 e T=0.5. Calcule as chances e ache a escolha para os mesmos valores `u=0.2` e `u=0.7` em cada temperatura. Você pode usar a função `temperar` do kit. Guarde comando e saída, ou mostre a conta detalhada se não rodar Python.
2. Diga, num parágrafo, por que a mudança de temperatura não divide novamente a entrada em tokens. Use também as peças e os ids do exemplo da aula para mostrar a diferença entre token e palavra.
3. Dê um exemplo de variação com T fixo e outro de escolha mantida entre temperaturas diferentes, usando seus resultados. Diga por que a resposta mais provável ainda pode errar a ficha.
4. Diga até onde essa prova vai: houve chamada de modelo treinado? O cálculo prova qualidade ou determinismo de um serviço real?

Entregue as contas ou a saída do que você rodou, e sua explicação. Eu olho o cálculo, a diferença entre os três conceitos, os exemplos de variação e os limites. Faça sua tentativa antes de consultar a solução.

<details><summary>Dica 1</summary>

Separe representação da entrada e escolha da saída. Veja em qual intervalo acumulado cada valor de sorteio cai.

</details>

<details><summary>Dica 2</summary>

Para T=0.5, eleve cada chance original ao quadrado e divida pela soma dos quadrados. Mantenha a ordem dos candidatos. Depois compare os mesmos valores de sorteio nas duas distribuições.

</details>
