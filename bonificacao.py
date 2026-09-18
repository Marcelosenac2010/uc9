import tkinter as tk
from tkinter import messagebox


# -----------------------------
# CONFIGURAÇÃO DA JANELA
# -----------------------------

janela = tk.Tk()

janela.title("Motor Financeiro - Bonificação Executiva e PLR")

largura = 500
altura = 430

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

pos_x = (largura_tela - largura) // 2
pos_y = (altura_tela - altura) // 2

janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
janela.resizable(False, False)

fundo = "#0f172a"
campo = "#1e293b"

janela.configure(bg=fundo)


# -----------------------------
# TÍTULO
# -----------------------------

titulo = tk.Label(
    janela,
    text="MOTOR FINANCEIRO",
    font=("Arial", 18, "bold"),
    fg="white",
    bg=fundo
)

titulo.pack(pady=(20, 5))


subtitulo = tk.Label(
    janela,
    text="Cálculo de Bonificação Executiva e PLR",
    font=("Arial", 10),
    fg="#94a3b8",
    bg=fundo
)

subtitulo.pack(pady=(0, 15))


# -----------------------------
# FORMULÁRIO
# -----------------------------

formulario = tk.Frame(
    janela,
    bg=fundo
)

formulario.pack()


# Nome
label_nome = tk.Label(
    formulario,
    text="Nome do Executivo/Gestor:",
    font=("Arial", 10, "bold"),
    fg="white",
    bg=fundo
)

label_nome.grid(row=0, column=0, sticky="w", pady=7)

entrada_nome = tk.Entry(
    formulario,
    width=32,
    font=("Arial", 10),
    bg=campo,
    fg="white",
    insertbackground="white"
)

entrada_nome.grid(row=0, column=1, pady=7)


# Salário
label_salario = tk.Label(
    formulario,
    text="Salário Base (R$):",
    font=("Arial", 10, "bold"),
    fg="white",
    bg=fundo
)

label_salario.grid(row=1, column=0, sticky="w", pady=7)

entrada_salario = tk.Entry(
    formulario,
    width=32,
    font=("Arial", 10),
    bg=campo,
    fg="white",
    insertbackground="white"
)

entrada_salario.grid(row=1, column=1, pady=7)


# Metas
label_metas = tk.Label(
    formulario,
    text="Atingimento de Metas (%):",
    font=("Arial", 10, "bold"),
    fg="white",
    bg=fundo
)

label_metas.grid(row=2, column=0, sticky="w", pady=7)

entrada_metas = tk.Entry(
    formulario,
    width=32,
    font=("Arial", 10),
    bg=campo,
    fg="white",
    insertbackground="white"
)

entrada_metas.grid(row=2, column=1, pady=7)


# -----------------------------
# FUNÇÃO DE CÁLCULO
# -----------------------------

def calcular_bonificacao():

    nome = entrada_nome.get().strip()
    salario_texto = entrada_salario.get().strip()
    metas_texto = entrada_metas.get().strip()

    # Validação do nome
    if not nome:
        resultado.config(
            text="ERRO: Informe o nome do executivo/gestor.",
            fg="#ef4444"
        )
        entrada_nome.focus()
        return

    # Validação dos números
    try:
        salario = float(salario_texto)
        metas = float(metas_texto)

    except ValueError:
        resultado.config(
            text="ERRO: Salário e metas devem ser valores numéricos.",
            fg="#ef4444"
        )
        return

    # Validação do salário
    if salario <= 0:
        resultado.config(
            text="ERRO: O salário deve ser maior que zero.",
            fg="#ef4444"
        )
        entrada_salario.focus()
        return

    # Validação das metas
    if metas <= 0:
        resultado.config(
            text="ERRO: O percentual de metas deve ser maior que zero.",
            fg="#ef4444"
        )
        entrada_metas.focus()
        return

    if metas > 200:
        resultado.config(
            text="ERRO: O percentual máximo permitido é 200%.",
            fg="#ef4444"
        )
        entrada_metas.focus()
        return

    # -----------------------------
    # REGRAS DE BONIFICAÇÃO
    # -----------------------------

    if metas < 80:
        percentual_bonus = 0
        categoria = "Sem direito à bonificação"

    elif metas <= 99:
        percentual_bonus = 0.50
        categoria = "Bonificação Regular"

    elif metas <= 120:
        percentual_bonus = 1.00
        categoria = "Bonificação Integral"

    elif metas <= 150:
        percentual_bonus = 1.50
        categoria = "Prêmio de Superação"

    else:
        percentual_bonus = 2.00
        categoria = "Bonificação Executiva Máxima"

    # -----------------------------
    # CÁLCULO
    # -----------------------------

    bonificacao = salario * percentual_bonus

    # -----------------------------
    # EXIBIÇÃO
    # -----------------------------

    resultado.config(
        text=(
            f"EXECUTIVO: {nome}\n"
            f"Categoria: {categoria}\n"
            f"Bonificação: R$ {bonificacao:,.2f}"
        ),
        fg="#22c55e"
    )


# -----------------------------
# BOTÃO
# -----------------------------

botao_calcular = tk.Button(
    janela,
    text="CALCULAR BONIFICAÇÃO",
    font=("Arial", 10, "bold"),
    bg="#2563eb",
    fg="white",
    width=25,
    command=calcular_bonificacao
)

botao_calcular.pack(pady=20)


# -----------------------------
# RESULTADO
# -----------------------------

label_resultado = tk.Label(
    janela,
    text="RESULTADO DO CÁLCULO",
    font=("Arial", 9, "bold"),
    fg="#94a3b8",
    bg=fundo
)

label_resultado.pack()


resultado = tk.Label(
    janela,
    text="Aguardando cálculo...",
    font=("Arial", 11, "bold"),
    fg="#94a3b8",
    bg=fundo,
    justify="center"
)

resultado.pack(pady=8)


# -----------------------------
# EXECUÇÃO
# -----------------------------

entrada_nome.focus()

janela.mainloop()