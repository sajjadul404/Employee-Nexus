import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# ---------------- DATABASE CONNECTION ----------------
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="companydb"
    )

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Employee Management System")
root.geometry("950x550")
root.config(bg="#f8c8dc")

# ---------------- VARIABLES ----------------
emp_id = tk.StringVar()
name = tk.StringVar()
email = tk.StringVar()
phone = tk.StringVar()
department = tk.StringVar()
salary = tk.StringVar()
search_var = tk.StringVar()   # 🔍 NEW

# ---------------- FUNCTIONS ----------------

def add_employee():
    if name.get()=="" or email.get()=="":
        messagebox.showerror("Error", "Name and Email Required")
        return

    con = connect_db()
    cur = con.cursor()
    cur.execute(
        "INSERT INTO employees (name,email,phone,department,salary) VALUES (%s,%s,%s,%s,%s)",
        (name.get(), email.get(), phone.get(), department.get(), salary.get())
    )
    con.commit()
    con.close()
    fetch_data()
    clear_fields()
    messagebox.showinfo("Success", "Employee Added Successfully")

def fetch_data():
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()

    employee_table.delete(*employee_table.get_children())
    for row in rows:
        employee_table.insert("", tk.END, values=row)
    con.close()

def search_employee():   # 🔍 NEW
    con = connect_db()
    cur = con.cursor()

    query = "SELECT * FROM employees WHERE name LIKE %s OR email LIKE %s"
    value = "%" + search_var.get() + "%"

    cur.execute(query, (value, value))
    rows = cur.fetchall()

    employee_table.delete(*employee_table.get_children())
    for row in rows:
        employee_table.insert("", tk.END, values=row)

    con.close()

def reset_search():   # 🔄 NEW
    search_var.set("")
    fetch_data()

def get_cursor(event):
    row = employee_table.focus()
    data = employee_table.item(row)["values"]

    if data:
        emp_id.set(data[0])
        name.set(data[1])
        email.set(data[2])
        phone.set(data[3])
        department.set(data[4])
        salary.set(data[5])

def update_employee():
    if emp_id.get()=="":
        messagebox.showerror("Error", "Select Employee First")
        return

    con = connect_db()
    cur = con.cursor()
    cur.execute("""
        UPDATE employees SET
        name=%s,
        email=%s,
        phone=%s,
        department=%s,
        salary=%s
        WHERE id=%s
    """, (name.get(), email.get(), phone.get(), department.get(), salary.get(), emp_id.get()))

    con.commit()
    con.close()
    fetch_data()
    clear_fields()
    messagebox.showinfo("Success", "Employee Updated Successfully")

def delete_employee():
    if emp_id.get()=="":
        messagebox.showerror("Error", "Select Employee First")
        return

    con = connect_db()
    cur = con.cursor()
    cur.execute("DELETE FROM employees WHERE id=%s", (emp_id.get(),))
    con.commit()
    con.close()
    fetch_data()
    clear_fields()
    messagebox.showinfo("Success", "Employee Deleted Successfully")

def clear_fields():
    emp_id.set("")
    name.set("")
    email.set("")
    phone.set("")
    department.set("")
    salary.set("")

# ---------------- FORM FRAME ----------------
form_frame = tk.Frame(root, bg="#f2a7c2", bd=5, relief=tk.RIDGE)
form_frame.place(x=30, y=70, width=390, height=450)

lbl_font = ("Arial", 12, "bold")
entry_font = ("Arial", 12)

tk.Label(form_frame, text="Name", bg="#f2a7c2", font=lbl_font).grid(row=0, column=0, padx=10, pady=15, sticky="w")
tk.Entry(form_frame, textvariable=name, font=entry_font, width=22).grid(row=0, column=1)

tk.Label(form_frame, text="Email", bg="#f2a7c2", font=lbl_font).grid(row=1, column=0, padx=10, pady=15, sticky="w")
tk.Entry(form_frame, textvariable=email, font=entry_font, width=22).grid(row=1, column=1)

tk.Label(form_frame, text="Phone", bg="#f2a7c2", font=lbl_font).grid(row=2, column=0, padx=10, pady=15, sticky="w")
tk.Entry(form_frame, textvariable=phone, font=entry_font, width=22).grid(row=2, column=1)

tk.Label(form_frame, text="Department", bg="#f2a7c2", font=lbl_font).grid(row=3, column=0, padx=10, pady=15, sticky="w")
tk.Entry(form_frame, textvariable=department, font=entry_font, width=22).grid(row=3, column=1)

tk.Label(form_frame, text="Salary", bg="#f2a7c2", font=lbl_font).grid(row=4, column=0, padx=10, pady=15, sticky="w")
tk.Entry(form_frame, textvariable=salary, font=entry_font, width=22).grid(row=4, column=1)

# ---------------- BUTTONS ----------------
btn_font = ("Arial", 11, "bold")

tk.Button(form_frame, text="ADD", width=14, font=btn_font, bg="#ff69b4", command=add_employee)\
    .grid(row=5, column=0, pady=25, padx=8)

tk.Button(form_frame, text="UPDATE", width=14, font=btn_font, bg="#ff69b4", command=update_employee)\
    .grid(row=5, column=1)

tk.Button(form_frame, text="DELETE", width=14, font=btn_font, bg="#ff69b4", command=delete_employee)\
    .grid(row=6, column=0, padx=8)

tk.Button(form_frame, text="CLEAR", width=14, font=btn_font, bg="#ff69b4", command=clear_fields)\
    .grid(row=6, column=1)

# ---------------- TABLE FRAME ----------------
table_frame = tk.Frame(root, bd=4, relief=tk.RIDGE)
table_frame.place(x=430, y=80, width=490, height=440)

scroll_y = tk.Scrollbar(table_frame, orient=tk.VERTICAL)
scroll_x = tk.Scrollbar(table_frame, orient=tk.HORIZONTAL)

employee_table = ttk.Treeview(
    table_frame,
    columns=("ID","Name","Email","Phone","Department","Salary"),
    yscrollcommand=scroll_y.set,
    xscrollcommand=scroll_x.set
)

scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
scroll_y.config(command=employee_table.yview)
scroll_x.config(command=employee_table.xview)

employee_table.heading("ID", text="ID")
employee_table.heading("Name", text="Name")
employee_table.heading("Email", text="Email")
employee_table.heading("Phone", text="Phone")
employee_table.heading("Department", text="Department")
employee_table.heading("Salary", text="Salary")

employee_table["show"] = "headings"

employee_table.column("ID", width=50)
employee_table.column("Name", width=120)
employee_table.column("Email", width=150)
employee_table.column("Phone", width=100)
employee_table.column("Department", width=120)
employee_table.column("Salary", width=80)

employee_table.pack(fill=tk.BOTH, expand=1)
employee_table.bind("<ButtonRelease-1>", get_cursor)

# ---------------- LOAD DATA ----------------
fetch_data()

root.mainloop()