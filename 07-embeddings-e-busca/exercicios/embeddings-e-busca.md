# Exercício: unidade errada, assunto certo

Objetivo: explicar representação e separar similaridade, relevância e prova da resposta.

A gerente da Loja Exemplo me pediu outra checagem: “A retirada na unidade Norte exige agendamento pela regra vigente?” O vetor didático da pergunta é `[0, 1]`. Você encontra esses vetores manuais no caso `autonomo` do kit, como na demonstração da aula.

| ID | Vetor manual | Unidade | Estado | Texto |
|---|---|---|---|---|
| S-agenda | [0, 1] | Sul | vigente | Na unidade Sul, a retirada exige agendamento. |
| N-agenda | [0.6, 0.8] | Norte | vigente | Na unidade Norte, a retirada não exige agendamento. |
| N-frete | [1, 0] | Norte | vigente | O frete depende do endereço de entrega. |

Escreva um parecer curto com:

1. Cosseno de cada par consulta/trecho e ordem dos candidatos. Você pode calcular à mão ou usar a função `cosseno` do kit.
2. O erro de escolher o primeiro candidato sem olhar os metadados, citando a condição que falha.
3. Uma resposta provada pela fonte aplicável, com ID, unidade e a negação mantida.
4. Uma explicação de por que os vetores são representações e o score não é confiança factual. Diferencie este cálculo de um teste com embeddings reais.
5. Uma proteção que ajude neste caso e um limite dela. Diga o que fazer se a fonte aplicável estiver faltando.

Critério de correção: cálculo e ordem coerentes; diagnóstico do erro de escopo; resposta fiel à fonte; diferença entre representação e verdade; proteção com limite e o que fazer quando falta prova. São dimensões de avaliação, sem nota de corte automática.

<details><summary>Dica 1</summary>

Leia a unidade da pergunta e a de cada documento antes de aceitar o candidato.

</details>

<details><summary>Dica 2</summary>

Multiplique as coordenadas correspondentes e normalize pelos comprimentos. Depois olhe unidade, estado e texto, incluindo o “não”. Se você filtrar metadados, veja também se o assunto responde à pergunta.

</details>
