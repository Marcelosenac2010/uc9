from Model.Dao.Ativo_DAO import AtivoDAO
from Ativos.View.Dashboard_view import DashboardView
from Ativos.Controller.Dashboard_controller import  DashboardController

if __name__ == "__main__":
    # 1. Instancia o DAO e garante a tabela criada
    dao = AtivoDAO()
    dao.criar_tabela()

    # 2. Inicializa a View do Tkinter
    app = DashboardView()

    # 3. Inicializa o Controller unindo View e Model(DAO)
    controller = DashboardController(app, dao)
    app.controller = controller  # Associa de volta à view se necessário

    # Dispara a aplicação gráfica
    app.mainloop()