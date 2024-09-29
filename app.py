
from codigo.classificar_itens import classificar_itens, conferir_entrada_de_dados
import pandas as pd
import streamlit as st
from io import BytesIO


def to_excel(df):
    output = BytesIO()
    # Gerenciar o ExcelWriter com o contexto 'with'
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
        # writer.save() não é necessário aqui
    processed_data = output.getvalue()
    return processed_data
    

def main():
    st.title("Classificação de Itens para ME/EPP e Ampla Concorrência")

    # Upload do arquivo Excel
    uploaded_file = st.file_uploader(
        "Selecione o arquivo Excel", type=["xlsx", "xls"])
    
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        #Confere o titulo das colunas
        if conferir_entrada_de_dados(df):
            # Aplicar a função de classificação
            df_classificado = classificar_itens(df)

        # Mostrar o DataFrame classificado
        st.write(df_classificado)

        # Criar o arquivo Excel em memória e permitir o download
        excel_data = to_excel(df_classificado)

        st.download_button(
            label="Baixar Planilha Classificada",
            data=excel_data,
            file_name="planilha_classificada.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

if __name__ == '__main__':
    main()
