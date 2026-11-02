import sys
from pathlib import Path
import unittest
from unittest.mock import Mock
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from laco import executar, ModeloRoteiro, rodar
from demo import chamada
from custos import custo
from decimal import Decimal


class PrototipoTest(unittest.TestCase):
    def test_resultado_correlacionado(self):
        m=ModeloRoteiro([chamada(),dict(tipo='texto',texto='separando')])
        r=rodar(m)
        self.assertEqual((r['passos'],r['tentativas'],r['execucoes']),(2,1,1))
        self.assertEqual(m.recebidos[1][-1],{'papel':'ferramenta','id':'c1','conteudo':{
            'ok':True,'pedido':{'id_pedido':1042,'status':'separando'}}})

    def test_negados_sem_efeito(self):
        for nome,args in [('cancelar_pedido','{}'),('consultar_pedido','{'),
                          ('consultar_pedido','{"id_pedido":true}'),
                          ('consultar_pedido','{"id_pedido":2088}')]:
            with self.subTest(args=args,nome=nome):
                consulta=Mock()
                self.assertFalse(executar(nome,args,consulta)[1])
                consulta.assert_not_called()

    def test_erro_volta_para_modelo(self):
        m=ModeloRoteiro([chamada(args='{'),dict(tipo='texto',texto='corrigir')])
        rodar(m)
        self.assertEqual(m.recebidos[1][-1]['conteudo']['erro'],'json_invalido')

    def test_teto_inclui_sucessos(self):
        m=ModeloRoteiro([chamada(id=str(i)) for i in range(4)])
        r=rodar(m,3)
        self.assertEqual((r['fim'],r['execucoes']),('limite_de_passos',3))
        self.assertEqual(len(m.recebidos),3)

    def test_falha_ferramenta_sem_detalhe(self):
        r,_=executar('consultar_pedido','{"id_pedido":1042}',Mock(side_effect=TimeoutError('privado')))
        self.assertEqual(r,{'ok':False,'erro':'falha_ferramenta'})

    def test_custo_soma_todas_chamadas(self):
        self.assertEqual(custo([{'entrada':30,'saida':8},{'entrada':50,'saida':10}]),Decimal('0.00304'))
        self.assertEqual(custo([{'entrada':80,'saida':18}])*1000,Decimal('3.04'))

    def test_uso_ausente_desconhecido(self):
        self.assertIsNone(custo([{'entrada':30,'saida':8},None]))
        self.assertEqual(custo([]),Decimal(0))

    def test_rejeita_dado_invalido(self):
        for u in [{'entrada':True,'saida':1},{'entrada':-1,'saida':2},{'entrada':1},{}]:
            with self.assertRaises(ValueError): custo([u])
        for tarifa in ['NaN','Infinity','-1']:
            with self.assertRaises(ValueError): custo([],entrada=tarifa)

    def test_texto_plausivel_nao_prova_fidelidade(self):
        r=rodar(ModeloRoteiro([chamada(),dict(tipo='texto',texto='Pedido entregue.')]))
        self.assertEqual(r['fim'],'resposta')
        self.assertEqual(r['mensagens'][1]['conteudo']['pedido']['status'],'separando')
        self.assertNotEqual(r['mensagens'][-1]['conteudo']['texto'],'Pedido 1042: separando.')

if __name__=='__main__': unittest.main()
