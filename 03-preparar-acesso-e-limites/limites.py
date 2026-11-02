"""Roda sem rede, sem variável de ambiente e sem credencial."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    max_tentativas: int
    max_entrada_chars: int
    max_saida_chars: int
    orcamento_unidades: int
    reserva_unidades: int

    def __post_init__(self):
        campos = vars(self)
        tetos = dict(max_tentativas=2, max_entrada_chars=200,
                     max_saida_chars=80, orcamento_unidades=10, reserva_unidades=10)
        if any(type(v) is not int or not 1 <= v <= tetos[k] for k, v in campos.items()):
            raise ValueError('configuracao_invalida')


class Sessao:
    def __init__(self, config, modelo):
        self.config = config
        self.modelo = modelo
        self.tentativas = 0
        self.reservado = 0

    def executar(self, entrada):
        c = self.config
        estado = None
        if not isinstance(entrada, str) or not entrada.strip() or len(entrada) > c.max_entrada_chars:
            estado = 'entrada_bloqueada'
        elif self.tentativas >= c.max_tentativas:
            estado = 'tentativas_esgotadas'
        elif self.reservado + c.reserva_unidades > c.orcamento_unidades:
            estado = 'orcamento_insuficiente'
        if estado:
            return self.registro(estado)
        # Reserva antes de executar. Falha não devolve reserva nem tentativa.
        self.tentativas += 1
        self.reservado += c.reserva_unidades
        try:
            saida = self.modelo(entrada, c.max_saida_chars)
        except Exception:
            return self.registro('falha_modelo')
        if not isinstance(saida, str) or len(saida) > c.max_saida_chars:
            return self.registro('saida_rejeitada')
        return self.registro('ok', len(saida))

    def registro(self, estado, saida_chars=0):
        # Lista permitida: não serializar entrada, resposta, exceção ou configuração externa.
        return dict(modo='offline', estado=estado, tentativas=self.tentativas,
                    reservado_unidades=self.reservado, saida_chars=saida_chars)


def modelo_fixo(entrada, max_saida_chars):
    return 'Demo pronta.'[:max_saida_chars]
