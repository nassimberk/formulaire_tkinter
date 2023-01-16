from tkinter import *
from tkinter import messagebox
from tkcalendar import *
import pymysql
from PIL import ImageTk,Image




class MyFormulaire:
     def __init__(self, appFrom):
         self.appFrom = appFrom
         self.appFrom.title("Formulaire avec une base de données")
         self.appFrom.geometry("708x498")
         self.appFrom.resizable(width=False, height=False)
         self.appFrom.iconbitmap("icon_sql.ico")
         self.image_FDC = Image.open("image_bg.png")
         self.image_BG = ImageTk.PhotoImage(self.image_FDC)
         self.FDC = Label(appFrom, image=self.image_BG)
         self.FDC.place(x=0, y=0)



         # La fenêtre des champs du formulaire :
         frame = Frame(self.appFrom, bg="#FF8C00")
         frame.place(x=50, y=50, width=600, height=400)
         title = Label(frame, text="Creer un compte", bg="#FF8C00", fg="white", font=('algerian', 20)).place(x=5, y=5)


         frame1 = Frame(frame, bg="#DC7633")
         frame1.pack(expand=YES)



         prenom = Label(frame1, text="Prénom: ", bg="#DC7633", fg="white", font=('time new roman', 10))
         prenom.grid(row=0, column=0)
         self.prenom_entry = Entry(frame1, fg="black", width=60)
         self.prenom_entry.grid(row=0, column=2)

         nom = Label(frame1, text="Nom    : ", bg="#DC7633", fg="white", font=('time new roman', 10))
         nom.grid(row=1, column=0)
         self.nom_entry = Entry(frame1, fg="black", width=60)
         self.nom_entry.grid(row=1, column=2)

         date_naissance = Label(frame1, text="Date de naissance: ", bg="#DC7633", fg="white", font=('time new roman', 10))
         date_naissance.grid(row=3, column=0)
         self.date_naissance_entry = DateEntry(frame1, fg="black", date_pattern="dd/mm/yy", width=57, state="readon")
         self.date_naissance_entry.grid(row=3, column=2)

         pays = Label(frame1, text="Pays de naissance: ", bg="#DC7633", fg="white", font=('time new roman', 10))
         pays.grid(row=4, column=0)
         self.pays_entry = Entry(frame1, fg="black", width=60)
         self.pays_entry.grid(row=4, column=2)

         email = Label(frame1, text="Email: ", bg="#DC7633", fg="white", font=('time new roman', 10))
         email.grid(row=5, column=0)
         self.email_entry = Entry(frame1, fg="black", width=60)
         self.email_entry.grid(row=5, column=2)

         telephone = Label(frame1, text="N° de téléphone: ", bg="#DC7633", fg="white", font=('time new roman', 10))
         telephone.grid(row=6, column=0)
         self.telephone_entry = Entry(frame1, fg="black", width=60)
         self.telephone_entry.grid(row=6, column=2)

         btn_valider = Button(frame1, text ="Valider", bg="#DC7633", fg="white", width=30, command=self.Formulaire_BDD)
         btn_valider.grid(row=7, column=2)



     def Formulaire_BDD(self):

        if self.prenom_entry.get() =="" or self.nom_entry.get()=="" or self.email_entry.get()=="":
            messagebox.showerror("Erreur","Remplissez tous les champs SVP!", parent=self.appFrom)

        else:

            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="formulaire")
                cur = con.cursor()
                cur.execute("select * from registre where Email=%s", self.email_entry.get())
                row = cur.fetchone()

                if row != None :
                    messagebox.showerror("Erreur", " Ce mail existe déjà", parent=self.appFrom)
                elif self.telephone_entry is not int():
                    messagebox.showerror("Erreur", " Entrez un bon numéro de téléphone, SVP!", parent=self.appFrom)
                else:
                    cur.execute("insert into registre(Prénom, Nom, Datenaissance, Paysnaissance, Email, Telephone) values(%s,%s,%s,%s,%s,%s)",
                            (self.prenom_entry.get(),
                            self.nom_entry.get(),
                            self.date_naissance_entry.get(),
                            self.pays_entry.get(),
                            self.email_entry.get(),
                            self.telephone_entry.get()
                     ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Seccess", "Ajout effectué avec succès", parent=self.appFrom)
            except Exception as es:
                messagebox.showerror("Erreur", f"Erreur de connexion : {str(es)}", parent=self.appFrom)

appFrom = Tk()
obj = MyFormulaire(appFrom)
appFrom.mainloop()