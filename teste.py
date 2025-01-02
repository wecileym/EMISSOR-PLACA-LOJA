from PIL import Image, ImageTk
import customtkinter as ctk

class App:
    def __init__(self, root):
        self.w = root
        
        # Destrói o frame atual, se houver
        for widget in self.w.winfo_children():
            if isinstance(widget, ctk.CTkFrame):
                widget.destroy()

        # Cria o frame principal
        self.Frame9 = ctk.CTkFrame(self.w, corner_radius=30)
        self.Frame9.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        # Carregar e redimensionar a imagem para caber no frame
        self.image_path = "Image/moveis-linhares.png"
        self.update_image()

        # Atualiza o layout quando o frame for redimensionado
        self.Frame9.bind("<Configure>", lambda event: self.update_image())

    def update_image(self):
        largura = self.Frame9.winfo_width()
        altura = self.Frame9.winfo_height()

        if largura > 1 and altura > 1:  # Evita erros antes do layout estar visível
            # Abrir e redimensionar a imagem para o tamanho do frame
            img_original = Image.open(self.image_path)
            img_resized = img_original.resize((largura, altura), Image.LANCZOS)
            self.img1 = ImageTk.PhotoImage(img_resized)

            # Adicionar a imagem ao frame
            label = ctk.CTkLabel(self.Frame9, image=self.img1, text="")
            label.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza no frame

# Inicialização do app
root = ctk.CTk()
root.geometry("800x600")
app = App(root)
root.mainloop()
