import streamlit as st
import requests
import json
import locale

st.image("images/quantum_banner_2.png", caption="Quantum Finance – Inteligência em Crédito")

def get_prediction(payload):
    endpoint = st.secrets["API-ENDPOINT"]
    headers = {
        "Content-Type": "application/json",
        "x-api-key": st.secrets["API-KEY"]
    }

    response = requests.post(endpoint, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        result = response.json()
        #locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        #predicted_value_formatted = locale.format_string("%d", result["prediction"], grouping=True)

        # Mapeamento da saída para classificações nominais
        mapeamento = {'Good': 2, 'Standard': 1, 'Poor': 0}
        label = {v: k for k, v in mapeamento.items()}.get(result["prediction"], "Indefinido")

        st.markdown("### Score estimado para o cliente:")
        st.success(f"Classificação do Crédito: **{label}**")
    else:
        st.error("Erro ao obter a previsão. Verifique os dados ou tente novamente mais tarde.")

# Título e introdução
st.title("💻 Avaliação Financeira Quantum Finance")
st.markdown("""
Este aplicativo utiliza um modelo de machine learning para prever o **credit score do cliente**, 
considerando o perfil financeiro e histórico de crédito do usuário.
O objetivo é fornecer uma estimativa do valor que o cliente pode obter em um financiamento ou empréstimo,
ajudando na tomada de decisões financeiras mais informadas.
""")

st.markdown("## 📋 Preencha os dados abaixo para estimar o credit score:")

# Entradas do usuário
age = st.number_input("Idade do cliente", min_value=18, max_value=99, step=1, help="Idade do comprador no momento da avaliação.")
occupation_value = st.selectbox(
    "Ocupação do cliente",
    [
        "1 - Executivo", "2 - Autônomo", "3 - CLT", "4 - Freelancer", "5 - Empresário",
        "6 - Estudante", "7 - Aposentado", "8 - Servidor Público", "9 - Desempregado",
        "10 - Técnico", "11 - Temporário", "12 - Agricultor", "13 - Doméstico", "14 - Outro"
    ],
    help="Classificação da ocupação de acordo com o sistema de categorias."
)
occupation = int(occupation_value.split(" - ")[0])

income = st.number_input("Renda anual (em R$)", step=1000.0, help="Renda total estimada no ano.")
bank_accounts = st.number_input("Número de contas bancárias", step=1, help="Contas ativas em bancos tradicionais ou digitais.")
credit_cards = st.number_input("Número de cartões de crédito", step=1, help="Incluindo cartões de lojas e bancos.")
interest_rate = st.slider("Taxa média de juros aplicada (%)", 0, 100, 5, help="Média estimada das taxas de empréstimos e financiamentos.")
num_loans = st.number_input("Quantidade de empréstimos ativos", step=1, help="Número de contratos de crédito pessoais ou consignados.")
delay_due = st.number_input("Dias de atraso mais recente", step=1, help="Último atraso registrado no pagamento.")
delayed_payments = st.number_input("Número total de pagamentos atrasados", step=1, help="Inclui todos os atrasos históricos conhecidos.")
credit_inquiries = st.number_input("Consultas recentes ao CPF", step=1, help="Quantidade de solicitações de crédito feitas por instituições.")

credit_mix_value = st.selectbox(
    "Qualidade do mix de crédito",
    ["1 - Pobre", "2 - Médio", "3 - Bom"],
    help="Classificação da variedade de produtos de crédito que o cliente possui."
)
credit_mix = int(credit_mix_value.split(" - ")[0])

outstanding_debt = st.number_input("Dívida total em aberto (R$)", step=100.0, help="Soma de valores não quitados.")
util_ratio = st.slider("Percentual de uso do limite de crédito (%)", 0.0, 100.0, 35.0, help="Quanto da linha de crédito o cliente utiliza.")
history_age = st.number_input("Tempo de histórico de crédito (em meses)", step=1, help="Tempo desde a primeira operação de crédito.")
min_payment = st.radio("O pagamento mínimo tem sido realizado?", ["Sim", "Não"], help="Indica se o usuário evita inadimplência.")
total_emi = st.number_input("Total de parcelas mensais (EMI)", step=50.0, help="Soma dos compromissos mensais em aberto.")
monthly_investment = st.number_input("Valor médio investido por mês (R$)", step=50.0, help="Inclui investimentos em renda fixa, variável etc.")

payment_behaviour_value = st.selectbox(
    "Comportamento de pagamento",
    ["1 - Excelente", "2 - Bom", "3 - Regular", "4 - Ruim", "5 - Muito Ruim"],
    help="Nível de confiabilidade com base no histórico de pagamentos do cliente."
)
payment_behaviour = int(payment_behaviour_value.split(" - ")[0])

monthly_balance = st.number_input("Saldo médio mensal restante (R$)", step=50.0, help="Média estimada do que sobra após os gastos mensais.")

# Conversão dos campos categóricos
min_payment_value = 1 if min_payment == "Sim" else 0

# Payload do modelo
payload = {
    "data": {
        "Age": age,
        "Occupation": occupation,
        "Annual_Income": income,
        "Num_Bank_Accounts": bank_accounts,
        "Num_Credit_Card": credit_cards,
        "Interest_Rate": interest_rate,
        "Num_of_Loan": num_loans,
        "Delay_from_due_date": delay_due,
        "Num_of_Delayed_Payment": delayed_payments,
        "Num_Credit_Inquiries": credit_inquiries,
        "Credit_Mix": credit_mix,
        "Outstanding_Debt": outstanding_debt,
        "Credit_Utilization_Ratio": util_ratio,
        "Credit_History_Age": history_age,
        "Payment_of_Min_Amount": min_payment_value,
        "Total_EMI_per_month": total_emi,
        "Amount_invested_monthly": monthly_investment,
        "Payment_Behaviour": payment_behaviour,
        "Monthly_Balance": monthly_balance
    }
}

if st.button("📊 Estimar o credit score"):
    with st.spinner("Analisando informações e calculando valor estimado..."):
        get_prediction(payload)


st.markdown("""
---
<div style="text-align: center; font-size: 14px;">
    Desenvolvido por <strong>Wagner, Arthur, Gustavo e Eduardo</strong> e equipe Quantum Finance © 2025
</div>
""", unsafe_allow_html=True)
