import os
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

# Carregar variáveis de ambiente (se quiser usar para outras configs)
load_dotenv()

# Configurar o modelo local via Ollama
llm = OllamaLLM(model="mistral")
  # ou "gpt-oss:20b", "llama2", etc.

# Caminho do código-fonte
codigo_path = "langchain-azure-testgen/src/exemplo.py"

# Ler o conteúdo do código
with open(codigo_path, "r", encoding="utf-8") as f:
    codigo = f.read()

# Criar o prompt para gerar testes
prompt = PromptTemplate.from_template(
    "Você é um especialista em testes Python. Gere testes unitários usando pytest para o seguinte código:\n\n{codigo}"
)

# Gerar os testes
resposta = llm.invoke(prompt.format(codigo=codigo))

# Salvar os testes gerados
output_path = "langchain-azure-testgen/tests/test_exemplo.py"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(resposta)

print("✅ Testes gerados e salvos em:", output_path)

