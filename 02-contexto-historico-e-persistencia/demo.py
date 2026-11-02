"""Duas execuções independentes comprovam leitura de arquivo após reinício."""
import argparse
import json
from pathlib import Path
from contexto import montar, salvar, carregar
P = Path(__file__).resolve().parent

def main():
    a=argparse.ArgumentParser()
    a.add_argument("etapa", choices=["iniciar", "retomar"])
    args=a.parse_args()
    saidas=P/"saidas";saidas.mkdir(exist_ok=True)
    arquivo=saidas/"estado.json"
    dados=json.loads((P/"dados/demo.json").read_text())
    if args.etapa == "iniciar":
        estado={"conversa":"A", "historico":[], "memoria":[]}
        c1=montar(estado,"A",dados["u1"],3)
        (saidas/"C1.json").write_text(json.dumps(c1,ensure_ascii=False,indent=2)+"\n")
        estado["historico"]=[dados["u1"],dados["a1"]]
        estado["memoria"]=[{"id":"m1","texto":"Formato preferido: tabela.","origem":"u1","conversa":"A"}]
        salvar(estado,arquivo)
        print("C1 | instrução=i | mensagens=u1 | memória incluída=nenhuma | omitidos=nenhum")
        print("Estado salvo em saidas/estado.json: histórico=u1,a1; memória=m1")
    else:
        estado=carregar(arquivo)
        c2=montar(estado,"A",dados["u2"],3)
        estado["historico"] += [dados["u2"],dados["a2"]]
        salvar(estado,arquivo)
        c3=montar(estado,"A",dados["u3"],1,True)
        for nome,c in [("C2",c2),("C3",c3)]:
            (saidas/(nome+".json")).write_text(json.dumps(c,ensure_ascii=False,indent=2)+"\n")
            print(nome+" | instrução=i | mensagens="+",".join(m["id"] for m in c["mensagens"])+
                  " | memória incluída="+(",".join(m["id"] for m in c["memoria_incluida"]) or "nenhuma")+
                  " | omitidos="+(",".join(m["id"] for m in c["omitidos"]) or "nenhum"))
        print("Arquivo preserva u1,a1,u2,a2 e m1. C3 não inclui o item escolhido.")
if __name__ == "__main__": main()
