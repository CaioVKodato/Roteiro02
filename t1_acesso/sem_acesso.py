import json
import os
import requests

def ler_configuracao(origem: str):
    if origem == "local":
        base = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(base, "config.json")) as f:
            return json.load(f)
    elif origem == "http":
        resp = requests.get("http://config-srv/config")
        return resp.json()
    elif origem == "s3":
        raise NotImplementedError("S3 não configurado neste lab")

try:
    cfg = ler_configuracao("local")
    print("Configuração carregada:", cfg)
except FileNotFoundError:
    print("config.json não encontrado — crie um para testar")