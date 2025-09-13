# Roda todos os testes
test:
    pytest

# Gera testes para todas as funções
gerar-testes:
    python main.py --arquivo langchain-azure-testgen/src/soma.py
    python main.py --arquivo langchain-azure-testgen/src/divisao.py
    python main.py --arquivo langchain-azure-testgen/src/exemplo.py

# Gera testes e roda tudo
all: gerar-testes test
