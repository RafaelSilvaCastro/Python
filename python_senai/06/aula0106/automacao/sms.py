# from twilio.rest import Client 

# # Configuração das credenciais da conta Twilio
# account_sid = 'ACa05ced2c1d702f21a81c78cf6a056157'
# auth_token = 'ae2305cd5a5f2e4aed74a850d5324abc'

# # Cria um cliente Twilio
# client = Client(account_sid, auth_token)

# # Envio da mensagem 
# message = client.messages.create(
#     body = 'Ola, esta e uma mensagem de teste!',
#     from_ = '+14146261841', # o numero twilio
#     to = '+5511975875234' # o numero de telefone para que quer manda mensagem 
# )

# print(message.sid) # para verificar o sid da mensagem