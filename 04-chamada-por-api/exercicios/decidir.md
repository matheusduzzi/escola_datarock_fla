# Exercício autônomo: decidir antes de repetir

A gerente da Loja Farol me pediu para separar os erros antes de tentar os pedidos outra vez. Você vai cuidar dos casos `cota`, `limite_taxa` e `json_invalido`, usando os arquivos do kit.

Programe em Python a função `decidir(registro)` em `minha_decisao.py`. Ela recebe um registro do leitor e retorna uma categoria: `revisar_saldo`, `aguardar_com_limite`, `investigar_corpo` ou `revisao_humana`. Mantenha o leitor e os dados como estão.

Entregue o arquivo da função e um `relatorio.md` com uma linha por caso. Em cada linha, coloque:

- Hash do pedido, HTTP e código de erro.
- Uso conhecido ou desconhecido.
- A decisão e o motivo, com os campos que você leu.

Diga por que o mesmo HTTP pode pedir ações diferentes. Gere os registros com o leitor e anote o comando usado. Rode outra vez e compare os arquivos byte a byte. O README do kit traz o comando de comparação. Prompt, texto de resposta e cabeçalhos ficam fora do relatório.

Seu trabalho está pronto quando separa as causas dos dois 429 e detecta o corpo inválido mesmo com HTTP 200. O uso desconhecido continua desconhecido. A função escolhe a ação, sem tentar o pedido de novo. Para códigos que ela não reconhece, retorne `revisao_humana`. As duas execuções precisam gerar registros idênticos.

Depois de criar a função, rode o teste na pasta dessa aula no kit:

```sh
python3 testar_decisao.py \
  --modulo minha_decisao.py
```

Se o arquivo ainda não existir, o teste para antes de chamar a função. Quando os cinco casos passarem, o resumo será `Contrato da decisão: 5 casos passaram. Nenhuma chamada real.` Ele testa suas decisões sobre os arquivos, não a qualidade de um modelo.

<details><summary>Dica 1</summary>

Comece pelo campo `erro`. O número HTTP sozinho não separa os dois casos 429. A decisão também não revela quanto foi usado.

</details>

<details><summary>Dica 2</summary>

Separe as causas de saldo, ritmo e corpo. Deixe a revisão humana para tudo que sua função não reconhece. Monte a tabela depois de gerar os registros, sem copiar o corpo inteiro.

</details>
