import customtkinter as ctk
from datetime import datetime

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("ERP Financial - Livro Razão e Audit Trail")

largura = 800  # Aumentado ligeiramente para acomodar o botão de exclusão
altura = 600
largura_tela = app.winfo_screenwidth()
altura_tela = app.winfo_screenheight()
pos_x = (largura_tela - largura) // 2
pos_y = (altura_tela - altura) // 2
app.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
app.resizable(False, False)

# Lista inicial de transações
transacoes = [
    {"id": "001", "data": "22/09/2026", "desc": "Licenciamento de Software", "valor": 4500.00, "status": "Pago"},
    {"id": "002", "data": "21/09/2026", "desc": "Serviço de Nuvem AWS", "valor": -1250.50, "status": "Débito"},
    {"id": "003", "data": "20/09/2026", "desc": "Consultoria Externa", "valor": -3200.00, "status": "Pendente"},
    {"id": "004", "data": "19/09/2026", "desc": "Recebimento de Cliente A", "valor": 12800.00, "status": "Crédito"},
]

def filtrar_transacoes():
    termo = entrada_busca.get().lower()
    for widget in scroll_frame.winfo_children():
        widget.destroy()
    
    filtradas = [t for t in transacoes if termo in t["desc"].lower() or termo in t["id"]]
    carregar_tabela(filtradas)

def limpar_busca():
    entrada_busca.delete(0, "end")
    filtrar_transacoes()

def adicionar_transacao():
    desc = entrada_nova_desc.get().strip()
    valor_texto = entrada_novo_valor.get().strip()
    status = combo_status.get()

    if not desc:
        lbl_msg.configure(text="Erro: Informe a descrição.", text_color="#ef4444")
        return

    try:
        valor = float(valor_texto)
    except ValueError:
        lbl_msg.configure(text="Erro: O valor deve ser numérico (ex: -150.00 ou 1500).", text_color="#ef4444")
        return

    novo_id = f"{len(transacoes) + 1:03d}"
    data_atual = datetime.now().strftime("%d/%m/%Y")

    transacoes.append({
        "id": novo_id,
        "data": data_atual,
        "desc": desc,
        "valor": valor,
        "status": status
    })

    entrada_nova_desc.delete(0, "end")
    entrada_novo_valor.delete(0, "end")
    lbl_msg.configure(text="Transação adicionada com sucesso!", text_color="#22c55e")

    filtrar_transacoes()

def excluir_transacao(trans_id):
    global transacoes
    # Remove a transação correspondente ao ID da lista global
    transacoes = [t for t in transacoes if t["id"] != trans_id]
    lbl_msg.configure(text=f"Transação ID {trans_id} excluída.", text_color="#ef4444")
    filtrar_transacoes()

def carregar_tabela(dados):
    total = 0.0
    for i, t in enumerate(dados):
        total += t["valor"]
        
        cor_status = "#22c55e" if t["status"] in ["Pago", "Crédito"] else "#ef4444"
        
        linha = ctk.CTkFrame(scroll_frame, fg_color="#1e293b", corner_radius=6)
        linha.pack(fill="x", pady=3, padx=5)
        
        lbl_id = ctk.CTkLabel(linha, text=t["id"], width=50, font=("Arial", 11, "bold"), text_color="white")
        lbl_id.pack(side="left", padx=5)
        
        lbl_data = ctk.CTkLabel(linha, text=t["data"], width=80, font=("Arial", 11), text_color="#94a3b8")
        lbl_data.pack(side="left", padx=5)
        
        lbl_desc = ctk.CTkLabel(linha, text=t["desc"], width=200, anchor="w", font=("Arial", 11), text_color="white")
        lbl_desc.pack(side="left", padx=5)
        
        val_str = f"R$ {t['valor']:,.2f}"
        lbl_valor = ctk.CTkLabel(linha, text=val_str, width=100, anchor="e", font=("Arial", 11, "bold"), text_color="white")
        lbl_valor.pack(side="left", padx=5)
        
        lbl_status = ctk.CTkLabel(linha, text=t["status"], width=80, font=("Arial", 11, "bold"), text_color=cor_status)
        lbl_status.pack(side="left", padx=5)
        
      
        btn_excluir = ctk.CTkButton(
            linha, 
            text="X", 
            width=30, 
            height=24, 
            fg_color="#ef4444", 
            hover_color="#dc2626", 
            font=("Arial", 11, "bold"),
            command=lambda tid=t["id"]: excluir_transacao(tid)
        )
        btn_excluir.pack(side="left", padx=10)
        
    lbl_total.configure(text=f"Saldo Líquido do Lote: R$ {total:,.2f}")

