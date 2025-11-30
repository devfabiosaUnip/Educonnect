import json
import re
import argparse


def carregar_dados(Dados_alunos):
    try:
        with open("alunos.json", 'r', encoding='utf-8') as files:
            return json.load(files)
    except FileNotFoundError:
        print("Erro: arquivo não encontrado.")
        return []
    except json.JSONDecodeError:
        print("Erro: arquivo JSON inválido.")
        return []



def buscar_alunos(alunos, nome=None, matricula=None, curso=None, status=None):
    resultados = []

    for aluno in alunos:
       
        if matricula and aluno['matricula'] != matricula:
            continue


        if nome and not re.search(nome, aluno['nome'], re.IGNORECASE):
            continue

       
        if curso and curso.lower() not in aluno['curso'].lower():
            continue

        
        if status and aluno['status'].lower() != status.lower():
            continue

        resultados.append(aluno)

    return resultados



def exibir_resultados(resultados):
    if not resultados:
        print("Nenhum aluno encontrado com os critérios fornecidos.")
        return

    print(f"\n{len(resultados)} aluno(s) encontrado(s):\n")
    for aluno in resultados:
        print(f"Matrícula: {aluno['matricula']}")
        print(f"Nome: {aluno['nome']}")
        print(f"Curso: {aluno['curso']}")
        print(f"Status: {aluno['status']}")
        print("-" * 40)



def main():
    caminho = "alunos.json"
    alunos = carregar_dados(caminho)

    if not alunos:
        return

    parser = argparse.ArgumentParser(description="Busca avançada de alunos.")
    parser.add_argument('--nome', type=str, help='Buscar por nome do aluno.')
    parser.add_argument('--matricula', type=str, help='Buscar por matrícula do aluno.')
    parser.add_argument('--curso', type=str, help='Buscar por curso do aluno.')
    parser.add_argument('--status', type=str, help='Buscar por status do aluno [ativo/inativo].')

    args = parser.parse_args()

    if any([args.nome, args.matricula, args.curso, args.status]):
        # Modo não interativo (linha de comando)
        print("\n=== BUSCA AVANÇADA DE ALUNOS (LINHA DE COMANDO) ===")
        resultados = buscar_alunos(alunos, args.nome, args.matricula, args.curso, args.status)
        exibir_resultados(resultados)
    else:
        # Modo interativo
        print("\n=== BUSCA AVANÇADA DE ALUNOS (INTERATIVA) ===")
        nome = input("Buscar por nome (pressione Enter para ignorar): ").strip() or None
        matricula = input("Buscar por matrícula (pressione Enter para ignorar): ").strip() or None
        curso = input("Buscar por curso (pressione Enter para ignorar): ").strip() or None
        status = input("Buscar por status [ativo/inativo] (pressione Enter para ignorar): ").strip() or None

        resultados = buscar_alunos(alunos, nome, matricula, curso, status)
        exibir_resultados(resultados)


if __name__ == "__main__":
    main()
