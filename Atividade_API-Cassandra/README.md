# Integração API Cassandra (Astra DB) 🚀

Este diretório contém a implementação da atividade prática de Banco de Dados NoSQL focada no consumo de APIs. O objetivo do projeto é demonstrar a replicação de um modelo de dados de sensores e a posterior extração dessas informações de um banco Apache Cassandra hospedado na nuvem (DataStax Astra DB) utilizando Python.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Bibliotecas:** `requests`
* **Banco de Dados:** DataStax Astra DB (Serverless Apache Cassandra)
* **Integração:** Stargate REST API (v2)

## ⚙️ Como Configurar e Executar

1. **Instale as dependências:**
   O script utiliza apenas a biblioteca padrão de requisições HTTP do Python. Caso não a tenha, instale via terminal:
   ```bash
   pip install requests
