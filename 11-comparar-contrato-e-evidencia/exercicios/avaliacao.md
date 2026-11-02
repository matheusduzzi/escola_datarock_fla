# Exercício autônomo: conferir todas as tentativas

Objetivo: repetir casos e conferir resultado contra fonte, produzindo um conjunto pequeno de avaliação rastreável.

A gerente da Central Exemplo me entregou quatro casos com três respostas preparadas para cada um. Ela quer saber quais respeitam o contrato e a fonte. Você faz essa conferência com o contrato da aula. A tarefa é de consulta; a única ação permitida é `nenhuma`.

1. Leia as fontes e as perguntas em `dados/`.
2. Na pasta do kit, rode `python3 repetir.py > minhas-saidas.json`. Rode novamente para outro arquivo e veja se o conteúdo é igual. Isso reproduz registros preparados, sem modelo.
3. Crie `minha-avaliacao.csv` com caso, tentativa, formato, fato, evidencia, limite, aceito, trecho_da_fonte e justificativa. Anote uma linha por saída. Julgue cada critério separadamente; se o formato for inválido, marque os critérios como falsos e explique que o conteúdo não foi avaliado.
4. Anote no seu relatório o total de tentativas, o total aceito, a fração aceita e os casos cujas tentativas foram todas aceitas. Não descarte erros.
5. Escolha uma falha e proponha uma correção de regra ou de conferência. Defina um caso novo que poderia refutar sua correção. Escreva uma discordância possível com o avaliador, apoiada por trecho, ou diga por que não encontrou uma.
6. Conclua o que esta execução mostra e o que ainda faltaria para avaliar um modelo real. Guarde a versão dos dados e hashes `SHA-256` dos arquivos usados.

Entregue os dois arquivos de respostas reproduzidas, a tabela e o relatório. Você usa os arquivos locais do kit para fazer toda a atividade.

## Dica 1

Abra a fonte indicada na pergunta antes de olhar a citação da resposta. Separe o que foi pedido do que foi citado.

## Dica 2

Monte uma linha por par caso/tentativa. Compare valor, unidade e condição juntos. Depois veja fonte/trecho e ação. Faça a soma só após terminar os julgamentos.

## Critério de correção

A entrega cobre todas as tentativas sem duplicações, aplica os quatro critérios do contrato, apoia julgamentos em trechos e mantém erros no total. Veja se o cálculo concorda com a tabela. O relatório separa reprodução de dados de avaliação real, anota versão/hashes, propõe correção refutável e trata discordâncias de modo explícito. Não há nota de corte de produção nesta atividade.
