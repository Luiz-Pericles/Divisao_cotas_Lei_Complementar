import pandas as pd
import math
import streamlit as st
# Função para classificar os itens conforme as regras


def classificar_itens(df):
    nova_tabela = []

    for index, row in df.iterrows():
        valor_estimado = row['VALOR ESTIMADO']
        quantidade = row['QUANTIDADE']

        if valor_estimado <= 80000:
            row['CLASSIFICAÇÃO'] = 'Exclusivo para ME/EPP'
            nova_tabela.append(row)
        else:
            # Criar item para cota exclusiva ME/EPP
            cota_exclusiva_valor = valor_estimado * 0.25
            if cota_exclusiva_valor > 80000:
                cota_exclusiva_valor = 80000
                # Calcular a quantidade proporcional para a cota exclusiva com base no valor ajustado
                cota_exclusiva_quantidade = (quantidade * cota_exclusiva_valor) / valor_estimado
                # Arrendodar a quantidade para o menor número inteiro
                cota_exclusiva_quantidade = math.floor(cota_exclusiva_quantidade)
                cota_exclusiva_valor = (valor_estimado / quantidade) * cota_exclusiva_quantidade
            else: 
                cota_exclusiva_quantidade = (
                quantidade * cota_exclusiva_valor) / valor_estimado
                cota_exclusiva_quantidade = math.floor(
                    cota_exclusiva_quantidade)
                cota_exclusiva_valor = (
                    valor_estimado / quantidade) * cota_exclusiva_quantidade

            item_cota_exclusiva = row.copy()
            item_cota_exclusiva['VALOR ESTIMADO'] = cota_exclusiva_valor
            item_cota_exclusiva['QUANTIDADE'] = round(
                cota_exclusiva_quantidade)
            item_cota_exclusiva['CLASSIFICAÇÃO'] = 'Exclusivo para ME/EPP'
            nova_tabela.append(item_cota_exclusiva)

            # Criar item para ampla concorrência
            cota_ampla_valor = valor_estimado - cota_exclusiva_valor
            cota_ampla_quantidade = quantidade - \
                item_cota_exclusiva['QUANTIDADE']

            item_cota_ampla = row.copy()
            item_cota_ampla['VALOR ESTIMADO'] = cota_ampla_valor
            item_cota_ampla['QUANTIDADE'] = cota_ampla_quantidade
            item_cota_ampla['CLASSIFICAÇÃO'] = 'Ampla concorrência'
            nova_tabela.append(item_cota_ampla)

    return pd.DataFrame(nova_tabela)



