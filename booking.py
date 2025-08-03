import tkinter as tk
from tkinter import messagebox
from database import create_connection

class BookingPage(tk.Frame):
    def __init__(self, parent, go_home_callback):
        super().__init__(parent)
        self.parent = parent
        self.go_home_callback = go_home_callback  # علشان نقدر نرجع للصفحة الرئيسية

        tk.Label(self, text="Book a Flight", font=("Arial", 16)).pack(pady=10)

        # ======= خانات الإدخال ========
        self.name_entry = self.create_input("Passenger Name")
        self.flight_entry = self.create_input("Flight Number")
        self.departure_entry = self.create_input("Departure")
        self.destination_entry = self.create_input("Destination")
        self.date_entry = self.create_input("Date (YYYY-MM-DD)")
        self.seat_entry = self.create_input("Seat Number")

        # ======= زر الحجز ========
        tk.Button(self, text="Submit", font=("Arial", 14), command=self.submit_booking).pack(pady=10)
        tk.Button(self, text="Back to Home", font=("Arial", 12), command=self.go_home_callback).pack(pady=5)

    def create_input(self, label_text):
        frame = tk.Frame(self)
        frame.pack(pady=5)
        tk.Label(frame, text=label_text, width=15, anchor='w').pack(side='left')
        entry = tk.Entry(frame, width=30)
        entry.pack(side='left')
        return entry

    def submit_booking(self):
        name = self.name_entry.get()
        flight_number = self.flight_entry.get()
        departure = self.departure_entry.get()
        destination = self.destination_entry.get()
        date = self.date_entry.get()
        seat_number = self.seat_entry.get()

        if not all([name, flight_number, departure, destination, date, seat_number]):
            messagebox.showerror("Error", "All fields are required.")
            return

        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, flight_number, departure, destination, date, seat_number))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Reservation booked successfully!")
        self.clear_form()

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.flight_entry.delete(0, tk.END)
        self.departure_entry.delete(0, tk.END)
        self.destination_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.seat_entry.delete(0, tk.END)
