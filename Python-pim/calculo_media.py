import json
import argparse


def calcular_media(lista_alunos):
    soma = 0
    for aluno in lista_alunos:

        soma += aluno["nota"]

    qnt = len(lista_alunos)
    if qnt > 0:
        media = soma / qnt
    else:
        media = 0
    return media


def main():
    parser = argparse.ArgumentParser(description="Calcula a média das notas de uma turma.")
    parser.add_argument('--turma-indice', type=int, help='O índice da turma a ser processada (0-base).', required=True)
    
    args = parser.parse_args()
    turma_para_processar = args.turma_indice

    try:
        with open('notas.json', 'r', encoding='utf-8') as file:
            dados = json.load(file) 
            
        if 0 <= turma_para_processar < len(dados):
            turma_selecionada = dados[turma_para_processar]
            alunos_notas_dicionario = turma_selecionada["alunos_notas"]
            turm_id = turma_selecionada["turm_id"]

            media = calcular_media(alunos_notas_dicionario)

            print(f"ID da Turma: {turm_id}")
            print(f"Média calculada: {media:.2f}")
        else:
            print(f"Erro: Índice de turma {turma_para_processar} fora do intervalo.")

    except FileNotFoundError:
        print("Erro: arquivo 'notas.json' não encontrado.")
    except json.JSONDecodeError:
        print("Erro: arquivo JSON 'notas.json' inválido.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()

