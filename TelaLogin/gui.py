import tkinter as tk
from tkinter import messagebox
# Importa as funções do seu arquivo de banco de dados
# (Certifique-se de que o arquivo anterior se chama banco.py)
import banco 

class AplicacaoLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Acesso")
        
        # Centralizar a janela na tela do usuário
        largura = 350
        altura = 250
        self.centralizar_janela(largura, altura)
        self.root.resizable(False, False)
        
        # Cria o container principal ou carrega a tela de login inicial
        self.criar_tela_login()

    def centralizar_janela(self, largura, altura):
        """Calcula a posição central da tela e ajusta a geometria da janela."""
        self.root.update_idletasks()
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        pos_x = (largura_tela // 2) - (largura // 2)
        pos_y = (altura_tela // 2) - (altura // 2)
        self.root.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

    def limpar_container(self):
        """Remove todos os widgets atuais da janela para trocar de tela."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def criar_tela_login(self):
        """Cria a interface gráfica para login e opção de cadastro."""
        self.limpar_container()
        
        tk.Label(self.root, text="Login do Sistema", font=("Arial", 16, "bold")).pack(pady=15)
        
        tk.Label(self.root, text="Usuário:").pack(anchor="w", padx=40)
        self.entry_usuario = tk.Entry(self.root, width=30)
        self.entry_usuario.pack(pady=5)
        
        tk.Label(self.root, text="Senha:").pack(anchor="w", padx=40)
        self.entry_senha = tk.Entry(self.root, show="*", width=30)
        self.entry_senha.pack(pady=5)
        
        btn_entrar = tk.Button(self.root, text="Entrar", width=15, bg="#4CAF50", fg="white", command=self.executar_login)
        btn_entrar.pack(pady=10)
        
        btn_ir_cadastro = tk.Button(self.root, text="Cadastrar Novo Usuário", width=20, command=self.criar_tela_cadastro)
        btn_ir_cadastro.pack(pady=2)

    def criar_tela_cadastro(self):
        """Cria a interface gráfica para cadastrar novos usuários."""
        self.limpar_container()
        
        tk.Label(self.root, text="Cadastro de Usuário", font=("Arial", 16, "bold")).pack(pady=15)
        
        tk.Label(self.root, text="Novo Usuário:").pack(anchor="w", padx=40)
        self.entry_cad_usuario = tk.Entry(self.root, width=30)
        self.entry_cad_usuario.pack(pady=5)
        
        tk.Label(self.root, text="Nova Senha:").pack(anchor="w", padx=40)
        self.entry_cad_senha = tk.Entry(self.root, show="*", width=30)
        self.entry_cad_senha.pack(pady=5)
        
        btn_cadastrar = tk.Button(self.root, text="Cadastrar", width=15, bg="#2196F3", fg="white", command=self.executar_cadastro)
        btn_cadastrar.pack(pady=10)
        
        btn_voltar = tk.Button(self.root, text="Voltar para o Login", width=20, command=self.criar_tela_login)
        btn_voltar.pack(pady=2)

    def executar_login(self):
        """Valida os dados inseridos consultando o banco de dados."""
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        
        if not usuario or not senha:
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return
            
        # Chama a função validar_login do módulo banco.py
        if banco.validar_login(usuario, senha):
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            self.criar_tela_principal()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")

    def executar_cadastro(self):
        """Cadastra o novo usuário utilizando o módulo de banco de dados."""
        usuario = self.entry_cad_usuario.get()
        senha = self.entry_cad_senha.get()
        
        if not usuario or not senha:
            messagebox.showwarning("Atenção", "Preencha todos os campos para cadastrar!")
            return
            
        # Chama a função cadastrar do módulo banco.py
        sucesso = banco.cadastrar(usuario, senha)
        if sucesso:
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            self.criar_tela_login()
        else:
            messagebox.showerror("Erro", "Não foi possível cadastrar o usuário.")

    def criar_tela_principal(self):
        """Tela exibida após o login bem-sucedido."""
        self.limpar_container()
        
        tk.Label(self.root, text="Bem-vindo ao Sistema!", font=("Arial", 18, "bold")).pack(pady=40)
        
        btn_sair = tk.Button(self.root, text="Sair / Desconectar", width=15, bg="#f44336", fg="white", command=self.criar_tela_login)
        btn_sair.pack(pady=20)


# --- Execução do Programa ---
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacaoLogin(root)
    root.mainloop()