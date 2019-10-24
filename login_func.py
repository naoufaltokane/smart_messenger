import email
import getpass
import imaplib
import smtplib
from tkinter import *
from EAR.ReplyIG import vp_start_gui
import time
import warnings
import EAR.IG2 as mailbox
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True


def login(email, pwd):
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(email, pwd)
        print('login info')
        print(email)
        print(pwd)

        print("login with success")
        return mail
    except Exception as e:
        print('something went wrong while trying to login')
        print(e)

def get_unread(top, eemail, pwd):
    for widget in top.winfo_children():
        widget.destroy()

    #top = tk.Tk()
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9'  # X11 color: 'gray85'
    _ana1color = '#d9d9d9'  # X11 color: 'gray85'
    _ana2color = '#ececec'  # Closest X11 color: 'gray92'
    font9 = "-family {Segoe UI Black} -size 12 -weight bold -slant" \
            " italic -underline 0 -overstrike 0"

    font10 = "-family {Segoe UI Black} -size 9 -slant" \
            " italic -underline 0 -overstrike 0"

    top.geometry("600x446+346+141")
    top.title("INBOX")
    top.configure(background="#d9d9d9")

    Label1 = tk.Label(top)
    Label1.place(relx=0.283, rely=0.045, height=81, width=254)
    Label1.configure(background="#d9d9d9")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(foreground="#000000")
    _img1 = tk.PhotoImage(file="../EAR/INBOX2.png")
    Label1.configure(image=_img1)
    Label1.configure(text='''Label''')
    Label1.configure(width=254)

    Frame1 = tk.Frame(top)
    Frame1.place(relx=0.05, rely=0.269, relheight=0.639, relwidth=0.925)

    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief='groove')
    Frame1.configure(background="#d9d9d9")
    Frame1.configure(width=555)

    Label2 = tk.Label(Frame1)
    Label2.place(relx=0.036, rely=0.035, height=21, width=154)
    Label2.configure(background="#d9d9d9")
    Label2.configure(disabledforeground="#a3a3a3")
    Label2.configure(font=font9)
    Label2.configure(foreground="#000000")
    Label2.configure(text='''Sender''')
    Label2.configure(width=154)

    Label3 = tk.Label(Frame1)
    Label3.place(relx=0.423, rely=0.035, height=21, width=194)
    Label3.configure(background="#d9d9d9")
    Label3.configure(disabledforeground="#a3a3a3")
    Label3.configure(font=font9)
    Label3.configure(foreground="#000000")
    Label3.configure(text='''Subject''')
    Label3.configure(width=194)

    Label4 = tk.Label(Frame1)
    Label4.place(relx=0.072, rely=0.035, height=22, width=32)
    Label4.configure(background="#d9d9d9")
    Label4.configure(disabledforeground="#a3a3a3")
    Label4.configure(foreground="#000000")
    _img2 = tk.PhotoImage(file="../EAR/logomail.png")
    Label4.configure(image=_img2)
    Label4.configure(text='''Label''')
    Label4.configure(width=32)

    Label5 = tk.Label(Frame1)
    Label5.place(relx=0.486, rely=0.018, height=31, width=34)
    Label5.configure(background="#d9d9d9")
    Label5.configure(disabledforeground="#a3a3a3")
    Label5.configure(foreground="#000000")
    _img3 = tk.PhotoImage(file="../EAR//rsz_unread.png")
    Label5.configure(image=_img3)
    Label5.configure(text='''Label''')
    Label5.configure(width=34)

    TSeparator1 = ttk.Separator(Frame1)
    TSeparator1.place(relx=0.009, rely=0.123, relwidth=1.009)



    print(eemail)
    print(pwd)
    mail = login(eemail, pwd)
    mail.select('INBOX')

    status, response = mail.search(None, '(UNSEEN)')
    #list des id des msg unread
    unread_msg_nums = response[0].split()

    # Print the count of all unread messages
    print (len(unread_msg_nums))

    # Print all unread messages
    status, response = mail.search(None, '(UNSEEN)')#"%s")')# % (sender_of_interest)
    import email
    box = response[0].split()

    for latest_email_uid in response[0].split():
        print(latest_email_uid)
        status, response = mail.fetch(latest_email_uid, '(RFC822)')
        msg = email.message_from_bytes(response[0][1])
        print("-------------------------")
        print(msg['To'])
        print(msg['Subject'])
        print(email.utils.parseaddr(msg['From']))
        for part in msg.walk():
            if part.get_content_type() == "text/plain":  # ignore attachments/html
                body = part.get_payload(decode=True)
                print(body.decode('utf-8'))
            else:
                continue
        print("-------------------------")

    _img4 = tk.PhotoImage(file="../EAR/logo2.png")

    i = 0.158
    for latest_email_uid in box:
        #get the body of the message
        for part in msg.walk():
            if part.get_content_type() == "text/plain":  # ignore attachments/html
                body = part.get_payload(decode=True)
                print(body.decode('utf-8'))
            else:
                continue
        txt = str(body.decode('utf-8'))
        send = str(email.utils.parseaddr(msg['From'])[1])
        print("sender is "+send)
        print(latest_email_uid)
        status, response = mail.fetch(latest_email_uid, '(RFC822)')
        msg = email.message_from_bytes(response[0][1])


        Label6 = tk.Label(Frame1)
        Label6.place(relx=0.009, rely=i, height=21, width=214)
        Label6.configure(background="#d9d9d9")
        Label6.configure(disabledforeground="#a3a3a3")
        Label6.configure(foreground="#000000")
        Label6.configure(text="" + email.utils.parseaddr(msg['From'])[1] + "")
        Label6.configure(width=214)
        Label6.configure(font=font10)

        Label7 = tk.Label(Frame1)
        Label7.place(relx=0.414, rely=i, height=21, width=264)
        Label7.configure(background="#d9d9d9")
        Label7.configure(disabledforeground="#a3a3a3")
        Label7.configure(foreground="#000000")
        Label7.configure(text="" + msg['Subject'] + "")
        Label7.configure(width=264)
        Label7.configure(font=font10)


        TSeparator2 = ttk.Separator(Frame1)
        TSeparator2.place(relx=0.0, rely=i+0.099, relwidth=1.009)

        Button1 = tk.Button(Frame1, command=lambda arg1=txt, arg2 =msg['Subject'] : vp_start_gui(send, arg2, body.decode('utf-8'), eemail, pwd))
        Button1.place(relx=0.901, rely=i, height=20, width=47)
        Button1.configure(activebackground="#ececec")
        Button1.configure(activeforeground="#000000")
        Button1.configure(background="#d9d9d9")
        Button1.configure(disabledforeground="#a3a3a3")
        Button1.configure(foreground="#000000")
        Button1.configure(highlightbackground="#d9d9d9")
        Button1.configure(highlightcolor="black")
        Button1.configure(image=_img4)
        Button1.configure(pady="0")
        Button1.configure(relief='flat')
        Button1.configure(text='''Button''')
        Button1.configure(width=47)

        i=i+0.108

    top.mainloop()

