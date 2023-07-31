import random as rd
from tkinter import *
import mysql.connector as con
import time
import tkinter.messagebox as tmsg
import datetime
from tkinter import ttk
from getpass import getpass

password = getpass("Enter your MySQL password here: ")
database = getpass("Select your database-> ")

con = con.connect(host="localhost",
                    user="root",
                    password=password,
                    database=database)
cur = con.cursor()

root = Tk()
root.title("Library Management System")
root.geometry("1536x864+0+0")
root.wm_iconbitmap("icons\\library icon.ico")

class LoginWindow:
    def __init__(self, root):
        titleframe = Frame(root, height=64, borderwidth=6, relief=RIDGE)
        titleframe.pack(side=TOP, fill=X)
        l_photo = PhotoImage(file="icons\\library logo.png")
        logo = Label(titleframe, image=l_photo)
        logo.image = l_photo
        logo.grid(row=0, column=0)
        title = Label(titleframe, text="Library Management System", font=("Digital-7 Mono", 36, "bold", "underline"),
                      justify=CENTER, width=60)
        title.grid(row=0, column=1)
        self.window()
        self.toolbar()

    def window(self):
        self.login_frame = Frame(root, height=700, width=600, relief=SOLID, bg="cadetblue", borderwidth=8)
        self.login_frame.pack(pady=80)

        ask_frame = Frame(self.login_frame, height=100, width=600, relief=FLAT, bg="grey")
        ask_frame.pack()

        self.employe_frame = Frame(ask_frame, height=100, width=300, relief=SOLID, borderwidth=2, bg="grey")
        self.employe_frame.grid(row=0, column=0)
        self.student_frame = Frame(ask_frame, height=100, width=300, relief=SOLID, borderwidth=2, bg="grey")
        self.student_frame.grid(row=0, column=1)

        employe_photo = PhotoImage(file="icons\\employee.png")
        student_photo = PhotoImage(file="icons\\student.png")

        self.employe = Label(self.employe_frame, image=employe_photo, relief=FLAT, bg="grey")
        self.employe.image = employe_photo
        self.employe.grid(row=0, column=0)
        self.employe_button = Button(self.employe_frame, text="Employee", width=11, font=("Cambria", 20, "bold"), height=4,
                                bg="grey", relief=FLAT, command=lambda: self.choose(self.employe_button))
        self.employe_button.grid(row=0, column=1)

        self.student = Label(self.student_frame, image=student_photo, relief=FLAT, bg="grey")
        self.student.image = student_photo
        self.student.grid(row=0, column=0)
        self.student_button = Button(self.student_frame, text="Customer", width=11, font=("Cambria", 20, "bold"), height=4,
                                bg="grey", relief=FLAT, command=lambda: self.choose(self.student_button))
        self.student_button.grid(row=0, column=1)

        self.user_value = StringVar()
        self.pass_value = StringVar()

        login = Frame(self.login_frame, height=500, width=500, relief=SOLID, bg="cadetblue", pady=24)
        login.pack()

        user_photo = PhotoImage(file="icons\\username.png")
        username = Label(login, text="Username:", font=("Cooper", 16, "bold"), padx=12, bg="cadetblue")
        username.grid(row=0, column=0)
        username_photo = Label(login, image=user_photo, bg="cadetblue")
        username.image = user_photo
        username_photo.grid(row=0, column=1)

        pass_photo = PhotoImage(file="icons\\password.png")
        password = Label(login, text="Password:", font=("Cooper", 16, "bold"), padx=12, bg="cadetblue")
        password.grid(row=1, column=0)
        password_photo = Label(login, image=pass_photo, bg="cadetblue")
        password_photo.image = pass_photo
        password_photo.grid(row=1, column=1)

        user_entry = Entry(login, textvariable=self.user_value, font=("Arial", 18), width=32, borderwidth=4, relief=SUNKEN)
        user_entry.grid(row=0, column=2, padx=16, pady=16)
        pass_entry = Entry(login, textvariable=self.pass_value, show="*", font=("Arial", 18), width=32, borderwidth=4, relief=SUNKEN)
        pass_entry.bind('<Return>', self.enter)
        pass_entry.grid(row=1, column=2, padx=16)

        forgot_pass = Button(login, text="Forgot Password??", font=("Arial", 12, "bold"), relief=FLAT, bg="cadetblue")
        forgot_pass.bind('<Button-1>', self.forgot_password)
        forgot_pass.grid(row=2, column=2, pady=4)

        l_a_frame = Frame(self.login_frame, width=600, height=100, relief=SOLID, borderwidth=2, bg="cadetblue")
        l_a_frame.pack(pady=12)

        login_photo = PhotoImage(file="icons\\login.png")
        exit_photo = PhotoImage(file="icons\\exit.png")

        main_login = Frame(l_a_frame, width=300, height=100, relief=SOLID, borderwidth=2, bg="cadetblue")
        main_login.grid(row=0, column=0)
        main_exit = Frame(l_a_frame, width=300, height=100, relief=SOLID, borderwidth=2, bg="cadetblue")
        main_exit.grid(row=0, column=1)

        m_login_photo = Label(main_login, image=login_photo, relief=FLAT, bg="cadetblue")
        m_login_photo.image = login_photo
        m_login_photo.grid(row=0, column=0)
        m_login_button = Button(main_login, text="Login", height=4, font=("Cambria", 14, "bold"), relief=FLAT, width=10, bg="cadetblue")
        m_login_button.bind('<Button-1>', self.enter)
        m_login_button.grid(row=0, column=1)

        m_exit_photo = Label(main_exit, image=exit_photo, relief=FLAT, bg="cadetblue")
        m_exit_photo.image = exit_photo
        m_exit_photo.grid(row=0, column=0)
        m_exit_button = Button(main_exit, text="Exit", height=4, font=("Cambria", 14, "bold"), relief=FLAT, width=10,
                               bg="cadetblue", command=lambda: root.destroy())
        m_exit_button.grid(row=0, column=1)

    def forgot_password(self, event):
        fp = Toplevel()
        fp.geometry("800x400")
        fp.title("Forgot Password")
        fp.wm_iconbitmap("icons\\library icon.ico")

        User = StringVar()
        fPass = StringVar()

        def change_pass():
            new_pass = fPass.get()
            new_user = User.get()
            if self.student_frame["bg"] == "pink":
                cur.execute(f"update customer set Cus_Password='{new_pass}' where Cus_Username='{new_user}'")
                con.commit()
                fp.destroy()

            elif self.employe_frame["bg"] == "pink":
                cur.execute(f"update employee set Emp_Password='{new_pass}' where Emp_Username='{new_user}'")
                con.commit()
                fp.destroy()

            time.sleep(0.02)
            tmsg.showinfo("Successfull!!", "You New Password has been changed successfully!!")

        username = Label(fp, text="Username:", font=("Cooper", 16, "bold"), padx=12)
        username.grid(row=0, column=0)
        f_password = Label(fp, text="Password:", font=("Cooper", 16, "bold"), padx=12)
        f_password.grid(row=1, column=0)

        User_entry = Entry(fp, textvariable=User, font=("Arial", 18), width=32, borderwidth=4, relief=SUNKEN)
        User_entry.grid(row=0, column=1, pady=16)
        Pass_entry = Entry(fp, textvariable=fPass, font=("Arial", 18), width=32, borderwidth=4, relief=SUNKEN)
        Pass_entry.grid(row=1, column=1, pady=16)

        fButton = Button(fp, text="Change", font=("Arial", 20, "bold"), borderwidth=4, relief=SOLID, width=8,
                         justify=CENTER, command=change_pass)
        fButton.grid(row=2, column=1)

    def enter(self, event):
        UserName = self.user_value.get()
        PassWord = self.pass_value.get()

        if self.student_frame["bg"]=="pink":
            cur.execute(f"Select Cus_Username, Cus_Password from customer where Cus_Username='{UserName}' and Cus_Password='{PassWord}'")
            data = cur.fetchall()
            if data==[]:
                tmsg.showerror("Library Management System", "Please enter valid username and password....")

            else:
                time.sleep(0.2)
                hour = int(datetime.datetime.now().hour)

                if hour >= 0 and hour < 12:
                    tmsg.showinfo("Welcome", "Good Morning!!")
                    self.hide_widget()
                    win3 = StudentLogin(root)
                elif hour >= 12 and hour < 18:
                    tmsg.showinfo("Welcome", "Good Afternoon!!")
                    self.hide_widget()
                    win3 = StudentLogin(root)
                else:
                    tmsg.showinfo("Welcome", "Good evening!!")
                    self.hide_widget()
                    win3 = StudentLogin(root)

        elif self.employe_frame["bg"]=="pink":
            cur.execute(f"Select Emp_Username, Emp_Password from employee where Emp_Username='{UserName}' and Emp_Password='{PassWord}'")
            data = cur.fetchall()

            if data==[]:
                tmsg.showerror("Library Management System", "Please enter valid username and password....")

            else:
                time.sleep(0.02)
                hour = int(datetime.datetime.now().hour)

                if hour >= 0 and hour < 12:
                    tmsg.showinfo("Welcome", "Good Morning!!")
                    self.hide_widget()
                    win2 = MainWindow(root)
                elif hour >= 12 and hour < 18:
                    tmsg.showinfo("Welcome", "Good Afternoon!!")
                    self.hide_widget()
                    win2 = MainWindow(root)
                else:
                    tmsg.showinfo("Welcome", "Good evening!!")
                    self.hide_widget()
                    win2 = MainWindow(root)

    def choose(self, button):
        if button["text"] == "Employee" and button["bg"] == "grey":
            button["bg"] = "pink"
            self.employe["bg"] = "pink"
            self.employe_frame["bg"] = "pink"
            self.student["bg"] = "grey"
            self.student_button["bg"] = "grey"
            self.student_frame["bg"] = "grey"

        elif button["text"] == "Employee" and button["bg"] == "pink":
            button["bg"] = "grey"
            self.employe["bg"] = "grey"
            self.employe_frame["bg"] = "grey"
            self.student["bg"] = "grey"
            self.student_button["bg"] = "grey"
            self.student_frame["bg"] = "grey"

        elif button["text"] == "Customer" and button["bg"] == "grey":
            button["bg"] = "pink"
            self.student["bg"] = "pink"
            self.student_frame["bg"] = "pink"
            self.employe["bg"] = "grey"
            self.employe_button["bg"] = "grey"
            self.employe_frame["bg"] = "grey"

        elif button["text"] == "Customer" and button["bg"] == "pink":
            button["bg"] = "grey"
            self.student["bg"] = "grey"
            self.student_frame["bg"] = "grey"
            self.employe["bg"] = "grey"
            self.employe_button["bg"] = "grey"
            self.employe_frame["bg"] = "grey"

    def hide_widget(self):
        self.login_frame.pack_forget()

    def toolbar(self):
        self.menubar = Menu(root)

        self.view_calls()
        self.view_more()

        root.config(menu=self.menubar)

    def view_calls(self):
        self.calls = Menu(self.menubar, tearoff=0)
        phone = Menu(self.calls, tearoff=0)
        self.calls.add_cascade(label="Phone Number", menu=phone)
        phone.add_command(label="8980063001", font=("cooper", 14, "bold"))
        phone.add_command(label="0260-2404300", font=("cooper", 14, "bold"))
        self.calls.add_separator()
        mail = Menu(self.calls, tearoff=0)
        self.calls.add_cascade(label="Mail", menu=mail)
        mail.add_command(label="lib.db@vallabhashram.in", font=("cooper", 14, "bold"))
        self.calls.add_separator()
        location = Menu(self.calls, tearoff=0)
        self.calls.add_cascade(label="Location", menu=location)
        location.add_command(label="N.H. NO.48, Killa-Pardi District-Valsad", font=("cooper", 14))
        location.add_command(label="Gujarat, India-(396 125)", font=("cooper", 14))
        self.menubar.add_cascade(label="Contact Us", menu=self.calls)

    def view_more(self):
        self.more = Menu(self.menubar, tearoff=0)
        self.more.add_command(label="Create New Account", command=self.new_account)
        self.more.add_command(label="Delete Your Account", command=self.delete_account)
        self.more.add_separator()
        self.more.add_command(label="FeedBack", command=feedback)
        self.more.add_separator()
        self.more.add_command(label="About Us", command=about)
        self.menubar.add_cascade(label="More", menu=self.more)

    def new_account(self):
        self.new = Toplevel()
        self.new.title("Library Management System")
        self.new.geometry("640x640+500+80")
        self.new.wm_iconbitmap("icons\\library icon.ico")

        id_label = Label(self.new, text="Id: ", font=("Arial", 16, "bold"), width=20, justify=CENTER)
        id_label.grid(row=0, column=0, pady=8)
        name_label = Label(self.new, text="Name: ", font=("Arial", 16, "bold"), width=20, justify=CENTER)
        name_label.grid(row=1, column=0, pady=8)
        surname_label = Label(self.new, text="Surname: ", font=("Arial", 16, "bold"), width=20, justify=CENTER)
        surname_label.grid(row=2, column=0, pady=8)
        username_label = Label(self.new, text="Username: ", font=("Arial", 16, "bold"), width=20, justify=CENTER)
        username_label.grid(row=3, column=0, pady=8)
        password_label = Label(self.new, text="Password: ", font=("Arial", 16, "bold"), width=20, justify=CENTER)
        password_label.grid(row=4, column=0, pady=8)
        age_label = Label(self.new, text="Age: ", font=("Arial", 16, "bold"), width=20, justify=CENTER)
        age_label.grid(row=5, column=0, pady=8)
        phone_label = Label(self.new, text="Contact Number: ", font=("Arial", 16, "bold"), width=20, justify=CENTER)
        phone_label.grid(row=6, column=0, pady=8)

        self.add_idvalue = StringVar()
        self.add_namevalue = StringVar()
        self.add_surnamevalue = StringVar()
        self.add_usernamevalue = StringVar()
        self.add_passwordvalue = StringVar()
        self.add_agevalue = StringVar()
        self.add_phonevalue = StringVar()

        id_entry = Entry(self.new, textvariable=self.add_idvalue, state=DISABLED, font=("Arial", 16, "bold"), width=24 ,borderwidth=2, relief=SUNKEN)
        id_entry.grid(row=0, column=1)
        name_entry = Entry(self.new, textvariable=self.add_namevalue, font=("Arial", 16, "bold"), width=24 ,borderwidth=2, relief=SUNKEN)
        name_entry.grid(row=1, column=1)
        surname_entry = Entry(self.new, textvariable=self.add_surnamevalue, font=("Arial", 16, "bold"), width=24 ,borderwidth=2, relief=SUNKEN)
        surname_entry.grid(row=2, column=1)
        username_entry = Entry(self.new, textvariable=self.add_usernamevalue, font=("Arial", 16, "bold"), width=24 ,borderwidth=2, relief=SUNKEN)
        username_entry.grid(row=3, column=1)
        password_entry = Entry(self.new, textvariable=self.add_passwordvalue, font=("Arial", 16, "bold"), width=24 ,borderwidth=2, relief=SUNKEN)
        password_entry.grid(row=4, column=1)
        age_entry = Entry(self.new, textvariable=self.add_agevalue, font=("Arial", 16, "bold"), width=24 ,borderwidth=2, relief=SUNKEN)
        age_entry.grid(row=5, column=1)
        phone_entry = Entry(self.new, textvariable=self.add_phonevalue, font=("Arial", 16, "bold"), width=24 ,borderwidth=2, relief=SUNKEN)
        phone_entry.grid(row=6, column=1)

        self.random_id()

        if self.student_frame["bg"]=="pink":
            create_button = Button(self.new, text="Create", font=("Arial", 16, "bold"), borderwidth=4, relief=SOLID, width=8)
            create_button.bind('<Button-1>', self.customer_create)
            create_button.grid(row=7, column=1, pady=12)

        elif self.employe_frame["bg"] == "pink":
            create_button = Button(self.new, text="Create", font=("Arial", 16, "bold"), borderwidth=4, relief=SOLID, width=8)
            create_button.bind('<Button-1>', self.employee_create)
            create_button.grid(row=7, column=1, pady=12)

    def random_id(self):
        cur.execute("select Cus_Id from customer_details")
        data = cur.fetchall()

        self.id_list = []
        for i in data:
            self.id_list.append(i)

        id = rd.randrange(100, 999)

        if id in self.id_list:
            pass
        else:
            self.add_idvalue.set(id)

    def customer_create(self, event):
        cur.execute(f"insert into customer values ({self.add_idvalue.get()}, '{self.add_namevalue.get()}', '{self.add_surnamevalue.get()}', '{self.add_usernamevalue.get()}', '{self.add_passwordvalue.get()}', {self.add_agevalue.get()}, '{self.add_phonevalue.get()}')")
        con.commit()
        tmsg.showinfo("Library Management System", "Your account has been created successfully!!")
        self.new.destroy()

    def employee_create(self, event):
        cur.execute(f"insert into employee values ({self.add_idvalue.get()}, '{self.add_namevalue.get()}', '{self.add_surnamevalue.get()}', '{self.add_usernamevalue.get()}', '{self.add_passwordvalue.get()}', {self.add_agevalue.get()}, '{self.add_phonevalue.get()}')")
        con.commit()
        tmsg.showinfo("Library Management System", "Your account has been created successfully!!")
        self.new.destroy()

    def delete_account(self):
        self.ask = Toplevel()
        self.ask.title("Library Management System")
        self.ask.geometry("400x400+600+200")
        self.ask.wm_iconbitmap("icons\\library icon.ico")

        id_label = Label(self.ask, text="Id: ", font=("Arial", 14, "bold"), width=12, justify=CENTER)
        id_label.grid(row=0, column=0, pady=12)
        username_label = Label(self.ask, text="Username: ", font=("Arial", 14, "bold"), width=12, justify=CENTER)
        username_label.grid(row=1, column=0, pady=12)

        self.delete_idvalue = StringVar()
        self.delete_uservalue = StringVar()

        id_entry = Entry(self.ask, textvariable=self.delete_idvalue, font=("Arial", 16, "bold"), width=16, borderwidth=2, relief=SUNKEN)
        id_entry.grid(row=0, column=1)
        name_entry = Entry(self.ask, textvariable=self.delete_uservalue, font=("Arial", 16, "bold"), width=16, borderwidth=2, relief=SUNKEN)
        name_entry.grid(row=1, column=1)

        if self.student_frame["bg"]=="pink":
            delete_button = Button(self.ask, text="Delete", font=("Arial", 16, "bold"), borderwidth=4, relief=SOLID, width=8)
            delete_button.bind('<Button-1>', self.customer_delete)
            delete_button.grid(row=2, column=1, pady=16)

        elif self.employe_frame["bg"] == "pink":
            delete_button = Button(self.ask, text="Delete", font=("Arial", 16, "bold"), borderwidth=4, relief=SOLID, width=8)
            delete_button.bind('<Button-1>', self.employee_delete)
            delete_button.grid(row=2, column=1, pady=16)

    def customer_delete(self, event):
        cur.execute(f"select * from customer where Cus_Id={self.delete_idvalue.get()} and Cus_Username='{self.delete_uservalue.get()}'")
        data = cur.fetchall()
        yes_no = tmsg.askyesno("Library Management System", "Do you really want to delete your account permanently??")

        if yes_no==YES:
            for i in data:
                a1 = i[0]
                a2 = i[1]
                a3 = i[2]
                a4 = i[3]
                a5 = i[4]
                a6 = i[5]
                a7 = i[6]

                cur.execute(f"insert into left_customer values ({a1}, '{a2}', '{a3}', '{a4}', '{a5}', {a6}, '{a7}')")

            cur.execute(f"delete from customer where Cus_Id={self.delete_idvalue.get()} and Cus_Username='{self.delete_uservalue.get()}'")
            con.commit()
            tmsg.showinfo("Library Management System", "Your account has been deleted successfully!!")
            self.ask.destroy()


    def employee_delete(self, event):
        cur.execute(
            f"select * from employee where Emp_Id={self.delete_idvalue.get()} and Emp_Username='{self.delete_uservalue.get()}'")
        data = cur.fetchall()
        yes_no = tmsg.askyesno("Library Management System", "Do you really want to delete your account permanently??")

        if yes_no == YES:
            for i in data:
                a1 = i[0]
                a2 = i[1]
                a3 = i[2]
                a4 = i[3]
                a5 = i[4]
                a6 = i[5]
                a7 = i[6]

                cur.execute(f"insert into left_employee values ({a1}, '{a2}', '{a3}', '{a4}', '{a5}', {a6}, '{a7}')")

            cur.execute(f"delete from employee where Emp_Id={self.delete_idvalue.get()} and Emp_Username='{self.delete_uservalue.get()}'")
            con.commit()
            tmsg.showinfo("Library Management System", "Your account has been deleted successfully!!")
            self.ask.destroy()

