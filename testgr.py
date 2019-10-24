from tkinter import *
import EAR.login_func as login

# fonction add event
def add_event():
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9'  # X11 color: 'gray85'
    _ana1color = '#d9d9d9'  # X11 color: 'gray85'
    _ana2color = '#ececec'  # Closest X11 color: 'gray92'
    font11 = "-family {Segoe UI} -size 14 -weight bold -slant " \
             "roman -underline 0 -overstrike 0"
    font12 = "-family {Courier New} -size 14 -weight normal -slant" \
             " roman -underline 0 -overstrike 0"
    font13 = "-family {Segoe UI} -size 13 -weight normal -slant " \
             "roman -underline 0 -overstrike 0"

    root = Tk()
    root.geometry("350x360+568+155")
    root.title("Login")
    root.configure(background="#99CCFF")

    fr = LabelFrame(root)
    fr.place(relx=0.0, rely=-0.014, relheight=1.014, relwidth=1.0)
    fr.configure(relief='groove')
    fr.configure(foreground="black")
    fr.configure(text='''Enter You Login Information''')
    fr.configure(background="#99CCFF")
    fr.configure(width=350)

    email = Label(fr)
    email.place(relx=0.086, rely=0.137, height=21, width=83, bordermode='ignore')
    email.configure(anchor='w')
    email.configure(background="#99CCFF")
    email.configure(disabledforeground="#a3a3a3")
    email.configure(font=font11)
    email.configure(foreground="#000000")
    email.configure(text='''email''')
    email.configure(width=83)

    pwd = Label(fr)
    pwd.place(relx=0.086, rely=0.342, height=21, width=83, bordermode='ignore')
    pwd.configure(activebackground="#f9f9f9")
    pwd.configure(activeforeground="black")
    pwd.configure(anchor='w')
    pwd.configure(background="#99CCFF")
    pwd.configure(disabledforeground="#a3a3a3")
    pwd.configure(font=font11)
    pwd.configure(foreground="#000000")
    pwd.configure(highlightbackground="#d9d9d9")
    pwd.configure(highlightcolor="black")
    pwd.configure(text='''pwd''')


    email_entry = Entry(fr)
    eemail = StringVar(root)
    email_entry.place(relx=0.414, rely=0.123, height=30, relwidth=0.497, bordermode='ignore')
    email_entry.configure(background="white")
    email_entry.configure(disabledforeground="#a3a3a3")
    email_entry.configure(font=font12)
    email_entry.configure(foreground="#000000")
    email_entry.configure(insertbackground="black")
    email_entry.configure(width=300)
    email_entry.configure(textvariable=eemail)


    password = StringVar(root)
    pwd_entry = Entry(fr)
    pwd_entry.place(relx=0.414, rely=0.329, height=30, relwidth=0.497, bordermode='ignore')
    pwd_entry.configure(background="white")
    pwd_entry.configure(disabledforeground="#a3a3a3")
    pwd_entry.configure(font=font12)
    pwd_entry.configure(width=300)
    pwd_entry.configure(foreground="#000000")
    pwd_entry.configure(highlightbackground="#d9d9d9")
    pwd_entry.configure(highlightcolor="black")
    pwd_entry.configure(insertbackground="black")
    pwd_entry.configure(selectbackground="#c4c4c4")
    pwd_entry.configure(selectforeground="black")
    pwd_entry.configure(textvariable=password)


    Button1 = Button(fr, command=lambda: login.get_unread(root, eemail.get(), password.get()))
    Button1.place(relx=0.229, rely=0.822, height=44, width=177, bordermode='ignore')
    Button1.configure(activebackground="#ececec")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#d9d9d9")
    Button1.configure(disabledforeground="#a3a3a3")
    Button1.configure(font=font11)
    Button1.configure(foreground="#1a9126")
    Button1.configure(highlightbackground="#d9d9d9")
    Button1.configure(highlightcolor="black")
    Button1.configure(pady="0")
    Button1.configure(text='''Validate''')
    Button1.configure(width=177)

    root.mainloop()


add_event()