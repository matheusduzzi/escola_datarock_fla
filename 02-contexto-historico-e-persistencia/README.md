# Kit local: contexto e persistência

Requer Python 3.9 ou superior; só biblioteca padrão. Sem instalação adicional, conta ou rede.
Você monta pedidos com os registros do kit. O código não chama um modelo.

Nessa pasta:

```sh
python3 -B demo.py iniciar
python3 -B demo.py retomar
```

O primeiro comando cria `saidas/estado.json` e `saidas/C1.json`. O segundo lê o estado e cria C2/C3. Rode nessa ordem. Rodar iniciar novamente reinicia os dados da demonstração. Para repetir do zero, rode os dois comandos outra vez. Retomar sem iniciar falha porque o arquivo está faltando, não por falta de memória do modelo.

Olhe o texto dos pedidos em `saidas/`. Os nomes de campos e papéis servem para acompanhar a montagem. Para usá-los numa API, você precisa adaptar o formato ao contrato dela. O limite conta mensagens selecionadas; não conta tokens. O programa não produz respostas do modelo.

No [exercício](exercicios/mapa.md), você usa `dados/exercicio.json` para montar e entregar seu próprio mapa. O conteúdo é autoral da Escola Datarock. Consulte as condições de uso no README principal.
