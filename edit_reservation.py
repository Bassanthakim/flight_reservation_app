import tkinter as tk
from tkinter import messagebox
import sqlite3

class EditReservationPage(tk.Frame):
    def __init__(self, parent, reservation_data, back_callback):
        super().__init__(parent)
        self.back_callback = back_callback
        self.reservation_id = reservation_data[0]  # أول عنصر هو ID

        tk.Label(self, text="Edit Reservation", font=("Arial", 16)).pack(pady=10)

        # الحقول
        labels = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        self.entries = []

        for i, label_text in enumerate(labels):
            tk.Label(self, text=label_text).pack()
            entry = tk.Entry(self)
            entry.insert(0, reservation_data[i+1])  # نبدأ من ثاني عنصر لأن أول واحد هو ID
            entry.pack()
            self.entries.append(entry)

        tk.Button(self, text="Update", command=self.update_reservation).pack(pady=10)

        tk.Button(self, text="Back", command=self.back_callback).pack()

    def update_reservation(self):
        new_data = [e.get() for e in self.entries]

        if not all(new_data):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        conn = sqlite3.connect("flights.db")
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE reservations
            SET name = ?, flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
            WHERE id = ?
        """, (*new_data, self.reservation_id))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Reservation updated successfully!")
        self.back_callback() 