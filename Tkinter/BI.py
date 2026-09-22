import tkinter as tk
from datetime import datetime

class DashboardExecutivo:
    def __init__(self, root):
        self.root = root
        self.configurar_janela()
        self.criar_componentes()

    def configurar_janela(self):
        # Título da Janela
        self.root.title("Dashboard Gerencial - Métricas & Desempenho Executivo")
        
        # Dimensões e Janela Fixa (não redimensionável)
        largura = 600
        altura = 420
        self.root.resizable(False, False)
        
        # Centralização obrigatória na tela (Center Screen)
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        pos_x = (largura_tela // 2) - (largura // 2)
        pos_y = (altura_tela // 2) - (altura // 2)
        
        self.root.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        
        # Tema Dark Slate corporativo (#0f172a)
        self.root.configure(bg="#0f172a")

    def criar_componentes(self):
        # 1. Cabeçalho Estilizado
        frame_cabecalho = tk.Frame(self.root, bg="#1e293b", height=60)
        frame_cabecalho.pack(fill="x", padx=10, pady=10)
        frame_cabecalho.pack_propagate(False)

        lbl_titulo = tk.Label(
            frame_cabecalho, 
            text="📊 Painel de Desempenho Corporativo (BI)", 
            bg="#1e293b", 
            fg="#f8fafc", 
            font=("Arial", 14, "bold")
        )
        lbl_titulo.pack(expand=True)

        # 2. Área Principal com Cartões de Métricas (KPIs)
        frame_kpis = tk.Frame(self.root, bg="#0f172a")
        frame_kpis.pack(fill="both", expand=True, padx=10, pady=5)

        # Configuração de grade 2x2 para os KPIs
        frame_kpis.grid_columnconfigure(0, weight=1)
        frame_kpis.grid_columnconfigure(1, weight=1)
        frame_kpis.grid_rowconfigure(0, weight=1)
        frame_kpis.grid_rowconfigure(1, weight=1)

        # Dados das métricas solicitadas
        kpis = [
            ("Receita Mensal", "R$ 458.900", "#38bdf8", 0, 0),
            ("Custo Operacional", "R$ 182.400", "#f43f5e", 0, 1),
            ("Margem do Lucro", "60.2%", "#4ade80", 1, 0),
            ("Novos Clientes", "+342", "#c084fc", 1, 1)
        ]

        for titulo, valor, cor, linha, coluna in kpis:
            self.criar_cartao_kpi(frame_kpis, titulo, valor, cor, linha, coluna)

        # 3. Rodapé Indicativo de Sincronização/Status
        frame_rodape = tk.Frame(self.root, bg="#1e293b", height=35)
        frame_rodape.pack(fill="x", side="bottom", padx=10, pady=10)
        frame_rodape.pack_propagate(False)

        hora_atual = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
        texto_rodape = f"Sistema v2.4.1 | Última sincronização: {hora_atual}"
        
        lbl_rodape = tk.Label(
            frame_rodape, 
            text=texto_rodape, 
            bg="#1e293b", 
            fg="#94a3b8", 
            font=("Arial", 9)
        )
        lbl_rodape.pack(expand=True)

    def criar_cartao_kpi(self, parent, titulo, valor, cor_destaque, linha, coluna):
        # Cartão individual simulando o design corporativo
        card = tk.Frame(parent, bg="#1e293b", bd=1, relief="solid")
        card.grid(row=linha, column=coluna, sticky="nsew", padx=8, pady=8)

        lbl_tit = tk.Label(card, text=titulo, bg="#1e293b", fg="#94a3b8", font=("Arial", 10))
        lbl_tit.pack(pady=(15, 5))

        lbl_val = tk.Label(card, text=valor, bg="#1e293b", fg=cor_destaque, font=("Arial", 16, "bold"))
        lbl_val.pack(pady=(0, 15))


if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardExecutivo(root)
    root.mainloop()