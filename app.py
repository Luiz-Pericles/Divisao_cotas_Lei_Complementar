from codigo.separadorcotaslicitacao import SeparadorCotasLicitacao
from codigo.classificar_itens import classificar_itens
import pandas as pd
import streamlit as st




def main():
    st.title("Classificação de Itens para ME/EPP e Ampla Concorrência")

    # Upload do arquivo Excel
    uploaded_file = st.file_uploader(
        "Selecione o arquivo Excel", type=["xlsx", "xls"])
    
    if uploaded_file:


    # Leitura do arquivo Excel
        df = pd.read_excel(uploaded_file)

    # Aplicar a função de classificação
        df_classificado = classificar_itens(df)

    # Download do arquivo processado
        st.write(df_classificado)
        st.download_button(
            label="Baixar Planilha Classificada",
            data=df_classificado.to_excel(index=False, engine='xlsxwriter'),
            file_name="planilha_classificada.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

if __name__ == '__main__':
    main()
