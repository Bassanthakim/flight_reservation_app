import tkinter as tk
from home import HomePage
from database import create_table

# نبدأ بتجهيز قاعدة البيانات
create_table()

# إنشاء نافذة البرنامج
root = tk.Tk()
root.title("Flight Reservation System")
root.geometry("600x400")

# عرض الصفحة الرئيسية
app = HomePage(root)
app.pack(fill="both", expand=True)

# تشغيل البرنامج
root.mainloop()
