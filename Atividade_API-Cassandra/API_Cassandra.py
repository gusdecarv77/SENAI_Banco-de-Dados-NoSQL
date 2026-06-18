import requests
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Cole as suas credenciais aqui
ASTRA_DB_ID = "011475e8-2c3b-42bc-9728-62ccb8ebd5b2"
ASTRA_DB_REGION = "us-east-2" 
ASTRA_TOKEN = "SUA_CHAVE_ASTRA_AQUI"
KEYSPACE = "default_keyspace"
TABLE = "leituras_sensor"

# 2. Monta a URL da API REST nativa do Astra DB (Stargate)
url = f"https://{ASTRA_DB_ID}-{ASTRA_DB_REGION}.apps.astra.datastax.com/api/rest/v2/keyspaces/{KEYSPACE}/{TABLE}/rows"

headers = {
    "X-Cassandra-Token": ASTRA_TOKEN,
    "Accept": "application/json"
}

print("Conectando à API do Cassandra (Astra DB)...\n")

# 3. Faz a requisição HTTP GET
response = requests.get(url, headers=headers)

if response.status_code == 200:
    dados = response.json()
    print("✅ Conexão bem-sucedida! Leituras recuperadas da nuvem:\n")
    
    for leitura in dados.get("data", []):
        sensor = leitura.get("sensor_id")
        data_leitura = leitura.get("data_leitura")
        temp = leitura.get("temperatura")
        status = leitura.get("status")
        
        print(f"Data: {data_leitura} | Sensor: {sensor} | Temp: {temp}°C | Status: {status}")
else:
    print(f"❌ Falha na conexão. Erro {response.status_code}: {response.text}")