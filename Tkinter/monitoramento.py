import tkinter as tk


# -----------------------------
# CONFIGURAÇÃO DA JANELA
# -----------------------------

janela = tk.Tk()
janela.title("Painel de Controle - Gestão de Ativos Corporativos (EAM)")

largura = 500
altura = 350

# Centralizar a janela
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

pos_x = (largura_tela - largura) // 2
pos_y = (altura_tela - altura) // 2

janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
janela.resizable(False, False)

# Cor principal
fundo = "#0f172a"

janela.configure(bg=fundo)


# -----------------------------
# CABEÇALHO
# -----------------------------

cabecalho = tk.Frame(
    janela,
    bg=fundo
)

cabecalho.pack(fill="x", padx=20, pady=(15, 5))

titulo = tk.Label(
    cabecalho,
    text="MONITORAMENTO DE ATIVOS",
    font=("Arial", 16, "bold"),
    fg="white",
    bg=fundo
)

titulo.pack(side="left")

status = tk.Label(
    cabecalho,
    text="● ONLINE",
    font=("Arial", 9, "bold"),
    fg="#22c55e",
    bg=fundo
)

status.pack(side="right")


# -----------------------------
# ÁREA DE MÉTRICAS
# -----------------------------

area_metricas = tk.Frame(
    janela,
    bg=fundo
)

area_metricas.pack(fill="x", padx=20, pady=10)


def criar_kpi(parent, titulo, valor):
    quadro = tk.Frame(
        parent,
        bg="#1e293b",
        width=210,
        height=70
    )

    quadro.pack_propagate(False)

    texto = tk.Label(
        quadro,
        text=titulo,
        font=("Arial", 9),
        fg="#94a3b8",
        bg="#1e293b"
    )

    texto.pack(anchor="w", padx=10, pady=(8, 0))

    numero = tk.Label(
        quadro,
        text=valor,
        font=("Arial", 18, "bold"),
        fg="white",
        bg="#1e293b"
    )

    numero.pack(anchor="w", padx=10)

    return quadro


# Primeira linha
kpi1 = criar_kpi(
    area_metricas,
    "Equipamentos Cadastrados",
    "120"
)

kpi1.grid(row=0, column=0, padx=(0, 5), pady=5)

kpi2 = criar_kpi(
    area_metricas,
    "Ativos em Operação",
    "98"
)

kpi2.grid(row=0, column=1, padx=(5, 0), pady=5)


# Segunda linha
kpi3 = criar_kpi(
    area_metricas,
    "Manutenção Preventiva",
    "17"
)

kpi3.grid(row=1, column=0, padx=(0, 5), pady=5)

kpi4 = criar_kpi(
    area_metricas,
    "Equipamentos Críticos",
    "5"
)

kpi4.grid(row=1, column=1, padx=(5, 0), pady=5)




painel_saude = tk.Frame(
    janela,
    bg="#1e293b",
    height=65
)

painel_saude.pack(
    fill="x",
    padx=20,
    pady=(5, 15)
)

painel_saude.pack_propagate(False)

texto_saude = tk.Label(
    painel_saude,
    text="SAÚDE OPERACIONAL DA INFRAESTRUTURA",
    font=("Arial", 9, "bold"),
    fg="#94a3b8",
    bg="#1e293b"
)

texto_saude.pack(pady=(8, 0))

saude = tk.Label(
    painel_saude,
    text="● 92%  |  OPERAÇÃO ESTÁVEL",
    font=("Arial", 15, "bold"),
    fg="#22c55e",
    bg="#1e293b"
)

saude.pack()


# -----------------------------
# EXECUÇÃO
# -----------------------------

janela.mainloop()