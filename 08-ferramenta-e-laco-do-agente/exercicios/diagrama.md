# Exercício autônomo: quem decide a execução?

A gerente da Loja Exemplo me pediu para mostrar onde o programa barra uma consulta indevida e onde ele para de tentar. Você faz esse desenho e acompanha cada resposta na tabela.

A sessão pode consultar só o pedido 3010. A única ferramenta permitida é `consultar_pedido`. Ela exige exatamente o campo `id_pedido`, inteiro positivo. Cada resposta do modelo gasta um passo, mesmo quando o pedido é negado. Há no máximo uma chamada de ferramenta por passo. O teto é de dois passos, checado antes de obter outra resposta.

Use as respostas programadas, nessa ordem:

```json
[
  {"tipo":"ferramenta","nome":"consultar_pedido","argumentos":{"id_pedido":3011}},
  {"tipo":"ferramenta","nome":"consultar_pedido","argumentos":{"id_pedido":"3010"}},
  {"tipo":"texto","texto":"Consulta concluída."}
]
```

1. Desenhe um diagrama com faixas ou caixas marcadas como modelo, código e ferramenta. Mostre a checagem antes de cada passo, o retorno de erro e a parada pelo teto. Inclua também a saída por resposta textual antecipada e a consulta permitida.
2. Faça uma tabela para cada resposta: foi consumida, é válida, é autorizada, rodou a ferramenta e qual resultado retornou? Para uma resposta não consumida, use “não avaliada”.
3. Anote o motivo de término, quantos passos foram gastos e quantas vezes a ferramenta rodou. Diga por que a frase final programada não prova que houve consulta.
4. Como você checa uma resposta com formato válido que menciona um pedido fora da sessão?

Seu desenho precisa separar as três responsabilidades e mostrar a volta do resultado. Todo pedido passa pela validação e pela autorização antes de chegar à ferramenta. O teto deve impedir a próxima chamada. A tabela precisa seguir as setas e separar uma frase de sucesso de uma operação feita.

<details><summary>Dica 1</summary>

Comece pela checagem do teto. Um inteiro e um número escrito entre aspas têm tipos diferentes.

</details>

<details><summary>Dica 2</summary>

Faça duas perguntas: o argumento tem o formato exigido? A sessão pode acessar o pedido? Depois de cada retorno, volte ao contador antes de ler a próxima resposta.

</details>
