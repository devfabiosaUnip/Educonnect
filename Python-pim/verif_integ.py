import json                 # PERMITE LER ARQUIVO

# ABRE ARQUIVO:
with open('alunos.json', 'r') as arquivo:
    alunos = json.load(arquivo)

erros = []

# VERIFICA CADA ALUNO E TIPO DE DADO:
for i, aluno in enumerate(alunos):
    if 'nome' not in aluno:
        erros.append(f"Aluno {i+1}: falta nome")
    elif type(aluno['nome']) != str:
        erros.append(f"Aluno {i+1}: não pode conter números.")
    
    if 'matricula' not in aluno:
        erros.append(f"Aluno {i+1}: falta matricula")
    elif type(aluno['matricula']) not in [int, str]:
        erros.append(f"Aluno {i+1}: matricula incorreta, digite apenas números e letras.")
    
    if 'curso' not in aluno:
        erros.append(f"Aluno {i+1}: falta curso")
    elif type(aluno['curso']) != str:
        erros.append(f"Aluno {i+1}: não pode conter números.")

# MOSTRA RESULTADO
if erros:
    for erro in erros:
        print(erro)
else:
    print("dados válidos")