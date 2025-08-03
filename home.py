import tkinter as tk
from booking import BookingPage
from reservations import ReservationsPage  # ← لازم تكوني ضفتي الملف ده

class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        master.title("Flight Reservation System")
        master.geometry("600x400")

        title = tk.Label(self, text="Welcome to Flight Reservation System", font=("Arial", 18))
        title.pack(pady=40)

        book_btn = tk.Button(self, text="Book Flight", font=("Arial", 14), width=20, command=self.book_flight)
        book_btn.pack(pady=10)

        view_btn = tk.Button(self, text="View Reservations", font=("Arial", 14), width=20, command=self.view_reservations)
        view_btn.pack(pady=10)

        self.pack(fill="both", expand=True)

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
