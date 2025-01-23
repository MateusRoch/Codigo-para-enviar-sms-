import pandas as pd
from twilio.rest import Client
# Passo a passo de solução

account_sid = " " # Aqui você deve usar o seu codigo sid da plataforma twilio
auth_token = " " # Aqui você deve usar o seu codigo token da plataforma twilio
client = Client(account_sid, auth_token)

# Abrir os arquivos em Excel
lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    if (tabela_vendas["Vendas"]>55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"]>55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"]>55000,"Vendas"].values[0]
        print(f"No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}")
        message = client.messages.create(
            to = "+XXXXXXXXXXX", #Aqui você coloca o seu numero de telefone
            from_ = "+XXXXXXXXXXXX", # Aqui você coloca o seu numero que você pode conseguir na plataforma twilio
            body = f"No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}"
        )
        print(message.sid)
# Para cada arquivo:
# Verificar se algum valor na coluna venda do arquivo é maior que 55.000
# Se for maior que 55.000 -> Enviar um SMS com Nome, o mês e as vendas do vendedor
# Caso não seja maior que 55.000 não fazer nada
