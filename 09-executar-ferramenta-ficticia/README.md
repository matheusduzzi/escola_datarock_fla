# Kit do aluno: Executar ferramenta fictícia

Use Python 3.9 ou superior. O kit usa só a biblioteca padrão e roda sem instalação adicional, rede, conta ou chave.

Abra a pasta dessa aula no kit do curso, onde estão `demo.py` e `laco.py`. Rode:

```sh
python3 -B demo.py
```

O programa mostra seis casos de consulta de pedidos e as mensagens recebidas antes de cada resposta. `laco.py` contém o loop e a função de consulta. Os arquivos em `dados/` mantêm as entradas iguais a cada execução.

Depois, leia `exercicios/estoque.md`, crie sua função em `resposta.py` e teste:

```sh
python3 -B conferir_resposta.py resposta.py
```

Esse segundo comando só funciona depois de você criar `resposta.py`. Se os exemplos passam, a saída é:

```text
Contrato público: zero, tipo inválido, nome proibido e teto conferidos.
```

Um `AssertionError` indica que algum retorno ficou diferente do esperado. Leia a asserção e compare com seu resultado. O verificador testa exemplos das regras; escreva também seu próprio teste.

Se precisar de ajuda, deixe um comentário na aula da Hotmart. Conte o objetivo, o comando, a saída e o que já tentou, sem dados pessoais.
