import json
import argparse
import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch


def main():
    parser = argparse.ArgumentParser(description="Gera uma lista de chamada em PDF para uma turma específica.")
    parser.add_argument('--turma-id', type=str, help='O ID da turma para a qual gerar a lista de chamada.', required=True)
    args = parser.parse_args()

    turma_alvo = args.turma_id
    try:
        with open('alunos_grandes.json', 'r', encoding='utf-8') as file:
            dados_alunos = json.load(file)
    except FileNotFoundError:
        print("Erro: arquivo 'alunos.json' não encontrado.")
        return
    except json.JSONDecodeError:
        print("Erro: arquivo JSON 'alunos.json' inválido.")
        return

    alunos_da_turma = [aluno for aluno in dados_alunos if aluno.get('turma_id') == turma_alvo]

    if not alunos_da_turma:
        print(f"Nenhum aluno encontrado para a turma {turma_alvo}.")
        return

    # Cria o diretório /pdf se não existir
    pdf_dir = "pdf"
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)

    # Configuração do PDF
    pdf_filename = os.path.join(pdf_dir, f"lista_chamada_{turma_alvo}.pdf")
    doc = SimpleDocTemplate(pdf_filename, pagesize=A4, 
                            leftMargin=0.5*inch, rightMargin=0.5*inch, 
                            topMargin=0.5*inch, bottomMargin=0.5*inch)
    styles = getSampleStyleSheet()

    # Estilo personalizado para UNIP e títulos
    styles.add(ParagraphStyle(name='UnipHeader',
                              parent=styles['h2'],
                              alignment=1,
                              spaceAfter=0.1*inch,
                              textColor=colors.blue)) # Um azul para a UNIP
    styles.add(ParagraphStyle(name='TitleCenter',
                              parent=styles['h1'],
                              alignment=1,
                              spaceAfter=0.2*inch,
                              textColor=colors.black))
    styles.add(ParagraphStyle(name='AlunoNomeRA',
                              parent=styles['Normal'],
                              fontSize=10,
                              leading=12)) # Espaçamento entre linhas

    story = []

    # Cabeçalho da UNIP
    story.append(Paragraph("UNIP - Universidade Paulista", styles['UnipHeader']))
    
    # Título principal
    story.append(Paragraph(f"Lista de Chamada - Turma: {turma_alvo}", styles['TitleCenter']))

    # Dados da tabela - Nova estrutura
    num_dias = 7 # Número de colunas para os dias
    tabela_headers = ["Nome do Aluno - RA"] + [f"Dia {i+1}" for i in range(num_dias)]
    tabela_dados = [tabela_headers]

    for aluno in alunos_da_turma:
        nome_ra = f"{aluno['nome']} - {aluno['matricula']}"
        row_data = [Paragraph(nome_ra, styles['AlunoNomeRA'])] + ["" for _ in range(num_dias)] # Colunas vazias para os dias
        tabela_dados.append(row_data)

    # Cria a tabela
    # Calcula a largura das colunas: 40% para Nome-RA, o resto dividido pelos dias
    col_widths = [4.0*inch] + [(A4[0] - 1.0*inch - 4.0*inch) / num_dias for _ in range(num_dias)]
    tabela = Table(tabela_dados, colWidths=col_widths)

    # Estilo da tabela
    tabela.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.Color(0.1, 0.3, 0.6, alpha=1)), # Azul escuro para cabeçalho (UNIP)
        ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('ALIGN',(0,0),(0,-1),'LEFT'), # Nome/RA alinhado à esquerda
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('BACKGROUND', (0,1), (-1,-1), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.Color(0.5, 0.5, 0.5)), # Bordas cinza
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))

    story.append(tabela)

    try:
        doc.build(story)
        print(f"PDF 'lista_chamada_{turma_alvo}.pdf' gerado com sucesso para a turma {turma_alvo}.")
    except Exception as e:
        print(f"Erro ao gerar PDF: {e}")

if __name__ == '__main__':
    main()