from Encrypt import  Chat_lib
from tkinter import *

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Login, PageOne, Register):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Login)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Login(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Login", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        self.fonte = ("Verdana", "8")
        self.container6 = Frame(self)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(self)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()

        self.lblusuario = Label(self.container6, text="Usuário:", font=self.fonte, width=10)
        self.lblusuario.pack(side=LEFT)

        self.txtusuario = Entry(self.container6)
        self.txtusuario["width"] = 25
        self.txtusuario["font"] = self.fonte
        self.txtusuario.pack(side=LEFT)

        self.lblsenha = Label(self.container7, text="Senha:", font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(self.container7)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha["font"] = self.fonte
        self.txtsenha.pack(side=LEFT)



        button = Button(self, text="Login",
                           command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = Button(self, text="Register",
                         command=lambda: controller.show_frame(Register))
        button2.pack()


class PageOne(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = Button(self, text="Back to Home",
                         command=lambda: controller.show_frame(Login))
        button1.pack()

        button2 = Button(self, text="Page Two",
                         command=lambda: controller.show_frame(Register))
        button2.pack()


class Register(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Register", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        self.fonte = ("Verdana", "8")
        self.container6 = Frame(self)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(self)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()

        self.lblusuario = Label(self.container6, text="Usuário:", font=self.fonte, width=10)
        self.lblusuario.pack(side=LEFT)

        self.txtusuario = Entry(self.container6)
        self.txtusuario["width"] = 25
        self.txtusuario["font"] = self.fonte
        self.txtusuario.pack(side=LEFT)

        self.lblsenha = Label(self.container7, text="Senha:", font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(self.container7)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha["font"] = self.fonte
        self.txtsenha.pack(side=LEFT)

        button = Button(self, text="Login",
                        command=lambda: controller.show_frame(Login))
        button.pack()

        button2 = Button(self, text="Register",
                         command=lambda: controller.show_frame(Register))
        button2.pack()


app = SeaofBTCapp()
app.mainloop()