# Pipeline de RAG Avançado com LangChain e Gemini 🤖

Este diretório contém a implementação de um pipeline de RAG Avançado (Retrieval-Augmented Generation) projetado para mitigar alucinações e otimizar a recuperação de contextos complexos a partir de documentos de texto discursivos.

## 🛠️ Tecnologias e Modelos Utilizados

* **Framework:** LangChain & LangChain Community
* **LLM de Otimização e Geração:** Google Gemini 1.5 Flash (via Google AI Studio)
* **Embeddings Locais:** `sentence-transformers/all-MiniLM-L6-v2` (HuggingFace)
* **Banco Vetorial:** FAISS (In-Memory)
* **Modelo de Re-ranqueamento:** `cross-encoder/ms-marco-MiniLM-L-6-v2` (HuggingFace)

## 🏗️ Arquitetura do Pipeline

O fluxo de processamento foi estruturado em três macroetapas para garantir a máxima relevância das respostas entregues pela LLM:

1. **Pré-Recuperação (Otimização de Consulta):** Utiliza o `MultiQueryRetriever` alimentado pelo Gemini para reescrever a pergunta inicial do usuário sob múltiplas perspectivas semânticas, expandindo o escopo da busca no banco vetorial.
2. **Recuperação Inicial:** O banco vetorial FAISS realiza uma busca por similaridade de cosseno tradicional, recuperando um conjunto inicial amplo de documentos candidatos (*Top K = 15*).
3. **Pós-Recuperação e Re-ranqueamento (Reranking):** Um modelo Cross-Encoder especializado recalcula a aderência semântica profunda entre a pergunta original e cada trecho recuperado. O `ContextualCompressionRetriever` filtra o ruído e comprime o resultado para os 3 trechos mais relevantes (*Top N = 3*), reduzindo custos de contexto e evitando a diluição da atenção da LLM.

## ⚙️ Como Executar

1. Instale os requisitos listados no arquivo de dependências:
   ```bash
   pip install -r requirements.txt
