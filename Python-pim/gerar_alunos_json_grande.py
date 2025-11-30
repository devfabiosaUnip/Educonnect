import json
import random

def gerar_alunos_grandes(num_turmas=5, alunos_por_turma=100):
    alunos_data = []
    cursos = ["Engenharia de Software", "Ciência da Computação", "Design Digital", "Análise e Desenvolvimento de Sistemas", "Redes de Computadores"]
    status_options = ["ativo", "inativo"]

    for i in range(num_turmas):
        turma_id = f"TURMA{i+1}"
        for j in range(alunos_por_turma):
            matricula = f"{random.randint(2020, 2024)}{random.randint(1000, 9999)}"
            nome = f"Aluno {j+1} da {turma_id}"
            curso = random.choice(cursos)
            status = random.choice(status_options)
            
            aluno = {
                "matricula": matricula,
                "nome": nome,
                "curso": curso,
                "status": status,
                "turma-id": turma_id
            }
            alunos_data.append(aluno)
            
    return alunos_data

if __name__ == "__main__":
    big_alunos = gerar_alunos_grandes()
    with open("alunos_grandes.json", 'w', encoding='utf-8') as f:
        json.dump(big_alunos, f, indent=2, ensure_ascii=False)
    print("Arquivo 'alunos_grandes.json' gerado com sucesso com 5 turmas e 100 alunos cada.")
