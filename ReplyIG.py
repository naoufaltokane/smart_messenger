#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.19
#  in conjunction with Tcl version 8.6
#    Dec 24, 2018 05:17:40 PM WAT  platform: Windows NT

import sys
from tkinter import *

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
import EAR.reply_func as rep



def vp_start_gui(sender, subject, body, mail, pwd):
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (sender, subject, body, mail, pwd, root)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, sender, subject, body, mail, pwd, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        font11 = "-family {Segoe UI} -size 14 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 9 -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("668x589+315+69")
        top.title("Reply ")
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.03, rely=0.034, relheight=0.484, relwidth=0.936)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=625)

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.048, rely=0.07, height=31, width=103)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#556080")
        self.Label1.configure(text='''Sender :''')
        self.Label1.configure(width=103)

        self.Label1_1 = tk.Label(self.Frame1)
        self.Label1_1.place(relx=0.048, rely=0.211, height=31, width=103)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font=font11)
        self.Label1_1.configure(foreground="#556080")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Subject :''')
        self.Label1_1.configure(width=103)

        self.Label1_2 = tk.Label(self.Frame1)
        self.Label1_2.place(relx=0.064, rely=0.368, height=31, width=93)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(activeforeground="black")
        self.Label1_2.configure(background="#d9d9d9")
        self.Label1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2.configure(font=font11)
        self.Label1_2.configure(foreground="#556080")
        self.Label1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2.configure(highlightcolor="black")
        self.Label1_2.configure(text='''Message :''')
        self.Label1_2.configure(width=93)

        self.LabelSender = tk.Label(self.Frame1)
        self.LabelSender.place(relx=0.288, rely=0.07, height=31, width=413)
        self.LabelSender.configure(background="#d9d9d9")
        self.LabelSender.configure(disabledforeground="#a3a3a3")
        self.LabelSender.configure(font=font11)
        self.LabelSender.configure(foreground="#000000")
        self.LabelSender.configure(text=sender)
        self.LabelSender.configure(width=413)

        self.LabelSubject = tk.Label(self.Frame1)
        self.LabelSubject.place(relx=0.272, rely=0.193, height=41, width=433)
        self.LabelSubject.configure(activebackground="#f9f9f9")
        self.LabelSubject.configure(activeforeground="black")
        self.LabelSubject.configure(background="#d9d9d9")
        self.LabelSubject.configure(disabledforeground="#a3a3a3")
        self.LabelSubject.configure(font=font11)
        self.LabelSubject.configure(foreground="#000000")
        self.LabelSubject.configure(highlightbackground="#d9d9d9")
        self.LabelSubject.configure(highlightcolor="black")
        self.LabelSubject.configure(text=subject)
        self.LabelSubject.configure(width=433)

        self.LabelMessage = tk.Label(self.Frame1)
        self.LabelMessage.place(relx=0.256, rely=0.386, height=151, width=423)
        self.LabelMessage.configure(activebackground="#f9f9f9")
        self.LabelMessage.configure(activeforeground="black")
        self.LabelMessage.configure(anchor='nw')
        self.LabelMessage.configure(background="#d9d9d9")
        self.LabelMessage.configure(disabledforeground="#a3a3a3")
        self.LabelMessage.configure(font=font12)
        self.LabelMessage.configure(foreground="#000000")
        self.LabelMessage.configure(highlightbackground="#d9d9d9")
        self.LabelMessage.configure(highlightcolor="black")
        self.LabelMessage.configure(text=body)
        self.LabelMessage.configure(width=449)
        self.LabelMessage.configure(wraplength="449")

        self.TextReply = tk.Text(top)
        self.TextReply.place(relx=0.045, rely=0.56, relheight=0.211
                , relwidth=0.904)
        self.TextReply.configure(background="white")
        self.TextReply.configure(font=font11)
        self.TextReply.configure(foreground="black")
        self.TextReply.configure(highlightbackground="#d9d9d9")
        self.TextReply.configure(highlightcolor="black")
        self.TextReply.configure(insertbackground="black")
        self.TextReply.configure(selectbackground="#c4c4c4")
        self.TextReply.configure(selectforeground="black")
        self.TextReply.configure(width=604)
        self.TextReply.configure(wrap='word')


        self.ButtonReply = tk.Button(top, command=lambda: rep.reply_to_mail(body, self.TextReply.get("1.0", END), sender, mail, pwd))
        self.ButtonReply.place(relx=0.509, rely=0.815, height=64, width=227)
        self.ButtonReply.configure(activebackground="#ececec")
        self.ButtonReply.configure(activeforeground="#000000")
        self.ButtonReply.configure(background="#556080")
        self.ButtonReply.configure(disabledforeground="#a3a3a3")
        self.ButtonReply.configure(font=font11)
        self.ButtonReply.configure(foreground="#ffffff")
        self.ButtonReply.configure(highlightbackground="#d9d9d9")
        self.ButtonReply.configure(highlightcolor="black")
        self.ButtonReply.configure(pady="0")
        self.ButtonReply.configure(text='''Reply''')
        self.ButtonReply.configure(width=227)

        self.ButtonSeeSuggets = tk.Button(top, command=lambda: rep.get_simil(body, self.TextReply))
        self.ButtonSeeSuggets.place(relx=0.12, rely=0.815, height=64, width=227)
        self.ButtonSeeSuggets.configure(activebackground="#ececec")
        self.ButtonSeeSuggets.configure(activeforeground="#000000")
        self.ButtonSeeSuggets.configure(background="#EECD48")
        self.ButtonSeeSuggets.configure(disabledforeground="#a3a3a3")
        self.ButtonSeeSuggets.configure(font=font11)
        self.ButtonSeeSuggets.configure(foreground="#ffffff")
        self.ButtonSeeSuggets.configure(highlightbackground="#d9d9d9")
        self.ButtonSeeSuggets.configure(highlightcolor="black")
        self.ButtonSeeSuggets.configure(pady="0")
        self.ButtonSeeSuggets.configure(text='''See suggestions !!''')

if __name__ == '__main__':
    vp_start_gui()





