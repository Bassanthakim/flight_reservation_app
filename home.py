import tkinter as tk
from booking import BookingPage
from reservations import ReservationsPage

class HomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#e6f2ff")

        tk.Label(self, text="Flight Reservation System", font=("Arial", 20, "bold"),
                 fg="#003366", bg="#e6f2ff").pack(pady=30)

        book_btn = tk.Button(self, text="Book a Flight", font=("Arial", 14),
                             bg="#007acc", fg="white", width=20, command=self.book_flight)
        book_btn.pack(pady=10)

        view_btn = tk.Button(self, text="View Reservations", font=("Arial", 14),
                             bg="#007acc", fg="white", width=20, command=self.view_reservations)
        view_btn.pack(pady=10)

    def book_flight(self):
        self.pack_forget()
        booking_page = BookingPage(self.master, self.show_home)
        booking_page.pack(fill="both", expand=True)

    def view_reservations(self):
        self.pack_forget()
        reservations_page = ReservationsPage(self.master, self.show_home)
        reservations_page.pack(fill="both", expand=True)

    def show_home(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        HomePage(self.master).pack(fill="both", expand=True)
