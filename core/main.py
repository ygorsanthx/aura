import requests  # 🚀 NOVO: Importa o pacote 'requests'
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# ➡️ ENDPOINT ORIGINAL: Verifica se o core está online
@app.get("/")
def read_root():
    return {"status": "aura core online"}

# 🚀 NOVO ENDPOINT DE TESTE: Usa o requests
@app.get("/test_requests")
def test_requests():
    """Faz uma requisição para o GitHub para testar o requests."""
    try:
        # Faz uma requisição para a API do GitHub (https://api.github.com/users/ygorsanthx)
        response = requests.get("https://api.github.com/users/ygorsanthx")
        
        if response.status_code == 200:
            dados = response.json()
            return {
                "status": "Conexao com GitHub OK",
                "http_status": response.status_code,
                "username_info": dados.get('name', 'N/A')
            }
        else:
             return {
                "status": "Falha na Conexao com GitHub",
                "http_status": response.status_code
            }
            
    except requests.exceptions.RequestException as e:
        return {"status": "Erro de conexao", "detail": str(e)}

# Bloco de execução do servidor (uvicorn)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
