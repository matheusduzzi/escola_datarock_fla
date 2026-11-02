# Kit local: embeddings e busca

Eu uso os textos da Loja Exemplo e vetores manuais para conferir o cálculo e a leitura das fontes. Você precisa de Python 3.9 ou superior, só com a biblioteca padrão. O código roda sem rede, conta ou instalação de modelo.

Na pasta do kit:

```sh
python3 -B dados/gerar.py
python3 -B busca.py
```

O primeiro comando recria os dados fixos. O segundo calcula o ranking da demonstração da aula. Abra `exercicios/embeddings-e-busca.md` para a tarefa autônoma e anote seu parecer em um arquivo próprio. A implementação do cálculo é apoio, o julgamento das fontes é sua tarefa.

Você recebe `busca.py`, `dados/gerar.py`, `dados/casos.json`, `dados/LEIA-ME.md` e o enunciado em `exercicios/embeddings-e-busca.md`, além destas instruções.
