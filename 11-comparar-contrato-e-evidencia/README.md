# Kit do aluno: comparar contrato e evidência

Eu reúno aqui os casos, as políticas e as respostas da Central Exemplo. As respostas foram preparadas manualmente e mantêm a mesma ordem. Você usa a versão `replay_sintetico_v1` para repetir a conferência.

Use Python 3.9 ou superior com a biblioteca padrão. Eu testei com 3.9.6. Você roda tudo localmente, sem instalar pacotes. Extraia o arquivo do kit e abra seu terminal na pasta extraída.

```sh
python3 guiada.py
python3 repetir.py > minhas-saidas.json
python3 repetir.py > minhas-saidas-2.json
```

Compare os dois arquivos e siga `exercicios/avaliacao.md`. Consulte `dados/fontes.json`, `dados/casos.json` e `dados/saidas.json`. `guiada.py` contém a resposta do exemplo resolvido G1; ele é independente da tarefa autônoma. `repetir.py` só lê e mostra as saídas, sem corrigi-las.

Para anotar os hashes, use `shasum -a 256 dados/*.json` no macOS ou `sha256sum dados/*.json` no Linux. Guarde os resultados no seu relatório. No Windows, use `Get-FileHash dados/*.json -Algorithm SHA256` no PowerShell.

O kit reúne este README, os dois programas, os dados e o enunciado. Use esses arquivos para montar sua avaliação. Os materiais foram criados para o curso.
