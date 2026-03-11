import tkinter as tk
from tkinter import ttk, messagebox

AZUL="#2563eb"
AZUL_ESCURO="#1e3a8a"
FUNDO="#f1f5f9"
BRANCO="#ffffff"
CINZA="#e2e8f0"
TEXTO="#1f2937"

usuarios={"admin":"123"}
treinos=[]
pontos_usuario=0

janela=tk.Tk()
janela.title("Better Team")
janela.geometry("1200x720")
janela.configure(bg=FUNDO)

style=ttk.Style()
style.theme_use("clam")

def limpar():
    for widget in janela.winfo_children():
        widget.destroy()

def tela_login():

    limpar()

    frame=tk.Frame(janela,bg=AZUL)
    frame.pack(fill="both",expand=True)

    caixa=tk.Frame(frame,bg=BRANCO,padx=50,pady=50)
    caixa.place(relx=0.5,rely=0.5,anchor="center")

    tk.Label(caixa,text="🏆 Better Team",font=("Segoe UI",22,"bold"),bg=BRANCO,fg=TEXTO).pack(pady=20)

    tk.Label(caixa,text="Email",bg=BRANCO).pack(anchor="w")
    email=tk.Entry(caixa,width=30)
    email.pack(pady=5)

    tk.Label(caixa,text="Senha",bg=BRANCO).pack(anchor="w")
    senha=tk.Entry(caixa,width=30,show="*")
    senha.pack(pady=5)

    def login():
        if email.get() in usuarios and usuarios[email.get()]==senha.get():
            dashboard()
        else:
            messagebox.showerror("Erro","Login inválido")

    tk.Button(caixa,text="Entrar",bg=AZUL,fg="white",width=25,pady=10,command=login).pack(pady=10)
    tk.Button(caixa,text="Criar Conta",bg="white",fg=AZUL,width=25,pady=10,command=tela_cadastro).pack()

def tela_cadastro():

    limpar()

    frame=tk.Frame(janela,bg=AZUL)
    frame.pack(fill="both",expand=True)

    caixa=tk.Frame(frame,bg=BRANCO,padx=50,pady=50)
    caixa.place(relx=0.5,rely=0.5,anchor="center")

    tk.Label(caixa,text="Criar Conta",font=("Segoe UI",22,"bold"),bg=BRANCO).pack(pady=20)

    tk.Label(caixa,text="Email",bg=BRANCO).pack(anchor="w")
    email=tk.Entry(caixa,width=30)
    email.pack(pady=5)

    tk.Label(caixa,text="Senha",bg=BRANCO).pack(anchor="w")
    senha=tk.Entry(caixa,width=30,show="*")
    senha.pack(pady=5)

    def cadastrar():

        if email.get()=="" or senha.get()=="":
            messagebox.showerror("Erro","Preencha os campos")
            return

        if email.get() in usuarios:
            messagebox.showerror("Erro","Usuário já existe")
            return

        usuarios[email.get()]=senha.get()
        messagebox.showinfo("Sucesso","Conta criada")
        tela_login()

    tk.Button(caixa,text="Cadastrar",bg=AZUL,fg="white",width=25,pady=10,command=cadastrar).pack(pady=10)
    tk.Button(caixa,text="Voltar",bg="white",fg=AZUL,width=25,pady=10,command=tela_login).pack()

def criar_topo():

    topo=tk.Frame(janela,bg=AZUL_ESCURO,height=70)
    topo.pack(fill="x")

    tk.Label(topo,text="🏆 Better Team",bg=AZUL_ESCURO,fg="white",font=("Segoe UI",18,"bold")).place(x=20,y=20)

    menu=tk.Frame(topo,bg=AZUL_ESCURO)
    menu.place(x=300,y=22)

    tk.Button(menu,text="Dashboard",bg=AZUL_ESCURO,fg="white",bd=0,command=dashboard).pack(side="left",padx=20)
    tk.Button(menu,text="Treinos",bg=AZUL_ESCURO,fg="white",bd=0,command=listas).pack(side="left",padx=20)
    tk.Button(menu,text="Ranking",bg=AZUL_ESCURO,fg="white",bd=0,command=ranking).pack(side="left",padx=20)
    tk.Button(menu,text="Adicionar Treino",bg=AZUL_ESCURO,fg="white",bd=0,command=adicionar_treino).pack(side="left",padx=20)

