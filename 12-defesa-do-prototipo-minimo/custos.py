"""Aritmética didática. Nunca consulta cobrança ou modelo real."""
from decimal import Decimal


def custo(usos, entrada='0.02', saida='0.08'):
    """Tarifas fictícias em R$/mil. Ausência de usage não significa zero."""
    tarifas = [Decimal(entrada), Decimal(saida)]
    if any(not t.is_finite() or t < 0 for t in tarifas):
        raise ValueError('tarifa inválida')
    ent = sai = 0
    for uso in usos:
        if uso is None:
            return None
        if type(uso) is not dict or set(uso) != {'entrada', 'saida'}:
            raise ValueError('uso inválido')
        if any(type(n) is not int or n < 0 for n in uso.values()):
            raise ValueError('contagem inválida')
        ent += uso['entrada']
        sai += uso['saida']
    return (ent * tarifas[0] + sai * tarifas[1]) / 1000
