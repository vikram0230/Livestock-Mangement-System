#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.1
#  in conjunction with Tcl version 8.6
#    Feb 22, 2020 12:07:40 PM IST  platform: Windows NT

from backend import DataBase
import addGoat_support
from tkinter import DISABLED, NORMAL
from tkcalendar import DateEntry
from datetime import datetime, date
from tkinter import messagebox


import sys

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

from tkinter import IntVar, StringVar


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    addGoat_support.set_Tk_var()
    top = Toplevel1(root)
    addGoat_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel(root)
    addGoat_support.set_Tk_var()
    top = Toplevel1(w)
    addGoat_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#40e0d0'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#40e0d0'  # X11 color: 'gray85'
        _ana1color = '#40e0d0'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[
                       ('selected', _compcolor), ('active', _ana2color)])

        self.db = DataBase()

        top.geometry("1300x760+20+20")
        top.minsize(800, 500)
        top.maxsize(1500, 750)
        top.resizable(0, 0)
        top.title("New Toplevel")
        top.configure(background="#40e0d0")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Gid_10 = tk.Label(top)
        self.Gid_10.place(relx=0.427, rely=0.021, height=38, width=209)
        self.Gid_10.configure(activebackground="#f9f9f9")
        self.Gid_10.configure(activeforeground="black")
        self.Gid_10.configure(background="#d9d9d9")
        self.Gid_10.configure(disabledforeground="#a3a3a3")
        self.Gid_10.configure(font="-family {Segoe UI} -size 20 -weight bold")
        self.Gid_10.configure(foreground="#000000")
        self.Gid_10.configure(highlightbackground="#d9d9d9")
        self.Gid_10.configure(highlightcolor="black")
        self.Gid_10.configure(text='''ADD GOAT''')

        self.isBornOrBought = IntVar(None, 0)

        self.Rbtnborn = tk.Radiobutton(top, command=self.disableVaccination)
        self.Rbtnborn.place(relx=0.427, rely=0.095,
                            relheight=0.034, relwidth=0.075)
        self.Rbtnborn.configure(activebackground="#ececec")
        self.Rbtnborn.configure(activeforeground="#000000")
        self.Rbtnborn.configure(background="#d9d9d9")
        self.Rbtnborn.configure(disabledforeground="#a3a3a3")
        self.Rbtnborn.configure(foreground="#000000")
        self.Rbtnborn.configure(highlightbackground="#d9d9d9")
        self.Rbtnborn.configure(highlightcolor="black")
        self.Rbtnborn.configure(justify='left')
        self.Rbtnborn.configure(text='''BORN''')
        self.Rbtnborn.configure(value=0)
        self.Rbtnborn.configure(variable=self.isBornOrBought)

        self.Rbtnbought = tk.Radiobutton(top, command=self.disableMotherId)
        self.Rbtnbought.place(relx=0.513, rely=0.095,
                              relheight=0.034, relwidth=0.075)
        self.Rbtnbought.configure(activebackground="#ececec")
        self.Rbtnbought.configure(activeforeground="#000000")
        self.Rbtnbought.configure(background="#d9d9d9")
        self.Rbtnbought.configure(disabledforeground="#a3a3a3")
        self.Rbtnbought.configure(foreground="#000000")
        self.Rbtnbought.configure(highlightbackground="#d9d9d9")
        self.Rbtnbought.configure(highlightcolor="black")
        self.Rbtnbought.configure(justify='left')
        self.Rbtnbought.configure(text='''BOUGHT''')
        self.Rbtnbought.configure(value=1)
        self.Rbtnbought.configure(variable=self.isBornOrBought)

        self.gdetails = tk.Label(top)
        self.gdetails.place(x=130,y=100, height=35, width=130)
        self.gdetails.configure(activebackground="#f9f9f9")
        self.gdetails.configure(activeforeground="black")
        self.gdetails.configure(background="#d9d9d9")
        self.gdetails.configure(disabledforeground="#a3a3a3")
        self.gdetails.configure(font="-family {Segoe UI} -size 13")
        self.gdetails.configure(foreground="#000000")
        self.gdetails.configure(highlightbackground="#d9d9d9")
        self.gdetails.configure(highlightcolor="black")
        self.gdetails.configure(text='''GOAT DETAILS''')

        self.Gid = tk.Label(top)
        self.Gid.place(x=80,y=155, height=35, width=98)
        self.Gid.configure(activebackground="#f9f9f9")
        self.Gid.configure(activeforeground="black")
        self.Gid.configure(background="#d9d9d9")
        self.Gid.configure(disabledforeground="#a3a3a3")
        self.Gid.configure(foreground="#000000")
        self.Gid.configure(highlightbackground="#d9d9d9")
        self.Gid.configure(highlightcolor="black")
        self.Gid.configure(text='''Goat ID''')

        self.TEntry1 = ttk.Entry(top)
        self.TEntry1.place(x=250,y=155, height=35, width=140)
        self.TEntry1.configure(takefocus="")

        self.breed = tk.Label(top)
        self.breed.place(x=80,y=200, height=35, width=98)
        self.breed.configure(activebackground="#f9f9f9")
        self.breed.configure(activeforeground="black")
        self.breed.configure(background="#d9d9d9")
        self.breed.configure(disabledforeground="#a3a3a3")
        self.breed.configure(foreground="#000000")
        self.breed.configure(highlightbackground="#d9d9d9")
        self.breed.configure(highlightcolor="black")
        self.breed.configure(text='''Breed''')

        self.TEntry1_22 = ttk.Entry(top)
        self.TEntry1_22.place(x=250,y=200,height=35, width=140)
        self.TEntry1_22.configure(takefocus="")

        self.DOB = tk.Label(top)
        self.DOB.place(x=80,y=245, height=35, width=98)
        self.DOB.configure(activebackground="#f9f9f9")
        self.DOB.configure(activeforeground="black")
        self.DOB.configure(background="#d9d9d9")
        self.DOB.configure(disabledforeground="#a3a3a3")
        self.DOB.configure(foreground="#000000")
        self.DOB.configure(highlightbackground="#d9d9d9")
        self.DOB.configure(highlightcolor="black")
        self.DOB.configure(text='''DOB''')

        self.goatDob = DateEntry(top, width=12, year=2019, month=6, day=22, 
        background='darkblue', foreground='white', borderwidth=2)
        self.goatDob.place(x=250,y=245, height=35, width=140)

        self.mother_id = tk.Label(top)
        self.mother_id.place(x=80,y=290, height=35, width=98)
        self.mother_id.configure(activebackground="#f9f9f9")
        self.mother_id.configure(activeforeground="black")
        self.mother_id.configure(background="#d9d9d9")
        self.mother_id.configure(disabledforeground="#a3a3a3")
        self.mother_id.configure(foreground="#000000")
        self.mother_id.configure(highlightbackground="#d9d9d9")
        self.mother_id.configure(highlightcolor="black")
        self.mother_id.configure(text='''Mother ID''')

        self.TEntry1_24 = ttk.Entry(top)
        self.TEntry1_24.place(x=250,y=335,height=35, width=140)
        self.TEntry1_24.configure(takefocus="")

        self.weight = tk.Label(top)
        self.weight.place(x=80,y=335, height=35, width=98)
        self.weight.configure(activebackground="#f9f9f9")
        self.weight.configure(activeforeground="black")
        self.weight.configure(background="#d9d9d9")
        self.weight.configure(disabledforeground="#a3a3a3")
        self.weight.configure(foreground="#000000")
        self.weight.configure(highlightbackground="#d9d9d9")
        self.weight.configure(highlightcolor="black")
        self.weight.configure(text='''Weight''')

        self.TEntry1_25 = ttk.Entry(top)
        self.TEntry1_25.place(x=250,y=290,height=35, width=140)
        self.TEntry1_25.configure(takefocus="")

        self.gender = tk.Label(top)
        self.gender.place(x=80,y=395, height=40, width=98)
        self.gender.configure(activebackground="#f9f9f9")
        self.gender.configure(activeforeground="black")
        self.gender.configure(background="#d9d9d9")
        self.gender.configure(disabledforeground="#a3a3a3")
        self.gender.configure(foreground="#000000")
        self.gender.configure(highlightbackground="#d9d9d9")
        self.gender.configure(highlightcolor="black")
        self.gender.configure(text='''Gender''')

        self.genderVal = IntVar()

        self.RbtnMale = tk.Radiobutton(top)
        self.RbtnMale.place(x=250,y=380,height=30,width=80)
        self.RbtnMale.configure(activebackground="#ececec")
        self.RbtnMale.configure(activeforeground="#000000")
        self.RbtnMale.configure(background="#d9d9d9")
        self.RbtnMale.configure(disabledforeground="#a3a3a3")
        self.RbtnMale.configure(foreground="#000000")
        self.RbtnMale.configure(highlightbackground="#d9d9d9")
        self.RbtnMale.configure(highlightcolor="black")
        self.RbtnMale.configure(justify='left')
        self.RbtnMale.configure(text='''MALE''')
        self.RbtnMale.configure(value=0)
        self.RbtnMale.configure(variable=self.genderVal)

        self.RbtnFemale = tk.Radiobutton(top)
        self.RbtnFemale.place(x=250,y=420,height=30,width=80)
        self.RbtnFemale.configure(activebackground="#ececec")
        self.RbtnFemale.configure(activeforeground="#000000")
        self.RbtnFemale.configure(background="#d9d9d9")
        self.RbtnFemale.configure(disabledforeground="#a3a3a3")
        self.RbtnFemale.configure(foreground="#000000")
        self.RbtnFemale.configure(highlightbackground="#d9d9d9")
        self.RbtnFemale.configure(highlightcolor="black")
        self.RbtnFemale.configure(justify='left')
        self.RbtnFemale.configure(text='''FEMALE''')
        self.RbtnFemale.configure(value=1)
        self.RbtnFemale.configure(variable=self.genderVal)

        self.health = tk.Label(top)
        self.health.place(x=890,y=100, height=35, width=150)
        self.health.configure(activebackground="#f9f9f9")
        self.health.configure(activeforeground="black")
        self.health.configure(background="#d9d9d9")
        self.health.configure(disabledforeground="#a3a3a3")
        self.health.configure(font="-family {Segoe UI} -size 12")
        self.health.configure(foreground="#000000")
        self.health.configure(highlightbackground="#d9d9d9")
        self.health.configure(highlightcolor="black")
        self.health.configure(text='''LAST VACCINATED''')

        self.v1 = tk.Label(top)
        self.v1.place(x=800,y=155, height=35, width=98)
        self.v1.configure(activebackground="#f9f9f9")
        self.v1.configure(activeforeground="black")
        self.v1.configure(background="#d9d9d9")
        self.v1.configure(disabledforeground="#a3a3a3")
        self.v1.configure(foreground="#000000")
        self.v1.configure(highlightbackground="#d9d9d9")
        self.v1.configure(highlightcolor="black")
        self.v1.configure(text='''V1''')

        self.cal1 = DateEntry(top, width=12, year=2020, month=6, day=22, 
        background='darkblue', foreground='white', borderwidth=2)
        self.cal1.place(x=1000,y=155, height=35, width=98)

        self.v2 = tk.Label(top)
        self.v2.place(x=800,y=200, height=35, width=98)
        self.v2.configure(activebackground="#f9f9f9")
        self.v2.configure(activeforeground="black")
        self.v2.configure(background="#d9d9d9")
        self.v2.configure(disabledforeground="#a3a3a3")
        self.v2.configure(foreground="#000000")
        self.v2.configure(highlightbackground="#d9d9d9")
        self.v2.configure(highlightcolor="black")
        self.v2.configure(text='''V2''')

        self.cal2 = DateEntry(top, width=12, year=2019, month=6, day=22, 
        background='darkblue', foreground='white', borderwidth=2)
        self.cal2.place(x=1000,y=200, height=35, width=98)

        self.v3 = tk.Label(top)
        self.v3.place(x=800,y=245, height=35, width=98)
        self.v3.configure(activebackground="#f9f9f9")
        self.v3.configure(activeforeground="black")
        self.v3.configure(background="#d9d9d9")
        self.v3.configure(disabledforeground="#a3a3a3")
        self.v3.configure(foreground="#000000")
        self.v3.configure(highlightbackground="#d9d9d9")
        self.v3.configure(highlightcolor="black")
        self.v3.configure(text='''V3''')

        self.cal3 = DateEntry(top, width=12, year=2019, month=6, day=22, 
        background='darkblue', foreground='white', borderwidth=2)
        self.cal3.place(x=1000,y=245, height=35, width=98)

        self.v4 = tk.Label(top)
        self.v4.place(x=800,y=290, height=35, width=98)
        self.v4.configure(activebackground="#f9f9f9")
        self.v4.configure(activeforeground="black")
        self.v4.configure(background="#d9d9d9")
        self.v4.configure(disabledforeground="#a3a3a3")
        self.v4.configure(foreground="#000000")
        self.v4.configure(highlightbackground="#d9d9d9")
        self.v4.configure(highlightcolor="black")
        self.v4.configure(text='''V4''')

        self.cal4 = DateEntry(top, width=12, year=2019, month=6, day=22, 
        background='darkblue', foreground='white', borderwidth=2)
        self.cal4.place(x=1000,y=290, height=35, width=98)

        self.v5 = tk.Label(top)
        self.v5.place(x=800,y=335, height=35, width=98)
        self.v5.configure(activebackground="#f9f9f9")
        self.v5.configure(activeforeground="black")
        self.v5.configure(background="#d9d9d9")
        self.v5.configure(disabledforeground="#a3a3a3")
        self.v5.configure(foreground="#000000")
        self.v5.configure(highlightbackground="#d9d9d9")
        self.v5.configure(highlightcolor="black")
        self.v5.configure(text='''V5''')

        self.cal5 = DateEntry(top, width=12, year=2019, month=6, day=22, 
        background='darkblue', foreground='white', borderwidth=2)
        self.cal5.place(x=1000,y=335, height=35, width=98)

        self.v6 = tk.Label(top)
        self.v6.place(x=800,y=380, height=35, width=98)
        self.v6.configure(activebackground="#f9f9f9")
        self.v6.configure(activeforeground="black")
        self.v6.configure(background="#d9d9d9")
        self.v6.configure(disabledforeground="#a3a3a3")
        self.v6.configure(foreground="#000000")
        self.v6.configure(highlightbackground="#d9d9d9")
        self.v6.configure(highlightcolor="black")
        self.v6.configure(text='''V6''')

        self.cal6 = DateEntry(top, width=12, year=2019, month=6, day=22, 
        background='darkblue', foreground='white', borderwidth=2)
        self.cal6.place(x=1000,y=380, height=35, width=98)

        self.v7 = tk.Label(top)
        self.v7.place(x=800,y=425, height=35, width=98)
        self.v7.configure(activebackground="#f9f9f9")
        self.v7.configure(activeforeground="black")
        self.v7.configure(background="#d9d9d9")
        self.v7.configure(disabledforeground="#a3a3a3")
        self.v7.configure(foreground="#000000")
        self.v7.configure(highlightbackground="#d9d9d9")
        self.v7.configure(highlightcolor="black")
        self.v7.configure(text='''V7''')

        self.cal8 = DateEntry(top, width=12, year=2019, month=6, day=22, 
        background='darkblue', foreground='white', borderwidth=2)
        self.cal8.place(x=1000,y=425, height=35, width=98)

        self.v8 = tk.Label(top)
        self.v8.place(x=800,y=470, height=35, width=98)
        self.v8.configure(activebackground="#f9f9f9")
        self.v8.configure(activeforeground="black")
        self.v8.configure(background="#d9d9d9")
        self.v8.configure(disabledforeground="#a3a3a3")
        self.v8.configure(foreground="#000000")
        self.v8.configure(highlightbackground="#d9d9d9")
        self.v8.configure(highlightcolor="black")
        self.v8.configure(text='''V8''')

        self.cal8 = DateEntry(top, width=12, year=2019, month=6, day=22, 
        background='darkblue', foreground='white', borderwidth=2)
        self.cal8.place(x=1000,y=470, height=35, width=98)

        self.Submit = tk.Button(top, command=self.acceptValues)
        self.Submit.place(relx=0.550, rely=0.842, height=30, width=59)
        self.Submit.configure(activebackground="#ececec")
        self.Submit.configure(activeforeground="#000000")
        self.Submit.configure(background="#d9d9d9")
        self.Submit.configure(disabledforeground="#a3a3a3")
        self.Submit.configure(foreground="#000000")
        self.Submit.configure(highlightbackground="#d9d9d9")
        self.Submit.configure(highlightcolor="black")
        self.Submit.configure(pady="0")
        self.Submit.configure(text='''SUBMIT''')

        self.Cancel = tk.Button(top, command=lambda: addGoat_support.destroy_window())
        self.Cancel.place(relx=0.430, rely=0.842, height=30, width=59)
        self.Cancel.configure(activebackground="#ececec")
        self.Cancel.configure(activeforeground="#000000")
        self.Cancel.configure(background="#d9d9d9")
        self.Cancel.configure(disabledforeground="#a3a3a3")
        self.Cancel.configure(foreground="#000000")
        self.Cancel.configure(highlightbackground="#d9d9d9")
        self.Cancel.configure(highlightcolor="black")
        self.Cancel.configure(pady="0")
        self.Cancel.configure(text='''CANCEL''')

        self.goatDob.set_date(datetime.date(datetime.now()))
        self.cal1.set_date(datetime.date(datetime.now()))
        self.cal2.set_date(datetime.date(datetime.now()))
        self.cal3.set_date(datetime.date(datetime.now()))
        self.cal4.set_date(datetime.date(datetime.now()))
        self.cal5.set_date(datetime.date(datetime.now()))
        self.cal6.set_date(datetime.date(datetime.now()))
        self.cal7.set_date(datetime.date(datetime.now()))
        self.cal8.set_date(datetime.date(datetime.now()))

    def acceptValues(self):
        goat_id = int(self.TEntry1.get())
        g_breed = self.TEntry1_22.get()
        g_dob = self.goatDob.get_date()
        g_weight = int(self.TEntry1_24.get())
        g_motherId = self.TEntry1_25.get()
        g_gender = 'm' if int(self.genderVal.get()) == 0 else 'f'
        g_isBornOrBought = self.isBornOrBought.get()

        v1Date = self.cal1.get_date()
        v2Date = self.cal2.get_date()
        v3Date = self.cal3.get_date()
        v4Date = self.cal4.get_date()
        v5Date = self.cal5.get_date()
        v6Date = self.cal6.get_date()
        v7Date = self.cal7.get_date()
        v8Date = self.cal8.get_date()

        # born = 0

        if g_gender == 'f' and g_isBornOrBought == 0:
            self.db.insertGoatRecord({'goat_id': goat_id, 'breed': g_breed, 'date_of_birth': g_dob,
                                'weight': g_weight, 'gender': g_gender, 'pregnant': 'No'}, mother_id=g_motherId)
        elif g_gender == 'f' and g_isBornOrBought == 1:
            self.db.insertGoatRecord({'goat_id': goat_id, 'breed': g_breed, 'date_of_birth': g_dob,
                                'weight': g_weight, 'gender': g_gender, 'pregnant': 'No', 'v1': str(v1Date), 'v2': str(v2Date), 'v3': str(v3Date), 'v4': str(v4Date), 'v5': str(v5Date), 'v6': str(v6Date), 'v7': str(v6Date), 'v8': str(v6Date)}, mother_id='null')
        elif g_gender == 'm' and g_isBornOrBought == 0:
            self.db.insertGoatRecord({'goat_id': goat_id, 'breed': g_breed, 'date_of_birth': g_dob,
                                'weight': g_weight, 'gender': g_gender, 'pregnant': 'No'}, mother_id=g_motherId)
        elif g_gender == 'm' and g_isBornOrBought == 1:
            self.db.insertGoatRecord({'goat_id': goat_id, 'breed': g_breed, 'date_of_birth': g_dob,
                                'weight': g_weight, 'gender': g_gender, 'pregnant': 'No', 'v1': str(v1Date), 'v2': str(v2Date), 'v3': str(v3Date), 'v4': str(v4Date), 'v5': str(v5Date), 'v6': str(v6Date), 'v7': str(v6Date), 'v8': str(v6Date)}, mother_id='null')

        self.showSuccess()
        
        print({'goat_id': goat_id, 'breed': g_breed, 'date_of_birth': g_dob,
                                'weight': g_weight, 'gender': g_gender, 'pregnant': 'No', 'v1': str(v1Date), 'v2': str(v2Date), 'v3': str(v3Date), 'v4': str(v4Date), 'v5': str(v5Date), 'v6': str(v6Date), 'v7': str(v6Date), 'v8': str(v6Date)})

        addGoat_support.destroy_window()

    def disableVaccination(self):
        self.TEntry1_25.config(state=NORMAL)  
        self.cal1.config(state=DISABLED)
        self.cal2.config(state=DISABLED)
        self.cal3.config(state=DISABLED)
        self.cal4.config(state=DISABLED)
        self.cal5.config(state=DISABLED)
        self.cal6.config(state=DISABLED)
        self.cal7.config(state=DISABLED)
        self.cal8.config(state=DISABLED)

    def disableMotherId(self):
        self.TEntry1_25.config(state=DISABLED) 
        self.cal1.config(state=NORMAL)
        self.cal2.config(state=NORMAL)
        self.cal3.config(state=NORMAL)
        self.cal4.config(state=NORMAL)
        self.cal5.config(state=NORMAL)
        self.cal6.config(state=NORMAL)
        self.cal7.config(state=NORMAL)
        self.cal8.config(state=NORMAL)

    def errorMsg(self):
        tk.messagebox.showerror("Input Error","Incorrect Data!")

    def showSuccess(self):
        tk.messagebox.showinfo("Success","Successfully Inserted")


if __name__ == '__main__':
    vp_start_gui()
