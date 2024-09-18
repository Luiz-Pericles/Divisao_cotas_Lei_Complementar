# Ferramenta de Divisão de Itens de Licitação com Base na Lei Complementar nº 123/2006 # 
Este script em Python foi desenvolvido para auxiliar na aplicação das regras do art. 48 da Lei Complementar nº 123, de 14 de dezembro de 2006, que estabelece critérios para a participação de Microempresas (ME) e Empresas de Pequeno Porte (EPP) em licitações públicas.

## Funcionalidades ##
A ferramenta processa uma planilha contendo uma tabela de itens de licitação e divide esses itens conforme as disposições da lei. O resultado é uma nova planilha onde os itens são classificados em duas categorias:

Exclusivo para empresas ME/EPP: Itens destinados exclusivamente para a participação de microempresas e empresas de pequeno porte.
Participação aberta, ampla concorrência: Itens que podem ser disputados por empresas de qualquer porte.
## Objetivo ##
Automatizar a divisão dos itens de licitação, garantindo a correta aplicação das cotas de participação para ME/EPP, de acordo com a legislação vigente, facilitando o trabalho dos gestores e agentes de contratação.

## Requisitos ##
- Python 3.x
- Bibliotecas: pandas, streamlit, openpyxl, xlsxwriter
## Como usar ##
1. Insira a planilha com a tabela de itens no formato suportado (.xlsx).
2. Execute o script para processar a divisão de acordo com as regras do art. 48 da Lei Complementar nº 123/2006.
3. O script gerará uma nova planilha com a classificação dos itens.
