# Kit da aula: Preparar acesso e limites

Aqui está o material dessa aula para você rodar. Tudo roda na sua máquina, sem rede e sem credencial, e o modelo é uma função com resposta fixa. Deixe seus segredos fora do kit e dos seus registros.

Você precisa de Python 3.9 ou superior, só com a biblioteca padrão. Eu rodei em Python 3.9.6. Dentro da pasta dessa aula:

```bash
python3 --version
python3 -B demo.py
python3 -B guiada.py
```

Se o seu terminal usa outro nome para o Python, use esse nome depois de olhar a versão. Um ambiente virtual é opcional nessa demo e não isola rede nem arquivos.

A demo lê `dados/config-demo.json` e imprime três linhas: o ambiente e duas decisões. O `guiada.py` escreve os limites no próprio código, com duas tentativas, e imprime duas decisões. Rode depois de responder à pergunta da prática guiada.

O exercício está em `exercicios/preparar-demo.md`. Crie seu código num arquivo separado, com `guiada.py` como modelo, e preencha `checklist.md`. Salve seus registros na sua máquina, sem pedidos, respostas inteiras ou cabeçalhos. Se o resultado sair diferente do que você previu, entregue a diferença explicada.

Arquivos:

- `limites.py`: as guardas;
- `demo.py`: a demonstração da aula;
- `guiada.py`: a prática guiada e o modelo para o seu script;
- `dados/`: a configuração e de onde ela veio.

Os limites, a Central Exemplo e o código foram escritos para a Escola Datarock. Não há dado externo nem aleatoriedade.

Sem acesso autorizado a uma API, continue por aqui. O acesso real pede autorização, orçamento, escopo e um lugar seguro para a credencial antes da aula «Chamada por API».
