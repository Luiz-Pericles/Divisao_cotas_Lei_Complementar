import pandas as pd
import math


# Função para classificar os itens conforme as regras

def classificar_itens(df):
    nova_tabela = []
    itens_inseridos = set()  # Conjunto para rastrear itens já inseridos

    for index, row in df.iterrows():
        valor_estimado = row['VALOR ESTIMADO']
        quantidade = row['QUANTIDADE']
        
        # Para o caso que o item é menor que 80k, ele apenas vai criar a coluna classificação com a classificação de tudo exclusivo e copia o restante da linha 
        if valor_estimado <= 80000:
            row['CLASSIFICAÇÃO'] = 'Exclusivo para ME/EPP'
            nova_tabela.append(row)
        else:
            # Calculando cota exclusiva
            cota_exclusiva_valor = valor_estimado * 0.25
            cota_exclusiva_quantidade = (quantidade * cota_exclusiva_valor) / valor_estimado
            cota_exclusiva_quantidade = math.floor(cota_exclusiva_quantidade)
            
            if cota_exclusiva_valor > 80000:
                cota_exclusiva_valor = 80000
                cota_exclusiva_quantidade = (quantidade * cota_exclusiva_valor) / valor_estimado
                cota_exclusiva_quantidade = math.floor(cota_exclusiva_quantidade)
            
            cota_exclusiva_valor = (valor_estimado / quantidade) * cota_exclusiva_quantidade
            
            # Criando item cota ampla
            cota_ampla_valor = valor_estimado - cota_exclusiva_valor
            cota_ampla_quantidade = quantidade - cota_exclusiva_quantidade
            item_cota_ampla = row.copy()
            item_cota_ampla['VALOR ESTIMADO'] = cota_ampla_valor
            item_cota_ampla['QUANTIDADE'] = cota_ampla_quantidade
            item_cota_ampla['CLASSIFICAÇÃO'] = 'Ampla concorrência'

            # Evitar duplicação adicionando um identificador único ao conjunto
            identificador_ampla = (item_cota_ampla['N'], 'Ampla concorrência')
            if identificador_ampla not in itens_inseridos:
                nova_tabela.append(item_cota_ampla)
                itens_inseridos.add(identificador_ampla)

            # Criando item cota exclusiva
            if cota_exclusiva_quantidade > 0:
                item_cota_exclusiva = row.copy()
                item_cota_exclusiva['VALOR ESTIMADO'] = cota_exclusiva_valor
                item_cota_exclusiva['QUANTIDADE'] = cota_exclusiva_quantidade
                item_cota_exclusiva['CLASSIFICAÇÃO'] = 'Exclusivo para ME/EPP'
                texto_adicional = " - Respeitando o limite de até 25% em cumprimento à LEI COMPLEMENTAR Nº 123, DE 14 DE DEZEMBRO DE 2006"
                item_cota_exclusiva['DESCRIÇÃO'] += texto_adicional

                # Evitar duplicação adicionando um identificador único ao conjunto
                identificador_exclusivo = (item_cota_exclusiva['N'], 'Exclusivo para ME/EPP')
                if identificador_exclusivo not in itens_inseridos:
                    nova_tabela.append(item_cota_exclusiva)
                    itens_inseridos.add(identificador_exclusivo)

    return pd.DataFrame(nova_tabela)

def conferir_entrada_de_dados(planilha_excel):
    titulo_das_colunas = planilha_excel.columns
    verificacao_nome_das_colunas = [
        'N', 'DESCRIÇÃO', 'UNIDADE FORNECIMENTO', 'QUANTIDADE', 'VALOR ESTIMADO']
    numero_verificador = 0 
    for i in range(0, 5):
        if verificacao_nome_das_colunas[i] == titulo_das_colunas[i]:
            numero_verificador += 1
        else:                
            print(f'Coluna {i+1}º está diferente')
    if numero_verificador != 5:
        raise ValueError("As colunas da planilha estão fora do padrão!")
    else:
        print("Nomes das colunas da planilha verificada!")
        return True


def carregar_instrucoes(arquivo_txt):
    with open(arquivo_txt, 'r', encoding='utf-8') as arquivo:
        instrucoes = arquivo.read()
    return instrucoes 







