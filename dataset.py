import math
import csv

# Carrega os dados de um arquivo CSV
def carregar_dados_csv(caminho_arquivo):
    dados = []
    with open(caminho_arquivo, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for linha in reader:
            dados.append({
                'titulo': linha.get('title', ''),
                'descricao': linha.get('description', '')
            })
    return dados

# Converte um texto em um vetor de palavras com frequência
def texto_para_vetor(texto):
    palavras = texto.lower().split()
    vetor = {}
    for palavra in palavras:
        vetor[palavra] = vetor.get(palavra, 0) + 1
    return vetor

# Calcula a similaridade do cosseno entre dois vetores
def similaridade_cosseno(v1, v2):
    intersecao = set(v1.keys()) & set(v2.keys())
    numerador = sum([v1[x] * v2[x] for x in intersecao])
    
    soma1 = sum([v1[x]**2 for x in v1.keys()])
    soma2 = sum([v2[x]**2 for x in v2.keys()])
    denominador = math.sqrt(soma1) * math.sqrt(soma2)

    if not denominador:
        return 0.0
    return float(numerador) / denominador

# Encontra a descrição mais parecida com o título inserido
def encontrar_descricao_similar(dados, entrada_titulo):
    vetor_entrada = texto_para_vetor(entrada_titulo)
    maior_sim = 0
    resultado = None

    for item in dados:
        vetor_desc = texto_para_vetor(item['descricao'])
        sim = similaridade_cosseno(vetor_entrada, vetor_desc)
        if sim > maior_sim:
            maior_sim = sim
            resultado = item
    return resultado

# Caminho do arquivo CSV (já convertido do XLSX)
arquivo = "netflix_dataset.csv"  # Certifique-se de que este arquivo exista na mesma pasta

# Executa o programa
dados = carregar_dados_csv(arquivo)
entrada = input("Digite um título: ")
resultado = encontrar_descricao_similar(dados, entrada)

if resultado:
    print("\nResultado mais parecido com base na descrição:")
    print(f"Título: {resultado['titulo']}")
    print(f"Descrição: {resultado['descricao']}")
else:
    print("Nenhum resultado encontrado.")