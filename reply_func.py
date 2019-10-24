from EAR import Processing as proc
import csv
from EAR.SimilsIG import vp_start_gui

from tkinter import *
from EAR import login_func

def get_simil(mail, textarea):
    L = proc.compare_simil_tfidf(mail, "emails.csv")
    print("the end here is the most simil reply")
    #print(L=[0])
    #print(L=[2])

    text1 = L[0]
    score1 = L[1]


    text2 = L[2]
    score2 = L[3]


    vp_start_gui(text1, score1, text2, score2, textarea)
    #start_simi_ig(text1, score1, text2, score2)









def start_simi_ig(mail):

    '''This class configures and populates the toplevel window.
       top is the toplevel containing window.'''
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
    font11 = "-family {Segoe UI} -size 8 -weight bold -slant "  \
        "roman -underline 0 -overstrike 0"
    font13 = "-family {Courier New} -size 16 -weight bold -slant "  \
        "roman -underline 0 -overstrike 0"
    font14 = "-family {Segoe UI} -size 18 -weight bold -slant "  \
        "roman -underline 0 -overstrike 0"



    top = Tk()
    top.geometry("532x547+388+127")
    top.title("Suggstions")
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
    Labelpassword.place(relx=0.066, rely=0.328, height=150, width=444)
    Labelpassword.configure(activebackground="#f9f9f9")
    Labelpassword.configure(activeforeground="black")
    Labelpassword.configure(background="#d9d9d9")
    Labelpassword.configure(disabledforeground="#a3a3a3")
    Labelpassword.configure(font=font11)
    Labelpassword.configure(foreground="#556080")
    Labelpassword.configure(highlightbackground="#d9d9d9")
    Labelpassword.configure(highlightcolor="black")
    Labelpassword.configure(text=mail)
    Labelpassword.configure(width=444)
    Labelpassword.configure(wraplength="400")

    top.mainloop()


def add_to_corpus(mail, reply):
    with open('test.csv', 'a', newline='') as csvfile:
         try:
            filewriter = csv.writer(csvfile)
            filewriter.writerow([mail, reply])
            print('new row added to dataset')
         except Exception as e:
            print(e)
            pass



def reply_to_mail(body, reply, reciept, mail, pwd):
    add_to_corpus(body, reply)
    send_reply(mail, pwd, reply, reciept, subject="test ear")


def send_reply(sender, pwd, body, reciept, subject):
    import smtplib
    from email.mime.text import MIMEText
    print(type(sender))
    sender = str(sender)
    print(type(sender))

    print("sender is "+sender)
    print("pwd is "+pwd)
    print("body is "+body)
    print("recepteur is "+reciept)
    print("subject is  "+subject)


    smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
    smtp_ssl_port = 465

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = reciept

    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(sender, pwd)
    server.sendmail(sender, reciept, msg.as_string())
    server.quit()
    print("msg sent")

