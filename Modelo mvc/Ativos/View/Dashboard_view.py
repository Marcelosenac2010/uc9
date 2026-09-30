import tkinter as tk

class DashboardView(tk.Tk):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller
        
        self.title("Dashboard de Ativos - EAM")
        self.geometry("700x400")
        self.configure(bg="#0f172a") # Fundo Dark Slate

        # Título Principal
        self.lbl_titulo = tk.Label(
            self, text="Monitoramento de Ativos (KPIs)", 
            font=("Arial", 16, "bold"), bg="#0f172a", fg="#f8fafc"
        )
        self.lbl_titulo.pack(pady=20)

        # Frame para os Cartões de KPIs
        self.frame_kpis = tk.Frame(self, bg="#0f172a")
        self.frame_kpis.pack(pady=10)

        # Cartão 1: Falhas Críticas
        self.cartao_criticas = self.criar_cartao(self.frame_kpis, "Falhas Críticas", "0", "#ef4444")
        self.cartao_criticas.pack(side=tk.LEFT, padx=10)

        # Cartão 2: Em Manutenção
        self.cartao_manutencao = self.criar_cartao(self.frame_kpis, "Em Manutenção", "0", "#f59e0b")
        self.cartao_manutencao.pack(side=tk.LEFT, padx=10)

        # Cartão 3: Em Operação
        self.cartao_operacao = self.criar_cartao(self.frame_kpis, "Em Operação", "0", "#10b981")
        self.cartao_operacao.pack(side=tk.LEFT, padx=10)

        # Rodapé com Status
        self.lbl_status = tk.Label(
            self, text="Status: Conectando...", 
            font=("Arial", 10), bg="#1e293b", fg="#94a3b8", anchor="w", relief=tk.SUNKEN
        )
        self.lbl_status.pack(side=tk.BOTTOM, fill=tk.X)

        # Se o controller já estiver conectado, atualiza os dados
        if self.controller:
            self.controller.carregar_kpis()

    def criar_cartao(self, parent, titulo, valor_inicial, cor_borda):
        """Função auxiliar para criar cartões de KPI visualmente limpos"""
        card = tk.Frame(parent, bg="#1e293b", bd=2, relief=tk.GROOVE, padx=20, pady=15)
        
        lbl_tit = tk.Label(card, text=titulo, font=("Arial", 11, "bold"), bg="#1e293b", fg="#cbd5e1")
        lbl_tit.pack()
        
        # Rótulo que guarda o valor numérico do KPI
        lbl_val = tk.Label(card, text=valor_inicial, font=("Arial", 22, "bold"), bg="#1e293b", fg=cor_borda)
        lbl_val.pack(pady=5)
        
        # Guarda a referência do label do valor para atualizar depois
        card.lbl_val = lbl_val 
        return card

    def atualizar_cartoes(self, criticas, manutencao, operacao):
        """Atualiza os números exibidos nos cartões dinamicamente"""
        self.cartao_criticas.lbl_val.config(text=str(criticas))
        self.cartao_manutencao.lbl_val.config(text=str(manutencao))
        self.cartao_operacao.lbl_val.config(text=str(operacao))

    def atualizar_status(self, mensagem):
        """Altera a mensagem do rodapé"""
        self.lbl_status.config(text=f" {mensagem}")