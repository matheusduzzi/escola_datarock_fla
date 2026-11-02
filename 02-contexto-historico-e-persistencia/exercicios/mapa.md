# Exercício: o fato ficou onde?

Objetivo: separar mensagens, janela de contexto e memória da aplicação por meio de um mapa de pedidos.

A gerente me pediu o mesmo rastreamento para as conversas B e C. Você encontra os estados em `dados/exercicio.json`, no kit do curso. Abra o JSON, olhe os registros e monte seu próprio mapa. O programa da demonstração serve de referência, mas não resolve este exercício.

1. Para B, monte o pedido com instrução i, pergunta b3 e só a última mensagem atual (`limite=1`), sem incluir memória. Liste IDs incluídos, IDs omitidos e registros que continuam no arquivo.
2. Diga quais informações esse pedido prova sobre item e formato. Proponha uma pergunta de confirmação apropriada.
3. Monte uma segunda versão que inclua a memória de B, mantendo o mesmo limite de mensagens. Diga o que o pedido passa a provar e o que continua faltando. Proponha como recuperar só o fato do item com sua origem, sem rodar chamada real.
4. Um colega sugere usar o estado de C para completar o pedido de B. Diga onde está a falha. Indique o resultado esperado da validação de conversa.
5. Entregue `mapa.md` com uma linha por versão: conversa, instrução, mensagens, memória incluída, omitidos, estado persistido e conclusão. Diga por que o limite de mensagens não mede tokens e qual parte persiste após encerrar o processo.

> **Dica 1**
> Separe primeiro o que existe no arquivo do que cada regra permite incluir. A pergunta também ocupa uma posição de mensagem nesse exemplo.

> **Dica 2**
> Olhe o histórico e depois a memória. Antes de incluir um fato, veja a origem dele e o id da conversa.

Critério de correção: mapa fiel às duas regras, conclusão que o pedido prova, proposta rastreável para o fato que falta, isolamento das conversas e diferença entre armazenamento e capacidade. Você resolve por inspeção, com os arquivos do kit, sem chamada de modelo. Não há nota de corte.
