# Exercício: contrato de triagem

Você vai validar saídas e rejeitar formatos ou valores inválidos. A resposta precisa dizer se o erro está na leitura ou no schema.

A responsável pela Central Exemplo me pediu para checar as sugestões de triagem antes de encaminhar os chamados. Você programa em Python um validador que recebe essa sugestão como texto. O trabalho termina na checagem; o programa não encaminha o chamado.

Na pasta dessa aula no kit do curso, crie `resposta.py` com `SCHEMA` e `validar(texto)`. Use estas regras:

- O objeto tem exatamente `categoria`, `prioridade` e `resumo`, todos obrigatórios.
- `categoria` é texto e aceita só `duvida`, `defeito` ou `troca`.
- `prioridade` é inteiro entre 1 e 3, inclusive. Texto numérico e booleano são inválidos. Um número como `2.0` é inteiro segundo JSON Schema.
- `resumo` é texto com comprimento entre 1 e 120 caracteres, inclusive. A regra mede comprimento, não qualidade; espaços podem passar e exigem revisão humana.
- Mantenha os tipos e os campos como chegaram. Se a saída quebra uma regra, rejeite sem tentar consertá-la.
- Use o dialeto 2020-12. Valide o próprio schema antes de testar os casos.
- Reutilize `ler_json` da demonstração para fazer a leitura estrita. Se usar a função `validar` como ponto de partida, adapte-a ao novo contrato.
- Sucesso: `{"ok": True, "etapa": "schema", "dado": objeto}`. Rejeição de leitura: `{"ok": False, "etapa": "leitura"}`. Rejeição de contrato: `{"ok": False, "etapa": "schema"}`. Campos adicionais de diagnóstico são permitidos no retorno da função.

Entregue também `relato.md`. Faça uma tabela com a entrada, a decisão, a etapa e o motivo. Inclua resposta boa, JSON quebrado, campo faltando, campo extra, tipo errado, enum inválido, limites e resumo vazio. Acrescente um caso que passa pelo schema e exige revisão humana. Diga por que testar esses textos preparados não mede a qualidade de um modelo real.

Com o ambiente ativado, rode `python -B -m unittest discover -s tests -v` na pasta dessa aula no kit. Os testes públicos checam o contrato, sem trazer uma implementação. Acrescente seus casos de fronteira e copie a saída real no relato.

Seu validador precisa aceitar o objeto válido e os valores nos limites, rejeitar cada erro e indicar a etapa correta. O dado aceito fica como chegou. As entradas previstas precisam de um retorno, sem derrubar o programa com um erro não tratado. No relato, diga o que o schema deixa passar mesmo com o conteúdo errado.

<details><summary>Dica 1: separar as duas perguntas</summary>

O texto pode ser lido como JSON? Só depois veja se os campos seguem o contrato. Compare um `2` com um `"2"` sem transformá-los.

</details>

<details><summary>Dica 2: declarar as restrições</summary>

Combine `type`, `properties`, `required` e `additionalProperties` no objeto. Em cada campo, escolha a regra que cabe: `enum`, `minimum`, `maximum`, `minLength` e `maxLength`. Com `iter_errors`, você detecta os erros sem depender da mensagem em inglês.

</details>
