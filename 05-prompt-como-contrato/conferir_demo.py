"""Candidatos autorais; nenhuma chamada de modelo ou avaliação semântica."""
def estrutura(entrada, saida):
    return (isinstance(saida,dict) and set(saida)=={'id','classe','evidencia','limite'}
        and saida['id']==entrada['id'] and isinstance(saida['id'],str)
        and saida['classe'] in ('cancelamento','acompanhamento','revisao')
        and saida['limite']=='triagem_sem_execucao'
        and ((saida['classe']=='revisao' and saida['evidencia'] is None)
        or (saida['classe']!='revisao' and isinstance(saida['evidencia'],str) and bool(saida['evidencia']))))
def citacao(entrada, saida):
    return saida['evidencia'] is None or saida['evidencia'] in entrada['texto']
def candidato(id,classe,evidencia):
    return dict(id=id,classe=classe,evidencia=evidencia,limite='triagem_sem_execucao')
if __name__=='__main__':
    casos=[('coerente',{'id':'M-A','texto':'Onde está minha compra?'},candidato('M-A','acompanhamento','Onde está minha compra?')),
      ('citacao_inventada',{'id':'M-A','texto':'Onde está minha compra?'},candidato('M-A','acompanhamento','A compra foi enviada.')),
      ('negacao_ignorada',{'id':'M-N','texto':'Não quero cancelar.'},candidato('M-N','cancelamento','Não quero cancelar.'))]
    for nome,entrada,saida in casos:
        print(f"{nome}: estrutura={'aceita' if estrutura(entrada,saida) else 'rejeitada'}; citacao={'aceita' if citacao(entrada,saida) else 'rejeitada'}")
    assert estrutura({'id':'M-B','texto':'Preciso de ajuda.'},candidato('M-B','revisao',None))
    print('Sem modelo: correspondencia semantica exige leitura humana.')
