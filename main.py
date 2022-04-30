
import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self, *arg, **kwargs):
        tk.Tk.__init__(self, *arg, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage, Registration, Merch, Clothes, Cart, Account, Aboutus, Help):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky='nsew')

            self.show_frame('StartPage')

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#FFF0F5")
        self.controller = controller
        self.controller.title('Online shop')
        self.controller.state('zoomed')

        big_lable = tk.Label(self, text='Online\nshop', font=('Candara', 50, 'bold'),fg='black', bg='#FFF0F5')
        big_lable.pack(pady=30)

        login_lable = tk.Label(self, text='Insert your login', font=('Candara', 15, 'bold'),fg='black', bg='#FFF0F5')
        login_lable.pack(pady=30)

        my_login = tk.StringVar()
        login_entry = tk.Entry(self, textvariable=my_login, font=('Candara', 15, 'bold'),fg='black', bg='#FFF0F5')
        login_entry.pack(pady=30)

        password_lable = tk.Label(self, text='Insert your password', font=('Candara', 15, 'bold'),fg='black', bg='#FFF0F5')
        password_lable.pack(pady=30)

        my_password = tk.StringVar()
        password_entry = tk.Entry(self, textvariable=my_password, font=('Candara', 15, 'bold'),fg='black', bg='#FFF0F5')
        password_entry.pack(pady=30)

        def check_password():
            if my_password.get() == '0' and my_login.get() == 'O':
                controller.show_frame('MenuPage')

                # right_lable = tk.Label(self, text = "right answer")
                # right_lable.pack()
            else:
                right_lable['text'] = 'Wrong password'

        password_button = tk.Button(self, text='Check', command=check_password,font=('Candara', 15, 'bold'),fg='black', bg='#FFF0F5')
        password_button.pack()
        right_lable = tk.Label(self, font=('Candara', 15, 'bold'),fg='black', bg='#FFF0F5')
        right_lable.pack(pady=30)

        def registr():
            controller.show_frame('Registration')

        registr_button = tk.Button(self, text='Registartion', command=registr,
                                   font=('Candara', 15, 'bold'),fg='black', bg='white')
        registr_button.pack(pady=30)


class Registration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#FFF0F5')
        self.controller = controller

        heading_lable = tk.Label(self, text="Registration", font=('Candara', 50, 'bold'),fg='black', bg='#FFF0F5')
        heading_lable.pack(pady=25)

        name_1_lable = tk.Label(self, text="Surname", font=('Candara', 15, 'bold'),fg='black', bg='#FFF0F5')
        name_1_lable.pack(pady=25)

        name_1_entry = tk.Entry(self, font=('Candara', 15, 'bold'), fg="black")
        name_1_entry.pack(pady=0)

        name_2_lable = tk.Label(self, text="Name", font=('Candara', 15, 'bold'),fg='black', bg='#FFF0F5')
        name_2_lable.pack(pady=25)

        name_2_entry = tk.Entry(self, font=('Candara', 15, 'bold'), fg="black")
        name_2_entry.pack(pady=0)

        name_3_lable = tk.Label(self, text="Login", font=('Candara', 15, 'bold'),fg='black', bg='#FFF0F5')
        name_3_lable.pack(pady=25)

        name_3_entry = tk.Entry(self, font=('Candara', 15, 'bold'), fg="black")
        name_3_entry.pack(pady=0)

        name_4_lable = tk.Label(self, text="Password", font=('Candara', 15, 'bold'),fg='black', bg='#FFF0F5')
        name_4_lable.pack(pady=25)

        name_4_entry = tk.Entry(self, font=('Candara', 15, 'bold'), fg="black")
        name_4_entry.pack(pady=0)

        save_button = tk.Button(self, text="Create a new user", bg="white", width=25,
                                font=('Candara', 15, 'bold'), fg="black")
        save_button.pack()
        save_button.place(x=800, y=650)

        def back():
            controller.show_frame('StartPage')

        back_button = tk.Button(self, text='Back', command=back, font=('Candara', 15, 'bold'),fg='black', bg='white')
        back_button.pack(pady=30)
        back_button.place(x=920, y=700)

class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent,bg='white')
        self.controller=controller
        big_lable = tk.Label(self, text='Welcome to page', font=('Candara', 50, 'bold'), fg='black', bg='white')
        big_lable.pack(pady=30)
        big_lable.place(x=500, y=40)

        def get_template():
            controller.show_frame('Merch')

        contact_button = tk.Button(self, text="Merch", command=(get_template), font=('Candara', 10, 'bold'), fg='#292421', bg='#FFF0F5')
        contact_button.pack(pady=30)
        contact_button.place(x=30, y=10)

        def get_clothes():
            controller.show_frame('Clothes')

        contact_button = tk.Button(self, text="Clothes", command=(get_clothes), font=('Candara', 10, 'bold'), fg='#292421', bg='#FFF0F5')
        contact_button.pack(pady=30)
        contact_button.place(x=83, y=10)

        def get_subs():
            controller.show_frame('PaidSubscriptions')

        contact_button = tk.Button(self, text="Cart", command=(get_subs), font=('Candara', 10, 'bold'), fg='#292421', bg='#FFF0F5')
        contact_button.pack(pady=30)
        contact_button.place(x=139, y=10)

        def get_account():
            controller.show_frame('Account')

        contact_button = tk.Button(self, text="Personal Account", command=(get_account), font=('Candara', 10, 'bold'), fg='#292421', bg='#FFF0F5')
        contact_button.pack(pady=30)
        contact_button.place(x=180, y=10)

        def get_about():
            controller.show_frame('About us')

        contact_button = tk.Button(self, text="About us", command=(get_about), font=('Candara', 10, 'bold'), fg='#292421', bg='#FFF0F5')
        contact_button.pack(pady=30)
        contact_button.place(x=294, y=10)

        def get_help():
            controller.show_frame('Help')

        contact_button = tk.Button(self, text="Help", command=(get_help), font=('Candara', 10, 'bold'), fg='#292421', bg='#FFF0F5')
        contact_button.pack(pady=30)
        contact_button.place(x=360, y=10)

