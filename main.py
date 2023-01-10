from tkinter import *
from tkinter import messagebox
from tkcalendar import *
import pymysql


class MyFormulaire:
     def __init__(self, appFrom):
         self.appFrom = appFrom
         self.appFrom.title("Formulaire avec une base de données")
         self.appFrom.geometry("800x600")
         self.appFrom.iconbitmap("icon_sql.ico")
         self.appFrom.config(bg="#1E90FF")

         # La fenêtre des champs du formulaire :
         frame = Frame(self.appFrom, bg="#00BFFF")
         frame.place(x=150, y=100, width=700, height=400)
         title = Label(frame, text="Creer un compte",bg="#00BFFF", fg="white", font=('algerian', 20)).place(x=5, y=5)

         frame1 = Frame(frame, bg="#ADD8E6")
         frame1.pack(expand=YES)

         # Les champs de renseignement :

         prenom = Label(frame1, text="Prénom: ", bg="#ADD8E6", fg="black", font=('time new roman', 10))
         prenom.grid(row=0, column=0)
         self.prenom_entry = Entry(frame1, fg="white", width=60)
         self.prenom_entry.grid(row=0, column=2)

         nom = Label(frame1, text="Nom    : ", bg="#ADD8E6", fg="black", font=('time new roman', 10))
         nom.grid(row=1, column=0)
         self.nom_entry = Entry(frame1, fg="white", width=60)
         self.nom_entry.grid(row=1, column=2)

         date_naissance = Label(frame1, text="Date de naissance: ", bg="#ADD8E6", fg="black", font=('time new roman', 10))
         date_naissance.grid(row=3, column=0)
         self.date_naissance_entry = DateEntry(frame1, fg="white", date_pattern="dd/mm/yy")
         self.date_naissance_entry.grid(row=3, column=2)

         pays = Label(frame1, text="Pays de naissance: ", bg="#ADD8E6", fg="black", font=('time new roman', 10))
         pays.grid(row=4, column=0)
         self.pays_entry = Entry(frame1, fg="white", width=60)
         self.pays_entry.grid(row=4, column=2)

         email = Label(frame1, text="Email: ", bg="#ADD8E6", fg="black", font=('time new roman', 10))
         email.grid(row=5, column=0)
         self.email_entry = Entry(frame1, fg="white", width=60)
         self.email_entry.grid(row=5, column=2)






appFrom = Tk()
obj = MyFormulaire(appFrom)
appFrom.mainloop()