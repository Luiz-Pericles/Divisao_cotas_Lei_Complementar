
from classificar_itens import classificar_itens, conferir_entrada_de_dados, carregar_instrucoes, gerar_planilha_exemplo
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
    st.title("Classificação de Itens para ME/EPP e Ampla Concorrência 3.2")

    # Upload do arquivo Excel
    uploaded_file = st.file_uploader(
        "Selecione o arquivo Excel", type=["xlsx", "xls"])
    
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        if conferir_entrada_de_dados(df):
            df_classificado = classificar_itens(df)
        else:
            print("Entrada de dados invalida")


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

    #Campo como usar no streamlit:
    st.header("Como usar a ferramenta: ")

    # Carregar e exibir o arquivo .txt com as explicações
    instrucoes = carregar_instrucoes('como_usar.txt')  # Certifique-se de que o arquivo .txt está no diretório correto
    st.text(instrucoes)

    # Gerar a planilha de exemplo
    df = gerar_planilha_exemplo()

    # Botão para download da planilha .xlsx
    st.download_button(
        label="Baixar Planilha de Exemplo",
        data=df.to_excel(index=False, engine='openpyxl'),  # Salva o DataFrame em formato Excel
        file_name='planilha_exemplo.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    # Se você quiser exibir a planilha na própria interface
    st.write("Prévia da planilha:")
    st.dataframe(df)


if __name__ == '__main__':
    main()
