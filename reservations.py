import tkinter as tk
from tkinter import messagebox
import sqlite3

class ReservationsPage(tk.Frame):
    def __init__(self, parent, back_callback):
        super().__init__(parent, bg="#f0f8ff")
        self.back_callback = back_callback

        tk.Label(self, text="All Reservations", font=("Arial", 18, "bold"),
                 fg="#003366", bg="#f0f8ff").pack(pady=20)

        self.table_frame = tk.Frame(self, bg="#f0f8ff")
        self.table_frame.pack(pady=10)

        self.load_data()

        tk.Button(self, text="Back to Home", command=self.back_callback,
                  font=("Arial", 12), bg="#cccccc").pack(pady=10)

    def load_data(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        headers = ["ID", "Name", "Flight", "From", "To", "Date", "Seat", "Edit", "Delete"]
        for i, header in enumerate(headers):
            tk.Label(self.table_frame, text=header, bg="#cce6ff", font=("Arial", 10, "bold"),
                     borderwidth=1, relief="solid", width=12).grid(row=0, column=i)

        conn = sqlite3.connect("flights.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reservations")
        rows = cursor.fetchall()
        conn.close()

        for row_idx, row in enumerate(rows, start=1):
            for col_idx, value in enumerate(row):
                tk.Label(self.table_frame, text=value, bg="#ffffff",
                         borderwidth=1, relief="solid", width=12).grid(row=row_idx, column=col_idx)

            # Edit button
            tk.Button(self.table_frame, text="Edit", bg="#ffd966", command=lambda r=row: self.edit_reservation(r)).grid(row=row_idx, column=7)
            # Delete button
            tk.Button(self.table_frame, text="Delete", bg="#ff9999", command=lambda rid=row[0]: self.delete_reservation(rid)).grid(row=row_idx, column=8)

    def delete_reservation(self, reservation_id):
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this reservation?")
        if confirm:
            conn = sqlite3.connect("flights.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM reservations WHERE id=?", (reservation_id,))
            conn.commit()
            conn.close()
            self.load_data()

    def edit_reservation(self, reservation):
        edit_win = tk.Toplevel(self)
        edit_win.title("Edit Reservation")
        edit_win.configure(bg="#f9f9f9")

        labels = ["Name", "Flight", "From", "To", "Date", "Seat"]
        fields = {}

        for i, label in enumerate(labels):
            tk.Label(edit_win, text=label, bg="#f9f9f9").grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(edit_win, width=30)
            entry.insert(0, reservation[i+1])  # Skip ID
            entry.grid(row=i, column=1, padx=10, pady=5)
            fields[label.lower()] = entry

        def save_changes():
            updated = tuple(fields[key].get().strip() for key in fields)
            if any(v == "" for v in updated):
                messagebox.showerror("Error", "All fields are required.")
                return

            conn = sqlite3.connect("flights.db")
            cursor = conn.cursor()
            cursor.execute('''
                 UPDATE reservations
                 SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=?
                 WHERE id=?
                ''', (*updated, reservation[0]))

            conn.commit()
            conn.close()
            edit_win.destroy()
            self.load_data()

        tk.Button(edit_win, text="Save Changes", bg="#4CAF50", fg="white", command=save_changes).grid(row=len(labels), column=0, columnspan=2, pady=10)
