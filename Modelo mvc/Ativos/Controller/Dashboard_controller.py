class DashboardController:
    def __init__(self, view, ativo_dao):
        self.view = view
        self.ativo_dao = ativo_dao
        
        # Vincula o botão de atualizar da view, se houver, ou carrega ao iniciar
        self.carregar_kpis()

    def carregar_kpis(self):
        try:
            # Conta diretamente do banco usando as strings do Enum/sistema
            criticas = self.ativo_dao.contar_por_estado("falhas criticas")
            manutencao = self.ativo_dao.contar_por_estado("em manutenção")
            operacao = self.ativo_dao.contar_por_estado("em operação")

            # Atualiza os cartões na View
            self.view.atualizar_cartoes(criticas, manutencao, operacao)
            self.view.atualizar_status("Status: Dados carregados com sucesso do banco.")
        except Exception as e:
            self.view.atualizar_status(f"Status: Erro ao carregar dados ({e})")