class MainWindow:
    def __init__(self, root):
        self.working_frame = Frame(root, height=600, width=1520)
        self.working_frame.pack(pady=8)
        self.button_frame = Frame(root, width=1520, height=60)
        self.button_frame.pack(pady=4)
        self.main_frames()
        self.library_info()
        self.list_book_names()
        self.mainwindow_buttons()
        self.library_table()
        self.toolbar()

    def main_frames(self):
        self.library_details = Frame(self.working_frame, height=600, width=900, relief=RIDGE, borderwidth=4, bg="cadetblue")
        self.library_details.grid(row=0, column=0)
        self.booklist_frame = Frame(self.working_frame, height=600, width=600, relief=RIDGE, borderwidth=4, bg="powder blue")
        self.booklist_frame.grid(row=0, column=1, padx=4)

        self.lib_details_frame = LabelFrame(self.library_details, text="Library Details: ", width=900, font=("new times roman", 16, "bold", "underline"), height=330, relief=RIDGE, borderwidth=8, bg="powder blue")
        self.lib_details_frame.grid(row=0, column=0)
        self.lib_info_frame = LabelFrame(self.library_details, text="Library Information: ", font=("new times roman", 16, "bold", "underline"), width=900, height=270, relief=RIDGE, borderwidth=8, bg="powder blue", pady=8)
        self.lib_info_frame.grid(row=1, column=0)
        self.book_photo_frame = LabelFrame(self.booklist_frame, text="Book Photo: ", font=("new times roman", 16, "bold", "underline"), height=300, width=600, relief=RIDGE, borderwidth=8)
        self.book_photo_frame.grid(row=0, column=0)
        self.book_name_frame = LabelFrame(self.booklist_frame, text="Book List: ", font=("new times roman", 16, "bold", "underline"), height=300, width=600, relief=RIDGE, borderwidth=8, bg="powder blue", pady=8)
        self.book_name_frame.grid(row=1, column=0)

    def library_info(self):
        #Making Labels:-
        self.id = Label(self.lib_details_frame, text="ID: ", font=("arial", 16, "bold"), bg="powder blue", width=16)
        self.id.grid(row=0, column=0, stick=W, pady=6)
        self.name = Label(self.lib_details_frame, text="Name: ", font=("arial", 16, "bold"), bg="powder blue", width=16)
        self.name.grid(row=1, column=0, stick=W, pady=6)
        self.surname = Label(self.lib_details_frame, text="Surname: ", font=("arial", 16, "bold"), bg="powder blue", width=16)
        self.surname.grid(row=2, column=0, stick=W, pady=6)
        self.phone_number = Label(self.lib_details_frame, text="Phone Number: ", font=("arial", 16, "bold"), width=16, bg="powder blue")
        self.phone_number.grid(row=3, column=0, stick=W, pady=6)
        self.book_id = Label(self.lib_details_frame, text="Book Id: ", font=("arial", 16, "bold"), width=16, bg="powder blue")
        self.book_id.grid(row=0, column=2, pady=6)
        self.book_name = Label(self.lib_details_frame, text="Book Name: ", font=("arial", 16, "bold"), width=16, bg="powder blue")
        self.book_name.grid(row=1, column=2, pady=6)
        self.issued_date = Label(self.lib_details_frame, text="Issued Date: ", font=("arial", 16, "bold"), width=16, bg="powder blue")
        self.issued_date.grid(row=2, column=2, pady=6)
        self.due_date = Label(self.lib_details_frame, text="Due Date: ", font=("arial", 16, "bold"), width=16, bg="powder blue")
        self.due_date.grid(row=3, column=2, pady=6)
        self.fine = Label(self.lib_details_frame, text="Fine: ", font=("arial", 16, "bold"), width=16, bg="powder blue")
        self.fine.grid(row=4, column=2, pady=6)

        #Making Entries:-
        self.idvalue = StringVar()
        self.namevalue = StringVar()
        self.surnamevalue = StringVar()
        self.phonevalue = StringVar()
        self.book_idvalue = StringVar()
        self.book_namevalue = StringVar()
        self.issuedvalue = StringVar()
        self.duevalue = StringVar()
        self.finevalue = StringVar()

        self.id_entry = Entry(self.lib_details_frame, font=("arial", 16), state=DISABLED, width=18, textvariable=self.idvalue)
        self.id_entry.grid(row=0, column=1, pady=6, padx=4)
        self.name_entry = Entry(self.lib_details_frame, font=("arial", 16), width=18, textvariable=self.namevalue)
        self.name_entry.grid(row=1, column=1, pady=6, padx=4)
        self.surname_entry = Entry(self.lib_details_frame, font=("arial", 16), width=18, textvariable=self.surnamevalue)
        self.surname_entry.grid(row=2, column=1, pady=6, padx=4)
        self.phone_number_entry = Entry(self.lib_details_frame, font=("arial", 16), width=18, textvariable=self.phonevalue)
        self.phone_number_entry.grid(row=3, column=1, pady=6, padx=4)
        self.book_id_entry = Entry(self.lib_details_frame, font=("arial", 16), width=18, textvariable=self.book_idvalue)
        self.book_id_entry.grid(row=0, column=3, pady=6, padx=4)
        self.book_name_entry = Entry(self.lib_details_frame, font=("arial", 16), state=DISABLED, width=18, textvariable=self.book_namevalue)
        self.book_name_entry.grid(row=1, column=3, pady=6, padx=4)
        self.issued_date_entry = Entry(self.lib_details_frame, font=("arial", 16), state=DISABLED, width=18, textvariable=self.issuedvalue)
        self.issued_date_entry.grid(row=2, column=3, pady=6, padx=4)
        self.due_date_entry = Entry(self.lib_details_frame, font=("arial", 16), state=DISABLED, width=18, textvariable=self.duevalue)
        self.due_date_entry.grid(row=3, column=3, pady=6, padx=4)
        self.fine_entry = Entry(self.lib_details_frame, font=("arial", 16), width=18, textvariable=self.finevalue)
        self.fine_entry.grid(row=4, column=3, pady=4, padx=6)

        self.random_id()

    def list_book_names(self):
        #Making scrollbar:-
        scrollbar = Scrollbar(self.book_name_frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        #Making list of books:-
        self.list_of_books = ["Python Programming (Class 11)", "Python Programming (Class 12)", "Wings of Fire", "Harry Porter", "Top 5000 Fun Facts", "Gulliver Travels", "Guiness World Records",
                         "All about CALCULUS", "General Knowledge", "Let's Play a Game", "Physics Around Us", "Human Encyclopedia", "Marvel Cinematic Universe", "Mysteries of Universe"]
        self.list_bookid = ["BKID482", "BKID642", "BKID871", "BKID382", "BKID905", "BKID460", "BKID973", "BKID142", "BKID467", "BKID712", "BKID512", "BKID840", "BKID862", "BKID321"]

        self.book_list = Listbox(self.book_name_frame, width=62, font=("arial", 13), relief=SUNKEN, yscrollcommand=scrollbar.set)
        self.book_list.bind('<<ListboxSelect>>', self.book_photo)
        self.book_list.pack(fill=BOTH)
        scrollbar.config(command=self.book_list.yview)

        for items in self.list_of_books:
            self.book_list.insert(END, items)

    def book_photo(self, event):
        try:
            value = str(self.book_list.get(self.book_list.curselection()))
            x = value

            borrowed_days = int(rd.randrange(8, 16))

            fine_ask = ["yes", "no"]
            ask = rd.choice(fine_ask)

            if x=="Python Programming (Class 11)":
                file = "Python Programming (Class 11)"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[0])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1+d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                if ask=="yes":
                    self.finevalue.set("Rs. "+str(rd.randrange(40, 160, 10)))
                else:
                    self.finevalue.set("")

            elif x=="Python Programming (Class 12)":
                file = "Python Programming (Class 12)"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[1])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                if ask == "yes":
                    self.finevalue.set("Rs. " + str(rd.randrange(40, 160, 10)))
                else:
                    self.finevalue.set("")

            elif x=="Wings of Fire":
                file = "Wings of Fire"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[2])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                if ask == "yes":
                    self.finevalue.set("Rs. " + str(rd.randrange(40, 160, 10)))
                else:
                    self.finevalue.set("")

            elif x=="Harry Porter":
                file = "Harry Porter"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[3])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                if ask == "yes":
                    self.finevalue.set("Rs. " + str(rd.randrange(40, 160, 10)))
                else:
                    self.finevalue.set("")

            elif x=="All about CALCULUS":
                file = "All about CALCULUS"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[4])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                if ask == "yes":
                    self.finevalue.set("Rs. " + str(rd.randrange(40, 160, 10)))
                else:
                    self.finevalue.set("")

            elif x=="Let's Play a Game":
                file = "Let's Play a Game"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[5])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                if ask == "yes":
                    self.finevalue.set("Rs. " + str(rd.randrange(40, 160, 10)))
                else:
                    self.finevalue.set("")

            elif x=="General Knowledge":
                file = "General Knowledge"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[6])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                if ask == "yes":
                    self.finevalue.set("Rs. " + str(rd.randrange(40, 160, 10)))
                else:
                    self.finevalue.set("")

            elif x=="Physics Around Us":
                file = "Physics Around Us"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[7])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                if ask == "yes":
                    self.finevalue.set("Rs. " + str(rd.randrange(40, 160, 10)))
                else:
                    self.finevalue.set("")

            elif x=="Human Encyclopedia":
                file = "Human Encyclopedia"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[8])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                if ask == "yes":
                    self.finevalue.set("Rs. " + str(rd.randrange(40, 160, 10)))
                else:
                    self.finevalue.set("")

            elif x=="Top 5000 Fun Facts":
                file = "Top 5000 Fun Facts"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[9])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                if ask == "yes":
                    self.finevalue.set("Rs. " + str(rd.randrange(40, 160, 10)))
                else:
                    self.finevalue.set("")

            elif x=="Gulliver Travels":
                file = "Gulliver Travels"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[10])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                if ask == "yes":
                    self.finevalue.set("Rs. " + str(rd.randrange(40, 160, 10)))
                else:
                    self.finevalue.set("")

            elif x=="Marvel Cinematic Universe":
                file = "Marvel Cinematic Universe"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[11])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                if ask == "yes":
                    self.finevalue.set("Rs. " + str(rd.randrange(40, 160, 10)))
                else:
                    self.finevalue.set("")

            elif x=="Guiness World Records":
                file = "Guiness World Records"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[12])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                if ask == "yes":
                    self.finevalue.set("Rs. " + str(rd.randrange(40, 160, 10)))
                else:
                    self.finevalue.set("")

            elif x=="Mysteries of Universe":
                file = "Mysteries of Universe"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[13])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                if ask == "yes":
                    self.finevalue.set("Rs. " + str(rd.randrange(40, 160, 10)))
                else:
                    self.finevalue.set("")
        except Exception as e:
            pass

    def library_table(self):
        #Creating Scrollbar:-
        scroll_x = ttk.Scrollbar(self.lib_info_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.lib_info_frame, orient=VERTICAL)


        self.lib_table = ttk.Treeview(self.lib_info_frame, height=11, column=("Cus_Id", "Cus_Name", "Cus_Surname",
                                                                   "Cus_Mob", "Book_Id", "Book_Name",
                                                                   "Issue_Date", "Due_Date", "Fine"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.lib_table.xview())
        scroll_y.config(command=self.lib_table.yview())

        self.lib_table.heading("Cus_Id", text="ID")
        self.lib_table.heading("Cus_Name", text="Name")
        self.lib_table.heading("Cus_Surname", text="Surname")
        self.lib_table.heading("Cus_Mob", text="Phone Number")
        self.lib_table.heading("Book_Id", text="ID")
        self.lib_table.heading("Book_Name", text="Book Name")
        self.lib_table.heading("Issue_Date", text="Issue Date")
        self.lib_table.heading("Due_Date", text="Due Date")
        self.lib_table.heading("Fine", text="Fine")


        self.lib_table["show"]="headings"

        self.lib_table.column("Cus_Id", width=75)
        self.lib_table.column("Cus_Name", width=100)
        self.lib_table.column("Cus_Surname", width=100)
        self.lib_table.column("Cus_Mob", width=100)
        self.lib_table.column("Book_Id", width=100)
        self.lib_table.column("Book_Name", width=120)
        self.lib_table.column("Issue_Date", width=105)
        self.lib_table.column("Due_Date", width=105)
        self.lib_table.column("Fine", width=70)

        self.lib_table.bind('<ButtonRelease-1>', self.get_cursor)
        self.show_record()

        self.lib_table.pack(fill=BOTH, expand=1)

    def mainwindow_buttons(self):
        self.addbutton = Button(self.button_frame, text="Issue Book", width=14, font=("new times roman", 20, "bold"), borderwidth=4, justify=CENTER, relief=SOLID, command=self.add_button)
        self.addbutton.grid(row=0, column=0, padx=12)
        self.deletebutton = Button(self.button_frame, text="Delete Data", width=14, font=("new times roman", 20, "bold"), borderwidth=4, justify=CENTER, relief=SOLID, command=self.delete_button)
        self.deletebutton.grid(row=0, column=1, padx=12)
        self.updatebutton = Button(self.button_frame, text="Update Data", width=14, font=("new times roman", 20, "bold"), borderwidth=4, justify=CENTER, relief=SOLID, command=self.update_button)
        self.updatebutton.grid(row=0, column=2, padx=12)
        self.resetbutton = Button(self.button_frame, text="Reset Data", width=14, font=("new times roman", 20, "bold"), borderwidth=4, justify=CENTER, relief=SOLID, command=self.reset_button)
        self.resetbutton.grid(row=0, column=3, padx=12)
        self.exitbutton = Button(self.button_frame, text="Exit Window", width=14, font=("new times roman", 20, "bold"), borderwidth=4, justify=CENTER, relief=SOLID, command=self.exit)
        self.exitbutton.grid(row=0, column=4, padx=12)

    def exit(self):
        ask = tmsg.askyesno("Library Management System", "Do you really want to exit??")

        if ask==YES:
            tmsg.showinfo("Library Management System", "Your account has been logged out succesfully\nHave a nive day!!")
            root.destroy()

    def add_button(self):
        if self.idvalue=="" and self.namevalue=="":
            tmsg.showerror("Library Management System", "Please enter valid data!!")

        else:
            cur.execute(f"insert into customer_details values ({self.idvalue.get()}, '{self.namevalue.get() }', '{self.surnamevalue.get()}', {self.phonevalue.get()}, '{self.book_idvalue.get()}', '{self.book_namevalue.get()}', '{self.issuedvalue.get()}', '{self.duevalue.get()}', '{self.finevalue.get()}')")
            self.show_record()
            con.commit()
            tmsg.showinfo("Library Management System", "Your record has been added successfully!!")

    def show_record(self):
        cur.execute(f"select * from customer_details")
        data = cur.fetchall()

        for record in self.lib_table.get_children():
            self.lib_table.delete(record)

        if len(data)!=0:
            for i in data:
                self.lib_table.insert(parent="", index=END, value=i)

    def delete_button(self):
        cur.execute(f"select * from customer_details where Cus_Name='{self.namevalue.get()}' and Cus_Surname='{self.surnamevalue.get()}'")
        data = cur.fetchall()

        for i in data:
            a1 = i[0]
            a2 = i[1]
            a3 = i[2]
            a4 = i[3]
            a5 = i[4]
            a6 = i[5]
            a7 = i[6]
            a8 = i[7]
            a9 = i[8]

            cur.execute(f"insert into delete_cus_details values ('{a1}', '{a2}', '{a3}', {a4}, '{a5}', '{a6}' ,'{a7}', '{a8}', '{a9}')")
            pass

        cur.execute(f"delete from customer_details where Cus_Name='{self.namevalue.get()}' and Cus_Surname='{self.surnamevalue.get()}'")
        con.commit()
        self.show_record()
        self.reset_button()
        tmsg.showinfo("Library Management System", "Record Deleted Successfully")

    def get_cursor(self, event):
        cur_row = self.lib_table.focus()
        content = self.lib_table.item(item=cur_row)
        row = content['values']

        self.idvalue.set(row[0])
        self.namevalue.set(row[1])
        self.surnamevalue.set(row[2])
        self.phonevalue.set(row[3])
        self.book_idvalue.set(row[4])
        self.book_namevalue.set(row[5])
        self.issuedvalue.set(row[6])
        self.duevalue.set(row[7])
        self.finevalue.set(row[8])

        if self.book_namevalue.get() == "General Knowledge":
            file = "General Knowledge"
            pic = PhotoImage(file=f"books\\{file}.png")
            book = Label(self.book_photo_frame, image=pic)
            book.image = pic
            book.grid(row=0, column=0)

        elif self.book_namevalue.get() == "All about CALCULUS":
            file = "All about CALCULUS"
            pic = PhotoImage(file=f"books\\{file}.png")
            book = Label(self.book_photo_frame, image=pic)
            book.image = pic
            book.grid(row=0, column=0)

        elif self.book_namevalue.get() == "Harry Porter":
            file = "Harry Porter"
            pic = PhotoImage(file=f"books\\{file}.png")
            book = Label(self.book_photo_frame, image=pic)
            book.image = pic
            book.grid(row=0, column=0)

        elif self.book_namevalue.get() == "Play a Game":
            file = "Play a Game"
            pic = PhotoImage(file=f"books\\{file}.png")
            book = Label(self.book_photo_frame, image=pic)
            book.image = pic
            book.grid(row=0, column=0)

        elif self.book_namevalue.get() == "Physics Around Us":
            file = "Physics Around Us"
            pic = PhotoImage(file=f"books\\{file}.png")
            book = Label(self.book_photo_frame, image=pic)
            book.image = pic
            book.grid(row=0, column=0)

        elif self.book_namevalue.get() == "Human Encyclopedia":
            file = "Human Encyclopedia"
            pic = PhotoImage(file=f"books\\{file}.png")
            book = Label(self.book_photo_frame, image=pic)
            book.image = pic
            book.grid(row=0, column=0)

        elif self.book_namevalue.get() == "Top 5000 Fun Facts":
            file = "Top 5000 Fun Facts"
            pic = PhotoImage(file=f"books\\{file}.png")
            book = Label(self.book_photo_frame, image=pic)
            book.image = pic
            book.grid(row=0, column=0)

        elif self.book_namevalue.get() == "Gulliver Travels":
            file = "Gulliver Travels"
            pic = PhotoImage(file=f"books\\{file}.png")
            book = Label(self.book_photo_frame, image=pic)
            book.image = pic
            book.grid(row=0, column=0)

        elif self.book_namevalue.get() == "Marvel Cinematic Universe":
            file = "Marvel Cinematic Universe"
            pic = PhotoImage(file=f"books\\{file}.png")
            book = Label(self.book_photo_frame, image=pic)
            book.image = pic
            book.grid(row=0, column=0)

        elif self.book_namevalue.get() == "Guiness World Records":
            file = "Guiness World Records"
            pic = PhotoImage(file=f"books\\{file}.png")
            book = Label(self.book_photo_frame, image=pic)
            book.image = pic
            book.grid(row=0, column=0)

        elif self.book_namevalue.get() == "Mysteries of Universe":
            file = "Mysteries of Universe"
            pic = PhotoImage(file=f"books\\{file}.png")
            book = Label(self.book_photo_frame, image=pic)
            book.image = pic
            book.grid(row=0, column=0)

        elif self.book_namevalue.get() == "Python Programming (Class 11)":
            file = "Python Programming (Class 11)"
            pic = PhotoImage(file=f"books\\{file}.png")
            book = Label(self.book_photo_frame, image=pic)
            book.image = pic
            book.grid(row=0, column=0)

        elif self.book_namevalue.get() == "Python Programming (Class 12)":
            file = "Python Programming (Class 12)"
            pic = PhotoImage(file=f"books\\{file}.png")
            book = Label(self.book_photo_frame, image=pic)
            book.image = pic
            book.grid(row=0, column=0)

        elif self.book_namevalue.get() == "Wings of Fire":
            file = "Wings of Fire"
            pic = PhotoImage(file=f"books\\{file}.png")
            book = Label(self.book_photo_frame, image=pic)
            book.image = pic
            book.grid(row=0, column=0)

    def update_button(self):
        if self.idvalue=="" and self.namevalue=="":
            tmsg.showerror("Library Management System", "Please select a record first....")

        else:
            cur.execute(f"update customer_details set Cus_Id={self.idvalue.get()}, Cus_Name='{self.namevalue.get()}', Cus_Surname='{self.surnamevalue.get()}', Cus_Mob='{self.phonevalue.get()}', Book_Id='{self.book_idvalue.get()}', Book_Name='{self.book_namevalue.get()}', Issue_Date='{self.issuedvalue.get()}', Due_Date='{self.duevalue.get()}', Fine='{self.finevalue.get()}' where Cus_Id={self.idvalue.get()}")
            con.commit()
            self.show_record()
            self.reset_button()
            tmsg.showinfo("Library Management System", "Your record is updated succesfully!!")

    def reset_button(self):
        self.namevalue.set("")
        self.surnamevalue.set("")
        self.phonevalue.set("")
        self.book_idvalue.set("")
        self.book_namevalue.set("")
        self.issuedvalue.set("")
        self.duevalue.set("")
        self.finevalue.set("")

    def random_id(self):
        cur.execute("select Cus_Id from customer_details")
        data = cur.fetchall()

        self.id_list = []
        for i in data:
            self.id_list.append(i)

        id = rd.randrange(100, 999)

        if id in self.id_list:
            pass
        else:
            self.idvalue.set(id)

    def toolbar(self):
        self.menubar = Menu(root)

        self.view_more()

        root.config(menu=self.menubar)

    def view_more(self):
        self.more = Menu(self.menubar, tearoff=0)
        self.more.add_command(label="FeedBack", command=feedback)
        self.more.add_separator()
        self.more.add_command(label="About Us", command=about)
        self.menubar.add_cascade(label="More", menu=self.more)

class StudentLogin:
    def __init__(self, root):
        self.working_frame = Frame(root, height=600, width=1520)
        self.working_frame.pack(pady=8)
        self.button_frame = Frame(root, width=1520, height=60)
        self.button_frame.pack(pady=4)
        self.main_frames()
        self.library_info()
        self.list_book_names()
        self.mainwindow_buttons()
        self.library_table()
        self.toolbar()

    def main_frames(self):
        self.library_details = Frame(self.working_frame, height=600, width=900, relief=RIDGE, borderwidth=4, bg="cadetblue")
        self.library_details.grid(row=0, column=0)
        self.booklist_frame = Frame(self.working_frame, height=600, width=600, relief=RIDGE, borderwidth=4, bg="powder blue")
        self.booklist_frame.grid(row=0, column=1, padx=4)

        self.lib_details_frame = LabelFrame(self.library_details, text="Library Details: ", width=900, font=("new times roman", 16, "bold", "underline"), height=330, relief=RIDGE, borderwidth=8, bg="powder blue")
        self.lib_details_frame.grid(row=0, column=0)
        self.lib_info_frame = LabelFrame(self.library_details, text="Library Information: ", font=("new times roman", 16, "bold", "underline"), width=900, height=270, relief=RIDGE, borderwidth=8, bg="powder blue", pady=8)
        self.lib_info_frame.grid(row=1, column=0)
        self.book_photo_frame = LabelFrame(self.booklist_frame, text="Book Photo: ", font=("new times roman", 16, "bold", "underline"), height=300, width=600, relief=RIDGE, borderwidth=8)
        self.book_photo_frame.grid(row=0, column=0)
        self.book_name_frame = LabelFrame(self.booklist_frame, text="Book List: ", font=("new times roman", 16, "bold", "underline"), height=300, width=600, relief=RIDGE, borderwidth=8, bg="powder blue", pady=8)
        self.book_name_frame.grid(row=1, column=0)

    def library_info(self):
        # Making Labels:-
        self.name = Label(self.lib_details_frame, text="Name: ", font=("arial", 16, "bold"), bg="powder blue", width=16)
        self.name.grid(row=0, column=0, stick=W, pady=6)
        self.surname = Label(self.lib_details_frame, text="Surname: ", font=("arial", 16, "bold"), bg="powder blue", width=16)
        self.surname.grid(row=1, column=0, stick=W, pady=6)
        self.phone_number = Label(self.lib_details_frame, text="Phone Number: ", font=("arial", 16, "bold"), width=16, bg="powder blue")
        self.phone_number.grid(row=2, column=0, stick=W, pady=6)
        self.age = Label(self.lib_details_frame, text="Age: ", font=("arial", 16, "bold"), width=16, bg="powder blue")
        self.age.grid(row=3, column=0, sticky=W, pady=6)
        self.book_id = Label(self.lib_details_frame, text="Book Id: ", font=("arial", 16, "bold"), width=16, bg="powder blue")
        self.book_id.grid(row=0, column=2, pady=6)
        self.book_name = Label(self.lib_details_frame, text="Book Name: ", font=("arial", 16, "bold"), width=16, bg="powder blue")
        self.book_name.grid(row=1, column=2, pady=6)
        self.issued_date = Label(self.lib_details_frame, text="Issued Date: ", font=("arial", 16, "bold"), width=16, bg="powder blue")
        self.issued_date.grid(row=2, column=2, pady=6)
        self.due_date = Label(self.lib_details_frame, text="Due Date: ", font=("arial", 16, "bold"), width=16, bg="powder blue")
        self.due_date.grid(row=3, column=2, pady=6)
        self.fine = Label(self.lib_details_frame, text="Price: ", font=("arial", 16, "bold"), width=16, bg="powder blue")
        self.fine.grid(row=4, column=2, pady=6)

        # Making Entries:-
        self.namevalue = StringVar()
        self.surnamevalue = StringVar()
        self.phonevalue = StringVar()
        self.agevalue = StringVar()
        self.book_idvalue = StringVar()
        self.book_namevalue = StringVar()
        self.issuedvalue = StringVar()
        self.duevalue = StringVar()
        self.finevalue = StringVar()

        self.name_entry = Entry(self.lib_details_frame, font=("arial", 16), width=18, textvariable=self.namevalue)
        self.name_entry.grid(row=0, column=1, pady=6, padx=4)
        self.surname_entry = Entry(self.lib_details_frame, font=("arial", 16), width=18, textvariable=self.surnamevalue)
        self.surname_entry.grid(row=1, column=1, pady=6, padx=4)
        self.phone_number_entry = Entry(self.lib_details_frame, font=("arial", 16), width=18, textvariable=self.phonevalue)
        self.phone_number_entry.grid(row=2, column=1, pady=6, padx=4)
        self.age_entry = Entry(self.lib_details_frame, font=("arial", 16), width=18, textvariable=self.agevalue)
        self.age_entry.grid(row=3, column=1, pady=6, padx=4)
        self.book_id_entry = Entry(self.lib_details_frame, font=("arial", 16), width=18, textvariable=self.book_idvalue)
        self.book_id_entry.grid(row=0, column=3, pady=6, padx=4)
        self.book_name_entry = Entry(self.lib_details_frame, font=("arial", 16), state=DISABLED, width=18, textvariable=self.book_namevalue)
        self.book_name_entry.grid(row=1, column=3, pady=6, padx=4)
        self.issued_date_entry = Entry(self.lib_details_frame, font=("arial", 16), state=DISABLED, width=18, textvariable=self.issuedvalue)
        self.issued_date_entry.grid(row=2, column=3, pady=6, padx=4)
        self.due_date_entry = Entry(self.lib_details_frame, font=("arial", 16), state=DISABLED, width=18, textvariable=self.duevalue)
        self.due_date_entry.grid(row=3, column=3, pady=6, padx=4)
        self.fine_entry = Entry(self.lib_details_frame, state=DISABLED, font=("arial", 16), width=18, textvariable=self.finevalue)
        self.fine_entry.grid(row=4, column=3, pady=4, padx=6)

    def list_book_names(self):
        # Making scrollbar:-
        scrollbar = Scrollbar(self.book_name_frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Making list of books:-
        self.list_of_books = ["Python Programming (Class 11)", "Python Programming (Class 12)", "Wings of Fire",
                              "Harry Porter", "Top 5000 Fun Facts", "Gulliver Travels", "Guiness World Records",
                              "All about CALCULUS", "General Knowledge", "Play a Game", "Physics Around Us",
                              "Human Encyclopedia", "Marvel Cinematic Universe", "Mysteries of Universe"]
        self.list_bookid = ["BKID482", "BKID642", "BKID871", "BKID382", "BKID905", "BKID460", "BKID973", "BKID142",
                            "BKID467", "BKID712", "BKID512", "BKID840", "BKID862", "BKID321"]

        self.book_list = Listbox(self.book_name_frame, width=62, font=("arial", 13), relief=SUNKEN,
                                 yscrollcommand=scrollbar.set)
        self.book_list.bind('<<ListboxSelect>>', self.book_photo)
        self.book_list.pack(fill=BOTH)
        scrollbar.config(command=self.book_list.yview)

        for items in self.list_of_books:
            self.book_list.insert(END, items)

    def book_photo(self, event):
        try:
            value = str(self.book_list.get(self.book_list.curselection()))
            x = value

            borrowed_days = int(rd.randrange(8, 16))

            book_price = {"Python Programming (Class 11)": "Rs. 499", "Python Programming (Class 12)": "Rs. 499", "Wings of Fire": "Rs. 449", "Harry Porter": "Rs. 599", "Top 5000 Fun Facts": "Rs. 549", "Gulliver Travels":"Rs. 649", "Guiness World Records":"Rs. 699", "Mysteries of Universe":"Rs. 899", "Marvel Cinematic Universe":"Rs. 749", "All about CALCULUS":"Rs. 949", "Human Encyclopedia":"Rs. 799", "Physics Around Us":"Rs. 849", "Play a Game":"Rs. 699", "General Knowledge":"Rs. 549", "Some Magic Trick":"Rs 799"}


            if x == "Python Programming (Class 11)":
                file = "Python Programming (Class 11)"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[0])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                self.finevalue.set(book_price[x])

            elif x == "Python Programming (Class 12)":
                file = "Python Programming (Class 12)"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[1])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                self.finevalue.set(book_price[x])

            elif x == "Wings of Fire":
                file = "Wings of Fire"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[2])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                self.finevalue.set(book_price[x])

            elif x == "Harry Porter":
                file = "Harry Porter"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[3])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                self.finevalue.set(book_price[x])

            elif x == "All about CALCULUS":
                file = "All about CALCULUS"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[4])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                self.finevalue.set(book_price[x])

            elif x == "Play a Game":
                file = "Play a Game"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[5])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                self.finevalue.set(book_price[x])

            elif x == "General Knowledge":
                file = "General Knowledge"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[6])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                self.finevalue.set(book_price[x])

            elif x == "Physics Around Us":
                file = "Physics Around Us"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[7])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                self.finevalue.set(book_price[x])

            elif x == "Human Encyclopedia":
                file = "Human Encyclopedia"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[8])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                self.finevalue.set(book_price[x])

            elif x == "Top 5000 Fun Facts":
                file = "Top 5000 Fun Facts"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[9])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                self.finevalue.set(book_price[x])

            elif x == "Gulliver Travels":
                file = "Gulliver Travels"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[10])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                self.finevalue.set(book_price[x])

            elif x == "Marvel Cinematic Universe":
                file = "Marvel Cinematic Universe"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[11])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                self.finevalue.set(book_price[x])

            elif x == "Guiness World Records":
                file = "Guiness World Records"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[12])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                self.finevalue.set(book_price[x])

            elif x == "Mysteries of Universe":
                file = "Mysteries of Universe"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)
                self.book_namevalue.set(file)
                self.book_idvalue.set(self.list_bookid[13])
                d1 = datetime.date.today()
                d2 = datetime.timedelta(borrowed_days)
                d3 = d1 + d2
                self.issuedvalue.set(d1)
                self.duevalue.set(d3)
                self.finevalue.set(book_price[x])
        except Exception as e:
            pass

    def library_table(self):
        # Creating Scrollbar:-
        scroll_x = ttk.Scrollbar(self.lib_info_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.lib_info_frame, orient=VERTICAL)

        self.lib_table = ttk.Treeview(self.lib_info_frame, height=11, column=("Cus_Name", "Cus_Surname",
                                                                              "Cus_Mob", "Cus_Age", "Book_Id", "Book_Name",
                                                                              "Issue_Date", "Due_Date", "Price"),
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.lib_table.xview())
        scroll_y.config(command=self.lib_table.yview())

        self.lib_table.heading("Cus_Name", text="Name")
        self.lib_table.heading("Cus_Surname", text="Surname")
        self.lib_table.heading("Cus_Mob", text="Phone Number")
        self.lib_table.heading("Cus_Age", text="Age")
        self.lib_table.heading("Book_Id", text="ID")
        self.lib_table.heading("Book_Name", text="Book Name")
        self.lib_table.heading("Issue_Date", text="Issue Date")
        self.lib_table.heading("Due_Date", text="Due Date")
        self.lib_table.heading("Price", text="Price")

        self.lib_table["show"] = "headings"

        self.lib_table.column("Cus_Name", width=100)
        self.lib_table.column("Cus_Surname", width=100)
        self.lib_table.column("Cus_Mob", width=100)
        self.lib_table.column("Cus_Age", width=75)
        self.lib_table.column("Book_Id", width=100)
        self.lib_table.column("Book_Name", width=120)
        self.lib_table.column("Issue_Date", width=105)
        self.lib_table.column("Due_Date", width=105)
        self.lib_table.column("Price", width=70)

        self.lib_table.bind('<ButtonRelease-1>', self.get_cursor)
        self.show_record()

        self.lib_table.pack(fill=BOTH, expand=1)

    def mainwindow_buttons(self):
        self.addbutton = Button(self.button_frame, text="Issue Book", width=14, font=("new times roman", 20, "bold"), borderwidth=4, justify=CENTER, relief=SOLID, command=self.add_button)
        self.addbutton.grid(row=0, column=0, padx=12)
        self.deletebutton = Button(self.button_frame, text="Delete Data", width=14, font=("new times roman", 20, "bold"), borderwidth=4, justify=CENTER, relief=SOLID, command=self.delete_button)
        self.deletebutton.grid(row=0, column=1, padx=12)
        self.updatebutton = Button(self.button_frame, text="Update Data", width=14, font=("new times roman", 20, "bold"), borderwidth=4, justify=CENTER, relief=SOLID, command=self.update_button)
        self.updatebutton.grid(row=0, column=2, padx=12)
        self.resetbutton = Button(self.button_frame, text="Reset Data", width=14, font=("new times roman", 20, "bold"), borderwidth=4, justify=CENTER, relief=SOLID, command=self.reset_button)
        self.resetbutton.grid(row=0, column=3, padx=12)
        self.exitbutton = Button(self.button_frame, text="Exit Window", width=14, font=("new times roman", 20, "bold"), borderwidth=4, justify=CENTER, relief=SOLID, command=self.exit)
        self.exitbutton.grid(row=0, column=4, padx=12)

    def exit(self):
        ask = tmsg.askyesno("Library Management System", "Do you really want to exit??")

        if ask == YES:
            tmsg.showinfo("Library Management System",
                          "Your account has been logged out succesfully\nHave a nive day!!")
            root.destroy()

    def add_button(self):
        if self.namevalue == "":
            tmsg.showerror("Library Management System", "Please enter valid data!!")

        else:
            cur.execute(f"insert into student_login values ('{self.namevalue.get()}', '{self.surnamevalue.get()}', '{self.phonevalue.get()}', {self.agevalue.get()}, '{self.book_idvalue.get()}', '{self.book_namevalue.get()}', '{self.issuedvalue.get()}', '{self.duevalue.get()}', '{self.finevalue.get()}')")
            self.show_record()
            con.commit()
            tmsg.showinfo("Library Management System", "Your record has been added successfully!!")

    def show_record(self):
        cur.execute(f"select * from student_login")
        data = cur.fetchall()

        for record in self.lib_table.get_children():
            self.lib_table.delete(record)

        if len(data) != 0:
            for i in data:
                self.lib_table.insert(parent="", index=END, value=i)

    def delete_button(self):
        cur.execute(f"select * from student_login where Cus_Name='{self.namevalue.get()}' and Cus_Surname='{self.surnamevalue.get()}'")
        data = cur.fetchall()

        for i in data:
            a1 = i[0]
            a2 = i[1]
            a3 = i[2]
            a4 = i[3]
            a5 = i[4]
            a6 = i[5]
            a7 = i[6]
            a8 = i[7]
            a9 = i[8]

            cur.execute(f"insert into delete_stud_login values ('{a1}', '{a2}', '{a3}', {a4}, '{a5}', '{a6}' ,'{a7}', '{a8}', '{a9}')")
            pass

        cur.execute(f"delete from student_login where Cus_Name='{self.namevalue.get()}' and Cus_Surname='{self.surnamevalue.get()}'")
        con.commit()
        self.show_record()
        self.reset_button()
        tmsg.showinfo("Library Management System", "Record Deleted Successfully")

    def get_cursor(self, event):
        try:
            cur_row = self.lib_table.focus()
            content = self.lib_table.item(item=cur_row)
            row = content['values']

            self.namevalue.set(row[0])
            self.surnamevalue.set(row[1])
            self.phonevalue.set(row[2])
            self.agevalue.set(row[3])
            self.book_idvalue.set(row[4])
            self.book_namevalue.set(row[5])
            self.issuedvalue.set(row[6])
            self.duevalue.set(row[7])
            self.finevalue.set(row[8])

            if self.book_namevalue.get() == "General Knowledge":
                file = "General Knowledge"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)

            elif self.book_namevalue.get() == "All about CALCULUS":
                file = "All about CALCULUS"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)

            elif self.book_namevalue.get() == "Harry Porter":
                file = "Harry Porter"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)

            elif self.book_namevalue.get() == "Play a Game":
                file = "Play a Game"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)

            elif self.book_namevalue.get() == "Physics Around Us":
                file = "Physics Around Us"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)

            elif self.book_namevalue.get() == "Human Encyclopedia":
                file = "Human Encyclopedia"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)

            elif self.book_namevalue.get() == "Top 5000 Fun Facts":
                file = "Top 5000 Fun Facts"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)

            elif self.book_namevalue.get() == "Gulliver Travels":
                file = "Gulliver Travels"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)

            elif self.book_namevalue.get() == "Marvel Cinematic Universe":
                file = "Marvel Cinematic Universe"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)

            elif self.book_namevalue.get() == "Guiness World Records":
                file = "Guiness World Records"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)

            elif self.book_namevalue.get() == "Mysteries of Universe":
                file = "Mysteries of Universe"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)

            elif self.book_namevalue.get() == "Python Programming (Class 11)":
                file = "Python Programming (Class 11)"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)

            elif self.book_namevalue.get() == "Python Programming (Class 12)":
                file = "Python Programming (Class 12)"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)

            elif self.book_namevalue.get() == "Wings of Fire":
                file = "Wings of Fire"
                pic = PhotoImage(file=f"books\\{file}.png")
                book = Label(self.book_photo_frame, image=pic)
                book.image = pic
                book.grid(row=0, column=0)

        except Exception as e:
            pass

    def update_button(self):
        if self.namevalue == "":
            tmsg.showerror("Library Management System", "Please select a record first....")

        else:
            cur.execute(f"update student_login set Cus_Name='{self.namevalue.get()}', Cus_Surname='{self.surnamevalue.get()}', Cus_Mob='{self.phonevalue.get()}', Cus_Age={self.agevalue.get()}, Book_Id='{self.book_idvalue.get()}', Book_Name='{self.book_namevalue.get()}', Issue_Date='{self.issuedvalue.get()}', Due_Date='{self.duevalue.get()}', Price='{self.finevalue.get()}' where Cus_Name='{self.namevalue.get()}'")
            con.commit()
            self.show_record()
            self.reset_button()
            tmsg.showinfo("Library Management System", "Your record is updated succesfully!!")

    def reset_button(self):
        self.namevalue.set("")
        self.surnamevalue.set("")
        self.phonevalue.set("")
        self.agevalue.set("")
        self.book_idvalue.set("")
        self.book_namevalue.set("")
        self.issuedvalue.set("")
        self.duevalue.set("")
        self.finevalue.set("")

    def toolbar(self):
        self.menubar = Menu(root)

        self.view_more()

        root.config(menu=self.menubar)

    def view_more(self):
        self.more = Menu(self.menubar, tearoff=0)
        self.more.add_command(label="FeedBack", command=feedback)
        self.more.add_separator()
        self.more.add_command(label="About Us", command=about)
        self.menubar.add_cascade(label="More", menu=self.more)

