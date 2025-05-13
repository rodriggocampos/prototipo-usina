import requests
import json
from pathlib import Path

def main():
    API_URL = "http://localhost:8000/api/v1/metricas/importar"
    JSON_FILE = Path(__file__).parent.parent / "metrics.json" 
    
    try:
        # Carrega os dados
        with open(JSON_FILE, "r") as f:
            metrics_data = json.load(f)
        
        # Envia para a API
        response = requests.post(API_URL, json=metrics_data)
        
        # Verifica resposta
        if response.status_code == 200:
            print(f"Sucesso! {len(metrics_data)} métricas importadas")
        else:
            print(f"Erro {response.status_code}: {response.text}")
            
    except Exception as e:
        print(f"Erro crítico: {str(e)}")

if __name__ == "__main__":
    main()