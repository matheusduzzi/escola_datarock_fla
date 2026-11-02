# Exercício autônomo: defender uma revisão do protótipo

Objetivo: explicar custo, limites e decisão de seguir ao curso Agentes de IA em produção usando código e testes que você consegue repetir.

A gerente me trouxe outra versão da consulta. Agora você recebe `dados/revisao.json` no kit, com contadores e três respostas programadas. A ferramenta encontrou `separando`, mas o texto final afirma `entregue`. O teto didático por caminho é R$ 0,015000. As tarifas são inventadas, em reais por mil tokens, para estudar a conta.

1. Rode a demonstração e os testes do kit. Anote comandos, saídas, versão Python e hashes dos arquivos usados.
2. Calcule o custo das três chamadas e a projeção para mil caminhos idênticos. Compare com o teto por caminho. Refaça a leitura do custo quando faltar o uso da segunda chamada. Diga o que a conta deixa de fora.
3. Programe um teste adicional que detecte a contradição entre fonte e frase. Mostre uma execução que falha com a frase recebida e outra que passa após corrigir a frase. Guarde as duas saídas e mantenha a fonte. Seu teste pode se limitar ao contrato fechado de status desse caso. Conte qual é esse limite.
4. Escreva `defesa.md` com tarefa e permissões, versões/caminhos, resultados normais e de falha, custo, situação da chamada real e decisão fundamentada. Escolha entre corrigir no curso Fundamentos de LLM e agentes, seguir ao curso Agentes de IA em produção para estudo controlado ou propor uma ampliação operacional. Para qualquer escolha, diga o que falta e qual prova você precisa obter em seguida. Faça essa tarefa com os arquivos do kit, sem rodar integração real.

Entregue seu parecer, o código adicional e os registros das execuções, sem credenciais. Você pode reunir também os resultados da validação de JSON, da execução de ferramenta e da comparação entre contrato e fonte. Mantenha as versões e separe os conjuntos.

## Dica 1

Liste todas as chamadas antes de calcular. Compare o status com o retorno da ferramenta, mesmo quando o loop terminou sem erro.

## Dica 2

Use `custos.custo` para a aritmética. Faça uma cópia dos usos e troque só o segundo por `None`. Para o teste, defina uma asserção para o status esperado e rode-a antes e depois da correção da frase.

## Critério de correção

Sua defesa permite repetir a conta completa e trata o uso que falta como desconhecido. Você mostra que o teste detecta a contradição e liga a decisão aos limites encontrados. Verifique correção, rastreabilidade, reprodução, falhas, leitura dos limites e utilidade. A avaliação segue esses critérios, sem nota de corte. A autorização de implantar depende de uma decisão própria. A solução integral fica reservada ao instrutor.
