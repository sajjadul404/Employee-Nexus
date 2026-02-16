import tkinter as tk
from tkinter import ttk

class employee:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("1300x650+0+0")
        self.mainLabel = tk.Label(self.root,bd=5,relief="groove", text="BUBT Employee Management", font=("Arial", 40, "bold"), bg="black", fg="gold")
        self.mainLabel.pack(side=tk.TOP, fill=tk.X) 


        #......Fram1......
        self.Fram1 = tk.Frame(self.root, bd=5, relief="groove",bg="lightblue")
        self.Fram1.place(x=10, y=80,width=370, height=550)

        self.idLable = tk.Label(self.Fram1, padx=5, text="Employee ID:",fg="Black",bg="lightblue", font=("Arial", 14, "bold"),pady=10)
        self.idLable.grid(row=0, column=0)
        self.idIn = tk.Entry(self.Fram1, font=("Arial", 14), width=15)
        self.idIn.grid(row=0, column=1,pady=10)

        self.nameLable = tk.Label(self.Fram1, padx=5, text="Employee Name:",fg="Black",bg="lightblue", font=("Arial", 14, "bold"),pady=10)
        self.nameLable.grid(row=1, column=0)
        self.nameIn = tk.Entry(self.Fram1, font=("Arial", 14), width=15)
        self.nameIn.grid(row=1, column=1,pady=10)

        self.desigLable = tk.Label(self.Fram1, padx=5, text="Designation:",fg="Black",bg="lightblue", font=("Arial", 14, "bold"),pady=10)
        self.desigLable.grid(row=2, column=0)
        self.desigIn = tk.Entry(self.Fram1, font=("Arial", 14), width=15)
        self.desigIn.grid(row=2, column=1,pady=10)

        self.salLable = tk.Label(self.Fram1, padx=5, text="Salary:",fg="Black",bg="lightblue", font=("Arial", 14, "bold"),pady=10)
        self.salLable.grid(row=3, column=0)
        self.salIn = tk.Entry(self.Fram1, font=("Arial", 14), width=15)
        self.salIn.grid(row=3, column=1,pady=10)

        self.genLable = tk.Label(self.Fram1, padx=5, text="Gender:",fg="Black",bg="lightblue", font=("Arial", 14, "bold"),pady=10)
        self.genLable.grid(row=4, column=0)
        self.genIn = ttk.Combobox(self.Fram1, font=("Arial", 14), width=13, state="readonly")
        self.genIn['values'] = ("Male", "Female", "Other")
        self.genIn.grid(row=4, column=1,pady=10)

        self.addrLable = tk.Label(self.Fram1, padx=5, text="Address:",fg="Black",bg="lightblue", font=("Arial", 14, "bold"),pady=10)
        self.addrLable.grid(row=5, column=0)
        self.addrIn = tk.Entry(self.Fram1, font=("Arial", 14), width=15)
        self.addrIn.grid(row=5, column=1,pady=10)


        #......Button Fram......
        self.btnFrame = tk.Frame(self.root, bd=5,bg="lightblue",relief="raised")
        self.btnFrame.place(x=25, y=450, width=340, height=150)

        self.addbtn = tk.Button(self.btnFrame,text="Add",width=10, font=("Arial", 14, "bold"))
        self.addbtn.grid(row=0,column=0,padx=20,pady=20)

        self.updatebtn = tk.Button(self.btnFrame,text="Update",width=10, font=("Arial", 14, "bold"))
        self.updatebtn.grid(row=0,column=1,padx=20,pady=20)

        self.deletebtn = tk.Button(self.btnFrame,text="Delete",width=10, font=("Arial", 14, "bold"))
        self.deletebtn.grid(row=1,column=0,padx=20,pady=10)

        self.cleartebtn = tk.Button(self.btnFrame,text="Clear",width=10, font=("Arial", 14, "bold"))
        self.cleartebtn.grid(row=1,column=1,padx=20,pady=10)


        
        #......Fram2......
        self.Fram2 = tk.Frame(self.root, bd=5, relief="groove",bg="lightblue")
        self.Fram2.place(x=400, y=80, width=870, height=550)

        self.searchLable = tk.Label(self.Fram2, padx=5, text="Search By:",fg="Black",bg="lightblue", font=("Arial", 14, "bold"),pady=10)
        self.searchLable.grid(row=0, column=0)
        self.searchType = ttk.Combobox(self.Fram2, font=("Arial", 14), width=13, state="readonly")
        self.searchType['values'] = ("ID", "Name")
        self.searchType.grid(row=0, column=1,pady=10)

        self.searchIn = tk.Entry(self.Fram2, font=("Arial", 14), width=15)
        self.searchIn.grid(row=0, column=2,pady=10,padx=10)

        self.searchbtn = tk.Button(self.Fram2,text="Search",width=10, font=("Arial", 14, "bold"))
        self.searchbtn.grid(row=0,column=3,padx=5,pady=10)

        self.showbtn = tk.Button(self.Fram2,text="Show All",width=10, font=("Arial", 14, "bold"))
        self.showbtn.grid(row=0,column=4,padx=10,pady=10)


        #.....Table Frame......
        self.tabFrame = tk.Frame(self.Fram2, bd=5, relief="groove")
        self.tabFrame.place(x=10, y=80, width=840, height=450)


root = tk.Tk()
obj = employee(root)
root.mainloop()
     