class Merch(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller
        self.controller.title('Online shop')
        self.controller.state('zoomed')

        big_lable = tk.Label(self, text='Merch', font=('Candara', 50, 'bold'), fg='black', bg='white')
        big_lable.pack(pady=30)
        text = tk.Label(self, text='', font=('Candara', 12, 'bold'), fg='black', bg='white')
        text.pack(pady=30)

        def return_MenuPage():
            controller.show_frame('MenuPage')

        return_button = tk.Button(self, text='Back', command=return_MenuPage,font=('Candara', 10, 'bold'), fg='white', bg='#FFF0F5')
        return_button.pack(pady=300)
        return_button.place(x=10, y=10)

class Clothes(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller
        self.controller.title('Online shop')
        self.controller.state('zoomed')

        big_lable = tk.Label(self, text='Clothes Available', font=('Candara', 50, 'bold'), fg='black', bg='white')
        big_lable.pack(pady=30)
        text = tk.Label(self, text='', font=('Candara', 12, 'bold'), fg='black', bg='white')
        text.pack(pady=30)

        def return_MenuPage():
            controller.show_frame('MenuPage')

        return_button = tk.Button(self, text='Back', command=return_MenuPage,font=('Candara', 10, 'bold'), fg='white', bg='#FFF0F5')
        return_button.pack(pady=300)
        return_button.place(x=10, y=10)

class Cart(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller
        self.controller.title('Online shop')
        self.controller.state('zoomed')

        big_lable = tk.Label(self, text='Cart', font=('Candara', 50, 'bold'), fg='black', bg='white')
        big_lable.pack(pady=30)
        text = tk.Label(self, text='', font=('Candara', 12, 'bold'), fg='black', bg='white')
        text.pack(pady=30)

        def return_MenuPage():
            controller.show_frame('MenuPage')

        return_button = tk.Button(self, text='Back', command=return_MenuPage,font=('Candara', 10, 'bold'), fg='white', bg='#FFF0F5')
        return_button.pack(pady=300)
        return_button.place(x=10, y=10)

class Account(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller
        self.controller.title('Online shop')
        self.controller.state('zoomed')

        big_lable = tk.Label(self, text='Personal Account', font=('Candara', 50, 'bold'), fg='black', bg='white')
        big_lable.pack(pady=30)
        text = tk.Label(self, text='', font=('Candara', 12, 'bold'), fg='black', bg='white')
        text.pack(pady=30)

        def return_MenuPage():
            controller.show_frame('MenuPage')

        return_button = tk.Button(self, text='Back', command=return_MenuPage,font=('Candara', 10, 'bold'), fg='white', bg='#FFF0F5')
        return_button.pack(pady=300)
        return_button.place(x=10, y=10)

class Aboutus(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller
        self.controller.title('Online shop')
        self.controller.state('zoomed')

        big_lable = tk.Label(self, text='Our Company and Services', font=('Candara', 50, 'bold'), fg='black', bg='white')
        big_lable.pack(pady=30)
        text = tk.Label(self, text='', font=('Candara', 12, 'bold'), fg='black', bg='white')
        text.pack(pady=30)

        def return_MenuPage():
            controller.show_frame('MenuPage')

        return_button = tk.Button(self, text='Back', command=return_MenuPage,font=('Candara', 10, 'bold'), fg='white', bg='#FFF0F5')
        return_button.pack(pady=300)
        return_button.place(x=10, y=10)

class Help(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller
        self.controller.title('Online shop')
        self.controller.state('zoomed')

        big_lable = tk.Label(self, text='Help Centre', font=('Candara', 50, 'bold'), fg='black', bg='white')
        big_lable.pack(pady=30)
        text = tk.Label(self, text='', font=('Candara', 12, 'bold'), fg='black', bg='white')
        text.pack(pady=30)

        def return_MenuPage():
            controller.show_frame('MenuPage')

        return_button = tk.Button(self, text='Back', command=return_MenuPage,font=('Candara', 10, 'bold'), fg='white', bg='#FFF0F5')
        return_button.pack(pady=300)
        return_button.place(x=10, y=10)

if __name__=='__main__':
    app = SampleApp()
    app.mainloop()