def dashboard():

    limpar()
    criar_topo()

    conteudo = tk.Frame(janela,bg=FUNDO)
    conteudo.pack(fill="both",expand=True,padx=40,pady=30)

    # --------- DADOS SIMULADOS ---------

    jogadores_ativos = 12
    treinos_semana = 18
    media_pontos = 1450
    sua_posicao = 4

    semana = [
        ("Seg",120),
        ("Ter",180),
        ("Qua",160),
        ("Qui",210),
        ("Sex",190),
        ("Sab",240),
        ("Dom",150)
    ]

    # --------- CARDS ---------

    def card(x,titulo,valor,icone):

        c = tk.Frame(conteudo,bg=BRANCO,width=240,height=110)
        c.place(x=x,y=0)

        tk.Label(
            c,
            text=f"{icone}  {titulo}",
            bg=BRANCO,
            fg="#64748b",
            font=("Segoe UI",10)
        ).pack(pady=10)

        tk.Label(
            c,
            text=valor,
            font=("Segoe UI",22,"bold"),
            bg=BRANCO,
            fg=AZUL
        ).pack()

    card(0,"Pontos Totais",pontos_usuario,"⭐")
    card(260,"Jogadores Ativos",jogadores_ativos,"👥")
    card(520,"Treinos da Semana",treinos_semana,"🏋")
    card(780,"Sua Posição",f"{sua_posicao}º","🏆")


    # --------- PROGRESSO SEMANAL ---------

    box1 = tk.Frame(conteudo,bg=BRANCO,width=520,height=350)
    box1.place(x=0,y=150)

    tk.Label(
        box1,
        text="Desempenho da Semana",
        font=("Segoe UI",12,"bold"),
        bg=BRANCO
    ).pack(pady=10)

    for dia,pontos in semana:

        linha = tk.Frame(box1,bg=BRANCO)
        linha.pack(fill="x",padx=20,pady=6)

        tk.Label(linha,text=dia,width=5,bg=BRANCO).pack(side="left")

        barra = ttk.Progressbar(
            linha,
            length=300,
            value=pontos,
            maximum=300
        )
        barra.pack(side="left",padx=10)

        tk.Label(
            linha,
            text=f"{pontos} pts",
            bg=BRANCO
        ).pack(side="left")


    # --------- TOP RANKING ---------

    ranking_box = tk.Frame(conteudo,bg=BRANCO,width=520,height=350)
    ranking_box.place(x=560,y=150)

    tk.Label(
        ranking_box,
        text="Top Jogadores",
        font=("Segoe UI",12,"bold"),
        bg=BRANCO
    ).pack(pady=10)

    ranking_simulado = [
        ("🥇 Lucas",1850),
        ("🥈 Marcos",1720),
        ("🥉 Fernanda",1600),
        ("4º Você",pontos_usuario),
        ("5º Carlos",1400)
    ]

    for nome,pontos in ranking_simulado:

        linha = tk.Frame(ranking_box,bg=BRANCO)
        linha.pack(fill="x",padx=20,pady=6)

        tk.Label(
            linha,
            text=nome,
            width=15,
            bg=BRANCO
        ).pack(side="left")

        ttk.Progressbar(
            linha,
            length=250,
            value=pontos,
            maximum=2000
        ).pack(side="left",padx=10)

        tk.Label(
            linha,
            text=f"{pontos} pts",
            bg=BRANCO
        ).pack(side="left")