# --- ELEMENTOS DA INTERFACE ---

# 1. Barra de Busca Superior
frame_topo = ctk.CTkFrame(app, fg_color="transparent")
frame_topo.pack(fill="x", padx=20, pady=10)

entrada_busca = ctk.CTkEntry(frame_topo, placeholder_text="Pesquisar por ID ou descrição...", width=380, height=35)
entrada_busca.pack(side="left", padx=(0, 10))

botao_filtrar = ctk.CTkButton(frame_topo, text="Filtrar", command=filtrar_transacoes, width=90, height=35, fg_color="#2563eb", hover_color="#1d4ed8")
botao_filtrar.pack(side="left", padx=(0, 5))

botao_limpar = ctk.CTkButton(frame_topo, text="Limpar", command=limpar_busca, width=80, height=35, fg_color="#475569", hover_color="#334155")
botao_limpar.pack(side="left")

# 2. Cabeçalho da Tabela
header_frame = ctk.CTkFrame(app, fg_color="#0f172a", height=30)
header_frame.pack(fill="x", padx=20)

ctk.CTkLabel(header_frame, text="ID", width=50, font=("Arial", 11, "bold"), text_color="#64748b").pack(side="left", padx=5)
ctk.CTkLabel(header_frame, text="Data", width=80, font=("Arial", 11, "bold"), text_color="#64748b").pack(side="left", padx=5)
ctk.CTkLabel(header_frame, text="Descrição", width=200, anchor="w", font=("Arial", 11, "bold"), text_color="#64748b").pack(side="left", padx=5)
ctk.CTkLabel(header_frame, text="Valor R$", width=100, anchor="e", font=("Arial", 11, "bold"), text_color="#64748b").pack(side="left", padx=5)
ctk.CTkLabel(header_frame, text="Status", width=80, font=("Arial", 11, "bold"), text_color="#64748b").pack(side="left", padx=5)
ctk.CTkLabel(header_frame, text="Ação", width=30, font=("Arial", 11, "bold"), text_color="#64748b").pack(side="left", padx=10)

# 3. Grid / Scrollable Frame
scroll_frame = ctk.CTkScrollableFrame(app, width=730, height=180, fg_color="#090d16")
scroll_frame.pack(padx=20, pady=5)

# 4. Formulário de Cadastro (Nova Transação)
frame_cadastro = ctk.CTkFrame(app, fg_color="#1e293b", corner_radius=8)
frame_cadastro.pack(fill="x", padx=20, pady=10)

ctk.CTkLabel(frame_cadastro, text="Adicionar Nova Transação", font=("Arial", 11, "bold"), text_color="#38bdf8").pack(anchor="w", padx=10, pady=(8, 4))

form_inputs = ctk.CTkFrame(frame_cadastro, fg_color="transparent")
form_inputs.pack(fill="x", padx=10, pady=4)

entrada_nova_desc = ctk.CTkEntry(form_inputs, placeholder_text="Descrição da Transação", width=280, height=30)
entrada_nova_desc.pack(side="left", padx=(0, 8))

entrada_novo_valor = ctk.CTkEntry(form_inputs, placeholder_text="Valor (Ex: 1500 ou -250)", width=160, height=30)
entrada_novo_valor.pack(side="left", padx=(0, 8))

combo_status = ctk.CTkComboBox(form_inputs, values=["Pago", "Crédito", "Débito", "Pendente"], width=130, height=30)
combo_status.pack(side="left", padx=(0, 8))
combo_status.set("Pago")

botao_adicionar = ctk.CTkButton(form_inputs, text="Adicionar", command=adicionar_transacao, width=90, height=30, fg_color="#22c55e", hover_color="#16a34a")
botao_adicionar.pack(side="left")

lbl_msg = ctk.CTkLabel(frame_cadastro, text="", font=("Arial", 10), text_color="#94a3b8")
lbl_msg.pack(anchor="w", padx=10, pady=(0, 6))

# 5. Rodapé com Saldo Líquido
frame_rodape = ctk.CTkFrame(app, fg_color="#1e293b", height=35)
frame_rodape.pack(fill="x", side="bottom", padx=20, pady=10)
frame_rodape.pack_propagate(False)

lbl_total = ctk.CTkLabel(frame_rodape, text="", font=("Arial", 12, "bold"), text_color="#22c55e")
lbl_total.pack(expand=True)


carregar_tabela(transacoes)

app.mainloop()