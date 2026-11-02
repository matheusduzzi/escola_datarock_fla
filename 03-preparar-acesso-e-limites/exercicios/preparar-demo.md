# Exercício: preparar uma segunda demo

Objetivo: configurar um ambiente de demonstração sem expor credenciais, com checklist e uma rodada com limite.

A coordenadora gostou da primeira demonstração e me pediu uma segunda, com limites mais apertados. Agora é com você.

1. Na pasta dessa aula, crie seu próprio script. Use `guiada.py` como modelo: ele importa `Config`, `Sessao` e `modelo_fixo` de `limites.py`, cria a sessão e chama `s.executar(entrada)`. Deixe `limites.py` como está.
2. Configure até duas tentativas, entrada de até 60 caracteres, saída de até 40 caracteres, orçamento de 8 unidades e reserva de 5 unidades por tentativa.
3. Antes de rodar, diga qual condição decide em cada etapa e quantas chamadas acontecem de verdade.
4. Na mesma sessão, rode nesta ordem: uma entrada com 61 caracteres, uma consulta curta inventada por você e outra consulta curta. Salve só os registros que a sessão retorna. O texto das consultas fica fora do registro compartilhado.
5. Preencha todas as linhas de `checklist.md`. No local do segredo, escreva "não usei". Para o acesso real, escreva "não rodei" e o que falta confirmar.
6. Responda: reiniciar o script libera um novo gasto real? Como você decide se pode seguir para a aula «Chamada por API»?

Entregue seu script, o checklist e os registros.

> **Dica 1**
> Separe a rejeição antes da chamada da falha depois da reserva. Qual das duas mexe nos contadores?

> **Dica 2**
> Acompanhe a soma da reserva acumulada com a reserva da próxima tentativa. Compare essa soma com o orçamento antes de chamar a função. Use o mesmo objeto Sessao nas três entradas.

Critério de correção: os limites pedidos, três decisões coerentes com a ordem das guardas e contadores e reserva explicados. O registro não traz dado sensível, e fica clara a diferença entre rodar sem rede e ter acesso real. Sua resposta precisa mostrar que os contadores zeram de um processo para outro.

Se travar, deixe um comentário na aula com objetivo, comando, saída e o que você já tentou, sem dados pessoais e sem chave.
