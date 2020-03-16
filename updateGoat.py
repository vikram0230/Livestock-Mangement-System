#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.2
#  in conjunction with Tcl version 8.6
#    Mar 10, 2020 10:12:20 AM IST  platform: Windows NT

import sys
from tkinter import messagebox
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

from tkinter import DISABLED, NORMAL
import updateGoat_support
from tkinter import BooleanVar, IntVar, END
from backend import DataBase
from datetime import datetime, date
from tkcalendar.dateentry import DateEntry

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    updateGoat_support.set_Tk_var()
    top = Toplevel1 (root)
    updateGoat_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    updateGoat_support.set_Tk_var()

    goatData = args[0]

    top = Toplevel1(w, goatData)
    updateGoat_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None, goatData=[]):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 9"
        font9 = "-family {Segoe UI} -size 12 -weight bold"

        top.geometry("450x690+484+55")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Update Goat")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.goatData = goatData
        self.db = DataBase()

        # By default self.mortality should be 1
        self.mortality = 'Alive'
        self.pregnant = 'No'

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.358, rely=0.001, height=29, width=118)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''UPDATE GOAT''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.042, rely=0.05, height=21, width=134)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''GOAT ID''')

        self.Text01 = tk.Entry(self.Frame1)
        self.Text01.place(relx=0.421, rely=0.05, relheight=0.04, relwidth=0.25)
        self.Text01.configure(background="white")
        self.Text01.configure(font="TkTextFont")
        self.Text01.configure(foreground="black")
        self.Text01.configure(highlightbackground="#d9d9d9")
        self.Text01.configure(highlightcolor="black")
        self.Text01.configure(insertbackground="black")
        self.Text01.configure(selectbackground="#c4c4c4")
        self.Text01.configure(selectforeground="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.042, rely=0.1, height=21, width=134)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''BREED''')

        self.Text02 = tk.Entry(self.Frame1)
        self.Text02.place(relx=0.421, rely=0.1, relheight=0.04, relwidth=0.25)
        self.Text02.configure(background="white")
        self.Text02.configure(font="TkTextFont")
        self.Text02.configure(foreground="black")
        self.Text02.configure(highlightbackground="#d9d9d9")
        self.Text02.configure(highlightcolor="black")
        self.Text02.configure(insertbackground="black")
        self.Text02.configure(selectbackground="#c4c4c4")
        self.Text02.configure(selectforeground="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.042, rely=0.15, height=21, width=134)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''DATE OF BIRTH''')

        self.Text03 = DateEntry(self.Frame1, width=12, year=2020, month=6, day=22, 
        background='darkblue', foreground='white', borderwidth=2)
        self.Text03.place(relx=0.421, rely=0.15, relheight=0.04, relwidth=0.25)

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.042, rely=0.2, height=21, width=134)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''PREGNANT DETAILS''')

        self.Label2_1 = tk.Label(self.Frame1)
        self.Label2_1.place(relx=0.084, rely=0.24, height=21, width=84)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#d9d9d9")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''PREGNANT''')

        self.Label2_2 = tk.Label(self.Frame1)
        self.Label2_2.place(relx=0.042, rely=0.28, height=21, width=104)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(background="#d9d9d9")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Label2_2.configure(foreground="#000000")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text='''WEIGHT DETAILS''')

        self.Label2_1 = tk.Label(self.Frame1)
        self.Label2_1.place(relx=0.084, rely=0.32, height=31, width=44)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#d9d9d9")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''WEIGHT''')

        self.Text2 = tk.Entry(self.Frame1)
        self.Text2.place(relx=0.421, rely=0.32, relheight=0.04, relwidth=0.135)
        self.Text2.configure(background="white")
        self.Text2.configure(font="TkTextFont")
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="#c4c4c4")
        self.Text2.configure(selectforeground="black")

        self.Label2_3 = tk.Label(self.Frame1)
        self.Label2_3.place(relx=0.035, rely=0.37, height=21, width=84)
        self.Label2_3.configure(activebackground="#f9f9f9")
        self.Label2_3.configure(activeforeground="black")
        self.Label2_3.configure(background="#d9d9d9")
        self.Label2_3.configure(disabledforeground="#a3a3a3")
        self.Label2_3.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Label2_3.configure(foreground="#000000")
        self.Label2_3.configure(highlightbackground="#d9d9d9")
        self.Label2_3.configure(highlightcolor="black")
        self.Label2_3.configure(text='''MORTALITY''')

        self.Label2_3 = tk.Label(self.Frame1)
        self.Label2_3.place(relx=0.047, rely=0.42, height=21, width=34)
        self.Label2_3.configure(activebackground="#f9f9f9")
        self.Label2_3.configure(activeforeground="black")
        self.Label2_3.configure(background="#d9d9d9")
        self.Label2_3.configure(disabledforeground="#a3a3a3")
        self.Label2_3.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Label2_3.configure(foreground="#000000")
        self.Label2_3.configure(highlightbackground="#d9d9d9")
        self.Label2_3.configure(highlightcolor="black")
        self.Label2_3.configure(text='''SOLD''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.065, rely=0.45, height=21, width=94)
        self.Label3.place_forget()
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font10)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''SOLD RATE''')

        self.Text1 = tk.Entry(self.Frame1)
        self.Text1.place(relx=0.421, rely=0.45, relheight=0.04, relwidth=0.25)
        self.Text1.place_forget()
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")

        self.Label0 = tk.Label(self.Frame1)
        self.Label0.place(relx=0.046, rely=0.52, height=21, width=94)
        self.Label0.configure(activebackground="#f9f9f9")
        self.Label0.configure(activeforeground="black")
        self.Label0.configure(background="#d9d9d9")
        self.Label0.configure(disabledforeground="#a3a3a3")
        self.Label0.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Label0.configure(foreground="#000000")
        self.Label0.configure(highlightbackground="#d9d9d9")
        self.Label0.configure(highlightcolor="black")
        self.Label0.configure(text='''VACCINATION''')

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.15, rely=0.55, height=21, width=180)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Anthrax''')

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.15, rely=0.6, height=21, width=180)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Haemorrhagic Septicemia(H.S)''')

        self.Label6 = tk.Label(self.Frame1)
        self.Label6.place(relx=0.15, rely=0.65, height=21, width=180)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Enterotoxaemia''')

        self.Label7 = tk.Label(self.Frame1)
        self.Label7.place(relx=0.18, rely=0.7, height=21, width=180)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Black Quarter''')

        self.Label8 = tk.Label(self.Frame1)
        self.Label8.place(relx=0.15, rely=0.75, height=21, width=180)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''P.P.R.''')

        self.Label9 = tk.Label(self.Frame1)
        self.Label9.place(relx=0.15, rely=0.8, height=21, width=180)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(text='''Foot & mouth disease''')

        self.Label10 = tk.Label(self.Frame1)
        self.Label10.place(relx=0.15, rely=0.85, height=21, width=180)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(activeforeground="black")
        self.Label10.configure(background="#d9d9d9")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(highlightbackground="#d9d9d9")
        self.Label10.configure(highlightcolor="black")
        self.Label10.configure(text='''Goat Pox''')

        self.Label11 = tk.Label(self.Frame1)
        self.Label11.place(relx=0.15, rely=0.9, height=21, width=180)
        self.Label11.configure(activebackground="#f9f9f9")
        self.Label11.configure(activeforeground="black")
        self.Label11.configure(background="#d9d9d9")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(highlightbackground="#d9d9d9")
        self.Label11.configure(highlightcolor="black")
        self.Label11.configure(text='''C.C.P.P''')

        self.Button1 = tk.Button(self.Frame1, command=lambda:self.vaccinated(1))
        self.Button1.place(relx=0.55, rely=0.55, height=24, width=140)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''REMOVE VACCINATION''')

        self.Button2 = tk.Button(self.Frame1, command=lambda:self.vaccinated(2))
        self.Button2.place(relx=0.55, rely=0.6, height=24, width=140)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''REMOVE VACCINATION''')

        self.Button3 = tk.Button(self.Frame1, command=lambda:self.vaccinated(3))
        self.Button3.place(relx=0.55, rely=0.65, height=24, width=140)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''REMOVE VACCINATION''')

        self.Button4 = tk.Button(self.Frame1, command=lambda:self.vaccinated(4))
        self.Button4.place(relx=0.55, rely=0.7, height=24, width=140)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''REMOVE VACCINATION''')

        self.Button5 = tk.Button(self.Frame1, command=lambda:self.vaccinated(5))
        self.Button5.place(relx=0.55, rely=0.75, height=24, width=140)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''REMOVE VACCINATION''')

        self.Button6 = tk.Button(self.Frame1, command=lambda:self.vaccinated(6))
        self.Button6.place(relx=0.55, rely=0.8, height=24, width=140)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''REMOVE VACCINATION''')

        self.Button6_1 = tk.Button(self.Frame1, command=lambda:self.vaccinated(7))
        self.Button6_1.place(relx=0.55, rely=0.85, height=24, width=140)
        self.Button6_1.configure(activebackground="#ececec")
        self.Button6_1.configure(activeforeground="#000000")
        self.Button6_1.configure(background="#d9d9d9")
        self.Button6_1.configure(disabledforeground="#a3a3a3")
        self.Button6_1.configure(foreground="#000000")
        self.Button6_1.configure(highlightbackground="#d9d9d9")
        self.Button6_1.configure(highlightcolor="black")
        self.Button6_1.configure(pady="0")
        self.Button6_1.configure(text='''REMOVE VACCINATION''')

        self.Button6_2 = tk.Button(self.Frame1, command=lambda:self.vaccinated(8))
        self.Button6_2.place(relx=0.55, rely=0.9, height=24, width=140)
        self.Button6_2.configure(activebackground="#ececec")
        self.Button6_2.configure(activeforeground="#000000")
        self.Button6_2.configure(background="#d9d9d9")
        self.Button6_2.configure(disabledforeground="#a3a3a3")
        self.Button6_2.configure(foreground="#000000")
        self.Button6_2.configure(highlightbackground="#d9d9d9")
        self.Button6_2.configure(highlightcolor="black")
        self.Button6_2.configure(pady="0")
        self.Button6_2.configure(text='''REMOVE VACCINATION''')

        self.Button7 = tk.Button(self.Frame1, command=destroy_Toplevel1)
        self.Button7.place(relx=0.232, rely=0.95, height=24, width=56)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''CANCEL''')

        self.Button8 = tk.Button(self.Frame1, command=self.submitData)
        self.Button8.place(relx=0.604, rely=0.95, height=24, width=56)
        self.Button8.configure(activebackground="#ececec")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#d9d9d9")
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''SAVE''')

        self.isPregnant = IntVar()

        self.Radiobutton1 = tk.Radiobutton(self.Frame1, command=lambda: self.setPregnancy(1))
        self.Radiobutton1.place(relx=0.421, rely=0.24, relheight=0.041
                , relwidth=0.099)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#d9d9d9")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(text='''YES''')
        self.Radiobutton1.configure(value=1)
        self.Radiobutton1.configure(variable=self.isPregnant)

        self.Radiobutton2 = tk.Radiobutton(self.Frame1, command=lambda: self.setPregnancy(0))
        self.Radiobutton2.place(relx=0.653, rely=0.24, relheight=0.041
                , relwidth=0.122)
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#d9d9d9")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify='left')
        self.Radiobutton2.configure(text='''NO''')
        self.Radiobutton2.configure(value=0)
        self.Radiobutton2.configure(variable=self.isPregnant)

        self.isAlive = IntVar()

        self.Radiobutton3 = tk.Radiobutton(self.Frame1, command=lambda: self.setMortality(1))
        self.Radiobutton3.place(relx=0.421, rely=0.37, relheight=0.041
                , relwidth=0.143)
        self.Radiobutton3.configure(activebackground="#ececec")
        self.Radiobutton3.configure(activeforeground="#000000")
        self.Radiobutton3.configure(background="#d9d9d9")
        self.Radiobutton3.configure(disabledforeground="#a3a3a3")
        self.Radiobutton3.configure(foreground="#000000")
        self.Radiobutton3.configure(highlightbackground="#d9d9d9")
        self.Radiobutton3.configure(highlightcolor="black")
        self.Radiobutton3.configure(justify='left')
        self.Radiobutton3.configure(text='''ALIVE''')
        self.Radiobutton3.configure(value=1)
        self.Radiobutton3.configure(variable=self.isAlive)

        self.Radiobutton4 = tk.Radiobutton(self.Frame1, command=lambda: self.setMortality(0))
        self.Radiobutton4.place(relx=0.653, rely=0.37, relheight=0.041
                , relwidth=0.143)
        self.Radiobutton4.configure(activebackground="#ececec")
        self.Radiobutton4.configure(activeforeground="#000000")
        self.Radiobutton4.configure(background="#d9d9d9")
        self.Radiobutton4.configure(disabledforeground="#a3a3a3")
        self.Radiobutton4.configure(foreground="#000000")
        self.Radiobutton4.configure(highlightbackground="#d9d9d9")
        self.Radiobutton4.configure(highlightcolor="black")
        self.Radiobutton4.configure(justify='left')
        self.Radiobutton4.configure(text='''DEAD''')
        self.Radiobutton4.configure(value=0)
        self.Radiobutton4.configure(variable=self.isAlive)

        self.isSold = IntVar()

        self.Radiobutton5 = tk.Radiobutton(self.Frame1, command=lambda: self.showSoldFrame(self.Label3, self.Text1))
        self.Radiobutton5.place(relx=0.421, rely=0.42, relheight=0.041
                , relwidth=0.122)
        self.Radiobutton5.configure(activebackground="#ececec")
        self.Radiobutton5.configure(activeforeground="#000000")
        self.Radiobutton5.configure(background="#d9d9d9")
        self.Radiobutton5.configure(disabledforeground="#a3a3a3")
        self.Radiobutton5.configure(foreground="#000000")
        self.Radiobutton5.configure(highlightbackground="#d9d9d9")
        self.Radiobutton5.configure(highlightcolor="black")
        self.Radiobutton5.configure(justify='left')
        self.Radiobutton5.configure(text='''YES''')
        self.Radiobutton5.configure(value=1)
        self.Radiobutton5.configure(variable=self.isSold)

        self.Radiobutton6 = tk.Radiobutton(self.Frame1, command=lambda: self.hideSoldFrame(self.Label3, self.Text1))
        self.Radiobutton6.place(relx=0.653, rely=0.42, relheight=0.041
                , relwidth=0.122)
        self.Radiobutton6.configure(activebackground="#ececec")
        self.Radiobutton6.configure(activeforeground="#000000")
        self.Radiobutton6.configure(background="#d9d9d9")
        self.Radiobutton6.configure(disabledforeground="#a3a3a3")
        self.Radiobutton6.configure(foreground="#000000")
        self.Radiobutton6.configure(highlightbackground="#d9d9d9")
        self.Radiobutton6.configure(highlightcolor="black")
        self.Radiobutton6.configure(justify='left')
        self.Radiobutton6.configure(text='''NO''')
        self.Radiobutton6.configure(value=0)
        self.Radiobutton6.configure(variable=self.isSold)

        # Disable the pregnancy radiobuttons if goat is male
        self.male = self.goatData[3]
        if self.male == 'm':
            self.Radiobutton1.config(state=DISABLED)
            self.Radiobutton2.config(state=DISABLED)
        else:
            self.Radiobutton1.config(state=NORMAL)
            self.Radiobutton2.config(state=NORMAL)

        self.Radiobutton2.select()

        # Disable Goat ID entry
        self.Text01.delete(0, END)
        self.Text01.insert(END, self.goatData[0])
        self.Text01.config(state=DISABLED)

        # Insert default value for breed
        self.Text02.delete(0, END)
        self.Text02.insert(END, self.goatData[1])

        # Insert default value for DOB
        self.Text03.set_date(datetime.strptime(self.goatData[2], '%Y-%m-%d').date())

    def setMortality(self, value):
        self.mortality = 'Alive' if value == 1 else 'Dead'

    def setPregnancy(self, value):
        self.pregnant = 'Yes' if value == 1 else 'No'

    def submitData(self):
        if self.male == 'f':
            pregnant = self.pregnant
        else:
            pregnant = 'No'

        alive = self.mortality

        # Checking if Weight has been updated or not
        try:
            weight = int(self.Text2.get())
            isWeightUpdated = True
        except:
            isWeightUpdated = False
            weight = 0

        try:
            sold_rate = int(self.Text1.get())
        except:
            sold_rate = None
            sold = False
        else:
            sold = True

        # Get breed
        breed = self.Text02.get()
        
        # Get DOB
        dob = self.Text03.get_date()

        if isWeightUpdated:
            self.db.updateGoatRecord(goatValues={
                'goat_id': self.goatData[0],
                'pregnant': pregnant,
                'breed': breed,
                'dob': dob,
                'weight': weight,
                'mortality': alive,
                'sold_rate': sold_rate,
                'sold_date': str(datetime.date(datetime.now()))
            }, isSold=sold, isWeightUpdated=isWeightUpdated)
        else:
            self.db.updateGoatRecord(goatValues={
                'goat_id': self.goatData[0],
                'pregnant': pregnant,
                'breed': breed,
                'dob': dob,
                'mortality': alive,
                'sold_rate': sold_rate,
                'sold_date': str(datetime.date(datetime.now()))
            }, isSold=sold, isWeightUpdated=isWeightUpdated)

        print({
                'goat_id': self.goatData[0],
                'weight': weight,
                'pregnant': pregnant,
                'mortality': alive,
                'sold_rate': sold_rate,
                'sold_date': str(datetime.date(datetime.now())),
                'breed': breed,
                'dob': dob
            }, sold)

        destroy_Toplevel1()

    def vaccinated(self, vacc_no):
        self.db.updateVaccination(vacc_no, self.goatData[0])
        messagebox.showinfo("Update","Vaccination Removed successfully")
        w.deiconify()

    def hideSoldFrame(self, widget1, widget2):
        widget1.place_forget()
        widget2.place_forget()

    def showSoldFrame(self, widget1, widget2):
        widget1.place(relx=0.065, rely=0.47, height=21, width=94)
        widget2.place(relx=0.421, rely=0.46, relheight=0.04, relwidth=0.25)