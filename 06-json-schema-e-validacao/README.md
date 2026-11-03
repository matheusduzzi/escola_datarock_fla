# Kit do aluno: JSON Schema e validação

Eu preparei respostas para testar a validação. Você roda a prática no computador, sem chamar um modelo. O gerador recria os mesmos casos a cada execução.

Você precisa saber programar em Python, criar funções e ler objetos JSON. Se precisar, volte aos cursos Primeiros passos em dados e Python para dados. A prática foi testada em Python 3.9.6 com jsonschema 4.25.1. Para continuar usando o código, escolha uma versão de Python com suporte e teste novamente a compatibilidade.

Na pasta dessa aula no kit do curso, prepare o ambiente e rode:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -B dados/gerar.py
.venv/bin/python -B validacao.py
```

No Windows, use o executável correspondente em `.venv/Scripts/`. A instalação precisa de acesso ao índice de pacotes. Depois disso, a prática roda sem rede.

`schema-demo.json` traz as regras da demonstração e `validacao.py` é o exemplo resolvido. `dados/respostas.json` tem os textos para testar, sem dizer quais passam. Use `dados/politica.json` para comparar o prazo aceito com o prazo da política.

Siga `exercicio.md`. Crie `resposta.py` e `relato.md`, ative o ambiente e rode `python -B -m unittest discover -s tests -v`. Antes de criar a resposta, o comando falha porque falta esse arquivo. Depois, ele precisa rodar os testes e terminar com `OK`. Os testes não contêm gabarito.

Esse kit traz os arquivos do aluno. A solução do instrutor fica separada. O material foi criado para a Escola Datarock; as condições de uso estão no README principal. Cada dependência mantém sua licença própria (jsonschema: MIT), incluindo os outros pacotes que ela usa. Os dados foram criados para o curso.
