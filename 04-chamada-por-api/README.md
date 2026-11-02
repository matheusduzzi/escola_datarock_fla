# Kit: chamada por API

Use Python 3.9 ou superior. Os programas usam só a biblioteca padrão. Abra o terminal na pasta dessa aula e rode:

```sh
python3 gerar_dados.py
python3 inspecionar.py --caso todos --saida saida/registro.jsonl
python3 inspecionar.py --caso incompleta --saida saida/incompleta.jsonl
```

O exercício está em `exercicios/decidir.md`. Crie `minha_decisao.py` com sua função e rode o teste público. O kit traz os casos de teste, sem a implementação da função.

Para comparar duas execuções:

```sh
python3 inspecionar.py --caso todos --saida saida/repetido.jsonl
python3 - <<'PYTHON'
from pathlib import Path
primeiro = Path("saida/registro.jsonl").read_bytes()
repetido = Path("saida/repetido.jsonl").read_bytes()
assert primeiro == repetido, "Os registros diferem"
print("Registros idênticos byte a byte")
PYTHON
```

Você escolhe os caminhos de saída. A comparação checa se os arquivos gerados são iguais.

## Sobre os arquivos

`dados/casos.json` contém respostas preparadas para o curso, com só os campos usados pelo leitor. O gerador usa valores fixos. O nome `modelo-demo-ficticio` é um rótulo local. O código não faz chamadas ao serviço e não foi feito para limpar logs reais. A procedência dos dados está em `dados/LEIA-ME.md`.

Código e dados foram criados para a Escola Datarock, sem conjunto de dados de terceiros. Consulte as condições de uso no README principal. Testar uma API real exige acesso autorizado e limites de gasto próprios, sem promessa de gratuidade.
