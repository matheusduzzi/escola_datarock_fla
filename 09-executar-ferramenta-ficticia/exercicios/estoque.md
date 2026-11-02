# Exercício autônomo: consultar estoque

A gerente também me pediu a quantidade disponível de dois produtos. Eu já tenho a tabela de estoque; falta ligar essa busca ao loop. Você adapta o executor, valida os argumentos e faz o resultado chegar ao modelo. O teste roda offline, com limite de tentativas.

Abra a pasta dessa aula no kit do curso e crie `resposta.py` com `executar_estoque(nome, texto)`. Leia a entrada com `ler_argumentos` e passe sua função como `executor` de `rodar`. Mantenha `laco.py` como está.

A ferramenta aceita é `consultar_estoque`. Ela recebe uma string JSON com exatamente o campo `sku`, uma string não vazia. O SKU é o código do produto: `CX-01` tem 7 unidades; `CX-02` tem 0. Outros códigos não estão na tabela. Use os tipos e os espaços como chegaram, sem conversão ou remoção automática.

Sua função retorna `(resultado, executou)` conforme estas regras:

| Condição | Resultado | executou |
|---|---|---|
| Nome diferente | `{"ok":false,"erro":"ferramenta_nao_permitida"}` | false |
| JSON inválido, duplicado ou acima do limite de `ler_argumentos` | `{"ok":false,"erro":"json_invalido"}` | false |
| Campos ou tipos inválidos | `{"ok":false,"erro":"argumentos_invalidos"}` | false |
| SKU não encontrado após consulta | `{"ok":false,"erro":"sku_nao_encontrado"}` | true |
| SKU encontrado | `{"ok":true,"sku":codigo,"quantidade":quantidade}` | true |

Para mostrar como sua função se comporta, entregue um teste próprio e um arquivo JSON com o resultado de dois roteiros:

1. Peça `CX-02` e depois uma resposta textual. Veja a mensagem que chegou ao modelo, incluindo a quantidade zero e o id da chamada.
2. Prepare quatro pedidos com `sku` booleano e ids diferentes. Rode com limite três e prove que o quarto ficou sem ser consumido. Diga por que as recusas também gastam passos.

Rode `python3 -B conferir_resposta.py resposta.py` na pasta dessa aula. O verificador testa exemplos dessas regras. Acrescente seus testes para campo extra, JSON malformado, SKU que não existe e retorno recebido. Seu teste precisa falhar se a função retornar sempre quantidade 7, mesmo para `CX-02`.

Para terminar, mostre estes resultados:

- As entradas recusadas antes da busca deixam `executou=False`.
- A consulta de `CX-02` retorna zero, e o resultado chega ao modelo com o id certo.
- A repetição para no limite, sem pedir a quarta resposta.
- Seu teste detecta a quantidade errada.
- Seu relato separa o teste do código local da avaliação de um modelo real.

Use esses itens para revisar sua entrega antes de terminar.

<details><summary>Dica 1</summary>

Comece pela leitura do JSON, depois valide os campos e faça a busca na tabela. Veja em que etapa cada erro aparece. Procurar um produto que não existe é diferente de recusar a entrada antes da busca.

</details>

<details><summary>Dica 2</summary>

Olhe o conjunto de chaves e o tipo exato antes de acessar a tabela. Teste se a chave existe: quantidade zero não significa produto fora da tabela. No loop, examine `modelo.recebidos` e o tamanho dessa lista, além dos contadores.

</details>
