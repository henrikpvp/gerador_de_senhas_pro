import customtkinter as ctk
from gerador_de_senhas import criar_senha
import pyperclip
from datetime import datetime # Importado para marcar a hora no histórico

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gerador Pro - Com Histórico")
        self.geometry("400x550") # Aumentado para caber o histórico
        self.resizable(False, False)

        # 1. Campo onde a senha aparece (Apenas leitura)
        self.output = ctk.CTkEntry(self, width=300, height=40, justify="center", font=("Consolas", 16))
        self.output.pack(pady=20)
        self.output.insert(0, "Clique em Gerar")
        self.output.configure(state="readonly")

        # 2. Slider de tamanho
        self.label_tamanho = ctk.CTkLabel(self, text="Tamanho: 16", font=("Arial", 12, "bold"))
        self.label_tamanho.pack()
        
        self.slider = ctk.CTkSlider(self, from_=8, to=32, command=self.mudar_label)
        self.slider.set(16)
        self.slider.pack(pady=10)

        # 3. Botão Gerar
        self.btn = ctk.CTkButton(self, text="GERAR SENHA", command=self.clique_gerar, font=("Arial", 14, "bold"))
        self.btn.pack(pady=20)

        # 4. ÁREA DE HISTÓRICO
        self.label_hist = ctk.CTkLabel(self, text="Histórico das últimas senhas:", font=("Arial", 11, "italic"))
        self.label_hist.pack(pady=(10, 0))
        
        # Campo de texto tipo Log (Scrollable)
        self.historico_txt = ctk.CTkTextbox(self, width=350, height=150, font=("Consolas", 12))
        self.historico_txt.pack(pady=10, padx=20)
        self.historico_txt.configure(state="disabled") # Começa desativado para edição

    def mudar_label(self, v):
        self.label_tamanho.configure(text=f"Tamanho: {int(v)}")

    def clique_gerar(self):
        tam = int(self.slider.get())
        
        # Gera a senha usando o seu outro arquivo
        nova_senha = criar_senha(tamanho=tam)
        
        # Atualiza o campo principal (Entry)
        self.output.configure(state="normal")
        self.output.delete(0, "end")
        self.output.insert(0, nova_senha)
        self.output.configure(state="readonly")
        
        # --- Lógica do Histórico ---
        hora_atual = datetime.now().strftime("%H:%M:%S")
        entrada_log = f"[{hora_atual}] {nova_senha}\n"
        
        self.historico_txt.configure(state="normal") # Habilita para escrever
        self.historico_txt.insert("1.0", entrada_log) # Insere no topo (linha 1, coluna 0)
        self.historico_txt.configure(state="disabled") # Trava novamente
        
        # Copia para o Windows
        pyperclip.copy(nova_senha)

if __name__ == "__main__":
    app = App()
    app.mainloop()