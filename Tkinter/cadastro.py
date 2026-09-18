import tkinter as tk
from tkinter import messagebox


# -----------------------------
# CONFIGURAÇÃO DA JANELA
# -----------------------------

janela = tk.Tk()

janela.title("Módulo de Recursos Humanos - HRMS")

largura = 500
altura = 400

# Centralizar janela
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

pos_x = (largura_tela - largura) // 2
pos_y = (altura_tela - altura) // 2

janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
janela.resizable(False, False)

fundo = "#1f1d13"
campo = "#576172"

janela.configure(bg=fundo)


# -----------------------------
# TÍTULO
# -----------------------------

titulo = tk.Label(
    janela,
    text="CADASTRO DE FUNCIONÁRIOS",
    font=("Arial", 20, "bold"),
    fg="white",
    bg=fundo
)

titulo.pack(pady=(20, 5))


subtitulo = tk.Label(
    janela,
    text="Módulo de Recursos Humanos (HRMS)",
    font=("Arial", 10),
    fg="#5486cc",
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


def criar_campo(texto, linha):
    label = tk.Label(
        formulario,
        text=texto,
        font=("Arial", 10, "bold"),
        fg="white",
        bg=fundo
    )

    label.grid(
        row=linha,
        column=0,
        sticky="w",
        padx=(0, 10),
        pady=6
    )

    entrada = tk.Entry(
        formulario,
        width=35,
        font=("Arial", 10),
        bg=campo,
        fg="white",
        insertbackground="white"
    )

    entrada.grid(
        row=linha,
        column=1,
        pady=6
    )

    return entrada


matricula = criar_campo("Matrícula:", 0)

nome = criar_campo("Nome Completo:", 1)

cargo = criar_campo("Cargo/Função:", 2)

departamento = criar_campo("Departamento:", 3)


# -----------------------------
# FUNÇÃO DE CADASTRO
# -----------------------------

def cadastrar():
    valor_matricula = matricula.get().strip()
    valor_nome = nome.get().strip()
    valor_cargo = cargo.get().strip()
    valor_departamento = departamento.get().strip()

    # Validação dos campos
    if not valor_matricula:
        auditoria.config(
            text="ALERTA: Informe a matrícula.",
            fg="#ef4444"
        )
        matricula.focus()
        return

    if not valor_nome:
        auditoria.config(
            text="ALERTA: Informe o nome completo.",
            fg="#ef4444"
        )
        nome.focus()
        return

    if not valor_cargo:
        auditoria.config(
            text="ALERTA: Informe o cargo/função.",
            fg="#ef4444"
        )
        cargo.focus()
        return

    if not valor_departamento:
        auditoria.config(
            text="ALERTA: Informe o departamento.",
            fg="#ef4444"
        )
        departamento.focus()
        return

    # Registro salvo
    auditoria.config(
        text=f"REGISTRO SALVO: {valor_nome} - Matrícula {valor_matricula}",
        fg="#22c55e"
    )


# -----------------------------
# FUNÇÃO DE RESET
# -----------------------------

def limpar():
    confirmar = messagebox.askyesno(
        "Confirmar limpeza",
        "Deseja realmente limpar todos os campos?"
    )

    if confirmar:
        matricula.delete(0, tk.END)
        nome.delete(0, tk.END)
        cargo.delete(0, tk.END)
        departamento.delete(0, tk.END)

        auditoria.config(
            text="Formulário limpo.",
            fg="#94a3b8"
        )

        matricula.focus()


# -----------------------------
# BOTÕES
# -----------------------------

botoes = tk.Frame(
    janela,
    bg=fundo
)

botoes.pack(pady=15)


botao_cadastrar = tk.Button(
    botoes,
    text="CONFIRMAR CADASTRO",
    font=("Arial", 10, "bold"),
    bg="#2563eb",
    fg="white",
    width=20,
    command=cadastrar
)

botao_cadastrar.grid(
    row=0,
    column=0,
    padx=5
)


botao_limpar = tk.Button(
    botoes,
    text="LIMPAR",
    font=("Arial", 10, "bold"),
    bg="#475569",
    fg="white",
    width=12,
    command=limpar
)

botao_limpar.grid(
    row=0,
    column=1,
    padx=5
)


# -----------------------------
# AUDITORIA
# -----------------------------

auditoria_titulo = tk.Label(
    janela,
    text="AUDITORIA DO SISTEMA",
    font=("Arial", 9, "bold"),
    fg="#94a3b8",
    bg=fundo
)

auditoria_titulo.pack()


auditoria = tk.Label(
    janela,
    text="Aguardando operação...",
    font=("Arial", 10),
    fg="#94a3b8",
    bg=fundo
)

auditoria.pack(pady=5)


# -----------------------------
# EXECUÇÃO
# -----------------------------

matricula.focus()

janela.mainloop()