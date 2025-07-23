# Bibliotecas utilizadas
import customtkinter as ctk
import tkinter as tk
from PIL import Image
from random import randint
import subprocess
import os
import sys
import ast
import json

# Configuração da tela
janela = ctk.CTk()
janela.title('RPG')
janela.geometry('1300x650')
janela.resizable(width= False, height= False)
janela._set_appearance_mode('dark')
janela.lift()
janela.focus_force()

imagem_FUNDO = Image.open("F:/jogo/Imagens/classes/fundo.png")
imagem_fundo = ctk.CTkImage(light_image=imagem_FUNDO, dark_image=imagem_FUNDO, size=(1300, 650))
label_fundo = ctk.CTkLabel(janela, image=imagem_fundo, text="")
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)


def carregar_arquivo():
    with open(r"F:\jogo\dados personagem.json", "r", encoding='latin-1') as arquivo:
        dados = json.load(arquivo)
        return dados["usuarios"]
    
def salvar_usuarios(lista_usuarios):
    with open(r"F:\jogo\dados personagem.json", "w") as arquivo:
        json.dump({"usuarios": lista_usuarios}, arquivo, indent=4, ensure_ascii=False)

def ir_para_o_jogo():        # Função que mandara ao jogo principal
    
    subprocess.Popen([sys.executable, r'F:\jogo\lobby.py'])
    janela.destroy()



            
dados_pessoais = {"Nome": "",
                 "Idade": "",
                 "Peso": "",
                 "Altura": "",
                 "Genero": "",
                 "Classe": ""
}

dados = {"nome": "",
         "senha": ""}

# Salva os dados póstos pelo jogador
def salvar_dados(dados, dados_pessoais):
    usuarios = carregar_arquivo()
    usuarios.append({"nome": dados["nome"], "senha": dados["senha"], "dados_pessoais": dados_pessoais})
    salvar_usuarios(usuarios)






# Frases de comprimento 
frases = ['Olá, Seja bem vindo',
          'ao seu jogo RPG, ',
          'aqui cada escolha',
          'importa, então',
          'cuidado!!!',
          'Clique na tecla G para iniciar'
         ]

label_texto = ctk.CTkLabel(
    janela,
    text="",
    font=("System", 36),
    bg_color="#120042",
    width=400,  # largura máxima em pixels
    anchor="center",
    justify="left"  # alinhamento do texto
)
label_texto.place(x=0, y=200)

ok = True
frase_index = 0
letra_index = 0
texto_atual = ""

def escrever_letra_por_letra():
    global frase_index, letra_index, texto_atual, ok

    if frase_index >= len(frases):
        ok = True
        return  # acabou as frases

    frase = frases[frase_index]

    if letra_index < len(frase):
        texto_atual += frase[letra_index]
        label_texto.configure(text=texto_atual)
        letra_index += 1
        janela.after(100, escrever_letra_por_letra)
    else:
        frase_index += 1
        letra_index = 0
        texto_atual += "\n"
        janela.after(500, escrever_letra_por_letra)
        
janela.after(1000, escrever_letra_por_letra)

genero_var = tk.StringVar(value="") 

dados_personagem = {'Nome': '',
                    'Idade': '',
                    'Peso': '',
                    'Altura': '',
                    'Genero': ''}



frame_principal = None
classe_jogador= [] # Para gravar a escolha do usuario


