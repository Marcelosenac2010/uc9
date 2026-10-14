from abc import ABC, abstractmethod
import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# ==========================================
# 1. MODEL & DAO (Camada de Dados)
# ==========================================


class Funcionario:

    def __init__(self, id, nome, cargo):
        self.id = id
        self.nome = nome
        self.cargo = cargo


class BaseDAO(ABC):

    def __init__(self, db_config=None):
        self.db_config = db_config or "hrms.db"

    def get_connection(self):
        try:
            return sqlite3.connect(self.db_config)
        except sqlite3.Error as err:
            raise ConnectionAbortedError(f"Problemas ao conectar: {err}")

    def dados_banco(self):
        try:
            conexao = self.get_connection()
            cursor = conexao.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS funcionario(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cargo TEXT NOT NULL
            )""")
            conexao.commit()
            cursor.close()
            conexao.close()
        except sqlite3.Error as err:
            raise Exception(f"Erro ao criar tabela: {err}")

    @abstractmethod
    def save(self, objeto):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def update(self, objeto):
        pass


class Funcionario_DAO(BaseDAO):

    def __init__(self, db_config=None):
        super().__init__(db_config)
        self.dados_banco()

    def save(self, funcionario: Funcionario):
        conexao = self.get_connection()
        cursor = conexao.cursor()
        try:
            cursor.execute(
                "INSERT INTO funcionario (nome, cargo) VALUES (?, ?)",
                (funcionario.nome, funcionario.cargo),
            )
            conexao.commit()
            funcionario.id = cursor.lastrowid
        except sqlite3.Error as err:
            conexao.rollback()
            raise Exception(f"Erro ao salvar funcionário: {err}")
        finally:
            cursor.close()
            conexao.close()

    def get_all(self):
        conexao = self.get_connection()
        cursor = conexao.cursor()
        try:
            cursor.execute("SELECT id, nome, cargo FROM funcionario")
            linhas = cursor.fetchall()
            return [Funcionario(linha[0], linha[1], linha[2]) for linha in linhas]
        except sqlite3.Error as err:
            raise Exception(f"Erro ao buscar funcionários: {err}")
        finally:
            cursor.close()
            conexao.close()

    def get_by_id(self, id):
        conexao = self.get_connection()
        cursor = conexao.cursor()
        try:
            cursor.execute(
                "SELECT id, nome, cargo FROM funcionario WHERE id = ?", (id,)
            )
            linha = cursor.fetchone()
            if linha:
                return Funcionario(linha[0], linha[1], linha[2])
            return None
        except sqlite3.Error as err:
            raise Exception(f"Erro ao buscar funcionário por ID: {err}")
        finally:
            cursor.close()
            conexao.close()

    def delete(self, id):
        conexao = self.get_connection()
        cursor = conexao.cursor()
        try:
            cursor.execute("DELETE FROM funcionario WHERE id = ?", (id,))
            conexao.commit()
        except sqlite3.Error as err:
            conexao.rollback()
            raise Exception(f"Erro ao deletar funcionário: {err}")
        finally:
            cursor.close()
            conexao.close()

    def update(self, funcionario: Funcionario):
        conexao = self.get_connection()
        cursor = conexao.cursor()
        try:
            cursor.execute(
                "UPDATE funcionario SET nome = ?, cargo = ? WHERE id = ?",
                (funcionario.nome, funcionario.cargo, funcionario.id),
            )
            conexao.commit()
        except sqlite3.Error as err:
            conexao.rollback()
            raise Exception(f"Erro ao atualizar funcionário: {err}")
        finally:
            cursor.close()
            conexao.close()


# ==========================================
# 2. VIEW (Camada de Interface Gráfica)
# ==========================================


class FuncionarioView:

    def __init__(self, root, controller):
        self.controller = controller
        self.controller.set_view(self)
        self.root = root
        self.root.title("Gerenciamento de Funcionários - HRMS")
        self.root.geometry("650x450")
        self.root.config(bg="#f0f0f0")

        self.id_selecionado = None
        self.nome_var = tk.StringVar()
        self.cargo_var = tk.StringVar()

        self._criar_widgets()
        self.controller.atualizar_tabela()

    def _criar_widgets(self):
        titulo = tk.Label(
            self.root,
            text="Cadastro de Funcionários",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0",
            fg="#333",
        )
        titulo.pack(pady=10)

        form_frame = tk.LabelFrame(
            self.root,
            text=" Dados do Funcionário ",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0",
            padx=15,
            pady=15,
        )
        form_frame.pack(fill="x", padx=20, pady=5)

        tk.Label(form_frame, text="Nome:", bg="#f0f0f0", font=("Arial", 10)).grid(
            row=0, column=0, sticky="w", pady=5
        )
        self.entry_nome = tk.Entry(
            form_frame, textvariable=self.nome_var, width=35, font=("Arial", 10)
        )
        self.entry_nome.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Cargo:", bg="#f0f0f0", font=("Arial", 10)).grid(
            row=1, column=0, sticky="w", pady=5
        )
        self.entry_cargo = tk.Entry(
            form_frame, textvariable=self.cargo_var, width=35, font=("Arial", 10)
        )
        self.entry_cargo.grid(row=1, column=1, padx=10, pady=5)

        btn_frame = tk.Frame(self.root, bg="#f0f0f0")
        btn_frame.pack(pady=10)

        self.btn_salvar = tk.Button(
            btn_frame,
            text="Salvar",
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold"),
            width=10,
            command=self.controller.salvar_funcionario,
        )
        self.btn_salvar.grid(row=0, column=0, padx=5)

        self.btn_atualizar = tk.Button(
            btn_frame,
            text="Atualizar",
            bg="#2196F3",
            fg="white",
            font=("Arial", 10, "bold"),
            width=10,
            command=self.controller.atualizar_funcionario,
        )
        self.btn_atualizar.grid(row=0, column=1, padx=5)

        self.btn_deletar = tk.Button(
            btn_frame,
            text="Excluir",
            bg="#f44336",
            fg="white",
            font=("Arial", 10, "bold"),
            width=10,
            command=self.controller.deletar_funcionario,
        )
        self.btn_deletar.grid(row=0, column=2, padx=5)

        self.btn_limpar = tk.Button(
            btn_frame,
            text="Limpar",
            bg="#9e9e9e",
            fg="white",
            font=("Arial", 10, "bold"),
            width=10,
            command=self.limpar_campos,
        )
        self.btn_limpar.grid(row=0, column=3, padx=5)

        tabela_frame = tk.Frame(self.root)
        tabela_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.tree = ttk.Treeview(
            tabela_frame, columns=("ID", "Nome", "Cargo"), show="headings"
        )
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Cargo", text="Cargo")

        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Nome", width=250, anchor="w")
        self.tree.column("Cargo", width=250, anchor="w")

        scrollbar = ttk.Scrollbar(
            tabela_frame, orient="vertical", command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.tree.bind("<<TreeviewSelect>>", self.controller.selecionar_funcionario)

    def limpar_campos(self):
        self.id_selecionado = None
        self.nome_var.set("")
        self.cargo_var.set("")
        if self.tree.selection():
            self.tree.selection_remove(self.tree.selection())

    def mostrar_mensagem(self, titulo, mensagem, tipo="info"):
        if tipo == "erro":
            messagebox.showerror(titulo, mensagem)
        elif tipo == "aviso":
            messagebox.showwarning(titulo, mensagem)
        else:
            messagebox.showinfo(titulo, mensagem)

    def pedir_confirmacao(self, titulo, mensagem):
        return messagebox.askyesno(titulo, mensagem)


# ==========================================
# 3. CONTROLLER (Camada de Controle)
# ==========================================


class FuncionarioController:

    def __init__(self, dao):
        self.dao = dao
        self.view = None

    def set_view(self, view):
        self.view = view

    def atualizar_tabela(self):
        for row in self.view.tree.get_children():
            self.view.tree.delete(row)

        try:
            funcionarios = self.dao.get_all()
            for f in funcionarios:
                self.view.tree.insert("", "end", values=(f.id, f.nome, f.cargo))
        except Exception as e:
            self.view.mostrar_mensagem(
                "Erro", f"Não foi possível carregar os dados: {e}", "erro"
            )

    def salvar_funcionario(self):
        nome = self.view.nome_var.get().strip()
        cargo = self.view.cargo_var.get().strip()

        if not nome or not cargo:
            self.view.mostrar_mensagem("Aviso", "Preencha todos os campos!", "aviso")
            return

        try:
            novo_func = Funcionario(id=None, nome=nome, cargo=cargo)
            self.dao.save(novo_func)
            self.view.mostrar_mensagem("Sucesso", "Funcionário cadastrado com sucesso!")
            self.view.limpar_campos()
            self.atualizar_tabela()
        except Exception as e:
            self.view.mostrar_mensagem("Erro", f"Erro ao salvar: {e}", "erro")

    def selecionar_funcionario(self, event):
        selecao = self.view.tree.selection()
        if selecao:
            item = self.view.tree.item(selecao)
            id_func = item["values"][0]

            func = self.dao.get_by_id(id_func)
            if func:
                self.view.id_selecionado = func.id
                self.view.nome_var.set(func.nome)
                self.view.cargo_var.set(func.cargo)

    def atualizar_funcionario(self):
        if not self.view.id_selecionado:
            self.view.mostrar_mensagem(
                "Aviso",
                "Selecione um funcionário na tabela para atualizar.",
                "aviso",
            )
            return

        nome = self.view.nome_var.get().strip()
        cargo = self.view.cargo_var.get().strip()

        if not nome or not cargo:
            self.view.mostrar_mensagem("Aviso", "Os campos não podem estar vazios.", "aviso")
            return

        try:
            func_atualizado = Funcionario(
                id=self.view.id_selecionado, nome=nome, cargo=cargo
            )
            self.dao.update(func_atualizado)
            self.view.mostrar_mensagem("Sucesso", "Funcionário atualizado com sucesso!")
            self.view.limpar_campos()
            self.atualizar_tabela()
        except Exception as e:
            self.view.mostrar_mensagem("Erro", f"Erro ao atualizar: {e}", "erro")

    def deletar_funcionario(self):
        if not self.view.id_selecionado:
            self.view.mostrar_mensagem(
                "Aviso", "Selecione um funcionário na tabela para excluir.", "aviso"
            )
            return

        if self.view.pedir_confirmacao(
            "Confirmação", "Deseja realmente excluir este funcionário?"
        ):
            try:
                self.dao.delete(self.view.id_selecionado)
                self.view.mostrar_mensagem("Sucesso", "Funcionário excluído com sucesso!")
                self.view.limpar_campos()
                self.atualizar_tabela()
            except Exception as e:
                self.view.mostrar_mensagem("Erro", f"Erro ao excluir: {e}", "erro")


if __name__ == "__main__":
    root = tk.Tk()

    dao = Funcionario_DAO()
    controller = FuncionarioController(dao)
    view = FuncionarioView(root, controller)

    root.mainloop()