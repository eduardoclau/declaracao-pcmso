import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from datetime import date
import tempfile

# ---------------------------------
# Função para gerar o PDF
# ---------------------------------
def gerar_pdf(texto, nome_arquivo):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        doc = SimpleDocTemplate(tmp.name, pagesize=A4)
        styles = getSampleStyleSheet()
        story = []

        for linha in texto.split("\n"):
            story.append(Paragraph(linha, styles["Normal"]))
            story.append(Spacer(1, 12))

        doc.build(story)
        return tmp.name

# ---------------------------------
# Interface Streamlit
# ---------------------------------
st.set_page_config(page_title="Declaração PCMSO - PDF", layout="centered")
st.title("📄 Gerador de Declaração PCMSO (PDF)")

medico = st.selectbox(
    "Selecione o médico responsável:",
    ["Adão Rinede Alves de Almeida", "Odilon Batista Soares"]
)

st.divider()

empresa = st.text_input("Nome da empresa")
cnpj = st.text_input("CNPJ")
rua = st.text_input("Rua")
numero = st.text_input("Número")
bairro = st.text_input("Bairro")
cidade_empresa = st.text_input("Cidade da empresa")
estado = st.text_input("Estado")
email = st.text_input("E-mail")

st.divider()

responsavel = st.text_input("Nome do responsável legal")
funcao = st.text_input("Função do responsável")
cpf = st.text_input("CPF do responsável")

cidade_assinatura = st.text_input("Cidade da assinatura")
data_assinatura = st.date_input("Data", value=date.today())

# ---------------------------------
# Texto da declaração
# ---------------------------------
if medico == "Adão Rinede Alves de Almeida":
    medico_texto = (
        "ADÃO RINEDE ALVES DE ALMEIDA, Médico do Trabalho CRM/SC 8899"
    )
    arquivo_saida = "Declaracao_PCMSO_Adao.pdf"
else:
    medico_texto = (
        "ODILON BATISTA SOARES, Médico do Trabalho CREMESC 4195 – RQE 3249"
    )
    arquivo_saida = "Declaracao_PCMSO_Odilon.pdf"

# ---------------------------------
# Geração
# ---------------------------------
if st.button("📥 Gerar PDF"):
    texto = f"""
DECLARAÇÃO

{empresa}, {cnpj}, localizada à {rua}, {numero}, {bairro}, {cidade_empresa},
{estado}, E-MAIL {email}, representada por {responsavel},
({funcao} – CPF {cpf}), DECLARO que {medico_texto} é responsável
pela coordenação e responsabilidade técnica do Programa de Controle
Médico de Saúde Ocupacional – PCMSO – desta empresa, para fins de informar
ao Conselho Regional de Medicina de SC – CREMESC, em cumprimento à
Resolução CFM 2376/2024 art. 3º.

{cidade_assinatura}, {data_assinatura.strftime("%d/%m/%Y")}


_________________________
Responsável (ass. digital)
"""

    caminho_pdf = gerar_pdf(texto, arquivo_saida)

    with open(caminho_pdf, "rb") as pdf:
        st.download_button(
            label="⬇️ Baixar PDF",
            data=pdf,
            file_name=arquivo_saida,
            mime="application/pdf"
        )

    st.success("PDF gerado com sucesso!")
