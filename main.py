import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

def obter_previsao(cidade):
    parametros = {
        'q': cidade,
        'appid': API_KEY,
        'units': 'metric', 
        'lang': 'pt_br'      
    }

    try:
        response = requests.get(BASE_URL, params=parametros)
        if response.status_code == 200:
            dados = response.json()
            return dados
        elif response.status_code == 404:
            print("Erro: Cidade não encontrada. Verifique a ortografia.")
            return None
        else:
            print(f"Erro ao acessar a API: Código {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return None
def mostrar_dados(dados):
    """Extrai e exibe as informações relevantes do JSON."""
    if not dados:
        return
    nome_cidade = dados['name']
    pais = dados['sys']['country']
    
    temperatura = dados['main']['temp']
    sensacao_termica = dados['main']['feels_like']
    temp_min = dados['main']['temp_min']
    temp_max = dados['main']['temp_max']
    umidade = dados['main']['humidity']
    
    condicao_principal = dados['weather'][0]['description'].capitalize()
    print("\n" + "="*40)
    print(f"Previsão do Tempo para: {nome_cidade}, {pais}")
    print("="*40)
    print(f"Condição Atual: {condicao_principal}")
    print(f"    Temperatura: {temperatura:.1f}°C")
    print(f"    Sensação Térmica: {sensacao_termica:.1f}°C")
    print(f"    Mínima/Máxima: {temp_min:.1f}°C / {temp_max:.1f}°C")
    print(f"Umidade: {umidade}%")
    print("="*40)
if __name__ == "__main__":
    cidade_input = input("Informe o nome da cidade para a previsão: ")
    if not cidade_input:
        print("Nenhuma cidade informada. Encerrando.")
    else:
        dados_clima = obter_previsao(cidade_input)
        mostrar_dados(dados_clima)