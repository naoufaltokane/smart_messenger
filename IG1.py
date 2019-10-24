from tkinter import *
import EAR.login_func as login


'''This class configures and populates the toplevel window.
   top is the toplevel containing window.'''
_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9' # X11 color: 'gray85'
_ana1color = '#d9d9d9' # X11 color: 'gray85'
_ana2color = '#ececec' # Closest X11 color: 'gray92'
font11 = "-family {Segoe UI} -size 16 -weight bold -slant "  \
    "roman -underline 0 -overstrike 0"
font13 = "-family {Courier New} -size 16 -weight bold -slant "  \
    "roman -underline 0 -overstrike 0"
font14 = "-family {Segoe UI} -size 18 -weight bold -slant "  \
    "roman -underline 0 -overstrike 0"



top = Tk()
top.geometry("532x547+388+127")
top.title("login")
top.configure(background="#d9d9d9")

Frame1 = Frame(top)
Frame1.place(relx=0.075, rely=0.293, relheight=0.612, relwidth=0.855)
Frame1.configure(relief='groove')
Frame1.configure(borderwidth="2")
Frame1.configure(relief='groove')
Frame1.configure(background="#d9d9d9")
Frame1.configure(width=455)

Labelemail = Label(Frame1)
Labelemail.place(relx=0.066, rely=0.119, height=46, width=78)
Labelemail.configure(background="#d9d9d9")
Labelemail.configure(disabledforeground="#a3a3a3")
Labelemail.configure(font=font11)
Labelemail.configure(foreground="#556080")
Labelemail.configure(text='''E-mail''')
Labelemail.configure(width=78)

Labelpassword = Label(Frame1)
Labelpassword.place(relx=0.066, rely=0.328, height=46, width=98)
Labelpassword.configure(activebackground="#f9f9f9")
Labelpassword.configure(activeforeground="black")
Labelpassword.configure(background="#d9d9d9")
Labelpassword.configure(disabledforeground="#a3a3a3")
Labelpassword.configure(font=font11)
Labelpassword.configure(foreground="#556080")
Labelpassword.configure(highlightbackground="#d9d9d9")
Labelpassword.configure(highlightcolor="black")
Labelpassword.configure(text='''Password''')
Labelpassword.configure(width=98)

eemail = StringVar(top)
EntryEmail = Entry(Frame1)
EntryEmail.place(relx=0.374, rely=0.149,height=27, relwidth=0.58)
EntryEmail.configure(background="white")
EntryEmail.configure(disabledforeground="#a3a3a3")
EntryEmail.configure(font=font13)
EntryEmail.configure(foreground="#000000")
EntryEmail.configure(insertbackground="black")
EntryEmail.configure(textvariable=eemail)

password = StringVar(top)
EntryPass = Entry(Frame1)
EntryPass.place(relx=0.374, rely=0.358,height=27, relwidth=0.58)
EntryPass.config(show="*")
EntryPass.configure(background="white")
EntryPass.configure(disabledforeground="#a3a3a3")
EntryPass.configure(font=font13)
EntryPass.configure(foreground="#000000")
EntryPass.configure(highlightbackground="#d9d9d9")
EntryPass.configure(highlightcolor="black")
EntryPass.configure(insertbackground="black")
EntryPass.configure(selectbackground="#c4c4c4")
EntryPass.configure(selectforeground="black")
EntryPass.configure(textvariable=password)
EntryPass.configure(width=264)

ButtonLogin = Button(Frame1, command=lambda: login.get_unread(top, eemail.get(), password.get()))
ButtonLogin.place(relx=0.308, rely=0.746, height=54, width=157)
ButtonLogin.configure(activebackground="#ececec")
ButtonLogin.configure(activeforeground="#000000")
ButtonLogin.configure(background="#EFCE4A")
ButtonLogin.configure(disabledforeground="#a3a3a3")
ButtonLogin.configure(font=font14)
ButtonLogin.configure(foreground="#ffffff")
ButtonLogin.configure(highlightbackground="#d9d9d9")
ButtonLogin.configure(highlightcolor="black")
ButtonLogin.configure(pady="0")
ButtonLogin.configure(text='''Log in''')
ButtonLogin.configure(width=157)

Label1 = Label(top)
Label1.place(relx=0.056, rely=0.0, height=149, width=469)
Label1.configure(background="#d9d9d9")
Label1.configure(disabledforeground="#a3a3a3")
Label1.configure(foreground="#000000")
_img1 = PhotoImage(file="../EAR/LOGO.png")
Label1.configure(image=_img1)
Label1.configure(text='''Label''')
Label1.configure(width=469)

top.mainloop()




