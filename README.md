✈️ Flight Booking System (Django)
📌 Overview

A full-stack Flight Booking Web Application built with Django that allows users to search flights, book tickets, manage reservations, and track booking history.
It supports multiple airlines (IndiGo, Air India, Vistara, SpiceJet, GoFirst) and provides features for booking, editing, deleting, and recovering bookings.

⚙️ Tech Stack

Backend: Django (Python)

Database: SQLite (default, can be switched to PostgreSQL/MySQL)

Frontend: Django Templates, HTML, CSS, Bootstrap

Other: ORM for database management

✨ Features

✅ Browse flights by airline (IndiGo, Air India, Vistara, SpiceJet, GoFirst)
✅ View detailed flight info (departure, arrival, price, flight number)
✅ Book flights with passenger details (name, email, phone, age)
✅ View booking summary with passenger & flight details
✅ Edit bookings after confirmation
✅ Cancel bookings with soft delete (recover later)
✅ Deleted bookings stored in history with timestamp
✅ Recover or permanently delete bookings

🔑 User Flow

Home Page → Navigate to available airlines.

Airline Page → View flights with details & prices.

Booking Form → Enter passenger details & confirm.

Booking Details → View/edit/delete bookings.

History → Access deleted bookings, recover, or delete permanently.

🚀 Installation & Setup

Clone the repository

git clone https://github.com/Gulshan215/Flight_booking_using_djnago.git
cd Flight_booking_using_djnago


Create & activate a virtual environment

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


Install dependencies

pip install django


Apply migrations & run server

python manage.py migrate
python manage.py runserver


Open in browser

http://127.0.0.1:8000/
