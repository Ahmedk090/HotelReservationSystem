# Class to represent a Guest
class Guest:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def display_info(self):
        print(f"Guest Name: {self.name}, Email: {self.email}, Phone: {self.phone_number}")


# Class to represent a Room
class Room:
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = True  # By default, the room is available

    def book_room(self):
        if self.is_available:
            self.is_available = False
            print(f"Room {self.room_number} has been booked.")
        else:
            print(f"Room {self.room_number} is already booked.")

    def release_room(self):
        self.is_available = True
        print(f"Room {self.room_number} is now available.")


# Class to represent a Reservation
class Reservation:
    def __init__(self, reservation_id, guest, room, check_in_date, check_out_date):
        self.reservation_id = reservation_id
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def display_reservation(self):
        print(f"Reservation {self.reservation_id}: Guest: {self.guest.name}, Room: {self.room.room_number}, Check-in: {self.check_in_date}, Check-out: {self.check_out_date}")


# Class to represent a Bill
class Bill:
    def __init__(self, reservation):
        self.reservation = reservation
        self.total_amount = self.calculate_total()

    def calculate_total(self):
        # Calculate the total price based on the number of nights
        nights = (self.reservation.check_out_date - self.reservation.check_in_date).days
        return nights * self.reservation.room.price_per_night

    def display_bill(self):
        print(f"Bill for Reservation {self.reservation.reservation_id}:")
        print(f"Total Amount: ${self.total_amount}")


# Simple date handling
from datetime import datetime

# Creating a Guest
guest1 = Guest("Ahmed Khalifa", "Ahmed009@example.com", "0562121090")
guest1.display_info()

# Creating a Room
room1 = Room(205, "Single", 500)
print(f"Room {room1.room_number} is available: {room1.is_available}")

# Booking the Room
room1.book_room()

# Creating a Reservation
check_in = datetime.strptime("2024-05-04", "%Y-%m-%d")
check_out = datetime.strptime("2024-05-06", "%Y-%m-%d")
reservation1 = Reservation(1, guest1, room1, check_in, check_out)
reservation1.display_reservation()

# Generating a Bill
bill1 = Bill(reservation1)
bill1.display_bill()

# Check-out and releasing the room
room1.release_room()

