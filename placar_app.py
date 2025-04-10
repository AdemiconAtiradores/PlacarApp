import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk


# Função para redimensionar a imagem mantendo a proporção pela altura
def redimensionar_imagem_por_altura(caminho_arquivo, altura_desejada=100):
    imagem = Image.open(caminho_arquivo)
    largura_original, altura_original = imagem.size
    # Calcula a nova largura mantendo a proporção
    nova_largura = int((altura_desejada / altura_original) * largura_original)
    # Redimensiona a imagem
    return imagem.resize((nova_largura, altura_desejada))


# Função para centralizar a imagem em um canvas de 100x100
def centralizar_imagem(imagem, largura_canvas=100, altura_canvas=100):
    largura_imagem, altura_imagem = imagem.size
    
    # Cria um fundo transparente de 100x100
    fundo = Image.new("RGBA", (largura_canvas, altura_canvas), (0, 0, 0, 0))
    
    # Calcula as posições para centralizar a imagem
    x_offset = (largura_canvas - largura_imagem) // 2
    y_offset = (altura_canvas - altura_imagem) // 2
    
    # Cola a imagem redimensionada no centro do fundo
    fundo.paste(imagem, (x_offset, y_offset))
    
    return fundo


# Função para atualizar o placar na janela secundária
def atualizar_placar():
    nome_time_a = entrada_nome_time_a.get()
    nome_time_b = entrada_nome_time_b.get()
    placar_time_a_label.config(text=str(placar_time_a))
    placar_time_b_label.config(text=str(placar_time_b))
    
    # Atualiza o nome dos times
    nome_time_a_label.config(text=nome_time_a)
    nome_time_b_label.config(text=nome_time_b)
    
    # Atualiza as imagens dos escudos
    if escudo_time_a_img:
        escudo_time_a_label.config(image=escudo_time_a_img)
    if escudo_time_b_img:
        escudo_time_b_label.config(image=escudo_time_b_img)


# Função para incrementar o placar do time A
def incrementar_time_a():
    global placar_time_a
    placar_time_a += 1
    atualizar_placar()


# Função para decrementar o placar do time A
def decrementar_time_a():
    global placar_time_a
    if placar_time_a > 0:
        placar_time_a -= 1
    atualizar_placar()


# Função para incrementar o placar do time B
def incrementar_time_b():
    global placar_time_b
    placar_time_b += 1
    atualizar_placar()


# Função para decrementar o placar do time B
def decrementar_time_b():
    global placar_time_b
    if placar_time_b > 0:
        placar_time_b -= 1
    atualizar_placar()


# Função para selecionar o escudo do time A
def selecionar_escudo_time_a():
    global escudo_time_a_img
    caminho_arquivo = filedialog.askopenfilename(title="Selecione o Escudo do Time A", filetypes=[("Imagens", "*.png *.jpg *.jpeg")])
    if caminho_arquivo:
        # Redimensiona a imagem mantendo a proporção pela altura
        escudo = redimensionar_imagem_por_altura(caminho_arquivo)
        # Centraliza a imagem em um "canvas" de 100x100
        escudo_centralizado = centralizar_imagem(escudo)
        escudo_time_a_img = ImageTk.PhotoImage(escudo_centralizado)
        atualizar_placar()

# Função para selecionar o escudo do time B
def selecionar_escudo_time_b():
    global escudo_time_b_img
    caminho_arquivo = filedialog.askopenfilename(title="Selecione o Escudo do Time B", filetypes=[("Imagens", "*.png *.jpg *.jpeg")])
    if caminho_arquivo:
        # Redimensiona a imagem mantendo a proporção pela altura
        escudo = redimensionar_imagem_por_altura(caminho_arquivo)
        # Centraliza a imagem em um "canvas" de 100x100
        escudo_centralizado = centralizar_imagem(escudo)
        escudo_time_b_img = ImageTk.PhotoImage(escudo_centralizado)
        atualizar_placar()


