import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk



class Logon(ctk.CTk): 

    def __init__(self):
        super().__init__()
        
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")

        self.geometry("800x600")
        self.minsize(800, 600)
        self.title('Login')
                
        # Imagem pattern imagem inical da tela de login
        img1 = ImageTk.PhotoImage(Image.open("Image/pattern.png"))
        l1 = ctk.CTkLabel(master=self, image=img1)
        l1.pack()

        Frame_Tela_Login = ctk.CTkFrame(master=l1, width=500, height=500, corner_radius=30)
        Frame_Tela_Login.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        l2 = ctk.CTkLabel(master=Frame_Tela_Login, text="Logar", font=('Century Gothic', 40))
        l2.place(x=190, y=45)

        self.Entry_Nome_User = ctk.CTkEntry(master=Frame_Tela_Login, width=390, height=50, placeholder_text='Nome', font=('Century Gothic', 20))
        self.Entry_Nome_User.place(x=60, y=130)

        self.Entry_Senha_User = ctk.CTkEntry(master=Frame_Tela_Login, width=390, height=50, placeholder_text='Senha', show="*", font=('Century Gothic', 20))
        self.Entry_Senha_User.place(x=60, y=200)

        l3 = ctk.CTkLabel(master=Frame_Tela_Login, text="Esqueceu senha?", font=('Century Gothic', 16))
        l3.place(x=310, y=255)

        Button_Logar = ctk.CTkButton(master=Frame_Tela_Login, width=390, height=50, text="Entrar", command=self.Show_Window_Home, corner_radius=6)
        Button_Logar.place(x=60, y=300)

        img2 = ctk.CTkImage(Image.open("Image/Google.webp").resize((20, 20), Image.LANCZOS))
       
        button2 = ctk.CTkButton(master=Frame_Tela_Login, image=img2, text="Google", width=390, height=50, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF', command="")
        button2.place(x=60, y=370)

    def Show_Window_Home(self):
            
            self.destroy()
            self.w = ctk.CTk()  
            self.w.minsize(800, 600)
            self.w.geometry("1280x720")
            self.w.title('Bem-vindo ao sistema!')

            # self.service = self.authenticate_google_drive()
            
            self.Frame_Widgets = ctk.CTkFrame(self.w, width=200, corner_radius=40)
            self.Frame_Widgets.pack(side="left", fill="both", padx=10, pady=10)

            Windows_Home = Window_Home(self.w, self.Frame_Widgets)
            Windows_Create = Window_Create(self.w, self.Frame_Widgets)
            Windows_View = Window_View(self.w, self.Frame_Widgets)
            Windows_User_Infor = Window_User_Infor(self.w, self.Frame_Widgets)
            Windows_Documents = Window_Documents(self.w, self.Frame_Widgets)



            icon_size = (80, 80)
            
            Home_Logo = Image.open("Image/home.png").resize(icon_size, Image.LANCZOS)
            Create_Document = Image.open("Image/criar.png").resize(icon_size, Image.LANCZOS)
            Add_image = Image.open("Image/documento.png").resize(icon_size, Image.LANCZOS)
            User_Infor= Image.open("Image/user.png").resize(icon_size, Image.LANCZOS)
            Documents_Placas = Image.open("Image/documents.png").resize(icon_size, Image.LANCZOS)
            # # Image_Criar = Image.open("Image/estatisticas.png").resize(icon_size, Image.LANCZOS)
            # # Image_Configuracao = Image.open("Image/configuracao.png").resize(icon_size, Image.LANCZOS)
            # # image7 = Image.open("sair.png").resize(icon_size, Image.LANCZOS)

            Home = ctk.CTkImage(light_image=Home_Logo, size=icon_size)
            Create = ctk.CTkImage(light_image=Create_Document, size=icon_size)
            Add = ctk.CTkImage(light_image=Add_image, size=icon_size)
            User = ctk.CTkImage(light_image=User_Infor, size=icon_size)
            Documents = ctk.CTkImage(light_image=Documents_Placas, size=icon_size)
            # # Criar = ctk.CTkImage(light_image=Image_Criar, size=icon_size)
            # # Configuracao = ctk.CTkImage(light_image=Image_Configuracao, size=icon_size)
            # # img7 = ctk.CTkImage(light_image=image7, size=icon_size)

            self.Frame_Widgets.grid_rowconfigure((0, 1, 2, 3, 4, 5 ), weight=1)
            self.Frame_Widgets.grid_columnconfigure(0, weight=1)

            icon_Home = ctk.CTkLabel(master=self.Frame_Widgets, image=Home, text="")
            icon_Home.grid(row=1, column=0, pady=10, padx=40, sticky="n")

            Icon_Create = ctk.CTkLabel(master=self.Frame_Widgets, image=Create, text="")
            Icon_Create.grid(row=2, column=0, pady=10, padx=40, sticky="n")

            icon_view = ctk.CTkLabel(master=self.Frame_Widgets, image=Add, text="")
            icon_view.grid(row=3, column=0, pady=10, padx=40, sticky="n")

            icon_User_infor = ctk.CTkLabel(master=self.Frame_Widgets, image=User, text="")
            icon_User_infor.grid(row=4, column=0, pady=10, padx=40, sticky="n")

            icon_Documents = ctk.CTkLabel(master=self.Frame_Widgets, image=Documents, text="")
            icon_Documents.grid(row=5, column=0, pady=10, padx=40, sticky="n")

            icon_Home.bind("<Button-1>", lambda e: Windows_Home.Show_Home())
            Icon_Create.bind("<Button-1>", lambda e : Windows_Create.Show_Edit())
            icon_view.bind("<Button-1>", lambda e : Windows_View.Show_View())
            icon_User_infor.bind("<Button-1>", lambda e : Windows_User_Infor.Show_User_Infor())
            icon_Documents.bind("<Button-1>", lambda e : Windows_Documents.Show_Documents())

            Windows_Home.Show_Home()
            self.w.mainloop()
    
class Window_Home():

    def __init__(self, master, frame_widgets):
        self.w = master
        self.Frame_Widgets = frame_widgets  # Armazena o Frame_Widgets

    def Show_Home(self):

        # Destroi o frame atual, se houver
        for widget in self.w.winfo_children():
            if isinstance(widget, ctk.CTkFrame) and widget != self.Frame_Widgets:
                widget.destroy()
        
        # Recria o Frame9 (o frame principal)
        self.Frame9 = ctk.CTkFrame(self.w, corner_radius=30)
        self.Frame9.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        # # Aqui você pode adicionar de volta os widgets que estavam no Frame9
        # largura_desejada = 1000# Exemplo de largura
        # altura_desejada = 1000 # Exemplo de altura

        # img_original = Image.open("Image/moveis-linhares.png")
        # img_resized = img_original.resize((largura_desejada, altura_desejada))  # Defina o tamanho desejado
        # img1 = ImageTk.PhotoImage(img_resized)

        # # Criar o label sem texto e com a imagem centralizada
        # l1 = ctk.CTkLabel(master=self.Frame9, image=img1, text="")  # Define text="" para remover o nome
        # l1.pack(anchor="center")  # Centraliza a imagem

class Window_Create():

     def __init__(self, master, frame_widgets):
        self.w = master
        self.Frame_Widgets = frame_widgets  # Armazena o Frame_Widgets
     

     def Show_Edit(self):

        # Destroi o frame atual, se houver
        for widget in self.w.winfo_children():
            if isinstance(widget, ctk.CTkFrame) and widget != self.Frame_Widgets:
                widget.destroy()
        
        # Recria o Frame9 (o frame principal)
        self.Frame9 = ctk.CTkFrame(self.w, corner_radius=30)
        self.Frame9.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
class Window_View():

     def __init__(self, master, frame_widgets):
        self.w = master
        self.Frame_Widgets = frame_widgets  # Armazena o Frame_Widgets
     

     def Show_View(self):

        # Destroi o frame atual, se houver
        for widget in self.w.winfo_children():
            if isinstance(widget, ctk.CTkFrame) and widget != self.Frame_Widgets:
                widget.destroy()
        
        # Recria o Frame9 (o frame principal)
        self.Frame9 = ctk.CTkFrame(self.w, corner_radius=30)
        self.Frame9.pack(side="left", fill="both", expand=True, padx=10, pady=10)

class Window_User_Infor():

     def __init__(self, master, frame_widgets):
        self.w = master
        self.Frame_Widgets = frame_widgets  # Armazena o Frame_Widgets
     

     def Show_User_Infor(self):

        # Destroi o frame atual, se houver
        for widget in self.w.winfo_children():
            if isinstance(widget, ctk.CTkFrame) and widget != self.Frame_Widgets:
                widget.destroy()
        
        # Recria o Frame9 (o frame principal)
        self.Frame9 = ctk.CTkFrame(self.w, corner_radius=30)
        self.Frame9.pack(side="left", fill="both", expand=True, padx=10, pady=10)

class Window_Documents():

     def __init__(self, master, frame_widgets):
        self.w = master
        self.Frame_Widgets = frame_widgets  # Armazena o Frame_Widgets
     

     def Show_Documents(self):

        # Destroi o frame atual, se houver
        for widget in self.w.winfo_children():
            if isinstance(widget, ctk.CTkFrame) and widget != self.Frame_Widgets:
                widget.destroy()
        
        # Recria o Frame9 (o frame principal)
        self.Frame9 = ctk.CTkFrame(self.w, corner_radius=30)
        self.Frame9.pack(side="left", fill="both", expand=True, padx=10, pady=10)












if __name__ == "__main__":
    logon = Logon()
    logon.mainloop()