def adicionar_treino():

    limpar()
    criar_topo()

    frame=tk.Frame(janela,bg=FUNDO)
    frame.pack(fill="both",expand=True)

    caixa=tk.Frame(frame,bg=BRANCO,padx=40,pady=40)
    caixa.pack(pady=60)

    tk.Label(caixa,text="Adicionar Treino",font=("Segoe UI",18,"bold"),bg=BRANCO).pack(pady=10)

    tk.Label(caixa,text="Nome do treino",bg=BRANCO).pack(anchor="w")
    nome=tk.Entry(caixa,width=40)
    nome.pack(pady=5)

    tk.Label(caixa,text="Pontuação",bg=BRANCO).pack(anchor="w")
    pontos=tk.Entry(caixa,width=20)
    pontos.pack(pady=5)

    def salvar():

        if nome.get()=="" or pontos.get()=="":
            messagebox.showerror("Erro","Preencha os campos")
            return

        try:
            p=int(pontos.get())
        except:
            messagebox.showerror("Erro","Pontuação inválida")
            return

        treinos.append({"nome":nome.get(),"pontos":p})

        messagebox.showinfo("Sucesso","Treino criado")
        listas()

    tk.Button(caixa,text="Salvar Treino",bg=AZUL,fg="white",width=25,pady=10,command=salvar).pack(pady=20)

def concluir_treino(index):

    global pontos_usuario
    pontos_usuario+=treinos[index]["pontos"]

    messagebox.showinfo("Treino concluído",f"+{treinos[index]['pontos']} pontos")

def listas():

    limpar()
    criar_topo()

    frame=tk.Frame(janela,bg=FUNDO)
    frame.pack(fill="both",expand=True,padx=40,pady=40)

    tabela=ttk.Treeview(frame,columns=("Treino","Pontos"),show="headings",height=15)

    tabela.heading("Treino",text="Treino")
    tabela.heading("Pontos",text="Pontos")

    tabela.column("Treino",width=600)
    tabela.column("Pontos",width=120)

    tabela.pack()

    for t in treinos:
        tabela.insert("",tk.END,values=(t["nome"],t["pontos"]))

    def concluir():

        selecionado=tabela.selection()

        if not selecionado:
            messagebox.showerror("Erro","Selecione um treino")
            return

        index=tabela.index(selecionado)
        concluir_treino(index)

    tk.Button(frame,text="Concluir Treino",bg=AZUL,fg="white",pady=10,width=20,command=concluir).pack(pady=20)

def ranking():

    limpar()
    criar_topo()

    frame=tk.Frame(janela,bg=FUNDO)
    frame.pack(fill="both",expand=True,padx=40,pady=40)

    tk.Label(frame,text="Ranking da Equipe",font=("Segoe UI",18,"bold"),bg=FUNDO).pack(anchor="w",pady=10)

    ranking_dados=[
        ("Lucas",1850),
        ("Marcos",1720),
        ("Fernanda",1600),
        ("Você",pontos_usuario),
        ("Carlos",1400),
        ("Ana",1320),
        ("Juliana",1200)
    ]

    ranking_dados.sort(key=lambda x: x[1], reverse=True)

    posicao=1

    for nome,pontos in ranking_dados:

        linha=tk.Frame(frame,bg=BRANCO,padx=20,pady=15)
        linha.pack(fill="x",pady=5)

        if nome=="Você":
            bg="#dbeafe"
        else:
            bg=BRANCO

        linha.configure(bg=bg)

        tk.Label(linha,text=f"{posicao}º",width=4,font=("Segoe UI",11,"bold"),bg=bg).pack(side="left")

        tk.Label(linha,text=nome,font=("Segoe UI",11,"bold"),bg=bg).pack(side="left")

        ttk.Progressbar(linha,length=500,value=pontos,maximum=2000).pack(side="left",padx=20)

        tk.Label(linha,text=f"{pontos} pts",bg=bg).pack(side="right")

        posicao+=1

tela_login()

janela.mainloop()