# Função para criar e configurar a janela secundária (placar)
def criar_janela_secundaria():
    # Criar a janela secundária
    janela_secundaria = tk.Toplevel(root)
    
    # Remover a barra de título e botões
    janela_secundaria.overrideredirect(True)
    
    # Definir o tamanho exato da janela secundária (479x189) e posicioná-la no canto superior esquerdo
    janela_secundaria.geometry("479x189+0+0")
    
    # Alterar o fundo da janela para preto
    janela_secundaria.config(bg="black")
    
    # Escudo e nome do Time A
    global escudo_time_a_label, placar_time_a_label, nome_time_a_label
    escudo_time_a_label = tk.Label(janela_secundaria, bg="black")
    escudo_time_a_label.place(x=20, y=15)  # Posição do escudo do Time A
    
    nome_time_a_label = tk.Label(janela_secundaria, text="Time A", font=("Arial", 32, "bold"), fg="white", bg="black")
    nome_time_a_label.place(x=30, y=120)  # Nome do time A abaixo do escudo
    
    # Escudo e nome do Time B
    global escudo_time_b_label, placar_time_b_label, nome_time_b_label
    escudo_time_b_label = tk.Label(janela_secundaria, bg="black")
    escudo_time_b_label.place(x=359, y=15)  # Posição do escudo do Time B
    
    nome_time_b_label = tk.Label(janela_secundaria, text="Time B", font=("Arial", 32, "bold"), fg="white", bg="black")
    nome_time_b_label.place(x=370, y=120)  # Nome do time B abaixo do escudo
    
    # Placar (pontuação) centralizado
    placar_time_a_label = tk.Label(janela_secundaria, text="0", font=("Arial", 56, "bold"), fg="white", bg="black")
    placar_time_a_label.place(x=160, y=75)  # Posição da pontuação do time A y=45
    
    tk.Label(janela_secundaria, text="-", font=("Arial", 56, "bold"), fg="white", bg="black").place(x=232, y=70)  # Separador y=40
    
    placar_time_b_label = tk.Label(janela_secundaria, text="0", font=("Arial", 56, "bold"), fg="white", bg="black")
    placar_time_b_label.place(x=290, y=75)  # Posição da pontuação do time B y=45

    # carrega imagem
    arquivo = "Ademicon.png"
    # redimensionar imagem
    imagem = redimensionar_imagem_por_altura(arquivo, 60)
    imagem = ImageTk.PhotoImage(imagem)
    logo_ademicon = tk.Label(janela_secundaria, image=imagem, bg="black")
    logo_ademicon.image = imagem
    logo_ademicon.place(x=135, y=5)  # Posição do logo Ademicon

    # define a janela como sempre no top
    # janela_secundaria.attributes('-topmost', True)

    atualizar_placar()


# Criar a janela principal
root = tk.Tk()
root.title("Painel de Controle do Placar")
root.geometry("340x370+479+0")

# Variáveis globais
placar_time_a = 0
placar_time_b = 0
escudo_time_a_img = None
escudo_time_b_img = None

# Nome dos times
ttk.Label(root, text="Nome do Time A:").pack(pady=5)
entrada_nome_time_a = ttk.Entry(root)
entrada_nome_time_a.pack(pady=5)

ttk.Label(root, text="Nome do Time B:").pack(pady=5)
entrada_nome_time_b = ttk.Entry(root)
entrada_nome_time_b.pack(pady=5)

# Seleção de escudos
ttk.Button(root, text="Selecionar Escudo Time A", command=selecionar_escudo_time_a).pack(pady=5)
ttk.Button(root, text="Selecionar Escudo Time B", command=selecionar_escudo_time_b).pack(pady=5)

# Controle de pontuação do Time A
frame_time_a = ttk.LabelFrame(root, text="Time A")
frame_time_a.pack(pady=10)
ttk.Button(frame_time_a, text="+", command=incrementar_time_a).pack(side=tk.LEFT, padx=5)
ttk.Button(frame_time_a, text="-", command=decrementar_time_a).pack(side=tk.LEFT, padx=5)

# Controle de pontuação do Time B
frame_time_b = ttk.LabelFrame(root, text="Time B")
frame_time_b.pack(pady=10)
ttk.Button(frame_time_b, text="+", command=incrementar_time_b).pack(side=tk.LEFT, padx=5)
ttk.Button(frame_time_b, text="-", command=decrementar_time_b).pack(side=tk.LEFT, padx=5)

# Botão para abrir a janela secundária
abrir_janela_btn = ttk.Button(root, text="Abrir Placar", command=criar_janela_secundaria)
abrir_janela_btn.pack(pady=10)

# define ícone da janela
root.iconbitmap("bola.ico")

# Iniciar o loop da aplicação
root.mainloop()
