from django.db import models

# Create your models here.
class IndigoModels(models.Model):
    name = models.CharField(max_length=30)  # Airline or flight name
    flight_number = models.CharField(max_length=10, unique=True)  # e.g., "6E123"
    depart_from = models.CharField(max_length=20)  # Departure city/airport
    departure_time = models.DateTimeField()  # Date and time of departure
    destination = models.CharField(max_length=20)  # Arrival city/airport
    arrival_time = models.DateTimeField()  # Date and time of arrival
    price = models.FloatField(default=0.00)  # Ticket price
    
class AirIndiaModel(models.Model):
    name = models.CharField(max_length=30)  # Airline or flight name
    flight_number = models.CharField(max_length=10, unique=True)  # e.g., "6E123"
    depart_from = models.CharField(max_length=20)  # Departure city/airport
    departure_time = models.DateTimeField()  # Date and time of departure
    destination = models.CharField(max_length=20)  # Arrival city/airport
    arrival_time = models.DateTimeField()  # Date and time of arrival
    price = models.FloatField(default=0.00)  # Ticket price  

class VistaraModel(models.Model):
    name = models.CharField(max_length=30)  # Airline or flight name
    flight_number = models.CharField(max_length=10, unique=True)  # e.g., "6E123"
    depart_from = models.CharField(max_length=20)  # Departure city/airport
    departure_time = models.DateTimeField()  # Date and time of departure
    destination = models.CharField(max_length=20)  # Arrival city/airport
    arrival_time = models.DateTimeField()  # Date and time of arrival
    price = models.FloatField(default=0.00)  # Ticket price 

class GoFirstModel(models.Model):
    name = models.CharField(max_length=30)  # Airline or flight name
    flight_number = models.CharField(max_length=10, unique=True)  # e.g., "6E123"
    depart_from = models.CharField(max_length=20)  # Departure city/airport
    departure_time = models.DateTimeField()  # Date and time of departure
    destination = models.CharField(max_length=20)  # Arrival city/airport
    arrival_time = models.DateTimeField()  # Date and time of arrival
    price = models.FloatField(default=0.00)  # Ticket price 

class SpiceJetModel(models.Model):
    name = models.CharField(max_length=30)  # Airline or flight name
    flight_number = models.CharField(max_length=10, unique=True)  # e.g., "6E123"
    depart_from = models.CharField(max_length=20)  # Departure city/airport
    departure_time = models.DateTimeField()  # Date and time of departure
    destination = models.CharField(max_length=20)  # Arrival city/airport
    arrival_time = models.DateTimeField()  # Date and time of arrival
    price = models.FloatField(default=0.00)  # Ticket price 

class BookingModel(models.Model):
    flight_name=models.CharField(max_length=50,default='Unknown')
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=40)
    phno=models.CharField(max_length=10)
    age=models.IntegerField(default=0)

class DeletedBookingModel(models.Model):
    flight_name = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phno = models.CharField(max_length=15)
    age = models.IntegerField()
    deleted_at = models.DateTimeField(auto_now_add=True)  # Timestamp of deletion
