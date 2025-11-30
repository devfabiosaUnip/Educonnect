import json                      # LER ARQUIVOS
from collections import Counter  # CONTAR FREQUÊNCIA DE PALAVRAS
import re                        # IGNORAR PONTUAÇÃO E ESPAÇO


# PALAVRAS QUE NÃO SERÃO CONTADAS:
stopwords = ['de', 'da', 'do', 'e', 'a', 'o', 'em', 'para', 'por', 'com','um', 'uma', 'é', 'que', 'na', 'no']


def freq_palavras():
    try:
        # ABRE E LÊ O ARQUIVO DE DISCIPLINAS, PERMITINDO LER CARACTERES ESPECIAIS:
        with open('disciplinas.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

        # SE DER ALGUM ERRO NA HORA DE ABRIR O ARQUIVO:
    except:
        print('Erro ao ler arquivo JSON.')
        return

    # JUNTA TODAS AS DESCRIÇÕES EM UMA STR:
    texto = ''
    for curso in dados:
        texto += curso.get('descricao', '') + ' '

    # DEIXA TUDO MINÚSCULO E SEPARA:
    texto = texto.lower()
    palavras = re.findall(r'\b\w+\b', texto)

    # TIRA AS PALAVRAS LISTADAS EM STOPWORDS
    filtro_palavras = [p for p in palavras if p not in stopwords]

    # CONTA OCORRÊNCIAS:
    contagem = Counter(filtro_palavras)

    # MOSTRA AS 15 MAIS COMUNS
    print('Palavras mais frequentes:\n')
    for palavra, qtd in contagem.most_common(15):
        print(f'{palavra}: {qtd}')


# EXECUTA PROGRAMA:
if __name__ == '__main__':
    freq_palavras()