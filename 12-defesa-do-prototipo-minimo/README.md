# Kit do aluno: defesa do protótipo mínimo

Eu uso Python 3.9.6 com biblioteca padrão. Você precisa de Python 3.9 ou superior, sem instalar pacotes. Extraia o ZIP e abra um terminal na pasta que contém este README. Os comandos rodam localmente, sem rede ou credenciais:

```sh
python3 demo.py
python3 -m unittest discover -s tests -v
```

Leia `exercicios/defesa.md` e use `dados/revisao.json` no exercício. Crie seus próprios `defesa.md` e teste adicional numa pasta de trabalho. Os testes do kit verificam o mecanismo da consulta. O teste de contradição e o parecer ficam por sua conta.

`laco.py` e `dados/pedidos.json` vêm da aula «Executar ferramenta fictícia». `custos.py`, `demo.py`, os testes e `dados/revisao.json` completam esse kit. O programa retorna respostas fixas, na versão `offline_sintetico_v1`, sem sorteio. São exemplos autorais para estudar o mecanismo.

As tarifas são inventadas para a conta didática. Os contadores vêm do programa, sem medição de uso ou latência de um modelo real. O kit roda o código local e calcula o custo desses valores. Para conectar um modelo e controlar gasto real, você precisa preparar e testar a integração.

O ZIP contém os materiais do aluno. A solução integral e o parecer respondido ficam com o instrutor. Consulte as condições de uso no README principal.
