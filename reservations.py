import tkinter as tk
from tkinter import messagebox
import sqlite3
from edit_reservation import EditReservationPage

class ReservationsPage(tk.Frame):
    def __init__(self, parent, back_callback):
        super().__init__(parent)
        self.back_callback = back_callback

        tk.Label(self, text="All Reservations", font=("Arial", 16)).pack(pady=10)

        self.reservations_frame = tk.Frame(self)
        self.reservations_frame.pack(pady=10)

        self.load_reservations()

        tk.Button(self, text="Back to Home", command=self.back_callback).pack(pady=10)

    def load_reservations(self):
        # مسح البيانات القديمة من الجدول
        for widget in self.reservations_frame.winfo_children():
            widget.destroy()

        # الاتصال بقاعدة البيانات
        conn = sqlite3.connect("flights.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM reservations")
        records = cursor.fetchall()
        conn.close()

        headers = ["ID", "Name", "Flight", "From", "To", "Date", "Seat", "Actions"]
        for col, header in enumerate(headers):
            tk.Label(self.reservations_frame, text=header, font=("Arial", 10, "bold"),
                     borderwidth=1, relief="solid", width=15).grid(row=0, column=col)

        for row_index, row in enumerate(records, start=1):
            for col_index, value in enumerate(row):
                tk.Label(self.reservations_frame, text=value, borderwidth=1,
                         relief="solid", width=15).grid(row=row_index, column=col_index)

            # أزرار تعديل وحذف
            edit_btn = tk.Button(self.reservations_frame, text="Edit", command=lambda r=row: self.edit_reservation(r))
            delete_btn = tk.Button(self.reservations_frame, text="Delete", command=lambda r=row: self.delete_reservation(r[0]))

            edit_btn.grid(row=row_index, column=7, padx=5, pady=2)
            delete_btn.grid(row=row_index, column=8, padx=5, pady=2)

    def delete_reservation(self, reservation_id):
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this reservation?")
        if confirm:
            conn = sqlite3.connect("flights.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM reservations WHERE id = ?", (reservation_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Deleted", "Reservation deleted successfully.")
            self.load_reservations()

    def edit_reservation(self, reservation_data):
        self.pack_forget()
        edit_page = EditReservationPage(self.master, self.back_callback, reservation_data)
        edit_page.pack(fill="both", expand=True)
