@echo off
echo Gerando testes para soma.py...
python main.py --arquivo langchain-azure-testgen/src/soma.py

echo Gerando testes para divisao.py...
python main.py --arquivo langchain-azure-testgen/src/divisao.py

echo Gerando testes para exemplo.py...
python main.py --arquivo langchain-azure-testgen/src/exemplo.py

echo ✅ Testes gerados com sucesso!
pause
