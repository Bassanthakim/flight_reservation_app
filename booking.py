import tkinter as tk
from tkinter import messagebox
import sqlite3

class BookingPage(tk.Frame):
    def __init__(self, parent, back_callback):
        super().__init__(parent, bg="#e6f2ff")
        self.back_callback = back_callback

        tk.Label(self, text="Book Your Flight", font=("Arial", 18, "bold"),
                 fg="#003366", bg="#e6f2ff").pack(pady=20)

        self.fields = {}

        form_data = [
            ("Name:", "name"),
            ("Flight:", "flight"),
            ("From:", "from_location"),
            ("To:", "to_location"),
            ("Date (YYYY-MM-DD):", "date"),
            ("Seat Number:", "seat")
        ]

        form_frame = tk.Frame(self, bg="#e6f2ff")
        form_frame.pack(pady=10)

        for i, (label_text, key) in enumerate(form_data):
            tk.Label(form_frame, text=label_text, bg="#e6f2ff", font=("Arial", 12)).grid(row=i, column=0, sticky="e", pady=5, padx=5)
            entry = tk.Entry(form_frame, width=30)
            entry.grid(row=i, column=1, pady=5, padx=5)
            self.fields[key] = entry

        tk.Button(self, text="Submit", font=("Arial", 12, "bold"),
                  bg="#007acc", fg="white", command=self.submit).pack(pady=15)

        tk.Button(self, text="Back to Home", command=self.back_callback,
                  font=("Arial", 12), bg="#cccccc").pack()

    def submit(self):
        data = {key: field.get().strip() for key, field in self.fields.items()}

        if any(value == "" for value in data.values()):
            messagebox.showerror("Error", "All fields are required.")
            return

        conn = sqlite3.connect("flights.db")
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO reservations (name, flight, from_location, to_location, date, seat)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (data["name"], data["flight"], data["from_location"], data["to_location"], data["date"], data["seat"]))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Reservation submitted successfully!")
        for field in self.fields.values():
            field.delete(0, tk.END)
