import tkinter as tk
from tkinter import messagebox
import sqlite3

class ReservationsPage(tk.Frame):
    def __init__(self, parent, back_callback):
        super().__init__(parent, bg="#e6f2ff")
        self.back_callback = back_callback

        tk.Label(self, text="All Reservations", font=("Arial", 16, "bold"),
                 bg="#e6f2ff", fg="#003366").pack(pady=20)

        # جدول عرض البيانات
        self.reservations_frame = tk.Frame(self, bg="#e6f2ff")
        self.reservations_frame.pack(pady=10)

        self.load_reservations()

        # زر الرجوع
        tk.Button(self, text="Back to Home", font=("Arial", 12, "bold"),
                  bg="#cccccc", command=self.back_callback).pack(pady=15)

    def load_reservations(self):
        # مسح أي بيانات قديمة في الجدول
        for widget in self.reservations_frame.winfo_children():
            widget.destroy()

        # الاتصال بقاعدة البيانات
        conn = sqlite3.connect("flights.db")
        cursor = conn.cursor()

        # جلب كل الحجوزات
        cursor.execute("SELECT * FROM reservations")
        records = cursor.fetchall()
        conn.close()

        # رؤوس الأعمدة
        headers = ["ID", "Name", "Flight", "From", "To", "Date", "Seat"]
        for col, header in enumerate(headers):
            tk.Label(self.reservations_frame, text=header, font=("Arial", 10, "bold"),
                     borderwidth=1, relief="solid", width=15, bg="#cce6ff").grid(row=0, column=col)

        # عرض كل صف
        for row_index, row in enumerate(records, start=1):
            for col_index, value in enumerate(row):
                tk.Label(self.reservations_frame, text=value, borderwidth=1, relief="solid",
                         width=15, bg="white").grid(row=row_index, column=col_index)
