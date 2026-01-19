import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from datetime import date
import tempfile

# ---------------------------------
# Função para gerar o PDF
# ---------------------------------
def gerar_pdf(texto):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        doc = SimpleDocTemplate(
            tmp.name,
            pagesize=A4,
            rightMargin=40,
            leftMargin=40,
            topMargin=40,
            bottomMargin=40
        )

        styles = getSampleStyleSheet()
        story = []

        for linha in texto.split("\n"):
            if linha.strip() == "":
                story.append(Spacer(1, 14))
            else:
                story.append(Paragraph(linha, styles["Normal"]))
                story.append(Spacer(1, 10))

        doc.build(story)
        return tmp.name

# ---------------------------------
# Configuração da página
# ---------------------------------
st.set_page_config(
    page_title="Declaração PCMSO - PDF",
    layout="centered"
)

st.title("📄 Gerador de Declaração PCMSO")

# ---------------------------------
# Seleção do médico
# ---------------------------------
medico = st.selectbox(
    "Selecione o médico responsável:",
    [
        "Adão Rinede Alves de Almeida",
        "Odilon Batista Soares"
    ]
)

st.divider()

# ---------------------------------
# Dados da empresa
# ---------------------------------
empresa = st.text_input("Nome da empresa")
cnpj = st.text_input("CNPJ")
rua = st.text_input("Rua")
numero = st.text_input("Número")
bairro = st.text_input("Bairro")
cidade_empresa = st.text_input("Cidade da empresa")
estado = st.text_input("Estado")
email = st.text_input("E-mail")

st.divider()

# ---------------------------------
# Responsável legal
# ---------------------------------
responsavel = st.text_input("Nome do responsável legal")
funcao = st.text_input("Função do responsável")

st.divider()

# ---------------------------------
# Local e datas
# ---------------------------------
cidade_assinatura = st.text_input("Cidade da assinatura")

data_inicio_responsabilidade = st.date_input(
    "Data de início da responsabilidade técnica",
    value=date.today()
)

data_assinatura = st.date_input(
    "Data da assinatura",
    value=date.today()
)

st.divider()

# ---------------------------------
# Texto conforme médico
# ---------------------------------
if medico == "Adão Rinede Alves de Almeida":
    medico_texto = (
        "ADÃO RINEDE ALVES DE ALMEIDA, Médico do Trabalho CRM/SC 8899"
    )
    nome_arquivo = "Declaracao_PCMSO_Adao.pdf"
else:
    medico_texto = (
        "ODILON BATISTA SOARES, Médico do Trabalho CREMESC 4195 – RQE 3249"
    )
    nome_arquivo = "Declaracao_PCMSO_Odilon.pdf"

# ---------------------------------
# Geração do PDF
# ---------------------------------
if st.button("📥 Gerar Declaração em PDF"):
    if not all([
        empresa, cnpj, rua, numero, bairro,
        cidade_empresa, estado, email,
        responsavel, funcao, cidade_assinatura
    ]):
        st.error("⚠️ Preencha todos os campos obrigatórios.")
    else:
        texto = f"""
DECLARAÇÃO

{empresa}, {cnpj}, localizada à {rua}, {numero}, {bairro}, {cidade_empresa},
{estado}, E-MAIL {email}, representada por {responsavel}
({funcao}), DECLARO que {medico_texto} é responsável pela coordenação
e responsabilidade técnica do Programa de Controle Médico de Saúde
Ocupacional – PCMSO – desta empresa, com início da responsabilidade
técnica em {data_inicio_responsabilidade.strftime("%d/%m/%Y")}, para fins
de informar ao Conselho Regional de Medicina de Santa Catarina – CREMESC,
em cumprimento à Resolução CFM 2376/2024 art. 3º.

{cidade_assinatura}, {data_assinatura.strftime("%d/%m/%Y")}


_________________________
Responsável (ass. digital)
"""

        caminho_pdf = gerar_pdf(texto)

        with open(caminho_pdf, "rb") as pdf:
            st.download_button(
                label="⬇️ Baixar PDF",
                data=pdf,
                file_name=nome_arquivo,
                mime="application/pdf"
            )

        st.success("✅ Declaração gerada com sucesso!")
