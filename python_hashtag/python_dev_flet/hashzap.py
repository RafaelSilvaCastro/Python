# Titulo: Hashzap
# Botao de iniciar
    # popup (janela na frente da tela)
    # Titulo: Bem vndo ao Hashzap 
    #campo de texto -> escreva seu nome no chat
    # botao: entrar no chat
        # sumir com o titulo hashzap 
        # sumir com o botao iniciar chat
        # fechar a janela (popup)
        # carregar o chat
            # as mensagens que ja foram enviadas (chat)
            # campo: digite sua mensagem 
            # botao de enviar
            
# Flet e usado para frontend e backend no python  
# pip install flet         

# importar o flet
import flet as ft 

# função principal do seu aplicativo
def main(pagina):
    # criar todas as funcionalidades
    
    # cria o elemento
    titulo = ft.Text("Hashzap")
    
    tituloJanela = ft.Text("Bem vindo ao Hashzap")
    campoNomeUsuario = ft.TextField(label="Escreva seu nome no chat")
    
    chat= ft.Column()
    
    def enviar_mensagem_tunel(mensagem): # criando a interação entre os usuarios
        textoChat = ft.Text(mensagem)
        chat.controls.append(textoChat)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)
        
    def enviar_mensagem(evento):
        textoMensagem = campoMensagem.value
        nomeUsuario = campoNomeUsuario.value
        mensagem = f"{nomeUsuario}: {textoMensagem}"
        pagina.pubsub.send_all(mensagem) # mandou a mensagem para todo mundo
        campoMensagem.value = ""
        pagina.update()
        
    campoMensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botaoEnviarMensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    linhaMensagem = ft.Row([campoMensagem, botaoEnviarMensagem])
    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botaoIniciar)
        janela.open = False
        pagina.add(chat)
        pagina.add(linhaMensagem)
        mensagem = f"{campoNomeUsuario.value} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()
    
    botaoEntrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    janela = ft.AlertDialog(title=tituloJanela, content=campoNomeUsuario, actions=[botaoEntrar])
    
    def iniciar_chat(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()
        

    botaoIniciar = ft.ElevatedButton("Iniciar Chat", on_click=iniciar_chat)
    
    # adiciona o elemento a imagem
    pagina.add(titulo)
    pagina.add(botaoIniciar)

# rodar o aplicativo
ft.app(main, view=ft.WEB_BROWSER) # mostrar o site em um navegador 