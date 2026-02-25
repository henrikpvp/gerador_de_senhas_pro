import customtkinter as ctk
from gerador_de_senhas import criar_senha
import pyperclip

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gerador Pro")
        self.geometry("400x400")

        # 1. Campo onde a senha aparece (Apenas leitura)
        self.output = ctk.CTkEntry(self, width=300, height=40, justify="center")
        self.output.pack(pady=20)
        self.output.insert(0, "Clique em Gerar")
        self.output.configure(state="readonly")

        # 2. Slider de tamanho
        self.label_tamanho = ctk.CTkLabel(self, text="Tamanho: 16")
        self.label_tamanho.pack()
        
        self.slider = ctk.CTkSlider(self, from_=8, to=32, command=self.mudar_label)
        self.slider.set(16)
        self.slider.pack(pady=10)

        # 3. Botão
        self.btn = ctk.CTkButton(self, text="GERAR SENHA", command=self.clique_gerar)
        self.btn.pack(pady=20)

    def mudar_label(self, v):
        self.label_tamanho.configure(text=f"Tamanho: {int(v)}")

    def clique_gerar(self):
        # Aqui pegamos o valor do slider, que SEMPRE será um número
        tam = int(self.slider.get())
        
        # Gera a senha usando o seu outro arquivo
        nova_senha = criar_senha(tamanho=tam)
        
        # Mostra na tela
        self.output.configure(state="normal")
        self.output.delete(0, "end")
        self.output.insert(0, nova_senha)
        self.output.configure(state="readonly")
        
        # Copia
        pyperclip.copy(nova_senha)

if __name__ == "__main__":
    app = App()
    app.mainloop()