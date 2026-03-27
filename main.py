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

# ---------------- LOAD DATA ----------------
fetch_data()

root.mainloop()