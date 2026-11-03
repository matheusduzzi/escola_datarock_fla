"""Especificação executável pública, sem implementação da resposta."""
import json
import unittest
from resposta import SCHEMA, validar
from jsonschema import Draft202012Validator

class Contrato(unittest.TestCase):
    def test_schema(self):
        self.assertEqual(SCHEMA["$schema"], "https://json-schema.org/draft/2020-12/schema")
        Draft202012Validator.check_schema(SCHEMA)
    def test_aceitas(self):
        for prioridade, resumo in [(1,"a"),(3,"x"*120),(2.0,"Texto fictício")]:
            d = dict(categoria="duvida", prioridade=prioridade, resumo=resumo)
            r = validar(json.dumps(d))
            self.assertIs(r["ok"], True)
            self.assertEqual(r["dado"], d)
    def test_rejeitadas(self):
        base = dict(categoria="defeito", prioridade=2, resumo="Falha fictícia")
        casos = [dict(base, prioridade=x) for x in [True,"2",0,4,1.5,None]]
        casos += [dict(base,categoria="outro"),dict(base,resumo=""),dict(base,resumo="x"*121),dict(base,extra=1),{},[],None]
        for d in casos:
            with self.subTest(d=d):
                r = validar(json.dumps(d))
                self.assertIs(r["ok"], False)
                self.assertEqual(r["etapa"], "schema")
    def test_leitura(self):
        for t in ["{", "{'categoria':'troca'}", "```json\n{}\n```", '{"a":NaN}', '{"a":1,"a":2}', "{} extra"]:
            with self.subTest(t=t):
                r=validar(t)
                self.assertIs(r["ok"], False)
                self.assertEqual(r["etapa"], "leitura")
if __name__ == "__main__": unittest.main()
