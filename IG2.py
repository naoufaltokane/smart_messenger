from tkinter import *

#fonction to show unread emails
def show_mails(Frame,):

    for widget in Frame.winfo_children():
        widget.destroy()
    ligne1 = ['Sender', 'Subject','View']
    for i in range(len(ligne1)):
        Label(Frame, text="" + str(ligne1[i]) + "", font = "Verdana 9", bg="#2894FF", width=30, borderwidth=2, relief="groove").grid(row=1, column=i)

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
    i = 2
    for lig in resultats:
        txt = str(lig[15])
        Label(Frame, text="" + lig[0] + "", width=10, borderwidth=2, relief="groove").grid(row=i, column=0)
        Label(Frame, text="" + lig[1] + "", width=10, borderwidth=2, relief="groove").grid(row=i, column=1)
        Label(Frame, text="" + lig[2] + "", width=10, borderwidth=2, relief="groove").grid(row=i, column=2)
        Label(Frame, text="" + lig[3] + "", width=10, borderwidth=2, relief="groove").grid(row=i, column=3)
        Label(Frame, text="" + lig[4] + "", width=10, borderwidth=2, relief="groove").grid(row=i, column=4)

        Button(Frame, text="View", command=lambda arg1=txt: c_wind.aff_client_info(arg1), width=10, borderwidth=2, relief="groove", bg="light green").grid(row=i, column=5)
        i += 1