# para o usuario escolher como ele quer saber sua classe
def entrar():
    global frame_principal
    global classe_jogador
    if frame_principal:
        frame_principal.destroy()

    frame_principal = ctk.CTkFrame(janela, width=1300, height=650)
    frame_principal.place(x=0, y=0)                             # Cria a nova tela
    linha_canvas = tk.Canvas(frame_principal, width=1300, height=650, bg="#1a1a1a", highlightthickness=0)
    linha_canvas.place(x=0, y=0)
    
    
    def login():
        global frame_principal
        if frame_principal:                     # Tira o que ta na tela
            frame_principal.destroy()

        
        frame_principal = ctk.CTkFrame(janela, width=1300, height=650)
        frame_principal.place(x=0, y=0)                             # Cria a nova tela
        linha_canvas = tk.Canvas(frame_principal, width=1300, height=650, bg="#1a1a1a", highlightthickness=0)
        linha_canvas.place(x=0, y=0)
        
        usuarios = arquivos = carregar_arquivo()

        nome = ctk.CTkEntry(frame_principal,
                            placeholder_text='Usuario',
                            font=('System', 25),
                            width=300,
                            height=60,
                            text_color='light pink',
                            )
        nome.place(x=500, y=150)

        senha = ctk.CTkEntry(frame_principal,
                            placeholder_text='Senha',
                            font=('System', 25),
                            width=300,
                            height=60,
                            text_color='light pink',
                            )
        senha.place(x=500, y=230)

        
        def procurar_usuario():
            usuario_encontrado = False
            for usuario in arquivos:
                if usuario["nome"] == nome.get() and usuario["senha"] == senha.get():
                    usuario_encontrado = True
                    break
            if usuario_encontrado:
                ir_para_o_jogo()
            else:
                tk.messagebox.showwarning("Atensão", "Usuario não encontrado")
        
        ctk.CTkButton(frame_principal,
                      text="Entrar",
                      font=("System", 28),
                      fg_color="#38663c",
                      hover_color="#163f12",
                      command=procurar_usuario
                      ).place(x=1100, y=550)

        ctk.CTkButton(frame_principal,
                      text="<- Voltar",
                      font=("System", 28),
                      fg_color="#38663c",
                      hover_color="#163f12",
                      command=entrar
                      ).place(x=60, y=550)


    def registrar_se():
        global frame_principal
        if frame_principal:                     # Tira o que ta na tela
            frame_principal.destroy()


        frame_principal = ctk.CTkFrame(janela, width=1300, height=650)
        frame_principal.place(x=0, y=0)                             # Cria a nova tela
        linha_canvas = tk.Canvas(frame_principal, width=1300, height=650, bg="#1a1a1a", highlightthickness=0)
        linha_canvas.place(x=0, y=0)
        
        usuarios = arquivos = carregar_arquivo()

        dados["nome"] = ctk.CTkEntry(frame_principal,
                            placeholder_text='Usuario',
                            font=('System', 25),
                            width=300,
                            height=60,
                            text_color='light pink',
                            )
        dados["nome"].place(x=500, y=150)

        dados["senha"] = ctk.CTkEntry(frame_principal,
                            placeholder_text='Senha',
                            font=('System', 25),
                            width=300,
                            height=60,
                            text_color='light pink',
                            )
        dados["senha"].place(x=500, y=230)

        
              
        

        
        def menu_de_escolha():
            global frame_principal
            global classe_jogador, dados
            dados = {"nome": dados["nome"].get(),
                     "senha": dados["senha"].get()}
            if frame_principal:
                frame_principal.destroy()

            
            frame_principal = ctk.CTkFrame(janela, width=1300, height=650)
            frame_principal.place(x=0, y=0)
            imagem_FUNDO = Image.open("F:/jogo/Imagens/classes/fundo_secundario.png")
            imagem_fundo = ctk.CTkImage(light_image=imagem_FUNDO, dark_image=imagem_FUNDO, size=(1300, 650))
            label_fundo = ctk.CTkLabel(janela, image=imagem_fundo, text="")
            label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

            usuarios = carregar_arquivo()


            frame_principal = None
            
            # Caso o usuario escolha selecionar classe

            def Selecionar_classe():
                global frame_principal
                global classe_jogador
                if frame_principal:
                    frame_principal.destroy()

                frame_principal = ctk.CTkFrame(janela, width=1300, height=650)
                frame_principal.place(x=0, y=0)
                linha_canvas = tk.Canvas(frame_principal, width=1300, height=650, bg="#1a1a1a", highlightthickness=0)
                linha_canvas.place(x=0, y=0)

                ctk.CTkLabel(frame_principal,
                            text='Criação do Personagem',
                            font=('System', 30, 'bold'),
                            bg_color='black'
                            ).place(x=25, y=15)

                
                
                


                def selecionar_classe_escolhida(nome_classe):  # Adiciona a classe na memoria
                    classe_jogador.clear()
                    classe_jogador.append(nome_classe)
                    confirmar_classe = tk.messagebox.askyesno("Confirmação", f"Você realmente que a classe {nome_classe}?")
                    if confirmar_classe:
                        continuar()
                    else:
                        Selecionar_classe
                        

                
                # Ver expecificações da classe
                def continuar():
                    global frame_principal
                    global classe_jogador
                    if frame_principal:
                        frame_principal.destroy()


                    frame_principal = ctk.CTkFrame(janela, width=1300, height=650)
                    frame_principal.place(x=0, y=0)
                    linha_canvas = tk.Canvas(frame_principal, width=1300, height=650, bg="#1a1a1a", highlightthickness=0)
                    linha_canvas.place(x=0, y=0)

                    ctk.CTkLabel(frame_principal,
                                text='Criação do Personagem',
                                font=('System', 30, 'bold'),
                                bg_color='black'
                                ).place(x=25, y=15)



                    # Cria outra aba de colocar as informaçoes pessoais do personagem
                    def Dados_Pessoais():
                        global frame_principal
                        if frame_principal:                     # Tira o que ta na tela
                            frame_principal.destroy()


                        frame_principal = ctk.CTkFrame(janela, width=1300, height=650)
                        frame_principal.place(x=0, y=0)                             # Cria a nova tela
                        linha_canvas = tk.Canvas(frame_principal, width=1300, height=650, bg="#1a1a1a", highlightthickness=0)
                        linha_canvas.place(x=0, y=0)


                        # Para só permitir valores numericos no peso e na altura
                        def somente_numeros(valor):
                            valor.replace(',', '.')
                    
                            return valor.replace('.', '').isdigit() or valor == ""

                        validar = janela.register(somente_numeros)   # ve se realmente so tem numeros

                        ctk.CTkLabel(frame_principal, text='Criação do Personagem', font=('System', 30, 'bold'), bg_color='black', ).place(x=25, y=15)

                        # Comfirma novamente a permisão de apenas numeros
                        def formatar_numero(event):
                            valor = event.widget.get().replace(',', '.')
                            event.widget.delete(0, 'end')
                            event.widget.insert(0, valor)

                        ctk.CTkLabel(frame_principal, text='DADOS PESSOAIS', font=('System', 40, 'bold'), bg_color='#1a1a1a', text_color="#830000", width=1300).place(x=0, y=60)


                        # Configuração Dos Dados Pessoais


                        dados_personagem = {'Nome': '',
                                        'Idade': '',
                                        'Peso': '',
                                        'Altura': '',
                                        'Genero': ''}
                        
                        # Pergunta 1

                        dados_personagem['Nome'] = ctk.CTkEntry(frame_principal,
                                                placeholder_text='',
                                                font=('System', 25),
                                                width=300,
                                                height=60,
                                                text_color='light pink',
                                                )
                        dados_personagem['Nome'].place(x=500, y=150)
                        ctk.CTkLabel(frame_principal, text='Nome:', font=('System', 25), text_color= 'light grey', bg_color='#1a1a1a').place(x=415, y=170)

                        # Pergunta 2

                        dados_personagem['Idade'] = ctk.CTkEntry(frame_principal,
                                                placeholder_text='',
                                                font=('System', 25),
                                                width= 300,
                                                height=60,
                                                text_color='light pink',
                                                validate='key',
                                                validatecommand=(validar, '%P')
                                                )
                        dados_personagem['Idade'].place(x=500, y=230)
                        ctk.CTkLabel(frame_principal, text='Idade:', font=('System', 25), text_color= 'light grey', bg_color='#1a1a1a').place(x=419, y=250)

                        # Pergunta 3

                        dados_personagem['Peso'] = ctk.CTkEntry(frame_principal,
                                                placeholder_text='',
                                                font=('System', 25),
                                                width= 300,
                                                height=60,
                                                text_color='light pink',
                                                validate='key',
                                                validatecommand=(validar, '%P')
                                                )
                        dados_personagem['Peso'].place(x=500, y=310)
                        ctk.CTkLabel(frame_principal, text='Peso:', font=('System', 25), text_color= 'light grey', bg_color='#1a1a1a').place(x=425, y=320)

                        # Pergunta 4

                        dados_personagem['Altura'] = ctk.CTkEntry(frame_principal,
                                                    placeholder_text='',
                                                    font=('System', 25),
                                                    width= 300,
                                                    height=60,
                                                    text_color='light pink',
                                                    validate='key',
                                                    validatecommand=(validar, '%P')
                                                    )
                        dados_personagem['Altura'].place(x=500, y=390)
                        ctk.CTkLabel(frame_principal, text='Altura:', font=('System', 25), text_color= 'light grey', bg_color='#1a1a1a').place(x=417, y=400)

                        # Pergunta 5

                        ctk.CTkLabel(frame_principal, text='Genêro:', font=('System', 25), text_color= 'light grey', width=1300, bg_color='#1a1a1a').place(x=0, y=460)
                        genero_var = tk.StringVar(value="")  

                        genero_m = ctk.CTkRadioButton(
                            frame_principal,
                            text="Masculino",
                            variable=genero_var,
                            value="Masculino",
                            text_color='light pink',
                            bg_color='#1a1a1a',
                            font=('System', 25),
                            ).place(x=470, y=505)

                        genero_f = ctk.CTkRadioButton(
                            frame_principal,
                            text="Feminino",
                            variable=genero_var,
                            value="Feminino",
                            text_color='light pink',
                            bg_color='#1a1a1a',
                            font=('System', 25)
                        ).place(x=640, y=505)

                        dados_personagem['Peso'].bind("<FocusOut>", formatar_numero)
                        dados_personagem['Altura'].bind("<FocusOut>", formatar_numero)


                        
                        def verificar_respostas():
                            # Aguarda todas as respostas em no dicioario
                            dados_pessoais = {
                                            'Nome': dados_personagem['Nome'].get(),
                                            'Idade': dados_personagem['Idade'].get(),
                                            'Peso': dados_personagem['Peso'].get(),
                                            'Altura': dados_personagem['Altura'].get(),
                                            'Genero': genero_var.get()
                                        }
                            
                            # Verifica se as respostas dadas são validas
                            if dados_pessoais['Idade'] == '' or dados_pessoais['Altura'] == '' or dados_pessoais['Nome'] == '' or dados_pessoais['Peso'] == '' or dados_pessoais['Genero'] == '':
                                tk.messagebox.showwarning("Atenção", "Preencha todos os campos.")

                            elif int(dados_pessoais['Idade']) <= 15 or int(dados_pessoais['Idade']) >= 100:
                                tk.messagebox.showwarning("Atenção", "Idade invalida: Tente entre 16 a 99.")

                            elif float(dados_pessoais['Peso']) <= 45 or float(dados_pessoais['Peso']) >= 151:
                                tk.messagebox.showwarning("Atenção", "Peso invalido: Tente entre 46 a 150.")

                            elif float(dados_pessoais['Altura']) < 1 or float(dados_pessoais['Altura'])>= 2.6:
                                tk.messagebox.showwarning("Atenção", "Altura invalida: Tente entre 1.00 a 2.50.")
                            
                            else:
                                dados_pessoais["Classe"] = classe_jogador[0]
                                salvar_dados(dados, dados_pessoais)
                                ir_para_o_jogo()     # Se todas as respostas forem validas, o usuario sera direcionado a tela do jogo
                        
                        ctk.CTkButton(frame_principal,
                                    text='Criar',
                                    command=verificar_respostas,
                                    font=('system', 29),                  # Botão que verifica as respostas
                                    fg_color='#850000'
                                    ).place(x=1100, y=570)





                    ctk.CTkButton(frame_principal,
                                text= 'Proximo ->',
                                bg_color='#1a1a1a',
                                corner_radius=20,
                                fg_color='#6a6a6a',
                                font=('system', 24, 'bold'),
                                text_color='light pink',
                                border_color='#7a7a7a',
                                border_width=2,
                                command=Dados_Pessoais
                                ).place(x=1030, y=590)

                    
                    


                    if classe_jogador[0] == 'Arqueiro':
                        ctk.CTkLabel(frame_principal,
                                    text='Arqueiros',
                                    bg_color='#1a1a1a',
                                    font=('system', 50, 'bold'),
                                    text_color="#03364B",
                                    fg_color="#5B99B1",
                                    corner_radius=30,
                                    width=1100,
                                    height=490,
                                    anchor='n'
                                    ).place(x=100, y=80)
                        
                        ctk.CTkLabel(frame_principal,
                                    text=' Dano: ?\n Velocidade: ?\n Defesa: ?\n Vida: ?\n Arma: ?',
                                    justify='left',
                                    bg_color="#182630",
                                    text_color="#1B2230",
                                    fg_color='#5B99B1',
                                    width=1100, height=380,
                                    font=('system', 38),
                                    anchor='nw'
                                    ).place(x=100, y=170)
                    
                        linha_canvas.create_line(650, 150, 650, 570, fill="#1a1a1a", width=2)

                    elif classe_jogador[0] == 'Espadachin':
                        ctk.CTkLabel(frame_principal,
                                    text='Espadachin',
                                    bg_color='#1a1a1a',
                                    font=('system', 50, 'bold'),
                                    text_color="#1C1C1C",
                                    fg_color="#808080",
                                    corner_radius=30,
                                    width=1100,
                                    height=490,
                                    anchor='n'
                                    ).place(x=100, y=80)
                        
                        ctk.CTkLabel(frame_principal,
                                    text=' Dano: ?\n Velocidade: ?\n Defesa: ?\n Vida: ?\n Arma: ?', 
                                    justify='left',
                                    bg_color="#182630",
                                    text_color="#242424",
                                    fg_color='#808080',
                                    width=1100,
                                    height=380,
                                    font=('system', 38),
                                    anchor='nw'
                                    ).place(x=100, y=170)
                        
                        linha_canvas.create_line(650, 150, 650, 570, fill="#1a1a1a", width=1)
                    


                    elif classe_jogador[0] == 'Assassino':
                        ctk.CTkLabel(frame_principal,
                                    text='Assassino',
                                    bg_color='#1a1a1a',
                                    font=('system', 50, 'bold'),
                                    text_color="#440202",
                                    fg_color="#FA8A76",
                                    corner_radius=30,
                                    width=1100,
                                    height=490,
                                    anchor='n'
                                    ).place(x=100, y=80)
                        
                        ctk.CTkLabel(frame_principal,
                                    text=' Dano: ?\n Velocidade: ?\n Defesa: ?\n Vida: ?\n Arma: ?',
                                    justify='left',
                                    bg_color="#182630",
                                    text_color="#520202",
                                    fg_color='#FA8A76',
                                    width=1100,
                                    height=380,
                                    font=('system', 38),
                                    anchor='nw'
                                    ).place(x=100, y=170)
                        
                        linha_canvas.create_line(650, 150, 650, 570, fill="#1a1a1a", width=1)
                    


                    elif classe_jogador[0] == 'Escudeiro':
                        ctk.CTkLabel(frame_principal,
                                    text='Escudeiro',
                                    bg_color='#1a1a1a',
                                    font=('system', 50, 'bold'),
                                    text_color="#360000",
                                    fg_color="#925959",
                                    corner_radius=30,
                                    width=1100,
                                    height=490,
                                    anchor='n'
                                    ).place(x=100, y=80)
                        
                        ctk.CTkLabel(frame_principal,
                                    text=' Dano: ?\n Velocidade: ?\n Defesa: ?\n Vida: ?\n Arma: ?',
                                    justify='left',
                                    bg_color="#182630",
                                    text_color="#471E00",
                                    fg_color='#925959',
                                    width=1100,
                                    height=380,
                                    font=('system', 38),
                                    anchor='nw'
                                    ).place(x=100, y=170)
                        
                        linha_canvas.create_line(650, 150, 650, 570, fill="#1a1a1a", width=1)
                    


                    elif classe_jogador[0] == 'Lanceiro':
                        ctk.CTkLabel(frame_principal,
                                    text='Lanceiro',
                                    bg_color='#1a1a1a',
                                    font=('system', 50, 'bold'),
                                    text_color="#410041",
                                    fg_color="#8A6E92",
                                    corner_radius=30,
                                    width=1100,
                                    height=490,
                                    anchor='n'
                                    ).place(x=100, y=80)
                        
                        ctk.CTkLabel(frame_principal,
                                    text=' Dano: ?\n Velocidade: ?\n Defesa: ?\n Vida: ?\n Arma: ?',
                                    justify='left',
                                    bg_color="#182630",
                                    text_color="#4B004B",
                                    fg_color='#8A6E92',
                                    width=1100, height=380,
                                    font=('system', 38),
                                    anchor='nw'
                                    ).place(x=100, y=170)
                        
                        linha_canvas.create_line(650, 150, 650, 570, fill="#1a1a1a", width=1)
                    


                    elif classe_jogador[0] == 'Batedor':
                        ctk.CTkLabel(frame_principal,
                                    text='Batedor',
                                    bg_color='#1a1a1a',
                                    font=('system', 50, 'bold'),
                                    text_color="#003803",
                                    fg_color="#76C47A",
                                    corner_radius=30,
                                    width=1100,
                                    height=490,
                                    anchor='n'
                                    ).place(x=100, y=80)
                        
                        ctk.CTkLabel(frame_principal,
                                    text=' Dano: ?\n Velocidade: ?\n Defesa: ?\n Vida: ?\n Arma: ?',
                                    justify='left',
                                    bg_color="#182630",
                                    text_color="#005004",
                                    fg_color='#76C47A',
                                    width=1100,
                                    height=380,
                                    font=('system', 38),
                                    anchor='nw'
                                    ).place(x=100, y=170)
                        
                    ctk.CTkLabel(frame_principal,
                                text='',
                                width=1,
                                height=420,
                                fg_color='grey',
                                anchor='n',
                                text_color='grey').place(x=650, y=150)

        
                
                # Botões para excoler sua classe

                imagem_ARQUEIRO = Image.open("F:/jogo/Imagens/classes/arco e flecha.png")
                imagem_arqueiro = ctk.CTkImage(light_image=imagem_ARQUEIRO, dark_image=imagem_ARQUEIRO, size=(260, 260))
                ctk.CTkButton(frame_principal,
                            text= 'Arqueiro\n',
                            anchor='s',
                            bg_color='#1a1a1a',
                            corner_radius=20,
                            fg_color='#5B99B1',
                            font=('system', 38, 'bold'),
                            text_color='#03364B',
                            width=270,
                            height=400,
                            hover_color="#335D6D",
                            image=imagem_arqueiro,
                            compound='top',
                            command=lambda: selecionar_classe_escolhida("Arqueiro")
                            ).place(x=60, y=140)
                
                imagem_ESPADACHIN = Image.open("F:/jogo/Imagens/classes/espada.png")
                imagem_espadachin = ctk.CTkImage(light_image=imagem_ESPADACHIN, dark_image=imagem_ESPADACHIN, size=(260, 260))
                ctk.CTkButton(frame_principal,
                            text= 'Espadachin\n',
                            anchor='s',
                            bg_color='#1a1a1a',
                            corner_radius=20,
                            fg_color='#808080',
                            font=('system', 38, 'bold'),
                            text_color='#1C1C1C',
                            width=270,
                            height=400,
                            image=imagem_espadachin,
                            compound='top',
                            hover_color="#535353",
                            command=lambda: selecionar_classe_escolhida("Espadachin")
                            ).place(x=370, y=140)

                imagem_ASSASSINO = Image.open("F:/jogo/Imagens/classes/faca.png")
                imagem_assassino = ctk.CTkImage(light_image=imagem_ASSASSINO, dark_image=imagem_ASSASSINO, size=(260, 260))
                ctk.CTkButton(frame_principal,
                            text= 'Assassino\n',
                            anchor='s',
                            bg_color='#1a1a1a',
                            corner_radius=20,
                            fg_color='#FA8A76',
                            font=('system', 38, 'bold'),
                            text_color='#440202',
                            width=270,
                            height=400,
                            hover_color="#86483D",
                            image=imagem_assassino,
                            compound='top',
                            command=lambda: selecionar_classe_escolhida("Assassino")
                            ).place(x=680, y=140)
                
                imagem_ESCUDEIRO = Image.open("F:/jogo/Imagens/classes/escudo.png")
                imagem_escudeiro = ctk.CTkImage(light_image=imagem_ESCUDEIRO, dark_image=imagem_ESCUDEIRO, size=(260, 260))
                ctk.CTkButton(frame_principal,
                            text= 'Escudeiro\n',
                            anchor='s',
                            bg_color='#1a1a1a',
                            corner_radius=20,
                            fg_color='#925959',
                            font=('system', 38, 'bold'),
                            text_color='#360000',
                            width=270,
                            height=400,
                            hover_color="#613838",
                            image=imagem_escudeiro,
                            compound='top',
                            command=lambda: selecionar_classe_escolhida("Escudeiro")
                            ).place(x=990, y=140)



                def proxima_tela():   # Segunda tela de classes
                    global frame_principal
                    if frame_principal:
                        frame_principal.destroy()

                    frame_principal = ctk.CTkFrame(janela, width=1300, height=650)
                    frame_principal.place(x=0, y=0)
                    linha_canvas = tk.Canvas(frame_principal, width=1300, height=650, bg="#1a1a1a", highlightthickness=0)
                    linha_canvas.place(x=0, y=0)

                    # Botões das classes

                    imagem_LANCEIRO = Image.open("F:/jogo/Imagens/classes/lanca.png")
                    imagem_lanceiro = ctk.CTkImage(light_image=imagem_LANCEIRO, dark_image=imagem_LANCEIRO, size=(260, 260))
                    ctk.CTkButton(frame_principal,
                                text= 'Lanceiro\n',
                                anchor='s',
                                bg_color='#1a1a1a',
                                corner_radius=20,
                                fg_color='#8A6E92',
                                font=('system', 38, 'bold'),
                                text_color='#410041',
                                width=270,
                                height=400,
                                hover_color="#5F4866",
                                image=imagem_lanceiro,
                                compound='top',
                                command=lambda: selecionar_classe_escolhida("Lanceiro")
                                ).place(x=60, y=140)

                    imagem_BATEDOR = Image.open("F:/jogo/Imagens/classes/besta.png")
                    imagem_batedor = ctk.CTkImage(light_image=imagem_BATEDOR, dark_image=imagem_BATEDOR, size=(260, 260))
                    ctk.CTkButton(frame_principal,
                                text= 'Batedor\n',
                                anchor='s',
                                bg_color='#1a1a1a',
                                corner_radius=20,
                                fg_color='#76C47A',
                                font=('system', 38, 'bold'),
                                text_color='#003803',
                                width=270,
                                height=400,
                                hover_color="#3E7041",
                                image=imagem_batedor,
                                compound='top',
                                command=lambda: selecionar_classe_escolhida("Batedor")
                                ).place(x=370, y=140)


                    # Botões para voltar para a outra tela de classes ou ver as especificações da classe que ela escolheu
                    ctk.CTkButton(frame_principal,
                                text= 'Proximo ->',
                                bg_color='#1a1a1a',
                                corner_radius=20,
                                fg_color='#7a7a7a',
                                font=('system', 24, 'bold'),
                                text_color='#5a5a5a',
                                border_color='#6a6a6a',
                                hover_color="#353535",
                                border_width=2
                                ).place(x=1030, y=590)

                    ctk.CTkButton(frame_principal,
                                text= '<- Voltar',
                                bg_color='#1a1a1a',
                                corner_radius=20,
                                fg_color='#6a6a6a',
                                font=('system', 24, 'bold'),
                                text_color='light pink',
                                border_color='#7a7a7a', 
                                border_width=2,
                                width=140,
                                hover_color="#353535",
                                command=Selecionar_classe
                                ).place(x=100, y=590)


                    
                # Botões para voltar para a do modo de escolher classe, ver as especificações da classe que ela escolheu da primeira tela
                # Ou ir para a proxima tela de classes
                ctk.CTkButton(frame_principal,
                            text= 'Proximo ->',
                            bg_color='#1a1a1a',
                            corner_radius=20,
                            fg_color='#6a6a6a',
                            font=('system', 24, 'bold'),
                            text_color='light pink',
                            border_color='#7a7a7a',
                            border_width=2,
                            hover_color="#353535",
                            command=proxima_tela
                            ).place(x=1030, y=590)

                ctk.CTkButton(frame_principal,
                            text= '<- Voltar',
                            bg_color='#1a1a1a',
                            corner_radius=20,
                            fg_color='#6a6a6a',
                            font=('system', 24, 'bold'),
                            text_color='light pink',
                            border_color='#7a7a7a',
                            border_width=2,
                            width=140,
                            hover_color="#353535",
                            command=menu_de_escolha
                            ).place(x=100, y=590)









            def Criação():
                global frame_principal
                if frame_principal:
                    frame_principal.destroy()

                frame_principal = ctk.CTkFrame(janela, width=1300, height=650)
                frame_principal.place(x=0, y=0)
                linha_canvas = tk.Canvas(frame_principal, width=1300, height=650, bg="#1a1a1a", highlightthickness=0)
                linha_canvas.place(x=0, y=0)

                # Linha vermelha
                linha_canvas.create_line(350, 90, 350, 650, fill="grey", width=2)
                linha_canvas.create_line(700, 90, 700, 650, fill="grey", width=2)
                linha_canvas.create_line(1050, 90, 1050, 650, fill="grey", width=2)

                ctk.CTkButton(frame_principal,
                            text= '<- Voltar',
                            bg_color='#1a1a1a',
                            corner_radius=20,
                            fg_color='#6a6a6a',
                            font=('system', 24, 'bold'),
                            text_color='light pink',
                            border_color='#7a7a7a',
                            border_width=2,
                            width=140,
                            hover_color="#353535",
                            command=menu_de_escolha
                            ).place(x=100, y=580)

                def somente_numeros(valor):
                    valor.replace(',', '.')
            
                    return valor.replace('.', '').isdigit() or valor == ""

                validar = janela.register(somente_numeros)

                ctk.CTkLabel(frame_principal, text='Criação do Personagem', font=('System', 30, 'bold'), bg_color='black', ).place(x=25, y=15)

                def formatar_numero(event):
                    valor = event.widget.get().replace(',', '.')
                    event.widget.delete(0, 'end')
                    event.widget.insert(0, valor)




                # Configuração Dos Dados Pessoais



                ctk.CTkLabel(frame_principal, text='Dados Pessoais', font=('System', 30, 'bold'), text_color= 'red', width=349, bg_color='#1a1a1a').place(x=0, y=100)
                dados_pessoais = {'Nome': '',
                                'Idade': '',
                                'Peso': '',
                                'Altura': '',
                                'Genero': ''}
                
                # Pergunta 1

                dados_pessoais['Nome'] = ctk.CTkEntry(frame_principal,
                                        placeholder_text='',
                                        font=('System', 20),
                                        width=200,
                                        height=40,
                                        text_color='light pink',
                                        )
                dados_pessoais['Nome'].place(x=74, y=200)
                ctk.CTkLabel(frame_principal, text='Nome:', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=30, y=205)

                # Pergunta 2

                dados_pessoais['Idade'] = ctk.CTkEntry(frame_principal,
                                        placeholder_text='Qual será sua idade? (Não adicione , nem .)',
                                        font=('System', 20),
                                        width= 200,
                                        height=40,
                                        text_color='light pink',
                                        validate='key',
                                        validatecommand=(validar, '%P')
                                        )
                dados_pessoais['Idade'].place(x=74, y=260)
                ctk.CTkLabel(frame_principal, text='Idade:', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=30, y=265)

                # Pergunta 3

                dados_pessoais['Peso'] = ctk.CTkEntry(frame_principal,
                                        placeholder_text='Qual será o peso? (Não adicione , nem .)',
                                        font=('System', 20),
                                        width= 200,
                                        height=40,
                                        text_color='light pink',
                                        validate='key',
                                        validatecommand=(validar, '%P')
                                        )
                dados_pessoais['Peso'].place(x=74, y=320)
                ctk.CTkLabel(frame_principal, text='Peso:', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=30, y=325)

                # Pergunta 4

                dados_pessoais['Altura'] = ctk.CTkEntry(frame_principal,
                                            placeholder_text='Qual será sua altura? (Não adicione "," nem ".")',
                                            font=('System', 20),
                                            width= 200,
                                            height=40,
                                            text_color='light pink',
                                            validate='key',
                                            validatecommand=(validar, '%P')
                                            )
                dados_pessoais['Altura'].place(x=74, y=390)
                ctk.CTkLabel(frame_principal, text='Altura:', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=30, y=395)

                # Pergunta 5

                ctk.CTkLabel(frame_principal, text='Genêro:', font=('System', 20), text_color= 'light grey', width=349, bg_color='#1a1a1a').place(x=0, y=455)
                genero_var = tk.StringVar(value="")  

                genero_m = ctk.CTkRadioButton(
                    frame_principal,
                    text="Masculino",
                    variable=genero_var,
                    value="Masculino",
                    text_color='light pink',
                    text_color_disabled='light grey',
                    bg_color='#1a1a1a',
                    font=('System', 18),
                    ).place(x=50, y=490)

                genero_f = ctk.CTkRadioButton(
                    frame_principal,
                    text="Feminino",
                    variable=genero_var,
                    value="Feminino",
                    text_color='light pink',
                    bg_color='#1a1a1a',
                    font=('System', 18)
                ).place(x=200, y=490)

                dados_pessoais['Peso'].bind("<FocusOut>", formatar_numero)
                dados_pessoais['Altura'].bind("<FocusOut>", formatar_numero)

                # Salvando os resultados em uma variavel
                
                dados_pessoais = {'Nome': dados_pessoais['Nome'],
                                'Idade': dados_pessoais['Idade'],
                                'Peso': dados_pessoais['Peso'],            # Quando for usar para exibir seu nome, usar .get()
                                'Altura': dados_pessoais['Altura'],
                                'Genero': genero_var}
                
                
                



                # Cornfiguranção Dos Dados Mentais




                ctk.CTkLabel(frame_principal, text='Dados Mentais', font=('System', 30, 'bold'), text_color= 'red', width=348, bg_color='#1a1a1a').place(x=351, y=100)

                # Função Utilizada Para Criar As Alternativas


                def alternativas(texto, para_onde, valor, x, y):
                    ctk.CTkRadioButton(
                    frame_principal,
                    text = texto,
                    variable= para_onde,
                    value= valor,
                    text_color= 'light pink',
                    bg_color= '#1a1a1a',
                    font=('System', 18)
                    ).place(x=x, y=y)
                    

                # Pergunta 1


                ctk.CTkLabel(frame_principal, text='  Você prefere planejar tudo antes de agir ou agi no', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=354, y=200)
                ctk.CTkLabel(frame_principal, text='momento:', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=354, y=223)
                mentais1 = tk.StringVar(value="")    

                mentais1_opção1 = alternativas('Planejar', mentais1, 'planejar', 394, 255)
                
                mentais1_opição2 =alternativas('Agir No Momento', mentais1, 'agir no momento', 520, 255)

                # Pergunta 2
                
                ctk.CTkLabel(frame_principal, text='  Quando está sob pressão, você mantém a calma', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=354, y=295)
                ctk.CTkLabel(frame_principal, text='ou se estressa facilmente:', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=354, y=318)

                mentais2 = tk.StringVar(value='')

                mentais2_opição1 = alternativas('Calma', mentais2, 'calma', 394, 350)
                
                mentais2_opição2 = alternativas('Estressado', mentais2, 'estressado', 520, 350)

                # Pergunta 3
                
                ctk.CTkLabel(frame_principal, text='  Você prefere resolver problemas sozinho ou pedir', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=354, y=390)
                ctk.CTkLabel(frame_principal, text='ajuda:', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=354, y=413)

                mentais3 = tk.StringVar(value='')

                mentais3_opição1 = alternativas('Sozinho', mentais3, 'sozinho', 394, 445)
                
                mentais3_opição2 = alternativas('Pedir Ajuda', mentais3, 'pedir ajuda', 520, 445)

                # Pergunta 4

                ctk.CTkLabel(frame_principal, text='  Você tem facilidade para se concentrar por longos', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=354, y=485)
                ctk.CTkLabel(frame_principal, text='períodos:', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=354, y=508 )

                mentais4 = tk.StringVar(value='')

                mentais4_opição1 = alternativas('Sim', mentais4, 'sim', 394, 540)
                
                mentais4_opição2 = alternativas('Não', mentais4, 'nao', 520, 540)

                # Pergunta 5

                ctk.CTkLabel(frame_principal, text='  Você costuma ser mais lógico ou mais criativo:', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=354, y=580)

                mentais5 = tk.StringVar(value='')

                mentais5_opição1 = alternativas('Lógico', mentais5, 'logico', 394, 612)
                
                mentais5_opição2 = alternativas('Criativo', mentais5, 'criativo', 520, 612)

                # Salvar As Respostas Na Biblioteca

                dados_mentais = {'planejamento': mentais1,
                                'calma_pressao': mentais2,
                                'resolver_problema': mentais3,            # Quando for usar para exibir seu nome, usar .get()
                                'concentracao': mentais4,
                                'logica_criatividade': mentais5}
                
                





                # Configuração Dados Fisicos




                ctk.CTkLabel(frame_principal, text='Dados Fisicos', font=('System', 30, 'bold'), text_color= 'red', width=348, bg_color='#1a1a1a').place(x=701, y=100)

                # Pergunta 1

                ctk.CTkLabel(frame_principal, text='  Você prefere força bruta ou agilidade para lutar:', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=704, y=200)
                fisico1 = tk.StringVar(value="")    

                fisico1_opção1 = alternativas('Força', fisico1, 'força', 744, 232)
                
                fisico1_opição2 =alternativas('Agilidade', fisico1, 'agilidade', 870, 232)

                # Pergunta 2
                
                ctk.CTkLabel(frame_principal, text='  Você aguenta mais tempo lutando ou tem', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=704, y=272)
                ctk.CTkLabel(frame_principal, text='explosões curtas de energia:', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=704, y=295)

                fisico2 = tk.StringVar(value='')

                fisico2_opição1 = alternativas('Resistente', fisico2, 'resistente', 744, 327)
                
                fisico2_opição2 = alternativas('Explosoes De Energia', fisico2, 'explosoes de energia', 870, 327)

                # Pergunta 3
                
                ctk.CTkLabel(frame_principal, text='  Você prefere ataques rápidos ou golpes poderosos:', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=704, y=367)
                fisico3 = tk.StringVar(value='')

                fisico3_opição1 = alternativas('Rápido', fisico3, 'rapido', 744, 399)
                
                fisico3_opição2 = alternativas('Poderoso', fisico3, 'poderoso', 870, 399)

                # Pergunta 4

                ctk.CTkLabel(frame_principal, text='  Você é bom em esquivar ou em bloquear ataques:', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=704, y=439)
                fisico4 = tk.StringVar(value='')

                fisico4_opição1 = alternativas('Esquiva', fisico4, 'esquiva', 744, 471)
                
                fisico4_opição2 = alternativas('Bloquear', fisico4, 'bloquear', 870, 471)

                # Pergunta 5

                ctk.CTkLabel(frame_principal, text='  Você se considera mais resistente a dores ou mais ', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=704, y=511)
                ctk.CTkLabel(frame_principal, text='resistente ao cansaço:', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=704, y=534)

                fisico5 = tk.StringVar(value='')

                fisico5_opição1 = alternativas('Dor', fisico5, 'dor', 744, 566)
                
                fisico5_opição2 = alternativas('Cansaço', fisico5, 'cansaço', 870, 566)

                # Salvar As Respostas Na Biblioteca

                dados_fisico = {'forca_ou_agilidade': fisico1,
                                'aguenta_tempo': fisico2,
                                'ataques_rapidos_ou_poderosos': fisico3,            # Quando for usar para exibir seu nome, usar .get()
                                'esquiva_ou_bloqueio': fisico4,
                                'resistencia_dor_ou_cansaco': fisico5}
                

                frame_principal = None

                # Proxima tela

                def Criação2():
                    global frame_principal
                    if frame_principal:
                        frame_principal.destroy()

                    frame_principal = ctk.CTkFrame(janela, width=1300, height=650)
                    frame_principal.place(x=0, y=0)
                    linha_canvas = tk.Canvas(frame_principal, width=1300, height=650, bg="#1a1a1a", highlightthickness=0)
                    linha_canvas.place(x=0, y=0)

                    # Linha vermelha
                    linha_canvas.create_line(350, 90, 350, 650, fill="grey", width=2)
                    linha_canvas.create_line(700, 90, 700, 650, fill="grey", width=2)
                    linha_canvas.create_line(1050, 90, 1050, 650, fill="grey", width=2)

                    ctk.CTkLabel(frame_principal, text='Criação do Personagem', font=('System', 30, 'bold'), bg_color='black').place(x=25, y=15)

                    







                    # Configuração de Dados Sociais


                    ctk.CTkLabel(frame_principal, text='Dados Sociais', font=('System', 30, 'bold'), text_color= 'red', width=348, bg_color='#1a1a1a').place(x=1, y=100)

                    # pergunta 1

                    ctk.CTkLabel(frame_principal, text='  Você prefere liderar ou seguir ordens:', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=4, y=200)
                    sociais1 = tk.StringVar(value="")    

                    sociais1_opção1 = alternativas('Liderar', sociais1, 'liderar', 44, 232)
                    
                    sociais1_opição2 =alternativas('Seguir', sociais1, 'seguir', 170, 232)
                    
                    # pergunta 2
                    
                    ctk.CTkLabel(frame_principal, text='  Você costuma ser mais amigável ou reservado ', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=4, y=272)
                    ctk.CTkLabel(frame_principal, text='com os outros:', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=4, y=295)

                    sociais2 = tk.StringVar(value='')

                    sociais2_opição1 = alternativas('Amigável', sociais2, 'amigavel', 44, 327)
                    
                    sociais2_opição2 = alternativas('Reservado', sociais2, 'reservado', 170, 327)
                    
                    # pergunta 3
                    
                    ctk.CTkLabel(frame_principal, text='  Você confia facilmente nas pessoas:', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=4, y=367)
                    sociais3 = tk.StringVar(value='')

                    sociais3_opição1 = alternativas('Sim', sociais3, 'sim', 44, 399)
                    
                    sociais3_opição2 = alternativas('Não', sociais3, 'nao', 170, 399)

                    # pergunta 4
                    
                    ctk.CTkLabel(frame_principal, text='  Você é bom em convencer e influenciar os outros:', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=4, y=439)
                    sociais4 = tk.StringVar(value='')

                    sociais4_opição1 = alternativas('Sim', sociais4, 'sim', 44, 471)
                    
                    sociais4_opição2 = alternativas('Não', sociais4, 'nao', 170, 471)

                    # pergunta 5
                    
                    ctk.CTkLabel(frame_principal, text='  Você prefere resolver conflitos com conversa ou ', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=4, y=511)
                    ctk.CTkLabel(frame_principal, text='com ação:', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=4, y=534)

                    sociais5 = tk.StringVar(value='')

                    sociais5_opição1 = alternativas('Conversa', sociais5, 'conversa', 44, 566)
                    
                    sociais5_opição2 = alternativas('Ação', sociais5, 'acao', 170, 566)

                    # Salvar As Respostas na biblioteca

                    dados_sociais = {'liderar_ou_seguir': sociais1,
                                    'amigavel_ou_reservado': sociais2,
                                    'confia_facilmente': sociais3,              # Quando for usar para exibir seu nome, usar .get()
                                    'convencer_os_outros': sociais4,
                                    'resolver_conflitos': sociais5}
                    
                




                    # Configuração De Dados De Combate




                    ctk.CTkLabel(frame_principal, text='Dados De Combate', font=('System', 30, 'bold'), text_color= 'red', width=348, bg_color='#1a1a1a').place(x=351, y=100)

                    # Pergunta 1

                    ctk.CTkLabel(frame_principal, text='  Você prefere ataques rápidos e furtivos ou ataques', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=354, y=200)
                    ctk.CTkLabel(frame_principal, text='lentos e fortes:', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=354, y=223)
                    combate1 = tk.StringVar(value="")    

                    combate1_opção1 = alternativas('Furtivo', combate1, 'furtivo', 394, 255)
                    
                    combate1_opição2 =alternativas('Forte', combate1, 'forte', 520, 255)

                    # Pergunta 2
                    
                    ctk.CTkLabel(frame_principal, text='  Você é melhor em defesa ou em ataque:', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=354, y=295)

                    combate2 = tk.StringVar(value='')

                    combate2_opição1 = alternativas('Defesa', combate2, 'defesa', 394, 327)
                    
                    combate2_opição2 = alternativas('Ataque', combate2, 'ataque', 520, 327)

                    # Pergunta 3
                    
                    ctk.CTkLabel(frame_principal, text='  Você prefere lutar sozinho ou com um parceiro:', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=354, y=367)

                    combate3 = tk.StringVar(value='')

                    combate3_opição1 = alternativas('Individual', combate3, 'sozinho', 394, 399)
                    
                    combate3_opição2 = alternativas('Em Time', combate3, 'time', 520, 399)

                    # Pergunta 4

                    ctk.CTkLabel(frame_principal, text='  Você tem mais experiência em combate corpo a', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=354, y=439)
                    ctk.CTkLabel(frame_principal, text='corpo ou à distância:', font=('System', 20), text_color= 'light grey', bg_color='#1a1a1a').place(x=354, y=462 )

                    combate4 = tk.StringVar(value='')

                    combate4_opição1 = alternativas('Corpo A Corpo', combate4, 'corpo a corpo', 394, 494)
                    
                    combate4_opição2 = alternativas('Distânte', combate4, 'distante', 520, 494)

                    # Salvar As Respostas Na Biblioteca

                    dados_combate = {'ataque_rapido_ou_lento': combate1,
                                    'defesa_ou_ataque': combate2,
                                    'lutar_sozinho_ou_parceiro': combate3,            # Quando for usar para exibir seu nome, usar .get()
                                    'experiencia_corpo_a_corpo_ou_distancia': combate4,}
                    

                    seleção =[]
                    def verificar(qual):
                        selecionado = qual.get()
                        if selecionado in seleção:
                            if selecionado == 'sim' or selecionado == 'nao':
                                quantos = seleção.count('sim')
                                quanton = seleção.count('nao')
                                if quantos < 3 or quanton < 3:
                                    seleção.append(selecionado)
                        else:
                            if selecionado:
                                seleção.append(selecionado)
                                


                    ctk.CTkLabel(frame_principal, text='Importante', font=('System', 30, 'bold'), text_color= 'red',width=249, bg_color='#1a1a1a').place(x=1051, y=100)
                    ctk.CTkLabel(frame_principal, text='  Após Clicar em\ncontinuar, vôce\nnão conseguir\ntrocar seus dados,\n então escolha com\natenção.', font=('System', 24), text_color= 'light grey', bg_color='#1a1a1a', anchor='center').place(x=1052, y=250 )
                    
                    
                    frame_principal = None

                    def Criação3():
                        global frame_principal
                        if frame_principal:
                            frame_principal.destroy()

                        frame_principal = ctk.CTkFrame(janela, width=1300, height=650)
                        frame_principal.place(x=0, y=0)
                        linha_canvas = tk.Canvas(frame_principal, width=1300, height=650, bg="#1a1a1a", highlightthickness=0)
                        linha_canvas.place(x=0, y=0)
                        table = ctk.CTkTabview(
                            master=frame_principal,
                            width=1200,  # Aumentei a largura para caber melhor
                            height=500,  # Adicionei altura fixa
                            corner_radius=10,
                            border_width=2,
                            bg_color='#1a1a1a',
                            fg_color='teal',  # Cor diferente do fundo
                            segmented_button_fg_color='#1a1a1a',
                            segmented_button_selected_color='teal',
                            segmented_button_unselected_color='#333333',
                            text_color='white'
                        )
                        table.place(x=50, y=75)

                        


                        table.add('Classe')
                        table.add('Dados Pessoais')
                        table.add('Dados Mentais')
                        table.add('Dados Fisicos')
                        table.add('Dados Sociais')
                        table.add('Dados De Combate')

                        
                        ctk.CTkLabel(
                            table.tab('Dados Pessoais'),
                            text=(
                            f'Nome: {dados_pessoais["Nome"].get()}\n'
                            f'Idade: {dados_pessoais["Idade"].get()}\n'
                            f'Altura: {dados_pessoais["Altura"].get()}\n'
                            f'Peso: {dados_pessoais["Peso"].get()}\n'
                            f'Gênero: {genero_var.get()}'
                            ),
                            text_color='black',
                            anchor='w',
                            justify='left',
                            font=('system', 23, 'bold')
                            ).pack(padx=10, pady=10)
                        

                        ctk.CTkLabel(
                            table.tab('Dados Mentais'),
                            text=(
                                f'Planejamento: {dados_mentais["planejamento"].get()}\n'
                                f'Trabalho Sob Pressão: {dados_mentais["calma_pressao"].get()}\n'
                                f'Resolver Problemas: {dados_mentais["resolver_problema"].get()}\n'
                                f'Concentração: {dados_mentais["concentracao"].get()}\n'
                                f'Pensamento: {dados_mentais["logica_criatividade"].get()}'
                            ),
                            text_color='black',
                            anchor='w',
                            justify='left',
                            font=('system', 23, 'bold')
                            ).pack(padx=10, pady=10)
                        

                        ctk.CTkLabel(
                            table.tab('Dados Fisicos'),
                            text= (f'Especialidade: {dados_fisico["forca_ou_agilidade"].get()}\n'
                                f'Tipo De Luta: {dados_fisico["aguenta_tempo"].get()}\n'
                                f'Tipo Do Ataque: {dados_fisico["ataques_rapidos_ou_poderosos"].get()}\n'
                                f'Defesa: {dados_fisico["esquiva_ou_bloqueio"].get()}\n'
                                f'resistente A: {dados_fisico["resistencia_dor_ou_cansaco"].get()}'
                                ),
                                text_color='black',
                                anchor='w',
                                justify='left',
                                font=('system', 23, 'bold')
                                ).pack(padx=10, pady=10)


                        ctk.CTkLabel(
                            table.tab('Dados Sociais'),
                            text= (f'Liderança: {dados_sociais["liderar_ou_seguir"].get()}\n'
                                f'Relações: {dados_sociais["amigavel_ou_reservado"].get()}\n'
                                f'Confia Facilmente: {dados_sociais["confia_facilmente"].get()}\n'
                                f'Resolução de Conflito: {dados_sociais["resolver_conflitos"].get()}\n'
                                f'Influente: {dados_sociais["convencer_os_outros"].get()}'
                                ),
                                text_color='black',
                                anchor='w',
                                justify='left',
                                font=('system', 23, 'bold')
                                ).pack(padx=10, pady=10)
                        

                        ctk.CTkLabel(
                            table.tab('Dados De Combate'),
                            text= (f'Tipo De Ataque: {dados_combate["ataque_rapido_ou_lento"].get()}\n'
                                f'Especialidade: {dados_combate["defesa_ou_ataque"].get()}\n'
                                f'Tipo De Luta: {dados_combate["lutar_sozinho_ou_parceiro"].get()}\n'
                                f'Esperiencia De Combate: {dados_combate["experiencia_corpo_a_corpo_ou_distancia"].get()}'),
                                text_color='black',
                                anchor='w',
                                justify='left',
                                font=('system', 23, 'bold')
                                ).pack(padx=10, pady=10)
                        
                        # Analise da escolha da classe

                        classe = {"arqueiro": 0,
                                "espadachin": 0,
                                "assassino": 0,
                                "escudeiro": 0,
                                "lanceiro": 0,
                                "batedor": 0,
                                "MODERADOR": 0}
                        
                        # Com base nos dados pessoais
                        
                        idade = int(dados_pessoais['Idade'].get())
                        peso = float(dados_pessoais['Peso'].get())
                        altura = float(dados_pessoais['Altura'].get())
                        
                        
                        if 22 <= idade <= 32 and 70 <= peso <= 90 and 1.70 <= altura <= 1.90:
                            classe["arqueiro"] += 1
                            classe["espadachin"] += 1

                        elif 22 <= idade <= 32 and 70 <= peso <= 90 and 1.90 <= altura <= 2.10:
                            classe["lanceiro"] += 1

                        elif 22 <= idade <= 28 and 60 <= peso <= 75 and 1.70 <= altura <= 1.90:
                            classe["assassino"] += 1

                        elif 30 <= idade <= 38 and peso >= 90:
                            classe["escudeiro"] += 1

                        # Com base nos dados mentais

                        # PERGUNTA 1

                        if dados_mentais["planejamento"].get() == 'planejar':
                            classe["espadachin"] += 1
                            classe["arqueiro"] += 2
                            classe["assassino"] += 3

                        elif dados_mentais["planejamento"].get() == 'agir no momento':
                            classe["batedor"] += 3
                            classe["lanceiro"] += 1
                            classe["escudeiro"] += 2

                        # PERGUNTA 2

                        if dados_mentais["calma_pressao"].get() == 'calma':
                            classe["espadachin"] += 2
                            classe["arqueiro"] += 2
                            classe["assassino"] += 1
                            classe["escudeiro"] += 3

                        elif dados_mentais["calma_pressao"].get() == 'estressado':
                            classe["lanceiro"] += 2
                            classe["batedor"] += 2

                        # PERGUNTA 3

                        if dados_mentais["resolver_problema"].get() == 'sozinho':
                            classe["assassino"] += 2
                            classe["batedor"] += 1
                            classe["espadachin"] += 3

                        elif dados_mentais["resolver_problema"].get() == 'pedir ajuda':
                            classe["arqueiro"] += 2
                            classe["batedor"] += 3
                            classe["espadachin"] += 3
                            classe["escudeiro"] += 1

                        # PERGUNTA 4

                        if dados_mentais["concentracao"].get() == 'sim':
                            classe["arqueiro"] += 3
                            classe["batedor"] += 1
                            classe["lanceiro"] += 3
                            classe["assassino"] += 2
                            classe["escudeiro"] += 2

                        elif dados_mentais["concentracao"].get() == 'nao':
                            classe["espadachin"] += 3

                        # PERGUNTA 5

                        if dados_mentais["logica_criatividade"].get() == 'logico':
                            classe["espadachin"] += 2
                            classe["escudeiro"] += 2
                            classe["batedor"] += 3

                        elif dados_mentais["logica_criatividade"].get() == 'criativo':
                            classe["assassino"] += 3
                            classe["arqueiro"] += 2
                            classe["lanceiro"] += 2


                        # Com base nos dados fisicos

                        # Pergunta 1
                        
                        if dados_fisico["forca_ou_agilidade"].get() == 'força':
                            classe["escudeiro"] += 3
                            classe["espadachin"] += 1
                            classe["batedor"] += 1

                        elif dados_fisico["forca_ou_agilidade"].get() == 'agilidade':
                            classe["batedor"] += 1
                            classe["lanceiro"] += 2
                            classe["assassino"] += 2
                            classe["espadachin"] += 1
                            classe["arqueiro"] += 3

                        # PERGUNTA 2

                        if dados_fisico["aguenta_tempo"].get() == 'resistente':
                            classe["escudeiro"] += 2
                            classe["espadachin"] += 2
                            classe["assassino"] += 4
                            classe["batedor"] += 1

                        elif dados_fisico["aguenta_tempo"].get() == 'explosoes de energia':
                            classe["batedor"] += 3
                            classe["lanceiro"] += 2
                            classe["arqueiro"] += 1

                        # PERGUNTA 3

                        if dados_fisico["ataques_rapidos_ou_poderosos"].get() == 'rapido':
                            classe["arqueiro"] += 3
                            classe["assassino"] += 2
                            classe["lanceiro"] += 1
                            classe["batedor"] += 3

                        elif dados_fisico["ataques_rapidos_ou_poderosos"].get()  == 'poderoso':
                            classe["espadachin"] += 1
                            classe["batedor"] += 2

                        # PERGUNTA 4

                        if dados_fisico["esquiva_ou_bloqueio"].get() == 'esquiva':
                            classe["arqueiro"] += 3
                            classe["batedor"] += 2
                            classe["lanceiro"] += 1
                            classe["assassino"] += 3
                            classe["espadachin"] += 2

                        elif dados_fisico["esquiva_ou_bloqueio"].get() == 'bloquear':
                            classe["escudeiro"] += 1

                        # PERGUNTA 5

                        if dados_fisico["resistencia_dor_ou_cansaco"].get() == 'dor':
                            classe["escudeiro"] += 1
                            classe["lanceiro"] += 2
                            classe["espadachin"] += 3
                            classe["batedor"] += 1
                            classe["assassino"] += 2

                        elif dados_fisico["resistencia_dor_ou_cansaco"].get() == 'cansaço':
                            classe["escudeiro"] += 3
                            classe["assassino"] += 2
                            classe["espadachin"] += 1
                            classe["arqueiro"] += 3

                        # Com base nos dados sociais

                        # PERGUNTA 1

                        if dados_sociais["liderar_ou_seguir"].get() == 'liderar':
                            classe["arqueiro"] += 3
                            classe["assassino"] += 2
                            classe["lanceiro"] += 1

                        elif dados_sociais["liderar_ou_seguir"].get() == 'seguir':
                            classe["escudeiro"] += 1
                            classe["espadachin"] += 2
                            classe["batedor"] += 3

                        # PERGUNTA 2

                        if dados_sociais["amigavel_ou_reservado"].get() == 'amigavel':
                            classe["escudeiro"] += 3
                            classe["arqueiro"] += 2
                            classe["espadachin"] += 1

                        elif dados_sociais["amigavel_ou_reservado"].get() == 'reservado':
                            classe["batedor"] += 1
                            classe["assassino"] += 2
                            classe["lanceiro"] += 3

                        # PERGUNTA 3

                        if dados_sociais["confia_facilmente"].get() == 'sim':
                            classe["escudeiro"] += 2
                            classe["espadachin"] += 3
                            classe["arqueiro"] += 2

                        elif dados_sociais["confia_facilmente"].get() == 'nao':
                            classe["assassino"] += 2
                            classe["lanceiro"] += 2
                            classe["batedor"] += 2

                        # PERGUNTA 4

                        if dados_sociais["resolver_conflitos"].get() == 'conversa':
                            classe["escudeiro"] += 3
                            classe["arqueiro"] += 3
                            classe["espadachin"] += 3

                        elif dados_sociais["resolver_conflitos"].get() == 'acao':
                            classe["assassino"] += 1
                            classe["batedor"] += 1
                            classe["lanceiro"] += 1

                        # PERGUNTA 5

                        if dados_sociais["convencer_os_outros"].get() == 'sim':
                            classe["espadachin"] += 1
                            classe["arqueiro"] += 2
                            classe["assassino"] += 2
                            classe["escudeiro"] += 1

                        elif dados_sociais["convencer_os_outros"].get() == 'nao':
                            classe["batedor"] += 2
                            classe["lanceiro"] += 1

                        # Com base nos dados sociais

                        # PERGUNTA 1

                        if dados_combate["ataque_rapido_ou_lento"].get() == 'furtivo':
                            classe["arqueiro"] += 2
                            classe["lanceiro"] += 1
                            classe["assassino"] += 3

                        elif dados_combate["ataque_rapido_ou_lento"].get() == 'forte':
                            classe["batedor"] += 2
                            classe["espadachin"] += 3
                            classe["escudeiro"] += 3

                        # PERGUNTA 2

                        if dados_combate["defesa_ou_ataque"].get() == 'defesa':
                            classe["escudeiro"] += 3

                        elif dados_combate["defesa_ou_ataque"].get() == 'ataque':
                            classe["lanceiro"] += 1
                            classe["espadachin"] += 1
                            classe["assassino"] += 1
                            classe["arqueiro"] += 1
                            classe["batedor"] += 1

                        # PERGUNTA 3

                        if dados_combate["lutar_sozinho_ou_parceiro"].get() == 'sozinho':
                            classe["assassino"] += 4
                            classe["batedor"] += 1
                            classe["lanceiro"] += 3

                        elif dados_combate["lutar_sozinho_ou_parceiro"].get() == 'time':
                            classe["arqueiro"] += 2
                            classe["espadachin"] += 1
                            classe["escudeiro"] += 1

                        # PERGUNTA 4

                        if dados_combate["experiencia_corpo_a_corpo_ou_distancia"].get() == 'corpo a corpo':
                            classe["escudeiro"] += 2
                            classe["batedor"] += 1
                            classe["espadachin"] += 2
                            classe["assassino"] += 3

                        elif dados_combate["experiencia_corpo_a_corpo_ou_distancia"].get() == 'distante':
                            classe["lanceiro"] += 2
                            classe["arqueiro"] += 1


                        classe_jogador.clear()
                        classe_jogador.append(max(classe, key=classe.get))
                        


                        ctk.CTkLabel(
                            master=table.tab('Classe'),
                            text=f'Sua classe:\n{classe_jogador[0]}',
                            text_color='black',
                            anchor='w',
                            justify='left',
                            font=('system', 23, 'bold')
                        ).pack(padx=10, pady=10)
                        



                        def salvar_e_ir():
                            global Usuario, senha
                            dados_convertidos = {
                            chave: valor.get() if hasattr(valor, "get") else valor          # Converte os valores para str
                            for chave, valor in dados_pessoais.items()
                            }
                            dados_convertidos["Classe"] = classe_jogador[0]
                            salvar_dados(dados, dados_convertidos)
                            ir_para_o_jogo()
                            
                        
                        ctk.CTkButton(frame_principal,
                                    text='Criar',
                                    command=salvar_e_ir,
                                    font=('system', 29),                  # Botão que vai para a tela do jogo
                                    fg_color='#850000',
                                    bg_color='teal'
                                    ).place(x=1100, y=520)
                    questões = []
                    def verifica():
                        global questões
                        questões = [sociais1, sociais2, sociais3, sociais4, sociais5, combate1, combate2, combate3, combate4]
                        for questao in questões:
                            verificar(questao)
                        if len(seleção) >= len(questões):
                            Criação3()
                        else:
                            tk.messagebox.showwarning("Atenção", "Preencha todos os campos!")
                        

                    ctk.CTkButton(frame_principal, text='Continuar ->', command=verifica, fg_color='teal', font=('system', 24, 'bold')).place(x=1093, y=580)


                # configuração do botão continuar
                    
                seleção =[]
                def verifica_questão(qual):
                    selecionado = qual.get()
                    if selecionado and selecionado not in seleção:      
                        seleção.append(selecionado)
                            


                ctk.CTkLabel(frame_principal, text='Importante', font=('System', 30, 'bold'), text_color= 'red',width=249, bg_color='#1a1a1a').place(x=1051, y=100)
                ctk.CTkLabel(frame_principal, text='  Após Clicar em\ncontinuar, vôce\nnão conseguir\ntrocar seus dados,\n então escolha com\natenção.', font=('System', 24), text_color= 'light grey', bg_color='#1a1a1a', anchor='w', justify='left').place(x=1052, y=250 )
                

                # Verifica se todas as informações são validas
                questões = []
                def verifica_resposta():
                    seleção.clear()

                    # Lista de campos obrigatórios do tipo .get()
                    campos = [
                        mentais1, mentais2, mentais3, mentais4, mentais5,
                        fisico1, fisico2, fisico3, fisico4, fisico5,
                        genero_var, dados_pessoais['Nome'], dados_pessoais['Altura'],
                        dados_pessoais['Idade'], dados_pessoais['Peso']
                    ]

                    for campo in campos:
                        if campo.get().strip():
                            verifica_questão(campo)
                        else:
                            tk.messagebox.showwarning("Atenção", "Preencha todos os campos!")
                            return

                    # Coleta os dados para validação numérica
                    try:
                        idade = int(dados_pessoais['Idade'].get())
                        peso = float(dados_pessoais['Peso'].get())
                        altura = float(dados_pessoais['Altura'].get())
                    except ValueError:
                        tk.messagebox.showwarning("Erro", "Idade, peso ou altura inválidos.")
                        return

                    if idade < 16 or idade > 99:
                        tk.messagebox.showwarning("Atenção", "Idade inválida: Tente entre 16 a 99.")
                    elif peso < 46 or peso > 150:
                        tk.messagebox.showwarning("Atenção", "Peso inválido: Tente entre 46 a 150.")
                    elif altura < 1.0 or altura > 2.5:
                        tk.messagebox.showwarning("Atenção", "Altura inválida: Tente entre 1.00 a 2.50.")
                    else:
                        Criação2()  # Avança para a próxima parte da criação
                        
                    
                    

                ctk.CTkButton(frame_principal, text='Continuar ->', command=verifica_resposta, fg_color='teal', font=('system', 24, 'bold')).place(x=1093, y=580)










            # Confimar a escolha
            def confirmar_acao():
                resposta = tk.messagebox.askyesno("Confirmação", "Você realmente deseja escolher sua classe aleatóriamente?")
                if resposta:
                    Classe_aleatoria()
                else:
                    menu_de_escolha()

            # Escolher a classe de forma aleatória
            def Classe_aleatoria():
                global frame_principal
                if frame_principal:
                    frame_principal.destroy()

                frame_principal = ctk.CTkFrame(janela, width=1300, height=650)
                frame_principal.place(x=0, y=0)
                linha_canvas = tk.Canvas(frame_principal, width=1300, height=650, bg="#1a1a1a", highlightthickness=0)
                linha_canvas.place(x=0, y=0)

                ctk.CTkLabel(frame_principal, text='Criação do Personagem', font=('System', 30, 'bold'), bg_color='black').place(x=25, y=15)
                
                # Sorteando
                numero_classe = randint(0, 5)
                classes = ['Arqueiro', 'Espadachin', 'Assassino', 'Escudeiro', 'Lanceiro', 'Batedor']
                classe_jogador.clear


                # Caso tenha sorteado a classe arqueiro
                if classes[numero_classe] == 'Arqueiro':
                    classe_jogador.append(classes[0])
                    ctk.CTkLabel(frame_principal,
                                    text='Arqueiros',
                                    bg_color='#1a1a1a',
                                    font=('system', 50, 'bold'),
                                    text_color="#03364B",
                                    fg_color="#5B99B1",            # fazendo local onde vai os textos
                                    corner_radius=30,
                                    width=1100,
                                    height=490,
                                    anchor='n'
                                    ).place(x=100, y=80)
                        
                    ctk.CTkLabel(frame_principal,
                                    text=' Dano: ?\n Velocidade: ?\n Defesa: ?\n Vida: ?\n Arma: ?',
                                    justify='left',
                                    bg_color="#182630",
                                    text_color="#1B2230",
                                    fg_color='#5B99B1',
                                    width=1100, height=380,            # fazendo local onde vai os dados da classe
                                    font=('system', 38),
                                    anchor='nw'
                                    ).place(x=100, y=170)
                    
                    
                # Caso tenha sorteado a classe Espadachin
                elif classes[numero_classe] == 'Espadachin':
                    classe_jogador.append(classes[1])
                    ctk.CTkLabel(frame_principal,
                                    text='Espadachin',
                                    bg_color='#1a1a1a',
                                    font=('system', 50, 'bold'),
                                    text_color="#1C1C1C",
                                    fg_color="#808080",            # fazendo local onde vai os textos
                                    corner_radius=30,
                                    width=1100,
                                    height=490,
                                    anchor='n'
                                    ).place(x=100, y=80)
                        
                    ctk.CTkLabel(frame_principal,
                                    text=' Dano: ?\n Velocidade: ?\n Defesa: ?\n Vida: ?\n Arma: ?', 
                                    justify='left',
                                    bg_color="#182630",
                                    text_color="#242424",
                                    fg_color='#808080',            # fazendo local onde vai os dados da classe
                                    width=1100,
                                    height=380,
                                    font=('system', 38),
                                    anchor='nw'
                                    ).place(x=100, y=170)
                        
                        
                # Caso tenha sorteado a classe Assassino
                elif classes[numero_classe] == 'Assassino':
                    classe_jogador.append(classes[2])
                    ctk.CTkLabel(frame_principal,
                                text='Assassino',
                                bg_color='#1a1a1a',
                                font=('system', 50, 'bold'),
                                text_color="#440202",
                                fg_color="#FA8A76",            # fazendo local onde vai os textos
                                corner_radius=30,
                                width=1100,
                                height=490,
                                anchor='n'
                                ).place(x=100, y=80)
                        
                    ctk.CTkLabel(frame_principal,
                                text=' Dano: ?\n Velocidade: ?\n Defesa: ?\n Vida: ?\n Arma: ?',
                                justify='left',
                                bg_color="#182630",
                                text_color="#520202",
                                fg_color='#FA8A76',            # fazendo local onde vai os dados da classe
                                width=1100,
                                height=380,
                                font=('system', 38),
                                anchor='nw'
                                ).place(x=100, y=170)
                    print(classe_jogador)
                        
                
                # Caso tenha sorteado a classe Escudeiro
                elif classes[numero_classe] == 'Escudeiro':
                    classe_jogador.append(classes[3])
                    ctk.CTkLabel(frame_principal,
                                    text='Escudeiro',
                                    bg_color='#1a1a1a',
                                    font=('system', 50, 'bold'),
                                    text_color="#360000",
                                    fg_color="#925959",            # fazendo local onde vai os textos
                                    corner_radius=30,
                                    width=1100,
                                    height=490,
                                    anchor='n'
                                    ).place(x=100, y=80)
                        
                    ctk.CTkLabel(frame_principal,
                                    text=' Dano: ?\n Velocidade: ?\n Defesa: ?\n Vida: ?\n Arma: ?',
                                    justify='left',
                                    bg_color="#182630",
                                    text_color="#471E00",
                                    fg_color='#925959',            # fazendo local onde vai os dados da classe
                                    width=1100,
                                    height=380,
                                    font=('system', 38),
                                    anchor='nw'
                                    ).place(x=100, y=170)
                        
                
                # Caso tenha sorteado a classe Lanceiro
                elif classes[numero_classe] == 'Lanceiro':
                    classe_jogador.append(classes[4])
                    ctk.CTkLabel(frame_principal,
                                    text='Lanceiro',
                                    bg_color='#1a1a1a',
                                    font=('system', 50, 'bold'),
                                    text_color="#410041",
                                    fg_color="#8A6E92",            # fazendo local onde vai os textos
                                    corner_radius=30,
                                    width=1100,
                                    height=490,
                                    anchor='n'
                                    ).place(x=100, y=80)
                        
                    ctk.CTkLabel(frame_principal,
                                    text=' Dano: ?\n Velocidade: ?\n Defesa: ?\n Vida: ?\n Arma: ?',
                                    justify='left',
                                    bg_color="#182630",
                                    text_color="#4B004B",
                                    fg_color='#8A6E92',                   # fazendo local onde vai os dados da classe     
                                    width=1100, height=380,
                                    font=('system', 38),
                                    anchor='nw'
                                    ).place(x=100, y=170)


                # Caso tenha sorteado a classe batedor
                elif classes[numero_classe] == 'Batedor':
                    classe_jogador.append(classes[5])
                    ctk.CTkLabel(frame_principal,
                                    text='Batedor',
                                    bg_color='#1a1a1a',
                                    font=('system', 50, 'bold'),
                                    text_color="#003803",
                                    fg_color="#76C47A",            # fazendo local onde vai os textos
                                    corner_radius=30,
                                    width=1100,
                                    height=490,
                                    anchor='n'
                                    ).place(x=100, y=80)
                        
                    ctk.CTkLabel(frame_principal,
                                    text=' Dano: ?\n Velocidade: ?\n Defesa: ?\n Vida: ?\n Arma: ?',
                                    justify='left',
                                    bg_color="#182630",
                                    text_color="#005004",
                                    fg_color='#76C47A',            # fazendo local onde vai os dados da classe
                                    width=1100,
                                    height=380,
                                    font=('system', 38),
                                    anchor='nw'
                                    ).place(x=100, y=170)
                    
                

                # Linha divisoria de um dado a outro
                ctk.CTkLabel(frame_principal,
                                text='',
                                width=1,
                                height=420,
                                fg_color='grey',
                                anchor='n',
                                text_color='grey').place(x=650, y=150)
                
                # Cria outra aba de colocar as informaçoes pessoais do personagem
                def dados_pessoais():
                    global frame_principal
                    if frame_principal:                     # Tira o que ta na tela
                        frame_principal.destroy()


                    frame_principal = ctk.CTkFrame(janela, width=1300, height=650)
                    frame_principal.place(x=0, y=0)                             # Cria a nova tela
                    linha_canvas = tk.Canvas(frame_principal, width=1300, height=650, bg="#1a1a1a", highlightthickness=0)
                    linha_canvas.place(x=0, y=0)


                    # Para só permitir valores numericos no peso e na altura
                    def somente_numeros(valor):
                        valor.replace(',', '.')
                
                        return valor.replace('.', '').isdigit() or valor == ""

                    validar = janela.register(somente_numeros)   # ve se realmente so tem numeros

                    ctk.CTkLabel(frame_principal, text='Criação do Personagem', font=('System', 30, 'bold'), bg_color='black', ).place(x=25, y=15)

                    # Comfirma novamente a permisão de apenas numeros
                    def formatar_numero(event):
                        valor = event.widget.get().replace(',', '.')
                        event.widget.delete(0, 'end')
                        event.widget.insert(0, valor)

                    ctk.CTkLabel(frame_principal, text='DADOS PESSOAIS', font=('System', 40, 'bold'), bg_color='#1a1a1a', text_color="#830000", width=1300).place(x=0, y=60)


                    # Configuração Dos Dados Pessoais


                    dados_personagem = {'Nome': '',
                                    'Idade': '',
                                    'Peso': '',
                                    'Altura': '',
                                    'Genero': ''}
                    
                    # Pergunta 1

                    dados_personagem['Nome'] = ctk.CTkEntry(frame_principal,
                                            placeholder_text='',
                                            font=('System', 25),
                                            width=300,
                                            height=60,
                                            text_color='light pink',
                                            )
                    dados_personagem['Nome'].place(x=500, y=150)
                    ctk.CTkLabel(frame_principal, text='Nome:', font=('System', 25), text_color= 'light grey', bg_color='#1a1a1a').place(x=415, y=170)

                    # Pergunta 2

                    dados_personagem['Idade'] = ctk.CTkEntry(frame_principal,
                                            placeholder_text='',
                                            font=('System', 25),
                                            width= 300,
                                            height=60,
                                            text_color='light pink',
                                            validate='key',
                                            validatecommand=(validar, '%P')
                                            )
                    dados_personagem['Idade'].place(x=500, y=230)
                    ctk.CTkLabel(frame_principal, text='Idade:', font=('System', 25), text_color= 'light grey', bg_color='#1a1a1a').place(x=419, y=250)

                    # Pergunta 3

                    dados_personagem['Peso'] = ctk.CTkEntry(frame_principal,
                                            placeholder_text='',
                                            font=('System', 25),
                                            width= 300,
                                            height=60,
                                            text_color='light pink',
                                            validate='key',
                                            validatecommand=(validar, '%P')
                                            )
                    dados_personagem['Peso'].place(x=500, y=310)
                    ctk.CTkLabel(frame_principal, text='Peso:', font=('System', 25), text_color= 'light grey', bg_color='#1a1a1a').place(x=425, y=320)

                    # Pergunta 4

                    dados_personagem['Altura'] = ctk.CTkEntry(frame_principal,
                                                placeholder_text='',
                                                font=('System', 25),
                                                width= 300,
                                                height=60,
                                                text_color='light pink',
                                                validate='key',
                                                validatecommand=(validar, '%P')
                                                )
                    dados_personagem['Altura'].place(x=500, y=390)
                    ctk.CTkLabel(frame_principal, text='Altura:', font=('System', 25), text_color= 'light grey', bg_color='#1a1a1a').place(x=417, y=400)

                    # Pergunta 5

                    ctk.CTkLabel(frame_principal, text='Genêro:', font=('System', 25), text_color= 'light grey', width=1300, bg_color='#1a1a1a').place(x=0, y=460)
                    genero_var = tk.StringVar(value="")  

                    genero_m = ctk.CTkRadioButton(
                        frame_principal,
                        text="Masculino",
                        variable=genero_var,
                        value="Masculino",
                        text_color='light pink',
                        bg_color='#1a1a1a',
                        font=('System', 25),
                        ).place(x=470, y=505)

                    genero_f = ctk.CTkRadioButton(
                        frame_principal,
                        text="Feminino",
                        variable=genero_var,
                        value="Feminino",
                        text_color='light pink',
                        bg_color='#1a1a1a',
                        font=('System', 25)
                    ).place(x=640, y=505)

                    dados_personagem['Peso'].bind("<FocusOut>", formatar_numero)
                    dados_personagem['Altura'].bind("<FocusOut>", formatar_numero)


                    
                    def verificar_respostas():
                        # Aguarda todas as respostas em no dicioario
                        dados_pessoais = {
                                        'Nome': dados_personagem['Nome'].get(),
                                        'Idade': dados_personagem['Idade'].get(),
                                        'Peso': dados_personagem['Peso'].get(),
                                        'Altura': dados_personagem['Altura'].get(),
                                        'Genero': genero_var.get()
                                    }
                        
                        # Verifica se as respostas dadas são validas
                        if dados_pessoais['Idade'] == '' or dados_pessoais['Altura'] == '' or dados_pessoais['Nome'] == '' or dados_pessoais['Peso'] == '' or dados_pessoais['Genero'] == '':
                            tk.messagebox.showwarning("Atenção", "Preencha todos os campos.")

                        elif int(dados_pessoais['Idade']) <= 15 or int(dados_pessoais['Idade']) >= 100:
                            tk.messagebox.showwarning("Atenção", "Idade invalida: Tente entre 16 a 99.")

                        elif float(dados_pessoais['Peso']) <= 45 or float(dados_pessoais['Peso']) >= 151:
                            tk.messagebox.showwarning("Atenção", "Peso invalido: Tente entre 46 a 150.")

                        elif float(dados_pessoais['Altura']) < 1 or float(dados_pessoais['Altura'])>= 2.6:
                            tk.messagebox.showwarning("Atenção", "Altura invalida: Tente entre 1.00 a 2.50.")
                        
                        else:
                            dados_pessoais["Classe"] = classe_jogador[0]
                            salvar_dados(dados, dados_pessoais)
                            ir_para_o_jogo()     # Se todas as respostas forem validas, o usuario sera direcionado a tela do jogo
                        
                    ctk.CTkButton(frame_principal,
                                    text='Criar',
                                    command=verificar_respostas,
                                    font=('system', 29),                  # Botão que verifica as respostas
                                    fg_color='#850000'
                                    ).place(x=1100, y=570)
                

                ctk.CTkButton(frame_principal,
                                text= 'Proximo ->',
                                bg_color='#1a1a1a',
                                corner_radius=20,
                                fg_color='#6a6a6a',
                                font=('system', 24, 'bold'),
                                text_color='light pink',
                                border_color='#7a7a7a',
                                border_width=2,
                                command=dados_pessoais
                                ).place(x=1030, y=590)


                








            

                ctk.CTkLabel(frame_principal, text='Criação do Personagem', font=('System', 30, 'bold'), bg_color='black').place(x=25, y=15)



            # Botão de que maneiro a sua classe sera escolhida: Sua Escolha
            imagem_ESCOLHA = Image.open("F:/jogo/Imagens/classes/escolha.png")
            imagem_escolha = ctk.CTkImage(light_image=imagem_ESCOLHA, dark_image=imagem_ESCOLHA, size=(260, 260))
            ctk.CTkButton(frame_principal,
                        text= 'Você escolhe\nsua classe\n',
                        anchor='s',
                        bg_color='#1a1a1a',
                        corner_radius=20,
                        fg_color="#855daa",
                        font=('system', 38, 'bold'),
                        text_color='black',
                        width=350,
                        height=400,
                        image=imagem_escolha,
                        compound='top',
                        hover_color="#6c4e88",
                        command=Selecionar_classe
                        ).place(x=63, y=140)


            # Botão de que maneira a sua classe sera escolhida: Aleatoriamente
            imagem_ALEATORIO = Image.open("F:/jogo/Imagens/classes/aleatorio.png" or "C:/jogo/Imagens/classes/aleatorio.png")
            imagem_aleatorio = ctk.CTkImage(light_image=imagem_ALEATORIO, dark_image=imagem_ALEATORIO, size=(260, 260))
            ctk.CTkButton(frame_principal,
                        text= 'Classe\naleatória\n',
                        anchor='s',
                        bg_color='#1a1a1a',
                        corner_radius=20,
                        fg_color="#AC5F5F",
                        font=('system', 38, 'bold'),
                        text_color='black',
                        width=350,
                        height=400,
                        image=imagem_aleatorio,
                        compound='top',
                        hover_color="#884e4e",
                        command=confirmar_acao
                        ).place(x=475, y=140)


            # Botão de que maneiro a sua classe sera escolhida: Sua Personalidade
            imagem_PERSONALIDADE = Image.open("F:/jogo/Imagens/classes/personalidade.png")
            imagem_personalidade = ctk.CTkImage(light_image=imagem_PERSONALIDADE, dark_image=imagem_PERSONALIDADE, size=(260, 260))
            ctk.CTkButton(frame_principal,
                        text= 'Clase com\nbase na\npersonalidade',
                        anchor='s',
                        bg_color='#1a1a1a',corner_radius=20,
                        fg_color="#6fbd51",
                        font=('system', 38, 'bold'),
                        text_color='black',
                        width=350,
                        height=400,
                        image=imagem_personalidade,
                        compound='top',
                        hover_color="#63884e",
                        command=Criação
                        ).place(x=887, y=140)







        def verificar_se_ja_existe():
            usuario_encontrado = False
            for usuario in usuarios:
                if usuario["nome"] == dados['nome'].get() and usuario["senha"] == dados['senha'].get():
                    usuario_encontrado = True
                    break
            if usuario_encontrado:
                tk.messagebox.showwarning("Atensão", "Esse nome ja existe")
            else:
                menu_de_escolha()

        ctk.CTkButton(frame_principal,
                      text="Entrar",
                      font=("System", 28),
                      fg_color="#38663c",
                      hover_color="#163f12",
                      command=verificar_se_ja_existe
                      ).place(x=1100, y=550)

        ctk.CTkButton(frame_principal,
                      text="<- Voltar",
                      font=("System", 28),
                      fg_color="#38663c",
                      hover_color="#163f12",
                      command=entrar
                      ).place(x=60, y=550)
                
    
    button_rgistrar = ctk.CTkButton(
    frame_principal,
    text="Registrar",
    font=("System", 28),
    fg_color="#38663c",
    hover_color="#163f12",
    command=registrar_se,
    width=200,
    height=50
    ).place(x=60, y=550)

    




    
    ctk.CTkButton(frame_principal,
                    text="Entrar",
                    font=("System", 28),
                    fg_color="#38663c",
                    hover_color="#163f12",
                    command=login
                    ).place(x=1100, y=550)
    
    
    


# Tecla para iniciar o jogo

tecla = ''
def tecla_precionada(event):
    global tecla
    if event.keysym.lower() == tecla and ok:
        entrar()
        janela.unbind('<Key>')

tecla = 'g'
janela.bind('<Key>', tecla_precionada)

janela.mainloop()
