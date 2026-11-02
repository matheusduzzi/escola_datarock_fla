# Dados da consulta

`pedidos.json` tem dois registros: 1042 e 1043, com seus status. O código permite consultar 9999, mas esse pedido não está na base. O pedido 2088 fica fora da lista permitida.

`casos.json` contém seis listas fixas de respostas. Cada chamada de ferramenta tem seu próprio id. O caso `repeticao` traz quatro propostas para testar se o limite três impede pedir a última.

Na pasta dessa aula, rode `python3 -B demo.py`. As entradas são fixas, sem sorteio ou consulta à rede, por isso o programa retorna o mesmo JSON.

Para o exercício de estoque, use os códigos de produto e as quantidades do enunciado. Eles são diferentes dos números de pedido usados aqui.
