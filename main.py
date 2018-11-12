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

        for F in (Login, Chat, Register):
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
        self.controller = controller
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

        self.bntLogin = Button(self, text="Login")
        self.bntLogin["command"] = self.login
        self.bntLogin.pack(side=LEFT)

        button2 = Button(self, text="Register",
                         command=lambda: controller.show_frame(Register))
        button2.pack(side= RIGHT)

    def login(self):

        user = self.txtusuario.get()
        print(user)
        password = self.txtsenha.get()
        login_result = Chat_lib.login(user,password)
        print(login_result)
        if login_result:
            self.controller.show_frame(Chat)
            print('login sendo feito')

class Chat(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Chat", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        self.fonte = ("Verdana", "8")
        self.controller = controller
        self.container6 = Frame(self)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(self)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.lblmsg = Label(self.container7, text="Mensages:", font=self.fonte, width=10)
        self.lblmsg.pack(side=LEFT)
        self.mesages = Chat_lib.get_mesages()
        t = Text(self.container7)
        for mesage in self.mesages:
            t.insert(END,mesage + '\n')
        t.pack()

        self.lblmsg = Label(self.container6, text="Mensagem:", font=self.fonte, width=10)
        self.lblmsg.pack(side=LEFT)

        self.txtmsg = Entry(self.container6)
        self.txtmsg["width"] = 25
        self.txtmsg["font"] = self.fonte
        self.txtmsg.pack(side=LEFT)

        # button1 = Button(self, text="Back to Home",
        #                  command=lambda: controller.show_frame(Login))
        # button1.pack(side=LEFT)

        self.bntLogin = Button(self, text="Send")
        self.bntLogin["command"] = self.send_mesege
        self.bntLogin.pack(side=RIGHT)

    def send_mesege(self):
        msg = self.txtmsg.get()
        Chat_lib.send_mesage(msg)

    def update(self):
        self.mesages = Chat_lib.get_mesages()




class Register(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Register", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        self.controller = controller
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

        self.bntLogin = Button(self, text="Register")
        self.bntLogin["command"] = self.register
        self.bntLogin.pack(side=RIGHT)

        button2 = Button(self, text="Login",
                         command=lambda: controller.show_frame(Register))
        button2.pack(side=LEFT)

    def register(self):
        user = self.txtusuario.get()
        password = self.txtsenha.get()
        print(user)
        print(password)
        Chat_lib.register(user, password)
        self.controller.show_frame(Login)


app = SeaofBTCapp()

app.mainloop()