def feedback():
    fd = Toplevel()
    fd.title("Send Feedback")
    fd.geometry("550x200")
    fd.wm_iconbitmap("icons\\library icon.ico")

    label = Label(fd, text="Write your FeedBack/Suggestion/Complain here", font="cooper 14")
    label.pack(pady=10)
    fd_value = StringVar()

    def send(event):
        with open("feedback.txt", "a") as f:
            f.write(f"{fd_value.get()}\n")

        tmsg.showinfo("Send FeedBack", "Thanks for your FeedBack/Suggestion/Complain!!")
        fd.destroy()

    fd_entry = Entry(fd, textvariable=fd_value, width=32, font="arial 16", borderwidth=2, relief=SUNKEN)
    fd_entry.bind("<Return>", send)
    fd_entry.pack(pady=10)

    fd_button = Button(fd, text="Send FeedBack", font="cooper 14", borderwidth=2, relief=GROOVE)
    fd_button.bind('<Button-1>', send)
    fd_button.pack(pady=12)

def about():
    tmsg.showinfo("About", "Made by:-\n          Jay Patel\n          Harsh Parmar")

win1 = LoginWindow(root)

def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    st_time.config(text=f"Time-> {hour}:{minute}:{second}")
    st_time.after(1000, clock)

def st_feed():
    f = open("feedback.txt", "rt")
    content = f.readlines()
    choice = rd.choice(content)

    st_feedback.config(text=f"FeedBack-> {choice}")
    st_feedback.after(12000, st_feed)
    f.close()

statusbar = Frame(root, relief=SUNKEN, borderwidth=2)
statusbar.pack(side=BOTTOM, fill=X)

statusvar = StringVar()
statusvar.set(f"FeedBack-> ")

st_feedback = Label(statusbar, text="FeedBack-> ")
st_feedback.pack(side=LEFT)

st_time = Label(statusbar, text="Time-> ")
st_time.pack(side=RIGHT)

clock()
st_feed()

root.mainloop()